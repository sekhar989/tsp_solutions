# TSP (Traveelling Salesman Problem) Solutions
This was a project in our Masters' Degree for the Artificial Intelligence Course in which we solved the classic [Travelling Salesmane Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using:

- Greedy Algorithm with Pattern Database Heuristic
- Genetic Algorithm

For the comprehensive report related to the project please refer [here.](https://github.com/sekhar989/tsp_solutions/blob/master/Report.pdf)

## Running Instructions:

- `main.py` → Main script which runs the Greedy and 2-OptSwap algorithms on the same set of dirt locations.

## Outputs
### Images
        
> `greedy_path.png` → Showing the path that'll be traversed by the agent using the path generated by Greedy Algorithm only
> `greedy2opt_path.png` → Showing the path that'll be traversed by the agent using the path generated by **Greedy Algorithm** and **2-OptSwap**  
> `ga_path.png` → Showing the path that'll be traversed by the agent using the path generated by Genetic Algorithm

Paths: Co-ordinates and actions performed by agent to travel from start location to an end location.  

`G2Opt.csv` → Actions w.r.t. Greedy and 2-OptSwap  

`GA.csv` → Actions w.r.t. Genetic Algorithm  

- `utils.py` → Utils contain all the required functions to solve TSP (Travelling Salesman Problem) using:
    - Greedy Search in combination with 2-OptSwap
    - Genetic Algorithm
    Not required to run this file.

- `pdb.py` → Script to generate a Pattern Database (PDB) for a (5,5) grid size. It prompts the user for the number of dirt locations (n) and the max number of locations (m) which should be considered as a partial problem. Number of locations is restricted to N[2,13] for time and memory constraints.
In order to run this file go the location where this file is present and make sure the environment has the required specification of python and all the packages mentioned in the ‘specificaions.txt’ file.

```bash
 $ > python pdb.py
   > Enter number of dirt locations (between 2 and 13): ‘n’
   > Enter max number of dirt locations (less than 6) to be used in PDB: ‘m’
```

## Instructions to run the DiceLab Extensions files

Primary File `dicelab_tsp_setup_01.py`

1. Open terminal.

2. Install VacuumWorld using the below instructions provided by DICELab:
	
	- Recommended step: Create a new virtual environment using virtualenv
		```bash
		$ > python3 -m virtualenv <directory name>
		$ > cd <directory name>
		$ > activate virtual environment:
			- Linux and MacOS: source bin/activate
			- Windows: Scripts/activate 
		```
  
  This will give a fresh environment to work with. Please ensure you are using Python 3.7+.  
  
  VacuumWorld is installed using the pip command (after activating your virtual environment):  
			
      ```bash
      $ > pip install vacuumworld
      ```
      
This command will also install `pystarworlds` and any other dependencies required to run VaccumWorld.

**VacuumWorld** can also be installed using pip command even if you're using conda environments. Please ensure that you're using Python 3.7+

3. Navigate to the folder where the zip file is present.

4. Unzip the contents of the zip file

5. Enter the below command to run the script:
	```bash
	$ > python3 <path to the folder>/dicelab_tsp_setup_01.py
	$ > python3 <path to the folder>/dicelab_tsp_setup_02.py```
  
6. Once the VacuumWorld screen appears, please press the play button to start the execution of the environment.
