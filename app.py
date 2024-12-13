from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/images")
def images():
    return render_template("images.html")

@app.route("/audio")
def audio():
    return render_template("audio.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Process form data
        print(f"Name: {request.form['name']}")
        print(f"Email: {request.form['email']}")
        print(f"Message: {request.form['message']}")
        return redirect(url_for("index"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
