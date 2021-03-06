from flask import Flask, jsonify, render_template, request, redirect, url_for
import re
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def signup_page():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        date = request.form['date']
        first_name = request.form['fName']
        last_name = request.form['lName']
        gender = request.form['gender']
        postal_code = request.form['postalCode']

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
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0

                print(email, password, date, first_name, last_name, gender, postal_code)
                return render_template('success_message.html')
                break

        if flag == -1:
            return render_template('error_message.html')

    else:
        return render_template('index.')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        date = request.form['date']
        first_name = request.form['fName']
        last_name = request.form['lName']
        gender = request.form['gender']
        postal_code = request.form['postalCode']

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
            elif not re.search("[_@$]", password):
                flag = -1
                break
            elif re.search("\s", password):
                flag = -1
                break
            else:
                flag = 0

                print(email, password, date, first_name, last_name, gender, postal_code)
                return jsonify({
                    'id':1,
                    'email':email,
                    'password':password,
                    'date':date,
                    'first_name':first_name,
                    'last_name':last_name,
                    'gender':gender,
                    'postal_code':postal_code
                })
                break

        if flag == -1:
            return render_template('error_message.html')

    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
