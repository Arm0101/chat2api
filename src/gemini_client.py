import google.generativeai as genai

class GeminiClient():
    def __init__(self, model, functions, api_key) -> None:
       self.model = genai.GenerativeModel(model, tools=functions)
       genai.configure(api_key=api_key)
    
    def get_response(self, msg, context, functions, retry=False):
        chat = self.model.start_chat(history=context)
        response = chat.send_message(msg)
        
        res = []
        for part in response.parts:
            if fn := part.function_call:
                print(fn)
                result = functions[fn.name](**fn.args)
                if 'err' not in result:
                    return result 
                
                if not retry:
                    new_msg = f'The result {result['result']} is incorrect, please fix this error: {result['err']}'
                    return self.get_response(new_msg, context, functions, retry=True)
            else:
                res.append(part.text)
                
        return ''.join(res)
