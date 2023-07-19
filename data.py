import requests
# used to get questions from ui, can add values to ui like below to customise

def generate_questions():
    params = {
        'amount': 10,
        'type': 'boolean'
    }
    url = 'https://opentdb.com/api.php'

    response = requests.get(url=url, params=params)
    # print(response.json())
    return response.json()['results']


# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
