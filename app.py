from flask import Flask, request, render_template
import openai

user = openai.OpenAI( 
    api_key = " #your OpenAI API key# "
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Render home page

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form.get("message", "").strip()  # Get user input from the form
    if not user_input:
        return "Please enter a message!"  # Error if no input

    try:
        # OpenAI API call
        response = user.chat.completions.create( 
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )

        # Get bot reply
        bot_reply = response.choices[0].message.content.strip()

        return render_template("index.html", user_input=user_input, bot_reply=bot_reply)

    except Exception as e:
        return f"Error: {str(e)}"  # Generic error message

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
