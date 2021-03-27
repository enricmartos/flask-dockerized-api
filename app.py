import os
from flask import Flask

from Classifier import Classifier

app = Flask(__name__)
port = int(os.environ.get('PORT', 8080))


@app.route('/predict-breast-cancer')
def hello_world():
    classifier = Classifier()
    accuracy_score = classifier.predict_breast_cancer()
    return 'The accuracy score of beast cancer prediction is ' + str(accuracy_score)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
