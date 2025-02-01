from flask import Flask, request, render_template
import openai

openai.api_key = " #your OpenAI API key# "

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Render home page

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form["message"]  # Get user input from the form
    if not user_input:
        return "Please enter a message!"  # Error if no input

    try:
        # OpenAI API call
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150,
            temperature=0.7
        )

        # Get bot reply
        bot_reply = response['choices'][0]['text'].strip()

        return render_template("index.html", user_input=user_input, bot_reply=bot_reply)

    except Exception as e:
        return f"Error: {str(e)}"  # Error message if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
