"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    response = request.args.get("game")
    person = request.args.get("person")
    if response == "no":
        return render_template("goodbye.html", person=person)    
    return render_template("game.html", person=person)


@app.route("/madlib", methods=["POST"])
def show_madlib():
    name = request.form.get("name")
    colors = request.form.getlist("colors")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    story = request.form.getlist("story")

    return render_template("madlib.html", name=name, colors=colors, noun=noun, adjective=adjective, story=story)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
