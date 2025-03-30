from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Corrected initialization

# Homepage route
@app.route("/")
def home():
    return render_template("home.html")  # Indentation fixed

# Contact form submission route
@app.route("/contact", methods=["POST"])
def contact():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Simulating backend processing
    print(f"Received message from {name} ({email}): {message}")

    # Redirect back to home page after submission
    return redirect(url_for("home"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
