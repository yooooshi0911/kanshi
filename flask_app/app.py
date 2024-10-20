from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('form_example.html')

@app.route('/update', methods=['POST'])
def update():
    data = request.form['data']
    print(f"Current input: {data}")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)