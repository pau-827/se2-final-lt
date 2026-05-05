from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ivy's CI/CD App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: rgba(0, 0, 0, 0.3);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }
            h1 {
                margin-bottom: 10px;
            }
            p {
                font-size: 18px;
            }
            .tag {
                margin-top: 15px;
                font-size: 14px;
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>👋 Hello, I'm Ivy!</h1>
            <p>Welcome to my CI/CD Flask App 🚀</p>
            <p>This app is deployed using GitHub Actions, Docker, and Azure.</p>
            <div class="tag">Status: Running smoothly ✅</div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)