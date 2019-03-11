from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    items = ["Iron", "Gold", "whatever else"]

    return render_template('home.html', Items=items)

if __name__ == "__main__":
    application.run()
