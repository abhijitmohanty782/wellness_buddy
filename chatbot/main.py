import textwrap
from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure Google Generative AI with your API key
genai.configure(api_key="AIzaSyAS6gookHzTI8WuHxhhYM0Fd6gsTI186H0")


# Function to convert text to Markdown format
def to_markdown(text):
    text = text.replace('**', '<br>')
    text = text.replace('*', '<br>•')
    return textwrap.indent(text, ' ')


# Define chatbot logic
def chatbot_response(query):
    # Create a GenerativeModel instance
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(query)
    generated_text = to_markdown(response.text)

    return generated_text


# Define route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user query from the form
        user_query = request.form['query']

        # Generate chatbot responseWe
        bot_response = chatbot_response(f'Act as an chatbot of Wellness Buddy website used for telling information about '
                                        f'cancer, tuberculosis and diabetes and their different types, symptoms, causes and their treatments and with that also say what are the possible diseases or predict from given symptoms for all diseases and also say info about different diseases symptoms do not reply to inrelevant queries, query = "{user_query}"')

        # Format bot response
        bot_response = to_markdown(bot_response)

        return render_template('result.html', user_query=user_query, bot_response=bot_response)
    else:
        return render_template('result.html')


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
