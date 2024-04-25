Classes

Question
- single question on a survey
- includes:
    - prompt
    - list of choices (Yes, No)
    - allows comments option

Survey
- includes:
    - title
    - instructions
    - list of Question Instances
        - [q1, q2, ...]


satisfaction_survey
- is an instance of Survey Class
- `.question` attribute is list of instances of Question class

**QUESTIONS**
- how to see the instance and all the keys and values inside of it?

```python
satisfaction_survey.items()
satisfaction_survey.questions[0]

dir(satisfaction_survey)
#results in only the arguments?
```


Storing the Responses
- can't have it as a global variable bc doesn't scale

Need to use cookies to "keep state"



everytime taking a survey, we are creating an instance of a survey
when pressing begin, doing a blank slate of survey

upon survey start,
-   TODO: reset the array

find a way to determine what question we are on without using a global question variable