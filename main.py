from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Test github Webhooks'

@app.route('/github', methods = ['POST'])
def github_webhook():
    if request.headers['Content-Type'] == 'application/json':
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)
