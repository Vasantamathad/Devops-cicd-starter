from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!doctype html>
    <html><head><title>DevOps CI/CD Starter</title></head>
    <body style="font-family: Arial, sans-serif; margin: 40px;">
      <h1>Hello from my Docker application!</h1>
      <p>My DevOps CI/CD starter web application is running.</p>
      <p>Check <a href="/health">/health</a> for application health.</p>
    </body></html>
    """

@app.get("/health")
def health():
    return jsonify(status="ok", app=os.getenv("APP_NAME", "devops-cicd-starter"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
