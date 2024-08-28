from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import time
import random
import threading

app = Flask(__name__)
app.secret_key = 'TmljZSB0cnksIGJ1dCB5b3VyIGZsYWcgaXMgaW4gYW5vdGhlciBjYXN0bGUK'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User database simulation
users = {
    'CipherBre4ker': <redacted>
}

# User class
class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None

# To keep track of the hacking simulation status
hacking_status = {"running": False, "messages": []}

def hacking():
    global hacking_status
    hacking_status["running"] = True
    hacking_status["messages"] = []

    time.sleep(2)
    hacking_status["messages"].append("Connecting to the target system...")
    time.sleep(2)
    hacking_status["messages"].append("Scanning network...")
    time.sleep(2)

    for _ in range(5):
        hacking_status["messages"].append(f"Accessing node: {random.randint(1000, 9999)}")
        time.sleep(random.uniform(0.5, 1.5))

    hacking_status["messages"].append("Hacking attempt in progress...")
    time.sleep(3)
    hacking_status["messages"].append("Error: Unauthorized access attempt detected!")
    time.sleep(2)
    hacking_status["messages"].append("Connection terminated.")
    hacking_status["running"] = False

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/start')
@login_required
def start_hacking():
    if not hacking_status["running"]:
        thread = threading.Thread(target=hacking)
        thread.start()
        return jsonify({"status": "Hacking started!"})
    else:
        return jsonify({"status": "Hacking already running!"})

@app.route('/status')
@login_required
def status():
    return jsonify(hacking_status)

if __name__ == '__main__':
    app.run(debug=True)
