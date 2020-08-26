import Constants
from Generation import Generation


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


