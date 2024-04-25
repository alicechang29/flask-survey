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


# option: when start survey, pass in question index at 0
@app.post("/begin")
def begin_survey():
    """
    Upon survey start, resets current question index and redicts to current
    question page
    """
    global CURRENT_QUESTION_INDEX
    CURRENT_QUESTION_INDEX = 0

    return redirect(f"/questions/{CURRENT_QUESTION_INDEX}")


@app.get("/questions/<question_index>")
def show_question(question_index):
    """
    Displays the current survey question
    """
    question = survey.questions[int(question_index)]

    return render_template(
        "question.jinja",
        question=question
    )


@app.post("/answer")
def handle_answer():
    """
    Takes user's survey answer and appends to RESPONSES list
    """

    answer = request.form["answer"]
    RESPONSES.append(answer)

    global CURRENT_QUESTION_INDEX

    if len(RESPONSES) < len(survey.questions):
        CURRENT_QUESTION_INDEX = CURRENT_QUESTION_INDEX + 1
        return redirect(f"/questions/{CURRENT_QUESTION_INDEX}")

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
    # {question1: answer1
    #  q2:a2  }
    print("!!!!!!!QA PAIR", question_response_pair)

    return render_template(
        "completion.jinja",
        question_response_pair=question_response_pair
    )
