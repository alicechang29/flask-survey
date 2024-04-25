from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []
CURRENT_QUESTION_INDEX = 0


@app.get("/")
def show_survey_start():
    title = survey.title
    instructions = survey.instructions

    return render_template(
        "survey_start.jinja",
        title=title,
        instructions=instructions)


# option: when start survey, pass in question index at 0
@app.post("/begin")
def begin_survey():

    global CURRENT_QUESTION_INDEX
    CURRENT_QUESTION_INDEX = 0

    return redirect(f"/questions/{CURRENT_QUESTION_INDEX}")


@app.get("/questions/<question_index>")
def show_question(question_index):

    question = survey.questions[int(question_index)]

    return render_template(
        "question.jinja",
        question=question
    )


@app.post("/answer")
def handle_answer():

    answer = request.form["answer"]  # I am not sure?? see form data
    RESPONSES.append(answer)

    global CURRENT_QUESTION_INDEX

    # if...else index < array.length
    CURRENT_QUESTION_INDEX = CURRENT_QUESTION_INDEX + 1
    return redirect(f"/questions/{CURRENT_QUESTION_INDEX}")
