from Generation import Generation

myGeneration = Generation()
myGeneration.create_first_generation()
print(myGeneration.agents_list)

myGeneration._create_couples()

print(myGeneration.couples)
