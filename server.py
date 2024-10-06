"""
Flask application for sentiment analysis that provides a web interface to analyze text input. 
It includes routes for analyzing sentiment and rendering the main index page.
"""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """sents the response"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."
    return f"The given text has been identified as {label.split('_')[1]}, with a score of {score}."


@app.route("/")
def render_index_page():
    """Renders index.html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
