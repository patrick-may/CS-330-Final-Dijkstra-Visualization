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

    # graph setup
    pos = nx.spring_layout(G, seed=0)
    nx.draw(G, pos, with_labels=True)

    # animation portion
    # applies Djikstra's visualization to graph G
    Djikstra_Updates = get_update_vis(G)
    framect = len(Djikstra_Updates[1])-1

    # generates animation and then shows to screen
    ani = animation.FuncAnimation(fig, update_graph, frames=framect, interval=1200, repeat=False, fargs=(fig, Djikstra_Updates))
    plt.show()
    
#update function that will update the graph to a new "Frame/Iteration" of Djikstras algorithm
def update_graph(frame, fig, update_list):
    import frame_gen
    frame_gen.graph_anim_frame(fig, update_list)

# gets list of edges from other portion of the project to show djikstra's in the order that they should
# be highlighted in
def get_update_vis(G):
    import djikstra_algo_vis
    
    # normally call Djikstra's ordering algo here on graph G
    # Edge_Order = djikstra_algo_vis.whole_djikstra(G)
    Graph_Frame_Dict = djikstra_algo_vis.whole_djikstra(G)
    return [ 0, Graph_Frame_Dict]

# helper function to get any graph input in Node and Edge form, allows for easier extension of input types
def get_graph_inp():
    """
    Edit this function to change the input graph from file/random_gen_normal/etc
    WARNING: using too high a value for random gen stuff may break visualization with too many nodes
    """

    import get_data
    Nodes, Edges = get_data.get_random_gnp(20)
    #Nodes, Edges = get_data.get_file()
    return Nodes, Edges

def main():  
    Nodes, Edges = get_graph_inp()
    blit(Nodes, Edges)

if __name__ == "__main__":
    main()

