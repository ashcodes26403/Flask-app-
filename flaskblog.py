from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Ashmit Sinha',
        'Title' : 'Blog 1',
        'content' : 'First Content',
        'date' : 'Jan 9th 2023'
    },
    {
        'author' : 'Oscar Sinha',
        'Title' : 'Blog 2',
        'content' : 'Second Content',
        'date' : 'Jan 10th 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')



if __name__ == '__main__':
    app.run(debug=True)