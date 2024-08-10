''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyse = request.args.get("textToAnalyze")
    response_json = sentiment_analyzer(text_to_analyse)
    if not response_json['label'] and not response_json['score']:
        return "Invalid input! Try again."
    label = response_json['label'][5:]
    score = response_json['score']
    res_text = f"The given text has been identified as {label} with a score of {score}."
    return ({"msg":res_text}, 200)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
