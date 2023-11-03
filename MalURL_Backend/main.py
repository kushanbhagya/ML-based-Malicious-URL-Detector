from flask import Flask, request, jsonify
import joblib  # For loading the model
from sklearn.feature_extraction.text import TfidfVectorizer
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/verify": {"origins": "http://localhost:3000"}})


# Load the trained model and vectorizer (Replace with your actual model and vectorizer loading)
model = joblib.load("trained_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Sample function to demonstrate URL verification
# def verify_url(url):
#     # This is a placeholder function, replace with your actual verification logic
#     # You can use model.predict and vectorizer.transform here
#     if "malicious" in url:
#         return "UNSAFE"
#     else:
#         return "SAFE"


# def verify_url_route():
#     try:
#         data = request.get_json()
#         url = data.get('url')

#         if not url:
#             return jsonify({'result': 'INVALID!'})

#         result = verify_url(url)  # Call your verification function here
#         print("url",data)
#         print("result",result)
#         return jsonify({'result': result})
#     except Exception as e:
#         return jsonify({'result': 'INVALID!'})
@app.route('/verify', methods=['OPTIONS'])    
def verify_url():
    print("data",data)
    try:
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({'result': 'INVALID!'})

        # Vectorize the URL using the loaded vectorizer
        url_vector = vectorizer.transform([url])

        # Make predictions using the loaded model
        prediction = model.predict(url_vector)
        result = prediction[0]
        print("url",data)
        print("result",result)
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'result': 'INVALID!'})


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
