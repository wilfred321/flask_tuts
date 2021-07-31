from flask import Flask,render_template,request,session
from flask_session import Session
import datetime

app = Flask(__name__)
app.debug = True

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
Session(app)

# @app.route("/")
# def base():
#     return "<h1>Hello, Viewer, Welcome to my website!</h1>"


# now = datetime.datetime.now()
# new_year = now.month == 1 and now.day == 1
# new_year = True
# # if new_year:
# #     print("Yes, It is new year")
# # else:
# #     print("Oops! It is not new year yet.")

# # @app.route("/")
# # def index():
# #     return render_template("index.html",new_year = new_year)


# @app.route("/index")
# def index():
#     names = ['Ali',"Jenn","Bob","Kaise"]
#     return render_template('index.html',names = names)

# @app.route("/more")
# def more():
#     return render_template('more.html')


# @app.route("/hello", methods = ["GET","POST"])
# def hello():
#     if request.method == "GET":
#         return "Please submit the form instead"
#     else:
#         name = request.form.get('name')
#         return render_template("hello.html",name = name)

notes = []

@app.route("/", methods = ["GET","POST"])
def notebook():
    if session.get("notes") == None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("notebook.html",notes = session["notes"])
