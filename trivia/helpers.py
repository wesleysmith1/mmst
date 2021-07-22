import html
import requests
import random

def get_token():
    data = requests.get('https://opentdb.com/api_token.php?command=request')
    data =  data.json()

    if data['response_code'] == 0:
        return data['token']
    else:
        raise ValueError(f"Invalid response from opentdb.com while retrieving token: {data}")

    return data['token']

def replace(x):
    # replace characters that didn't decode properly with correct ones
    # x = x.replace("&quot;", '"')
    # x = x.replace("&#039;", "'")
    return html.unescape(x)

def clean(x):
    if type(x) == list:
        result = []
        for i in x:
            result.append(replace(i))
        return result
    else:
        return replace(x)

def get_question(token):

    if not token:
        token=''
    # &quot; &#039;
    data = requests.get(f'https://opentdb.com/api.php?amount=1&type=multiple&token={token}')

    data = data.json()

    if data['response_code'] == 0:
        question = clean(data['results'][0]['question'])

        correct_answer = clean(data['results'][0]['correct_answer'])

        answers = clean(data['results'][0]['incorrect_answers'])

        answers.append(correct_answer)
        random.shuffle(answers)
        return dict(
            question=question, 
            solution=correct_answer, 
            options=answers,
        )
    else:
        raise ValueError(f"Invalid response from opentdb.com: {data}")