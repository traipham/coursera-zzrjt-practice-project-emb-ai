import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=data, headers=headers)
    json_response = json.loads(response.text)
    doc_sentiment = json_response['documentSentiment']
    label = doc_sentiment['label']
    score = doc_sentiment['score']
    if response.status_code == 500:
        label = None
        score = None
    res = dict(label=label, score=score)
    return res


if __name__ == "__main__":
    response = sentiment_analyzer("I love this new technology")
    print(response)