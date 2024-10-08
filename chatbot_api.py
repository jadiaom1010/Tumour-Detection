# chatbot_api.py

def get_chatbot_response(question):
    # Simple response logic (you can expand this)
    # Replace this with actual logic or API calls as needed
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "what is brain tumor?": "A brain tumor is an abnormal growth of cells in the brain.",
        "bye": "Goodbye! Have a great day!"
    }
    
    # Return a response if it exists, otherwise return a default message
    return responses.get(question.lower(), "I'm sorry, I don't understand that.")
