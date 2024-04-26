from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []  # it's still global but can be lower case, because not constant


@app.get("/")
def show_survey_start():
    """
    Upon page load, returns a string of HTML that displays survey title and
    instructions
    """
    title = survey.title                # just pass these over to the template to handle
    instructions = survey.instructions

    return render_template(
        "survey_start.jinja",
        title=title,
        instructions=instructions)


@app.post("/begin")
def begin_survey():
    """
    Upon survey start, resets RESPONSES list and redirects to current
    question page
    """
    global RESPONSES    # need global then it'd create a new response
    RESPONSES = []

    return redirect("/questions/0")


# /<query parameter> can change types
@app.get("/questions/<int:question_index>")
def show_question(question_index):
    """
    Displays the current survey question
    """
    question = survey.questions[question_index]

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
def show_completion():  # FIXME: survery_complete, because completion is akin to a state
    """
    Shows completion page with user's questions and answers
    """
    question_response_pair = {}  # FIXME: rename key_to_value
    # FIXME: check out jinja syntax for loop
    for index, question in enumerate(survey.questions):
        question_response_pair[question.prompt] = RESPONSES[index]

    return render_template(
        "completion.jinja",
        question_response_pair=question_response_pair
    )
