import config_constants

# treatment variables
production_rounds = 2 #10

# options 
# NO_PARTICIPATION: manager decides
# PARTICIPATION: worker decides
# NEGOTIATION: players negotiate
# bonus_setting = config_constants.NO_PARTICIPATION
bonus_setting = config_constants.NEGOTIATION

# can manager update bonus after round?
discretion = True

lira_per_dollar = 30

probability_difficult = .2

# lira earnings per grid decoded
trivia_earnings = 20
manager_earnings = 10
manager_salary = 100
worker_earnings = 5
worker_salary = 100
manager_bonus_percentage = .1

pilot_worker_earnings = 2

worker_bonus = 150
manager_contrib = 15
# amount of worker bonus paid by the manager

# stats for instructions
pilot_percentage_one = '75'
pilot_grids_one = '22'
pilot_percentage_two = '25'
pilot_grids_two = '29'
pilot_participants = 35

participation_fee = 5