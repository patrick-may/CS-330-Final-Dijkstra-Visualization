"""CS 330 Spring 2022 Final Project by Patrick May, Angad Singh
This graph generating function had multiple iterations before our most recent design
Worked on by: Patrick + Angad
"""
import networkx as nx

def graph_anim_frame(fig, update_list):
    """
    Function to animate through a list of networkx graphs in update_list
    Playing around with node_size, font_size, font_weight may be beneficial depending on one's display
    """
    # clear current pyplot figure that is drawn
    fig.clear()

    # reset hack counter if replaying animation
    if update_list[0] == len(update_list[1]):
        update_list[0] = 0

    # Spring layout will auto setup graph to give shorter 'stronger' edges to higher weight values
    # always setting seed to 0 so random overall node position is always same (creates a static node illusion)
    
    current_frame_graph = update_list[1][update_list[0]]

    pos = nx.spring_layout(current_frame_graph, seed=0, k=0.2)

    # get all the special info we got in dijkstra_algo_vis.py from current graph
    
    node_colors = list(nx.get_node_attributes(current_frame_graph, "color").values())
    
    node_renames = nx.get_node_attributes(current_frame_graph, "rename")
    
    edge_colors = list(nx.get_edge_attributes(current_frame_graph,"color").values())
    
    edge_thick = list(nx.get_edge_attributes(current_frame_graph,"thickness").values())
    
    edge_label_loc = nx.get_edge_attributes(current_frame_graph, "weight")

    # draw graph with all special information as part of drawn visualization
    # does main work of drawing an individual graph
    # documentation for nx.draw found here: https://networkx.org/documentation/stable/reference/drawing.html
    nx.draw(current_frame_graph, pos,  edge_color=edge_colors, node_color=node_colors, node_size=1000, 
            font_size=14, font_weight="bold", width=edge_thick, labels=node_renames, with_labels=True)
    nx.draw_networkx_edge_labels(current_frame_graph, pos, edge_labels=edge_label_loc)

    # ugly hack to preserve index in update_list per frame
    # probably a better way to do this, but understanding helper functions of matplotlib.plotly.anim functions is 
    # not the primary goal of project
    update_list[0]+=1
    