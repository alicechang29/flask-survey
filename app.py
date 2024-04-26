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
    """
    Upon page load, returns a string of HTML that displays survey title and
    instructions
    """
    title = survey.title
    instructions = survey.instructions

    return render_template(
        "survey_start.jinja",
        title=title,
        instructions=instructions)


@app.post("/begin")
def begin_survey():
    """
    Upon survey start, resets RESPONSES list and redicts to current
    question page
    """
    global RESPONSES
    RESPONSES = []

    return redirect(f"/questions/0")


@app.get("/questions/<question_index>")
def show_question(question_index):
    """
    Displays the current survey question
    """
    question = survey.questions[int(question_index)]

    return render_template(
        "question.jinja",
        question=question,
    )


@app.post("/answer")
def handle_answer():
    """
    Takes user's survey answer and appends to RESPONSES list, redirects to
    the next available question or the thank you page
    """

    answer = request.form["answer"]
    RESPONSES.append(answer)

    next_question_index = len(RESPONSES)

    if len(RESPONSES) < len(survey.questions):
        return redirect(f"/questions/{next_question_index}")
    else:
        return redirect("/completion")


@app.get("/completion")
def show_completion():
    """
    Shows completion page with user's questions and answers
    """
    question_response_pair = {}
    for index, question in enumerate(survey.questions):
        question_response_pair[question.prompt] = RESPONSES[index]

    return render_template(
        "completion.jinja",
        question_response_pair=question_response_pair
    )
