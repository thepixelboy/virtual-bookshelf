from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

bookshelf = []


@app.route("/")
def home():
    return render_template("index.html", bookshelf=bookshelf)


@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["book_title"],
            "author": request.form["book_author"],
            "rating": request.form["book_rating"],
        }

        bookshelf.append(new_book)

        return redirect(url_for("home"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
