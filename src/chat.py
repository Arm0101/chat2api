import streamlit as st

class Chat:
    
    def __init__(self) -> None:
        if 'history' not in st.session_state:
            st.session_state.history = []

    
    def reset(self):
        st.session_state.history.clear()
    
    def add(self, msg, role):
        st.session_state.history.append({'msg': msg,'role': role})

    def show_history(self):
        for entry in st.session_state.history:
            with st.chat_message(entry['role']):
                st.write(entry['msg'])

    def get_context(self, n):
        if 'history' not in st.session_state:
            return []
        
        if n <= 0:
            return []
        
        if n > len(st.session_state.history):
            n = len(st.session_state.history)

        return [{'role': 'user' if h['role'] =='user' else 'model', 'parts': h['msg']} 
                for h in st.session_state.history[-n:]]