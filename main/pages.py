from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

import config_constants, config

from helpers import get_role, get_round_key, formatted_key

class DIntroduction(Page):
    def vars_for_template(self):
        return dict(
            pilot_percentage_one=config.pilot_percentage_one,
            pilot_grids_one=config.pilot_grids_one,
            pilot_percentage_two=config.pilot_percentage_two,
            pilot_grids_two=config.pilot_grids_two,
            pilot_participants=config.pilot_participants,
            worker_bonus=config.worker_bonus,
        )

    def is_displayed(self):
        return self.group.discretion


class NDIntroduction(Page):
    def vars_for_template(self):
        return dict(
            pilot_percentage_one=config.pilot_percentage_one,
            pilot_grids_one=config.pilot_grids_one,
            pilot_percentage_two=config.pilot_percentage_two,
            pilot_grids_two=config.pilot_grids_two,
            pilot_participants=config.pilot_participants,
            worker_bonus=config.worker_bonus,
        )

    def is_displayed(self):
        return not self.group.discretion


class NegotiationBonus(Page):
    live_method = 'live_target'

    def vars_for_template(self):
        return dict(
            # custom_role=self.player.custom_role,
            target_round=self.group.target_round,
            proposed_target=self.group.proposed_target,
            final_target=self.group.final_target,
            worker_bonus=config.worker_bonus,
        )

    def is_displayed(self):
        return self.group.bonus_setting == config_constants.NEGOTIATION


class NoParticipationBonus(Page):
    form_model = 'group'
    form_fields = ['final_target']

    def is_displayed(self):
        return self.player.role == Constants.manager_role and self.group.bonus_setting == config_constants.NO_PARTICIPATION

    def vars_for_template(self):
        return dict(
            worker_bonus=config.worker_bonus,
        )

class ParticipationBonus(Page):
    form_model = 'group'
    form_fields = ['final_target']

    def is_displayed(self):
        return self.player.role == Constants.worker_role and self.group.bonus_setting == config_constants.PARTICIPATION

    def vars_for_template(self):
        return dict(
            worker_bonus=config.worker_bonus,
        )

class ParticipationWait(WaitPage):
    body_text = "The worker is currently setting a target for his or her performance for this period. This performance target represents the number of grids the worker must correctly submit to be eligible for the bonus. Please wait."

    def is_displayed(self):
        return self.group.bonus_setting == config_constants.PARTICIPATION

# only the worker should see this
class NoParticipationWait(WaitPage):

    def is_displayed(self):
        return self.group.bonus_setting == config_constants.NO_PARTICIPATION

    # todo: this is not needed here right? 
    def vars_for_template(self):
        if self.player.role == Constants.worker_role:
            body_text = "The manager is currently setting a target for your performance for this period. This performance target represents the number of grids you must correctly submit to be eligible for the bonus. Please wait."
        else:
            body_text = "Waiting for the other participant."

        return dict(body_text=body_text)

class NegotiationWait(WaitPage):
    body_text = "Please wait for the manager."

    def is_displayed(self):
        return self.group.bonus_setting == config_constants.NEGOTIATION

class TargetResult(Page):
    timeout_seconds = 15

    def vars_for_template(self):
        return dict(
            # custom_role=self.player.custom_role,
            trivia_earnings=Constants.trivia_earnings,
        )

class PreGame(WaitPage):
    pass


class Game(Page):
    timeout_seconds = 120

    live_method = 'live_game'

    def vars_for_template(self):

        vars = dict(question=self.player.get_trivia_question())        

        key = formatted_key(self.round_number)

        self.player.difficult = self.group.difficult

        vars.update({
            # 'custom_role': self.player.custom_role,
            'difficult': self.player.difficult,
            'key': key,
        })

        return vars

def set_payoffs(group):
    """
    This function is for no discretion only treatment
    """

    players = group.get_players()
    for player in players:
        # calculate payoff
        player.calculate_payoff()

class PostGame(WaitPage):
    after_all_players_arrive = set_payoffs

class NDResults(Page):
    def vars_for_template(self):

        # vars for template
        vars = dict(
            # custom_role=self.player.custom_role,
            difficulty='difficult' if self.player.group.difficult else 'normal',
            standard_bonus=Constants.worker_bonus,
            standard_contrib=Constants.manager_contrib,
            manager_salary=Constants.manager_salary,
            worker_salary=Constants.worker_salary,
            manager_bonus_percentage=int(config.manager_bonus_percentage * 100),
            manager_bonus_contribution=self.group.bonus * Constants.manager_contrib_percentage,
            target_reached=self.group.target_reached(self.player),
            payoff_lira=self.player.payoff_lira,
            prob_difficult=int(config.probability_difficult * 100),
            prob_easy=int(100 - config.probability_difficult * 100),
        )

        if self.player.is_manager():
            vars['worker_decodes'] = self.group.get_worker().decodes_completed

        return vars

    def is_displayed(self):
        return not self.group.discretion

class DWorkerResults1(Page):
    # timeout_seconds = 60

    def is_displayed(self):
        return self.player.role == Constants.worker_role and self.group.discretion
    
    def vars_for_template(self):

        vars = dict(
            # custom_role=self.player.custom_role,
            difficulty='difficult' if self.player.group.difficult else 'normal',
            standard_bonus=self.group.bonus,
            standard_contrib=Constants.manager_contrib,
            manager_salary=Constants.manager_salary,
            worker_salary=Constants.worker_salary,
            manager_bonus_percentage=int(config.manager_bonus_percentage * 100),
            target_reached=self.group.target_reached(self.player),
            prob_difficult=int(config.probability_difficult * 100),
            prob_easy=int(100 - config.probability_difficult * 100)
        )

        if self.player.is_manager():
            vars['worker_decodes'] = self.group.get_worker().decodes_completed

        return vars

class DManagerResults1(Page):
    form_model = 'group'
    form_fields = ['bonus']

    def is_displayed(self):
        return self.player.role == Constants.manager_role and self.group.discretion
    
    def vars_for_template(self):

        vars = dict(
            # custom_role=self.player.custom_role,
            difficulty='difficult' if self.player.group.difficult else 'normal',
            standard_bonus=Constants.worker_bonus,
            standard_contrib=Constants.manager_contrib,
            manager_salary=Constants.manager_salary,
            worker_salary=Constants.worker_salary,
            manager_bonus_percentage=int(config.manager_bonus_percentage * 100),
            target_reached=self.group.target_reached(self.player),
            worker_bonus=config.worker_bonus,
            prob_difficult=int(config.probability_difficult * 100),
            prob_easy=int(100 - config.probability_difficult * 100)
        )

        if self.player.is_manager():
            vars['worker_decodes'] = self.group.get_worker().decodes_completed

        return vars

def discretion_payoff(group):
    players = group.get_players()
    for player in players:
        # calculate payoff
        player.apply_discretion()

# apply bonus function should only do one thing first of all
# chack bonuses when others are checked and set the default value then... do not add bonus to to blanace i dont think
# then make a different functino that upates the default bonuses if needed

class DiscretionWait(WaitPage):
    """This syncs group after the manager uses their discretion for worker bonus"""
    after_all_players_arrive = discretion_payoff

    def is_displayed(self):
        return self.group.discretion


class DResults2(Page):
    def vars_for_template(self):

        vars = dict(
            # custom_role=self.player.custom_role,
            difficulty='difficult' if self.player.group.difficult else 'normal',
            worker_bonus=self.group.bonus,
            bonus_contrib=self.group.bonus * Constants.manager_contrib_percentage,
            manager_bonus_percentage=int(config.manager_bonus_percentage * 100),
            manager_bonus_contribution=config.manager_bonus_percentage * self.group.bonus,
            manager_salary=Constants.manager_salary,
            worker_salary=Constants.worker_salary,
        )

        if self.player.is_manager():
            vars['worker_decodes'] = self.group.get_worker().decodes_completed

        return vars

    def is_displayed(self):
        return self.group.discretion

page_sequence = [
        DIntroduction, 
        NDIntroduction,
        NegotiationBonus,
        NoParticipationBonus,
        ParticipationBonus,
        ParticipationWait,
        NoParticipationWait,
        NegotiationWait,
        TargetResult,
        PreGame,
        Game,
        PostGame,
        NDResults,
        DWorkerResults1,
        DManagerResults1,
        DiscretionWait,
        DResults2,
    ]

# if config.discretion:
#     if config.bonus_setting == config_constants.NO_PARTICIPATION:
#         page_sequence = [DIntroduction, NoParticipationBonus, NoParticipationWait, TargetResult, PreGame, Game, PostGame, DWorkerResults1, DManagerResults1, DiscretionWait, DResults2]
#     elif config.bonus_setting == config_constants.PARTICIPATION:
#         page_sequence = [DIntroduction, ParticipationBonus, ParticipationWait, TargetResult, PreGame, Game, PostGame, DWorkerResults1, DManagerResults1, DiscretionWait, DResults2]
#     else:
#         page_sequence = [DIntroduction, NegotiationBonus, NegotiationWait, TargetResult, PreGame, Game, PostGame, DWorkerResults1, DManagerResults1, DiscretionWait, DResults2]
# else:
#     if config.bonus_setting == config_constants.NO_PARTICIPATION:
#         page_sequence = [NDIntroduction, NoParticipationBonus, NoParticipationWait, TargetResult, PreGame, Game, PostGame, NDResults]
#     elif config.bonus_setting == config_constants.PARTICIPATION:
#         page_sequence = [NDIntroduction, ParticipationBonus, ParticipationWait, TargetResult, PreGame, Game, PostGame, NDResults]
#     else:
#         page_sequence = [NDIntroduction, NegotiationBonus, NegotiationWait, TargetResult, PreGame, Game, PostGame, NDResults]
