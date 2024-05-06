from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)  # create an instance of flask application
nlp = spacy.load('en_core_web_sm')  # load spacy eng model that includes
# data & algorithms spacy needs to analyze english text


@app.route("/")  # decorator that tells flask what url should trigger the function below
def home():  # user will be able to view once url matches the specified url
    return render_template('index.html')  # returns a html file from template, index.html,
# which should contain the user interface for chatbot


@app.route("/chat", methods=['POST'])
def chat():
    user_input = request.json['message']
    doc = nlp(user_input)
    response = "Let me think about that."
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True)




