# markov.py
import numpy


class Link:  # Represents a link from one state to another
    def __init__(self, node_to, probability):
        self.node_to = node_to
        self.probability = probability


class Node:  # Represents a state in the Markov chain
    def __init__(self, data, links=None):
        self.node_links = links or []
        self.node_data = data

    def add_link(self, link):
        self.node_links.append(link)

    def add_links(self, links):
        for l in links:
            self.node_links.append(l)


def get_random_node(node):  # returns the next state to witch the system transits to
    p_list = []
    is_prop = 0

    # gather all possible links
    for n in node.node_links:
        p_list.append(n.probability)
        is_prop += n.probability

    # check whether our transitions probabilities equal to one
    if is_prop < 1:
        # if not, add the probability to "stay in the same state" (a.k.a "rejection")
        p_list.append(1 - is_prop)
        node.add_link(Link(node, 1 - is_prop))

    # choose a random transition (including to "stay in the same state" based on probabilities p=p_list
    return numpy.random.choice(numpy.arange(0, len(node.node_links)), p=p_list)


class MarkovSimulator:
    def __init__(self, node_list):
        self.node_list = node_list
        self.current_node = node_list[0]
        self.probabilities = {}

    def flush_pb(self):
        self.probabilities = {}

    def get_probabilities(self):
        p = {}
        total = 0
        for pb in self.probabilities:
            total += self.probabilities[pb]

        for pb in self.probabilities:
            p.update({pb: float(float(self.probabilities[pb])/float(total))})
        return p

    def run(self, i=1000):  # Markov simulation, i is the number of steps
        self.current_node = self.node_list[0]  # Start the simulation at S(1)
        if self.probabilities.has_key(self.current_node.node_data):
            self.probabilities[self.current_node.node_data] += 1
        else:
            self.probabilities.update({self.current_node.node_data: 1})

        while self.current_node.node_links and i > 0:  # while we are not dead-locked and have steps to do
            # transition to the next state
            self.current_node = self.current_node.node_links[get_random_node(self.current_node)].node_to

            # add our freshly chosen state to the probabilities
            if self.current_node.node_data in self.probabilities:
                self.probabilities[self.current_node.node_data] += 1
            else:
                self.probabilities.update({self.current_node.node_data: 1})

            # finish step
            i = i - 1
