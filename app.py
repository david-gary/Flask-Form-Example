from flask import Flask, render_template, request

app = Flask(__name__)

correct_count = 0


# GET requests at this URL will be handled by this function, but POST requests will not
@app.get('/')
def index():
    # reset the correct_count
    global correct_count
    correct_count = 0
    return render_template('index.html', correct_count=correct_count)


# POST requests at this URL will be handled by this function
@app.route('/form', methods=['POST'])
def form():
    # store name from form so other functions can access it
    global name
    name = request.form['name']
    return render_template('form.html', name=name)


# POST requests at this URL will be handled by this function, but not GET requests
@app.post('/results')
def results():
    global correct_count
    if request.form['number'] == '9354':
        correct_count += 1
    return render_template('results.html', name=name, correct_count=correct_count)


if __name__ == '__main__':
    app.run(debug=True)
