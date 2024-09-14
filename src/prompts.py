
BASE_PROMPT = """
   Your goal is to respond to a user by making API requests based on the information provided in the context.\
    If you don’t have enough details, such as the URL or the necessary parameters, ask the user for clarification.\
    URLs must start with http or https. For instance, (/cat) is not a valid URL. \
    In cases like /:value, treat ":value" as a dynamic parameter. For example, in /users/:id, ":id" should be replaced with an actual user ID, resulting in /users/123.\
    To add parameters to a URL, append a query string. Example: https://api.com/resource?key=value \
    The user’s input may be translated to match the API documentation if necessary. \
    Extract the URL from the context (do not use these examples). 
"""
def user_prompt(msg, api_info):
    return f"""
    {BASE_PROMPT}

    Use this API documentation to extract the correct URL: {api_info}.
    Retrieve this information using the given API: {msg}
"""