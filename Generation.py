import Constants
from Agent import Agent
import random as rand


def _produce_zygote(parent1, parent2, id_counter):
    gamete1 = parent1.provide_gamete()
    inheritance1 = parent1.provide_inheritance()
    gamete2 = parent2.provide_gamete()
    inheritance2 = parent2.provide_inheritance()
    average_gamete_fitness = (gamete1 + gamete2) / 2
    environmental_randomness = (rand.randint(
        (-1 * Constants.ENVIRONMENTAL_RANDOMNESS_RANGE), Constants.ENVIRONMENTAL_RANDOMNESS_RANGE
    ))
    zygote_fitness = average_gamete_fitness + environmental_randomness
    total_inheritance = inheritance1 + inheritance2
    new_child = Agent(agent_id=id_counter, fitness=zygote_fitness, inheritance=total_inheritance)
    return new_child


class Generation:
    def __init__(self):
        self.population_size = Constants.GENERATION_SIZE
        self.agents_list = []
        self.couples = []

    def __str__(self):
        output = ""
        for agent in self.agents_list:
            output += "\n" + str(agent)
        return str(output)

    def create_first_generation(self):
        for i in range(self.population_size):
            new_agent = Agent(agent_id=i)
            self.agents_list.append(new_agent)

    def create_next_generation(self, list_offspring):
        self.agents_list = list_offspring

    def maturate_generation(self):
        self._grow_old()
        self._create_couples()

    def have_children(self):
        return self._have_children()

    def _grow_old(self):
        for agent in self.agents_list:
            agent.grow_old()

    def _create_couples(self):
        singles_pool = self.agents_list.copy()
        num_singles_remaining = len(singles_pool)
        for i in range(int(self.population_size / 2)):
            agent_one_index = rand.randint(0, num_singles_remaining - 1)
            agent_one = singles_pool[agent_one_index]
            singles_pool.remove(agent_one)
            num_singles_remaining = len(singles_pool)
            agent_two_index = rand.randint(0, num_singles_remaining - 1)
            agent_two = singles_pool[agent_two_index]
            singles_pool.remove(agent_two)
            num_singles_remaining = len(singles_pool)
            self.couples.append([agent_one, agent_two])

    def _have_children(self):
        new_generation = []
        id_counter = 0
        for couple in self.couples:
            child1 = _produce_zygote(couple[0], couple[1], id_counter)
            id_counter += 1
            child2 = _produce_zygote(couple[0], couple[1], id_counter)
            id_counter += 1
            new_generation.append(child1)
            new_generation.append(child2)
        return new_generation



