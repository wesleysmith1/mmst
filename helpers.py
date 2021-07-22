import keys
from keys import generate_key
import questions
from config_constants import QUESTIONS_PER_ROUND
import config

def get_role(participant_id):
    return 'worker' if participant_id % 2 else 'manager'

def get_round_key(round_number):
    key = eval(f"keys.round_{round_number}")
    return key

def get_pilot_key(round_number):
    key = eval(f"keys.pilot_{round_number}")
    return key

def formatted_key(round_number):
    key = get_round_key(round_number)
    nums = list(key.values())
    num_row1, num_row2 = nums[:13], nums[13:]
    letters = list(key.keys())
    letter_row1, letter_row2 = letters[:13], letters[13:]

    key = dict(
        numbers=nums,
        num_row1=num_row1,
        num_row2=num_row2,
        letter_row1=letter_row1,
        letter_row2=letter_row2,
    )
    return key

def formatted_pilot_key(round_number):
    key = get_pilot_key(round_number)
    nums = list(key.values())
    num_row1, num_row2 = nums[:13], nums[13:]
    letters = list(key.keys())
    letter_row1, letter_row2 = letters[:13], letters[13:]

    key = dict(
        numbers=nums,
        num_row1=num_row1,
        num_row2=num_row2,
        letter_row1=letter_row1,
        letter_row2=letter_row2,
    )
    return key