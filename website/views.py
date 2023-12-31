from flask import Blueprint, render_template, make_response, jsonify, request
from .wordle.getWords import words
from .wordle.solve import getColors

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")


@views.route('/load')
def load():
    if request.args:

        g_word = request.args.get('w')
        n_word = request.args.get('n')

        if len(n_word) != 5:
            return make_response(jsonify({}), 200)

        colors = getColors(g_word, n_word)
        return make_response(jsonify(colors), 200)


@views.route('/word')
def word():
    new_word = words()
    return make_response(jsonify(new_word), 200)
