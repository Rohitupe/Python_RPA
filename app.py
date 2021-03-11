from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date as d
from Signup import sign_up, login_user
import re

app = Flask(__name__)

# database setup
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///rpa.db'
db = SQLAlchemy(app)


# database model
# Signup Info Table
class RPA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(50), default='N/A')
    postal_code = db.Column(db.String(6), nullable=False, default="W1F7NU")

    def __repr__(self):
        return f"{self.first_name} {self.last_name} = {self.id}"


# Login Info table
class RPALogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lEmail = db.Column(db.String(200), nullable=False)
    lPassword = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.id} = {self.lEmail}"


@app.route("/", methods=['GET', 'POST'])
def signup():
    data = RPA.query.all()
    # print(len(data))

    if request.method == "GET":
        # delete all records
        data = RPA.query.all()
        if len(data) != 0:
            db.session.query(RPA).delete()
            db.session.commit()

    if request.method == "POST":
        # create only single record
        email = request.form['email']
        password = request.form['password']
        date = request.form['date']
        first_name = request.form['fName']
        last_name = request.form['lName']
        gender = request.form['gender']
        # postal_code = request.form['postalCode']

        # change date type from string to datetime.date
        date_type = datetime.strptime(date, "%Y-%m-%d")
        # print(email, password, date_type, first_name, last_name, gender, postal_code)
        # print(email, password, date_type, first_name, last_name, gender)

        data = RPA.query.all()

        # if len(data) == 0:
        #     if (d.today().year - date_type.year) > 16:
        #         # newUser = RPA(email=email, password=password, date=date_type, first_name=first_name, last_name=last_name, gender=gender, postal_code=int(postal_code))
        #         newUser = RPA(email=email, password=password, date=date_type, first_name=first_name,
        #                       last_name=last_name, gender=gender)
        #         db.session.add(newUser)
        #         db.session.commit()
        # else:
        #     return render_template('error_password.html')

        if (d.today().year - date_type.year) > 16:
            flag = 0
            while True:
                if (len(password) < 8):
                    flag = -1
                    break
                elif not re.search("[a-z]", password):
                    flag = -1
                    break
                elif not re.search("[A-Z]", password):
                    flag = -1
                    break
                elif not re.search("[0-9]", password):
                    flag = -1
                    break
                else:
                    flag = 0
                    sign_up(email, password, date_type, first_name, last_name, gender, 'W1F7NU')

                    return redirect('/login')

            if flag == -1:
                return render_template('error_password.html')
        else:
            return render_template('error_age.html')
    else:
        return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_data = RPALogin.query.all()
    # print(len(login_data))

    if request.method == "GET":
        # delete all records
        login_data = RPALogin.query.all()
        if len(login_data) != 0:
            db.session.query(RPALogin).delete()
            db.session.commit()

    if request.method == "POST":
        # create only single record
        lEmail = request.form['lEmail']
        lPassword = request.form['lPassword']

        # print(lEmail, lPassword)

        # login_data = RPALogin.query.all()

        # if len(login_data) == 0:
        #     newUser = RPALogin(lEmail=lEmail, lPassword=lPassword)
        #     db.session.add(newUser)
        #     db.session.commit()
        # else:
        #     return render_template('error_password.html')

        flag = 0
        while True:
            if len(lPassword) < 8:
                flag = -1
                break
            elif not re.search("[a-z]", lPassword):
                flag = -1
                break
            elif not re.search("[A-Z]", lPassword):
                flag = -1
                break
            elif not re.search("[0-9]", lPassword):
                flag = -1
                break
            else:
                flag = 0
                login_user(lEmail, lPassword)
                return render_template('success_message.html')

        if flag == -1:
            return render_template('login_error_password.html')

    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
