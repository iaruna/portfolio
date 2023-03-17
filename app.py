from flask import Flask, render_template
app = Flask(__name__)

f = open('static/about.txt', mode="r")
data = f.read()
f.close()

@app.route('/')
def home():
    name = "Aruna"
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    