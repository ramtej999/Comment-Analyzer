import google.generativeai as genai

# Set your Gemini API Key
genai.configure(api_key="Replace this with your API key")


def summarize_comments(comments):
    prompt = f"Summarize the following comments and extract key discussion points:\n\n{comments}"
    
    # Use Gemini Flash 2.0
    model = genai.GenerativeModel("gemini-2.0-flash") # Initialize the model 
    # previous used model is "gemini-1.5-flash"
    # Generate summary
    response = model.generate_content(prompt)
    return response.text
