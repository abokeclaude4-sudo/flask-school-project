from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            return render_template('dashboard.html')
        else:
            return "Invalid credentials"

    return render_template('login.html')


# Change Password Page
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            return "New passwords do not match"

        if current_password == "1234":
            return "Password changed successfully"
        else:
            return "Current password is incorrect"

    return render_template('change_password.html')


# Run App
if __name__ == '__main__':
    app.run(debug=True)