import config_constants

# treatment variables
production_rounds = 3

# options 
# NO_PARTICIPATION: manager decides
# PARTICIPATION: worker decides
# NEGOTIATION: players negotiate
bonus_setting = config_constants.NO_PARTICIPATION
# bonus_setting = config_constants.PARTICIPATION

# can manager update bonus after round?
discretion = True

lira_per_dollar = 50    

probability_difficult = .2

# lira earnings per grid decoded
trivia_earnings = 20
manager_earnings = 10
worker_earnings = 5
manager_bonus_percentage = .1

pilot_worker_earnings = 2

worker_bonus = 200
manager_contrib = 20
# amount of worker bonus paid by the manager

# stats for instructions
pilot_percentage_one = '25'
pilot_grids_one = 'y'
pilot_percentage_two = '75'
pilot_grids_two = 'z'
pilot_participants = 30

participation_fee = 5