from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def index():
    name=['莊孝維', '裝可愛', '莊英俊', '莊肥肥', 25]
    return render_template("index.jinja.html", names=name)
@app.route("/feature")
def feature():
    return render_template("feature.jinja.html")
@app.route("/description")
def description():
    return render_template("description.jinja.html")
@app.route("/product")
def product():
    return render_template("product.jinja.html")