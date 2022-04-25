import networkx as nx
import copy

def get_path(prev_dict, current_node, start_node):
    """
    Follow pointer dictionary prev_dict to construct list of edges that is a path backwards
    from current working node in djikstra's algo to the progenitor node
    """
    path_edges = []
    prior_node = current_node
    
    while(current_node != start_node):
        prior_node = prev_dict[current_node]
        path_edges.append( (current_node, prior_node) )
        current_node = prior_node

    path_edges.append( (current_node, prior_node) )

    return path_edges 
    
def whole_djikstra(G):
    """
    Given a networkx graph G,
    This function will calculate all least-cost paths to all other nodes from start_node
    Will a list of Graphs, each graph corresponding to a frame that should be displayed
        Specific attributes are enclosed in each graph that are used in frame_gen.py (not fully decoupled, just have
        to know to use "thickness", "color", "weight", etc)

    """
    print("Enter name of starting node")
    start_node = int(input())
    node_list = list(G.nodes)
    
    dist = {start_node:0}
    predecessor_dict = {start_node: start_node}
    node_queue = []

    per_frame_list = [] #list of a graph for each frame of anim
    frame_graph = copy.deepcopy(G)

    #start by setting all node distances except source to infinite.
    for node in node_list:
        if node != start_node:
            dist[node] = float('inf')

        node_queue.append( (dist[node], node) ) #add tuple of (distance, node) to priority queue
        
        ## visualization portion, setting all nodes initially to proper color + titling them
        if node != start_node:
            frame_graph.nodes[node]["color"] = "blue"
            retitle = str(node) + ": inf"
            frame_graph.nodes[node]["rename"] = retitle
        else:
            frame_graph.nodes[node]["color"] = "yellow"
            retitle = str(node) + ": 0"
            frame_graph.nodes[node]["rename"] = retitle

    nx.set_edge_attributes(frame_graph, "gray", name="color")
    nx.set_edge_attributes(frame_graph, 2, name="thickness")
    
    # add first frame of animation
    per_frame_list.append(frame_graph)

    while len(node_queue):  # while items in node_queue
        work_node = min(node_queue) 
        node_queue.remove(work_node) #get and pop minimum of node_queue (using list as a min-priority here)
        work_node = work_node[1] #strip weight/distance that node name was packaged with

        frame_graph = copy.deepcopy(G)
        
        #VISUALIZATION PIECE
        #Setting node color and names
        for n in G.nodes:
            if n == start_node:
                frame_graph.nodes[n]["color"] = "yellow"
            elif n == work_node:
                frame_graph.nodes[n]["color"] = "green"

            elif n in G.adj[work_node]:
                frame_graph.nodes[n]["color"] = "red"
            else:
                frame_graph.nodes[n]["color"] = "blue"
            
            frame_graph.nodes[n]["rename"] = str(n) + ": " + str(dist[n])

        for adj_node in G.adj[work_node]:
            individual_frame = copy.deepcopy(frame_graph)
            alt_path = dist[work_node] + G[work_node][adj_node]["weight"]

            # for each adjacent node to the work node, see if its path is shorter than prior believed distance          
            if alt_path < dist[adj_node]:
                # if so, update queue with proper distances, adjust predecessor dict and distance dict
                node_queue = [ (alt_path, adj_node) if item == (dist[adj_node], adj_node) else item for item in node_queue]
                dist[adj_node] = alt_path
                predecessor_dict[adj_node] = work_node  #  each node points to its predecessor in path, follow pointers
                                                        #  until start node is reached to construct physical shortest path
            
            #visualize path from start to work node
            edge_path = get_path(predecessor_dict, work_node, start_node)
            for e in G.edges:
                # show the adjacent node that we are probing by making edge to node thick + red
                if e == (work_node, adj_node) or e == (adj_node, work_node):
                    
                    individual_frame[e[0]][e[1]]["color"] = "red"
                    individual_frame[e[0]][e[1]]["thickness"] = 10
                
                # show path from start to work node with thinner red edge path
                elif e in edge_path or e in [tup[::-1] for tup in edge_path]:
                    individual_frame[e[0]][e[1]]["color"] = "red"
                    individual_frame[e[0]][e[1]]["thickness"] = 7

                # show unused as thinner gray
                else:
                    individual_frame[e[0]][e[1]]["color"] = "gray"
                    individual_frame[e[0]][e[1]]["thickness"] = 2
            
            #add graph as a frame to display
            per_frame_list.append(individual_frame)

    # printing these as they are the normal Djikstra's algorithm results to discuss         
    print("Distance dictionary from origin node:\n",dict(sorted(dist.items())))
    print("Predecessor pointer dictionary to work backwards to origin:\n",dict(sorted(predecessor_dict.items())))
    
    # creating one last frame to show, with no active path finding
    finish_frame=copy.deepcopy(per_frame_list[-1])
    nx.set_node_attributes(finish_frame, "blue", name="color")
    finish_frame.nodes[start_node]["color"] = "yellow"
   
    nx.set_edge_attributes(finish_frame, "gray", name="color")
    nx.set_edge_attributes(finish_frame, 2, name="thickness")
    

    per_frame_list.append(finish_frame)

    return per_frame_list
    
## UNUSUED TESTING CODE FOR INDIVIDUAL SCRIPT TESTING
def main():
    import get_data
    Nodes, Edges = get_data.get_random_normal(4, 10)
    G = nx.Graph()
    G.add_nodes_from(Nodes)
    G.add_weighted_edges_from(Edges)
    whole_djikstra(G)

if __name__ == "__main__":
    main()



    
    