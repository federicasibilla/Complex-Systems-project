# Complex Systems project
 Repository for course project in modelling complex systems

# Code files
- `game.py` contains the falling ball game with a chromosome of rules as a test input.
- `show_game.py` contains the visualizaion of the falling ball game visualization with a chromosome of rules as a test input. The file can be used for videos. It cannot be run on Google Collab as it needs a video support.
- `GA.py` contains the genetic algorithm. Must be modified to change the way to select parents or the way to reproduce them. Contains also 
- `aux_func.py` contains the functions necessary to run GA (parent selection and offspring method)
- `fitness_heatmaps.py` contains the code used to generate the fitness over λ or over *s* heatmaps
- `velocity_heatmaps.py` contains the code used to generate the speed velocity over λ or over *s* heatmaps

## Requirements
- Python 3.8 or higher
- Python module `numpy`
- Python module `random`
- Python module `math`
- Python module `pygame`
- Python module `copy`
- Python module `matplotlib`

# Other content
[This video](https://youtu.be/4Wabw-BbCKs) shows how the evolution of the behavior of the best chromosome over the generations.
