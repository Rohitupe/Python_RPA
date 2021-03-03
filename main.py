from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__)

info = []

@app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        title = request.form['email']
        author = request.form['password']
        content = request.form['date']
        
        info.append(title)

        return redirect(url_for('login_info'))
    else:
        return render_template('index.html')

@app.route('/info', methods=['GET', 'POST'])
def login_info():
    for i in info:
        return jsonify(
            title=i
        )

if __name__ == "__main__":
    app.run(debug=True)