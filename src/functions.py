import requests
import streamlit as st
from PIL import Image
from io import BytesIO

def call_api(url):
    res = requests.get(url)
    
    if res.status_code == 400:
        return {'err': res.json().get('message', 'Bad Request'), 'result': url}
    
    if res.status_code != 200:
        return f'Error {url}'
    
    content_type = res.headers['Content-Type']
    
    if 'image' in content_type:
        img = Image.open(BytesIO(res.content))
        st.image(img,width=500 ,caption='Image from API')
        return url
    else:
        return res.text


function_declarations = {'function_declarations': [
    {
        'name': 'call_api',
        'description': 'Generate the required URL to make an API call',
        'parameters': {'type': 'object',
        'properties': {
            'url': {'type': 'string', 'description': 'API endpoint URL (params are accepted)'}},
            'required': ['url']
        }
    }
    ]
}



functions = {
    'call_api': call_api
}