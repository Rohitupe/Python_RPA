from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from Signup import sign_up, login_user

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
    postal_code = db.Column(db.Integer, nullable=False)

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
    print(len(data))

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
        postal_code = request.form['postalCode']


        # change date type from string to datetime.date
        date_type = datetime.strptime(date, "%Y-%m-%d")
        print(email, password, date_type, first_name, last_name, gender, postal_code)

        data = RPA.query.all()

        if len(data) == 0:
            newUser = RPA(email=email, password=password, date=date_type, first_name=first_name, last_name=last_name, gender=gender, postal_code=int(postal_code))
            db.session.add(newUser)
            db.session.commit()
        else:
            return render_template('error_message.html')

        sign_up(email, password, date_type, first_name, last_name, gender, postal_code)
        return redirect('/login')

    else:
        return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_data = RPALogin.query.all()
    print(len(login_data))

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

        print(lEmail, lPassword)

        login_data = RPALogin.query.all()

        if len(login_data) == 0:
            newUser = RPALogin(lEmail=lEmail, lPassword=lPassword)
            db.session.add(newUser)
            db.session.commit()
        else:
            return render_template('error_message.html')

        login_user(lEmail, lPassword)
        return render_template('success_message.html')

    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)