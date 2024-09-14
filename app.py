import streamlit as st
from src.gemini_client import GeminiClient


from src.chat import Chat
from src.utils import load_content
from src.prompts import user_prompt
from src.functions import function_declarations, functions



st.set_page_config(page_title='Chat2API')
st.title('Chat2API')

client = GeminiClient('gemini-1.5-flash-latest', functions=function_declarations ,api_key=st.secrets['gemini_secret_key'])
chat = Chat()



if 'api_doc_url' not in st.session_state:
    st.session_state.api_doc_url = ''
if 'api_doc_content' not in st.session_state:
    st.session_state.api_doc_content = ''


api_url = st.text_input("", placeholder='Enter a url')


if api_url != st.session_state.api_doc_url:
    chat.reset()
    st.session_state.api_doc_url = api_url
    st.session_state.api_doc_content = load_content(api_url)
    


chat.show_history()

msg = st.chat_input()

if msg:
    with st.chat_message('user'):
        st.write(msg)
        chat.add(msg,'user')

    with st.chat_message('assistant'):
        resp = client.get_response(user_prompt(msg, st.session_state.api_doc_content), context=chat.get_context(5) , functions= functions)
        if resp:
            st.write(resp)      
            chat.add(resp, 'assistant')
