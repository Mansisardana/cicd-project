from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>CI/CD Project</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                margin-top: 100px;
            }
            h1 {
                font-size: 50px;
            }
            p {
                font-size: 20px;
            }
            .box {
                background: rgba(0,0,0,0.3);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 CI/CD Pipeline Success!</h1>
            <p>Deployed using Jenkins, Docker & AWS EC2</p>
            <p>Automated with GitHub Webhook ⚡</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
