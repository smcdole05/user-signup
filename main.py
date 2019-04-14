from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('welcome_form.html')

@app.route("/welcome")
def welcome():
    #take name from request
    username = request.args.get('user_name')
    return render_template("welcome_greeting.html", name=username)

@app.route("/", methods=['POST'])
def validate_signup():

    username = request.form['user_name']
    password = request.form['password']
    password_check = request.form['confirm_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_check_error = ''
    email_error = ''

    #username 
    #do not leave blank
    #must be between 3 and 20 characters, no spaces
    #perserve what the user types
    if username == '':
        username_error = "That is not a valid username"
        username = ''
    elif " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Username must not contain spaces, and must be between 3-20 characters"
        username = ''

    #password 
    #same requirements as username
    #must match with password confirmation
    #clear field if error occurs
    if password == '':
        password_error = "That is not a valid password"
        password = ''
    elif " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Username must not contain spaces, and must be between 3-20 characters"
        password = ''

    #additional password verification field
    #must match with password
    #clear field if error occurs
    if password_check == '':
        password_check_error = "That password does not match"
        password_check = ''
    elif " " in password_check or len(password_check) < 3 or len(password_check) > 20:
        password_check_error = "That password does not match"
        password_check = ''

    #optionally an email
    #may be empty
    #must have a single @
    #must have a single .
    #contains no spaces
    #between 3 and 20 characters long
    #preserve what the user types
    if len(email) > 0 and len(email) < 3 or len(email) > 20:
        email_error = "Email length must be between 3 and 20 characters"
        email = ""
    elif " " in email:
        email_error = "Email must not contain spaces"
        email = ""
    else:
        symbol_count = 0
        period_count = 0
        for char in email:
            if char == '@':
                symbol_count += 1
            if symbol_count > 1:
                email_error = "Email must contain no more than one @ or ."
                email = ""
            if char == '.':
                period_count += 1
            if period_count > 1:
                email_error = "Email must contain no more than one @ or ."
                email = ""
    
    if not username_error and not password_error and not password_check_error and not email_error:
        return redirect('/welcome?user_name={0}'.format(username))
    else:
        return render_template('welcome_form.html', username_error=username_error,
               password_error=password_error, password_conf_error=password_check_error,
               email_error=email_error, username=username, email=email)



        



app.run()