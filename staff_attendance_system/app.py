from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # needed for sessions and flash messages

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'], endpoint='admin_login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin123':
            session['user'] = username
            return redirect(url_for('attendance'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('admin_login.html')

# Attendance page (protected)
@app.route('/attendance')
def attendance():
    if 'user' not in session:
        return redirect(url_for('admin_login'))
    return render_template('attendance.html')

# Employees page (protected)
@app.route('/employees')
def employees():
    if 'user' not in session:
        return redirect(url_for('admin_login'))
    return render_template('employees.html')

# Reports page (protected)
@app.route('/reports')
def reports():
    if 'user' not in session:
        return redirect(url_for('admin_login'))
    return render_template('reports.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)

