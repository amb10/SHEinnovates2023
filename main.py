@app.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)