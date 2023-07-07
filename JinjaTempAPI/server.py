from flask import Flask, render_template
import requests

def getage(name):
    url = "https://api.agify.io"
    params = {
        "name": name
    }
    request = requests.get(url, params=params)
    data = request.json()
    return data["age"]

def getgender(name):
    url = "https://api.genderize.io"
    params = {
        "name": name
    }
    request = requests.get(url, params=params)
    data = request.json()
    return data["gender"]

app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    gender = getgender(name)
    age = getage(name)
    name = name
    return render_template("index.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)