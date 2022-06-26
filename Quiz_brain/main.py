import requests
import json
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []


def get_data_from_api():
    """Get the data with api request"""
    parameters = {
        'amount': 10,
        'type': 'boolean'
    }
    response = requests.get(url='https://opentdb.com/api.php', params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['results']


def write_data_to_file():
    """Write the fetched data into the file"""
    data_dict = get_data_from_api()
    try:
        with open('data.py', 'w') as file:
            file.write(f'question_data = {json.dumps(data_dict, indent=4)}')
    except FileNotFoundError:
        print('No Data was found')


if __name__ == '__main__':
    # fetch the question into the data bank
    write_data_to_file()
    # arrange the question against the correct answer
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    # initialize the outer classes
    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)


