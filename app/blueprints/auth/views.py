from flask import request, redirect, url_for, render_template, flash
from app.blueprints.auth.models import User
from flask_login import login_user, logout_user, current_user, login_required
from app.blueprints.auth import bp as auth_bp 
from app import db

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_email = request.form['email']
        form_password = request.form['password']
        
        user = User.query.filter_by(email=form_email).first()
        
        if user is not None and user.verify_password_hash(form_password):
            login_user(user) # allow log a user in, pass in the user info 
            flash('User successfully logged in', 'success') #has to be displayed using jinja 
            return redirect(url_for('main.home'))

        flash('There was an error logging in. Try again.', 'danger')
        return redirect(url_for('auth.login'))
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST']) #by default = GET, read/get html on server to display on browser, post info to our server in return 
def register():
    if request.method == 'POST':
        res = request.form
        if res['confirm_password'] == res['password']:
            u = User(first_name=res['first_name'], last_name=res['last_name'], password=res['password'])
            u.save()
        return redirect(url_for('auth.login'))
        print(res) #only print if we 'POST' try to send form data 
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User logged out successfully', 'info') #info is blue color
    return redirect(url_for('auth.login'))

@auth_bp.route('/follow')
@login_required
def follow():
    user_id = request.args.get('user_id')
    u = User.query.get(user_id)

    current_user.follow(u)
    flash(f'You have followed the {u.first_name} {u.last_name}', 'success')
    return redirect(url_for('main.explore'))

@auth_bp.route('/unfollow')
@login_required
def unfollow():
    user_email = request.args.get('email')
    u = User.query.filter_by(email=user_email).first()

    current_user.unfollow(u)
    flash(f'You have unfollowed the {u.first_name} {u.last_name}', 'info')
    return redirect(url_for('main.explore'))

@auth_bp.route('/update', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user = User.query.get(current_user.id)
        form = request.form #store all the "name" as dict keys
        if form['password'] and form['confirm_password']:
            if form['password'] == form['confirm_password']:
                user.password = form['password']
                user.create_password_hash(user.password)
        user.first_name = form['first_name']
        user.last_name = form['last_name']

        db.session.commit()
        flash("User's information has updated successfully", 'success')
    return redirect(url_for('main.profile'))