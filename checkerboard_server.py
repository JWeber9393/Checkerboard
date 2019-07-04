from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkerboard():
    print('*'*100)
    print("root route good!")
    return render_template("checkerboard.html")

@app.route("/<num>")
def checkerboard2(num):
    print('*'*100)
    print("num route good!")
    return render_template("checkerboard.html", num_times = int(num))

if __name__=="__main__":
    app.run(debug = True)