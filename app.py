from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure upload folder (for future media uploads)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        # Handle form submission (future expansion can store this data in a database)
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # For now, just print the data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        
        # Redirect back to home after submission
        return redirect(url_for("index"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
