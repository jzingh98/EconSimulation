import random as rand
import numpy as np
import Constants

class Agent:
    def __init__(self,):
        self.fitness = 0
        self.assets_initial = 0
        self.assets_final = 0

    def provide_gamete(self):
        gamete_fitness = np.random.normal(self.fitness, Constants.GAMETE_FITNESS_STD, None)
        return gamete_fitness

    def provide_inheritance(self):
        provided_inheritance = self.assets_final * Constants.PROPORTION_GIVING_AS_INHERITANCE
        return provided_inheritance

    def grow_old(self):
        investments = self._exploit_assets()

    def _exploit_assets(self):
        accumulated_investments = self.assets_initial * (1 + Constants.AVERAGE_ASSET_RETURN) ** Constants.AVERAGE_ASSET_LIFESPAN
        return accumulated_investments

    def _exploit_fitness(self):
        accumulated_career_success = Constants.CAREER_SUCCESS_CONSTANT * (1.05 ** Constants.CAREER_SUCCESS_EXPONENTIAL)
        return accumulated_career_success



