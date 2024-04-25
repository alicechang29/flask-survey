from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []


@app.get("/")
def show_survey_start():
    title = survey.title
    instructions = survey.instructions

    return render_template(
        "survey_start.jinja",
        title=title,
        instructions=instructions)


# fires at page load
@app.get("/questions/<question_index>")
def show_question(question_index):

    question = survey.questions[int(question_index)]

    return render_template(
        "question.jinja",
        question=question
    )
