
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template('index.html')

@app.route("/check_password", methods=['POST'])
def check_password():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"Username: {username}, Password: {password}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
