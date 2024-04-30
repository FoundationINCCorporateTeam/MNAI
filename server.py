from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define a dictionary of responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Feeling great!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"]
}

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    user_input = data["message"].lower()

    # Check if the message exists in the responses dictionary
    if user_input in responses:
        # If it does, randomly select a response from the list of responses
        bot_response = random.choice(responses[user_input])
    else:
        # If the message is not found, return a default response
        bot_response = "I'm sorry, I don't understand that."

    return jsonify({"message": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
