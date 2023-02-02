from flask import Flask, render_template, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisvariable-can-change"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
boggle_game = Boggle()


# entry_list= {}
# first_board1 = boggle_game.make_board()

@app.route("/")
def main_page():
    """Main page for boggle"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("mainpage.html", board=board, highscore=highscore, nplays=nplays)

@app.route("/check-word")
def entry_check():
    """Checks the word to see if it is available on  the game board or not, has already been used or not."""
    word = request.args["word"]
    print (word)
    board = session["board"]
    # if "entry" not in session:
        # session['entry'] = []
        
    # session["entry"].append(entry)
    response = boggle_game.check_valid_word(board, word)
    # flash(response)
    # return redirect("/")

    return jsonify({'result': response})
    
@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)