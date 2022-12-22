from flask import Flask, render_template, request
import pickle


with open('amz_reviews_model.bin', 'rb') as f:
    tfidf, model = pickle.load(f)


def review_quality_prediction(text, tfidf, model):
    """Function for applying the review quality model"""
    review = tfidf.transform([text])
    y_pred = model.predict(review)
    return y_pred[0]


app = Flask(__name__)


@app.route("/")
def my_form_home():
    return render_template('home.html')


@app.route("/", methods=['POST', 'GET'])
def predict():
    text = request.form['Review']
    
    pred = review_quality_prediction(text, tfidf, model)
    rev_pred = ""
    
    if pred == "hq":
        rev_pred = "high quality"
    elif pred == "lq":
        rev_pred = "low quality"   
    
    return render_template('prediction.html', data=rev_pred, data2=text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)