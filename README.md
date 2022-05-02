# Welcome to our Computer Networking Final Project for CS 330 at the College of Wooster!
Currently, this project randomly generates a graph using builtin functions of the networkx library and performs djikstra's algorithm across all nodes on the graph.

## Quickstart
- Clone/download repo 
- For this project, you must have the python libraries **networkx** and **matplotlib** installed globally/in venv/etc. If you are unsure if you have these, enter the following in the command line: `pip install -r requirements.txt` if you have cloned the repository, otherwise `pip install matplotlib`, `pip install networkx`
- run `python display_graph.py`.
- Input the starting node to begin from. (I suggest 0 unless you know how big graph will be)
- Watch the animation!

### Easily changeable code
- In **__display_graph.py__**, in function __get_graph_input()__, you can easily change the graph that ends up being animated over by switching the __get_data()__ input function. For more documentation on what types of graphs __get_data()__ can produce and parameters needed for them, read over comments and docstrings in **__get_data.py__**
- In **__display_graph.py__**, in function __blit()__, the `animation.funcAnimation(...)` line. Formal reference for this function can be found [here](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.animation.FuncAnimation.html). The main argument I would draw attention to is **interval**, as that is the time in ms that each frame is displayed. For slower steps between frames, try `interval=1200`, `interval=2000`, etc.

## How the animation works
The visualizer uses `matplotlib.plotly.animation` as the primary animation library. In `animation.funcAnimation`, one of the arguments is the update function for the matplot. This update function has been moved to `frame_gen.py`, as it was growing to be a large function. __update()__ in **__display_graph.py__** passes the desired graph to __graph_anim_frame()__ in **__frame_gen.py__**, which begins by passing the graph to __full_djikstra__ in **__djikstra_algo_vis.py__**. __full djikstra__ gets the start node (currently just from standard input) and performs the whole algorithm on the graph. Each frame of the graph is added as an entirely new __networkx__ graph to a list which returns to **__frame_gen.py__**. __full_djikstra__ also prints out two dictinaries, the first with key value pairs of a node's name to its distance from starting node. The second a previous pointer dict, which can be used to follow the key's value to construct the directions to the shortest path back to the start node. The returned list of graphs is then iterated through, with each graph being displayed as a new frame.