from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    
    try:
        # Initialize Gemini Pro model
        model = genai.GenerativeModel("gemini-1.5-pro")
        
        # Get the response from Gemini
        response = model.generate_content(user_message)
        ai_message = response.text
        
        return jsonify({"response": ai_message})
    
    except Exception as e:
        return jsonify({"response": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
