"""CS 330 Spring 2022 Final Project by Patrick May, Angad Singh
Functions for getting graphs to display. Currently supports some builtin random graphs
And reading a graph from a text file
Worked on by: Angad, final touches by Patrick
"""
import networkx as nx
import random, time

"""
File contains different methods of getting an initial graph to visualize

Each method must return:
    A list of Nodes: [ 'node 1', 'node 2', 'node 3', etc.] currently should be integer values, 0, 1, 2, ...
    A list of weighted edges as tuples. Each tuple: ( *node 1*, *node 2*, *weight of edge* )
    example: [ (1, 2, 1), (2, 3, 4), (3, 4, 10), etc.]
"""

def get_random_normal(graph_order, num_nodes):
    """
    Creates a random normal graph. All nodes are of order graph_order (all have graph_order num of edges)
    And Total number of nodes is num_nodes
    Edge weight is randomly assigned between 1-10, for different weight range change randint(1,10) to desired range
    """
    #print(time.localtime())
    random.seed(time.localtime().tm_sec)
    G = nx.random_regular_graph(graph_order, num_nodes)
    Edges = G.edges
    Weighted_Edges = []

    for e in Edges:
        Edge_tuple = (e[0], e[1], random.randint(1, 10))
        Weighted_Edges.append(Edge_tuple)

    Nodes = list(G.nodes)
    return Nodes, Weighted_Edges

def get_random_gnp(num_nodes):
    """
    Creates a gnp graph using a networkx buildit gnp graph generator
    To us, a gnp graph has more random distribution of edges per node compared to
    random_normal and not as unpredictable as random_lobster
    Documentation on what gnp graph is found here: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model"""
    random.seed(time.localtime().tm_sec)
    G = nx.fast_gnp_random_graph(num_nodes, 0.25)
    Nodes = list(G)
    Edges = G.edges
    Weighted_Edges = []

    for e in Edges:
        Edge_tuple = (e[0], e[1], random.randint(1, 10))
        Weighted_Edges.append(Edge_tuple)

    return Nodes, Weighted_Edges

#somewhat of a broken function but I though a lobster graph was funny
def get_random_lobster(num_back_nodes):
    """
    Creates a random lobster graph with backbone node ct:= num back nodes
    Internal to the function, randomly generate probability of edge placement
    Edge weight is randomly assigned between 1-10
    """

    random.seed(time.localtime().tm_sec)
    prob_tail = random.random()
    prob_extra = random.random()
    G = nx.random_lobster(num_back_nodes, prob_tail, prob_extra)
    Nodes = list(G)
    Edges = G.edges
    Weighted_Edges = []

    for e in Edges:
        Edge_tuple = (e[0], e[1], random.randint(1, 10))
        Weighted_Edges.append(Edge_tuple)

    
    return Nodes, Weighted_Edges

# currently not fully working
def get_file():
    """
    Reads in a graph from a file name that is in local folder and input from command line.
    Each line of the file must begin with N (a node) or E (an edge)
    For N:
        one space followed by continuous string of node name
    For E:
        one space, node_name1, space, node_name2, space, edge weight

    Currently does not have bad input detection.
    """
    print("Enter File Name:")
    file_name = input()
    Nodes = []
    Weighted_Edges = []
    with open(file_name, "r") as inp_file:
        for line in inp_file:
            line_data = line.split()
            if(line_data[0] == "N"):
                Nodes.append( int(line_data[1]) )
            elif(line_data[0] == "E"):
                Weighted_Edges.append( (tuple(int(i) for i in line_data[1:4])) )

    return Nodes, Weighted_Edges

    