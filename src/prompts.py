
BASE_PROMPT = """
   Your goal is to respond to a user by making API requests based on the information provided in the context.\
    If you don’t have enough details, such as the URL or the necessary parameters, ask the user for clarification.\
    URLs must start with http or https. For instance, (/cat) is not a valid URL. \
    In cases like /:value, treat ":value" as a dynamic parameter. For example, in /users/:id, ":id" should be replaced with an actual user ID, resulting in /users/123.\
    To add parameters to a URL, append a query string. Example: https://api.com/resource?key=value \
    The user’s input may be translated to match the API documentation if necessary. \ 
"""

API_DOC_PROMPT = """
    From this HTML file corresponding to the API documentation, extract the relevant information and create a well-structured documentation,\
    divided into paragraphs. In each paragraph, explain clearly and concisely the different uses of the API.\
    Additionally, attempt to infer the full URL of the endpoints in case it's not explicitly provided.\
    """

def user_prompt(msg, api_info):
    return f"""
    {BASE_PROMPT}

    Use the provided API documentation in {api_info} to extract the correct URL for retrieving the information requested by the user: {msg}.
    You may combine different parameters from the endpoints if necessary in order to construct a URL that fulfills the user's request.\
    Ensure that all required parameters are included, and the url is formatted correctly.
"""