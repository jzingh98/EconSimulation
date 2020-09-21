import Constants
from Generation import Generation
from prettytable import PrettyTable


class Simulator:
    def __init__(self):
        self.num_generations = Constants.NUM_GENERATIONS
        self.current_generation_index = 0
        self.generations_stack = []

    def __str__(self):
        counter = 0
        output = ""
        for generation in self.generations_stack:
            output += "\n\n\nGENERATION " + str(counter) + "\n---------------"
            output += str(generation)
            counter += 1
        return str(output)

    def print_table(self):
        counter = 0
        for generation in self.generations_stack:
            print("\n\n\nGENERATION " + str(counter) + "\n---------------")
            x = PrettyTable()
            x.field_names = ["ID", "Fitness", "Wealth"]
            for agent in generation.agents_list:
                x.add_row([agent.id, agent.fitness, agent.assets_final])
            print(x)
            counter += 1

    def print_statistics(self):
        counter = 0
        x = PrettyTable()
        x.field_names = ["Generation", "Avg Fitness", "Avg Wealth"]
        for generation in self.generations_stack:
            fitness_sum = 0
            wealth_sum = 0
            for agent in generation.agents_list:
                fitness_sum += agent.fitness
                wealth_sum += agent.assets_final
            fitness_avg = fitness_sum/Constants.GENERATION_SIZE
            wealth_avg = wealth_sum/Constants.GENERATION_SIZE
            x.add_row([counter, fitness_avg, wealth_avg])
            counter += 1
        print(x)

    def run_simulation(self):
        offspring = []
        while self.current_generation_index < self.num_generations:
            if self.current_generation_index == 0:
                current_generation = self._create_first_generation()
            else:
                current_generation = self._create_next_generation(offspring)
            current_generation.maturate_generation()
            offspring = current_generation.have_children()
            self.generations_stack.append(current_generation)
            self.current_generation_index += 1

    def _create_first_generation(self):
        first_generation = Generation()
        first_generation.create_first_generation()
        return first_generation

    def _create_next_generation(self, offspring):
        next_generation = Generation()
        next_generation.create_next_generation(offspring)
        return next_generation


