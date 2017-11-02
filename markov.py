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


def get_random_node(node):
    p_list = []
    is_prop = 0
    for n in node.node_links:
        p_list.append(n.probability)
        is_prop += n.probability
    if is_prop < 1:
        p_list.append(1 - is_prop)
        node.add_link(Link(node, 1 - is_prop))
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

    def run(self, i=1000):
        self.current_node = self.node_list[0]
        if self.probabilities.has_key(self.current_node.node_data):
            self.probabilities[self.current_node.node_data] += 1
        else:
            self.probabilities.update({self.current_node.node_data: 1})

        while self.current_node.node_links and i > 0:
            self.current_node = self.current_node.node_links[get_random_node(self.current_node)].node_to
            if self.current_node.node_data in self.probabilities:
                self.probabilities[self.current_node.node_data] += 1
            else:
                self.probabilities.update({self.current_node.node_data: 1})
            i = i - 1
