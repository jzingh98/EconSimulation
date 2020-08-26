import Constants
import numpy as np


def _default_fitness():
    return np.random.normal(Constants.DEFAULT_FITNESS_MEAN, Constants.DEFAULT_FITNESS_STD, None)


def _default_inheritance():
    return np.random.normal(Constants.DEFAULT_FITNESS_MEAN, Constants.DEFAULT_FITNESS_STD, None)


class Agent:
    def __init__(self, agent_id, fitness=_default_fitness(), inheritance=_default_inheritance()):
        self.id = agent_id
        self.fitness = fitness
        self.earnings = 0
        self.assets_initial = inheritance
        self.assets_final = 0

    def __str__(self):
        output = "ID: " + str(self.id) + "\nFitness: " + str(self.fitness) + "\nWealth: " + str(self.assets_final)
        return output

    def provide_gamete(self):
        gamete_fitness = np.random.normal(self.fitness, Constants.GAMETE_FITNESS_STD, None)
        return gamete_fitness

    def provide_inheritance(self):
        provided_inheritance = self.assets_final * Constants.PROPORTION_GIVING_AS_INHERITANCE
        return provided_inheritance

    def grow_old(self):
        self.assets_final = self._exploit_inheritance()
        self.earnings = self._exploit_fitness()

    def _exploit_inheritance(self):
        accumulated_investments = self.assets_initial * \
                                  ((1 + Constants.AVERAGE_ASSET_RETURN) ** Constants.AVERAGE_ASSET_LIFESPAN)
        return accumulated_investments

    def _exploit_fitness(self):
        accumulated_career_success = Constants.CAREER_SUCCESS_CONSTANT * \
                                     (Constants.CAREER_SUCCESS_EXPONENTIAL ** self.fitness)
        return accumulated_career_success

