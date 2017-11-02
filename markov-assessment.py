# markov-assessment.py
from markov import *  # see markov.py
from fractions import Fraction


# Instantiate the Markov Chain with 9 states (class Node)
chain = [Node(1), Node(2), Node(3),
         Node(4), Node(5), Node(6),
         Node(7), Node(8), Node(9)]

# Add links (class Link) between the states, with their transition probabilities
chain[0].add_links({Link(chain[3], Fraction("1/4")),   # Add a link from S(1) to S(4) with a transition probability of 1/4
                    Link(chain[1], Fraction("1/4"))})  # Same for S(1) to S(2)

chain[1].add_links({Link(chain[4], Fraction("1/4")),   # Repeat for each state
                    Link(chain[2], Fraction("1/4")),
                    Link(chain[0], Fraction("1/4"))})

chain[2].add_links({Link(chain[5], Fraction("1/4")),
                    Link(chain[1], Fraction("1/4"))})

chain[3].add_links({Link(chain[6], Fraction("1/4")),
                    Link(chain[4], Fraction("1/4")),
                    Link(chain[0], Fraction("1/8"))})

chain[4].add_links({Link(chain[7], Fraction("1/4")),
                    Link(chain[5], Fraction("1/4")),
                    Link(chain[1], Fraction("1/8")),
                    Link(chain[3], Fraction("1/4"))})

chain[5].add_links({Link(chain[8], Fraction("1/4")),
                    Link(chain[2], Fraction("1/8")),
                    Link(chain[4], Fraction("1/4"))})

chain[6].add_links({Link(chain[7], Fraction("1/4")),
                    Link(chain[3], Fraction("1/6"))})

chain[7].add_links({Link(chain[8], Fraction("1/4")),
                    Link(chain[4], Fraction("1/6")),
                    Link(chain[6], Fraction("1/4"))})

chain[8].add_links({Link(chain[5], Fraction("1/6")),
                    Link(chain[7], Fraction("1/4"))})

# Instantiate the Markov Chain Simulator
sim = MarkovSimulator(chain)

cell_1 = []  # list of results for cell 1
cell_3 = []  # cell 3
cell_9 = []  # cell 9

# Run simulation 10000 times with 3 time steps (Task 3)
print("Running simulation 10000 times with 3 time steps")
for i in range(0, 10000):
    sim.run(3)
    cell_1.append(sim.get_probabilities()[1]) if 1 in sim.get_probabilities() else cell_1.append(0)
    cell_3.append(sim.get_probabilities()[3]) if 3 in sim.get_probabilities() else cell_3.append(0)
    cell_9.append(sim.get_probabilities()[9]) if 9 in sim.get_probabilities() else cell_9.append(0)
    sim.flush_pb()

print("Probability to be in state 1: " + str(numpy.mean(cell_1)) + ", with a deviation of +/- " + str(numpy.std(cell_1)))
print("Probability to be in state 3: " + str(numpy.mean(cell_3)) + ", with a deviation of +/- " + str(numpy.std(cell_3)))
print("Probability to be in state 9: " + str(numpy.mean(cell_9)) + ", with a deviation of +/- " + str(numpy.std(cell_9)))


# Run the simulation again, but this time once for 1000000 time steps (Task 4)
sim.flush_pb()  # Restart the system
print("---------")

cell_1 = []
cell_3 = []
cell_9 = []

print("Running simulation once with 1 000 000 time steps (this can take a while)")
sim.run(1000000)

cell_1.append(sim.get_probabilities()[1]) if 1 in sim.get_probabilities() else cell_1.append(0)
cell_3.append(sim.get_probabilities()[3]) if 3 in sim.get_probabilities() else cell_3.append(0)
cell_9.append(sim.get_probabilities()[9]) if 9 in sim.get_probabilities() else cell_9.append(0)

print("'Steady state' probability to be in state 1: " + str(numpy.mean(cell_1)))
print("'Steady state' probability to be in state 3: " + str(numpy.mean(cell_3)))
print("'Steady state' probability to be in state 9: " + str(numpy.mean(cell_9)))

# Script output:
#
# Running simulation 10000 times with 3 time steps
# Probability to be in state 1: 0.524, with a deviation of +/- 0.263910969836
# Probability to be in state 3: 0.03525, with a deviation of +/- 0.107679791512
# Probability to be in state 9: 0.0, with a deviation of +/- 0.0
# ---------
# Running simulation once with 1 000 000 time steps (this can take a while)
# 'Steady state' probability to be in state 1: 0.0551309448691
# 'Steady state' probability to be in state 3: 0.0557129442871
# 'Steady state' probability to be in state 9: 0.166646833353
#
