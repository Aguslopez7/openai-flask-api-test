from flask import Flask, request, jsonify
from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the log level
    format='%(asctime)s - [%(levelname)s] - %(message)s',  # Log message format
)

# Initialize Flask and the OpenAI client
app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get JSON data from the client
        data = request.get_json()

        # Ensure the required fields are present
        model = data.get("model")
        messages = data.get("messages")

        if not model or not messages:
            logging.error("Error: Missing 'model' or 'messages'.")
            return jsonify({"error": "'model' and 'messages' are required"}), 400

        # Call the OpenAI API with the provided body
        chat_completion = client.chat.completions.create(
            model=model,
            messages=messages
        )

        # Extract the response message
        response_message = chat_completion.choices[0].message.content
        formatted_message = response_message.replace("\n", " ")  # Replace newlines with spaces
        logging.info(f"Response message: {formatted_message}")
        return jsonify({"response": formatted_message})

    # Handle OpenAI API-specific errors
    except OpenAIError as openai_error:
        return jsonify({"error": "OpenAI API Error", "message": str(openai_error)}), 500
    
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
