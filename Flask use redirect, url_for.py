
from flask import Flask, redirect, url_for

a = Flask(__name__)

@a.route("/hi")
def hi():
    return "Hey... Welcome..."

@a.route("/hello")
def hel():
    return "Hello User Team..."

def greet():
    return "Hey... Good Morning to all...!"
a.add_url_rule("/Greeting", view_func=greet)

# _______________________________________________________
# Veriable <name>
@a.route("/<name>")
def vs(name):
    return f"Welcome : {name}"

@a.route("/admin")
def anu():
    return f"Hello admin"

@a.route("/user/<other>")
def max(other):
    return f"Hello user {other}"

@a.route("/welcome/<person>")
def pers_on(person):
    if person=="admin":
        return redirect(url_for("anu"))
    else:
        return redirect(url_for("max", other=person))

if __name__=="__main__":
    a.run()