from flask import render_template, request, redirect, url_for, session, flash
from app import app

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Login route with explicit endpoint 'admin_login'
@app.route('/login', methods=['GET', 'POST'], endpoint='admin_login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin123':
            session.permanent = True
            session['user'] = username
            return redirect(url_for('attendance'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('admin_login.html')

# Protected routes
@app.route('/attendance')
def attendance():
    if 'user' not in session:
        return redirect(url_for('admin_login'))
    return render_template('attendance.html')


@app.route('/employees')
def employees():
    if 'user' not in session:
        return redirect(url_for('admin_login'))
    return render_template('employees.html')

@app.route('/reports')
def reports():
    if 'user' not in session:
        return redirect(url_for('admin_login'))
    return render_template('reports.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out successfully', 'info')
    return redirect(url_for('admin_login'))
