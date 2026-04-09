from flask import Flask, redirect, url_for

m=Flask(__name__)

@m.route("/h")
def new():
    return "hello World"

@m.route("/hi")
def gr():
    return "hello"

def gre():
    return "hi"
m.add_url_rule('/hello',view_func=gre)

# variable <a>
@m.route("/<name>")
def vb(name):
    return f"hello {name}" 

@m.route("/admin")
def ad():
    return f"hello admin"


@m.route("/user/<n>")
def us(n):
    return f"hello user {n}"

@m.route("/guest/<na>")
def name(na):
    if na=="admin":
        return redirect(url_for("ad"))
    else:
        return redirect(url_for("us",n=na))
if __name__=="__main__":
    m.run()