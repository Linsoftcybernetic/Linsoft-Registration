from flask import Flask,request,render_template,request, redirect, url_for, flash,jsonify
import mysql.connector
# from flask_wtf import FlaskForm
# from wtforms import StringField, TelField,validators,TextAreaField,ValidationError
from flask_cors import CORS
from mysql.connector import Error
import os
import smtplib
# import imghdr
from email.message import EmailMessage

app=Flask(__name__)
CORS(app)
app = Flask(__name__)
app.config['SECRET-KEY'] = "jadesql_password"
app.secret_key = 'your_secret_key_here'  

# Database configuration
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Onuchukwu12!",
    "database": "linsoft"
}

def get_db():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Connection to database Error: {e}")
        return None
    
def mail(to_email,subject, body):
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # contacts = ['joy49867@gmail.com', 'philipobinna871@gmail.com', 'martinsonuchukwuchimdinyerem@gmail.com']


    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'jadevictor247@gmail.com'
    msg['To'] = to_email

    msg.set_content(body,'plain')

    # msg.add_alternative("""\
    # <!DOCTYPE html>
    # <html>
    #     <body>
    #         <h1 style="color:SlateGray;">This is an HTML Email using python smtp!</h1>
    #     </body>
    # </html>
    # """, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('jadevictor247@gmail.com', 'rfhi sawh bgjo itda')
            smtp.send_message(msg)
    except Exception as e:
        flash ('Failed to send email')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# @app.route('/courses/', methods=['GET'])
# def courses():
#     connection=get_db()
#     if connection is None:
#         return jsonify({'success':False, 'message': 'Error', 'data': ''}),500
#     try:
#         with connection.cursor(dictionary=True) as cursor:
#             cursor.execute("SELECT * FROM courses")
#             result = cursor.fetchall()
#             return jsonify({'success':True, 'message': 'connection succesful', 'data': result})
#     except Error as e:
#         return jsonify({"success": False, "message": str(e), 'data': ''}),500
#     finally:
#         connection.close()

@app.route('/register/', methods=['GET', 'POST'])
def register():
    # Payment proccessor comes first before registration
        # --- write your code here ---
    # End of payment proccessor
    
    connection = get_db()
    if connection is None:
        flash('Database connection failed!', 'error')
        return redirect(url_for('register'))
        # return jsonify({'success': False, 'message': 'db error', 'data': ''})
    
    items = []  # Initialize items with an empty list
    selected_item = None  # Initialize selected_item with None
    selected_course_name = None  # Initialize selected_id with None
    
    try:
        with connection.cursor() as cursor:
            # for linsoft_course
            # Fetch all items for the dropdown on page load
            cursor.execute("SELECT id, course_name FROM linsoft_course")
            items = cursor.fetchall()
            # print(items)

            if request.method == 'POST':
                action = request.form.get('action')

                if action == 'select_course' and 'course_name' in request.form:
                    selected_course_name = request.form.get('course_name')
                    cursor.execute("SELECT duration, instructor, cost FROM linsoft_course WHERE course_name = %s", (selected_course_name,))
                    selected_item = cursor.fetchone()
                    return render_template('register.html', items=items, selected_item=selected_item)
                
                # Handle form submission and insert data into the database
                fname = request.form.get('fname')
                lname = request.form.get('lname')
                gender = request.form.get('gender')
                email = request.form.get('email')
                phone = request.form.get('phone')
                country = request.form.get('country')
                state = request.form.get('state')
                city = request.form.get('city')
                course = request.form.get('course_name')
                refer = request.form.get('refer')
                duration = request.form.get('duration')
                instructor = request.form.get('instructor')
                amount = request.form.get('amount')
                
                """ print(f"Duration: {duration}")
                print(f"Instructor: {instructor}")
                print(f"Amount: {amount}") """

                # for student
                sql = """INSERT INTO student (first_name, last_name, gender, email, phone, country, state, city, referral_email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = (fname, lname, gender, email, phone, country, state, city, refer)
                cursor.execute(sql, val)
                connection.commit()
                student_id=cursor.lastrowid
                
                # # for course
                sql = """INSERT INTO course (student_id, name, duration, cost, instructor)
                        VALUES (%s, %s, %s, %s, %s)"""
                val = (student_id, course, duration,  amount, instructor)
                cursor.execute(sql, val)
                connection.commit()
                student_id=cursor.lastrowid
                
                # for email
                subject = 'Registration Confirmation'
                body = f"Dear {fname.upper()}, \n\nThank you for registering for the course: {course}.\nDuration: {duration}\nInstructor: {instructor}\nAmount: {amount}\n\nEnjoy your learning, see you in class soon.\n\nBest regards,\nThe Team"
                mail(email, subject, body)
                
                flash('Your Registration is Successful. \n\nCheck your mail for more details.', 'success')
                return redirect(url_for('register'))
            
    except Error as e:
        flash('Registration Unsuccessful', 'danger')
        print(f"Error: {e}")
        # return jsonify({'success':False, 'message': str(e), 'data': ''})
    finally:
        connection.close()
    return render_template('register.html', items=items, selected_item=selected_item, selected_course_name=selected_course_name)

# def mail():
if __name__ == "__main__":
    app.run(debug=True)
    