from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps CI/CD!"

app.run(host='0.0.0.0', port=5000)
test webhook
