from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home3.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    processed_text = text.upper()
    return render_template("bienvenue.html" , message = processed_text )

if __name__ == '__main__':
   app.run(debug=True)