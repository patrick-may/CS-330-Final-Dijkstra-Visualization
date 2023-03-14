"""CS 330 Spring 2022 Final Project by Patrick May, Angad Singh
driver file that runs the whole thing, mainly handles coupling other files
sets up and handles the initial animation call
Worked on by: Patrick
"""
from matplotlib import pyplot as plt, animation
import networkx as nx

def blit(Nodes, Edges):
    # setting up graph picture
    plt.rcParams["figure.figsize"] = [10, 10]
    
    fig = plt.figure(dpi=80)

    # adding nodes and edges to graph
    G = nx.Graph()
    for n in Nodes:
        G.add_node(n)

    G.add_weighted_edges_from(Edges)
    
    # animation portion
    # applies Dijkstra's visualization to graph G
    Dijkstra_Updates = get_update_vis(G)
    framect = len(Dijkstra_Updates[1])-1

    # uses matplotlib to make an animation with update function update_graph
    # documentation here: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.animation.FuncAnimation.html
    #changing interval (value in ms) changes how fast each frame changes
    ani = animation.FuncAnimation(fig, update_graph, frames=framect, interval=500, repeat=True, fargs=(fig, Dijkstra_Updates))
    plt.show()
    
    #import save_to (saving animations currently not functional)
    
#update function that will update the graph to a new "Frame/Iteration" of Dijkstras algorithm
def update_graph(frame, fig, update_list):
    import frame_gen
    frame_gen.graph_anim_frame(fig, update_list)

# gets list of edges from other portion of the project to show dijkstra's in the order that they should
# be highlighted in
def get_update_vis(G):
    #this is the main coupling between djikstra algo portion and visualization portion
    import dijkstra_algo_vis
    
    # normally call Dijkstra's ordering algo here on graph G
    Graph_Frame_Dict = dijkstra_algo_vis.whole_dijkstra(G)
    return [ 0, Graph_Frame_Dict]

# helper function to get any graph input in Node and Edge form, allows for easier extension of input types
def get_graph_inp():
    """
    Edit this function to change the input graph from file/random_gen_normal/etc
    WARNING: using too high a value for random gen stuff may break visualization with too many nodes
    """

    import get_data
    Nodes, Edges = get_data.get_random_normal(4, 14)
    #Nodes, Edges = get_data.get_file()
    return Nodes, Edges

def main():  
    Nodes, Edges = get_graph_inp()
    blit(Nodes, Edges)

if __name__ == "__main__":
    main()

