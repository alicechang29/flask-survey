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