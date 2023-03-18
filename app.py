from flask import Flask, render_template
app = Flask(__name__)

f = open('static/about.txt', mode="r")
data = f.read()
f.close()


@app.route('/')
def home():
    name = "Aruna"
    position = "{Python Developer}"
    intro = "Knowledge of Python web frameworks and Basic understanding of front-end technologies"
    return render_template('index.html', name=name, position=position, intro=intro)

@app.route('/about')
def about():
    return render_template('about.html', data=data)

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")




if __name__ == '__main__':
    app.run(debug=True)
    