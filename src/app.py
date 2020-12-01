from flask import Flask, render_template
app = Flask(__name__)

forms = [
    {
        'title' : 'web development',
        'question' : 'Quality and value of user inferfaces.'
    },
    {
        'title' : 'security',
        'question' : 'Quality, value, and speed of secuiryt services.'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', forms=forms)

@app.route('/home/form')
def form():
    return render_template('form.html', forms=forms)

if __name__ == '__main__':
    app.run(debug=True)