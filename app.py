from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <head>
        <title>CI/CD Dashboard</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                margin-top: 100px;
            }}
            .box {{
                background: rgba(0,0,0,0.3);
                padding: 40px;
                border-radius: 20px;
                display: inline-block;
                box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
                animation: fadeIn 1.5s ease-in-out;
            }}
            h1 {{
                font-size: 45px;
            }}
            p {{
                font-size: 20px;
            }}
            .version {{
                color: #ffd700;
                font-weight: bold;
                margin-top: 10px;
            }}
            .time {{
                margin-top: 20px;
                font-size: 16px;
                color: #e0f7ff;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 CI/CD Pipeline Updated!</h1>
            <p>Deployed using Jenkins, Docker & AWS EC2</p>
            <p class="version">✔ Version 2 Auto Redeployed via Webhook</p>
            <div class="time">Last Updated: {current_time}</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
