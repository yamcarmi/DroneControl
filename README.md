# Drone Control

this is an exercise given by XTEND

create a console application to simulate a flight, using XTEND drones. The code should be submitted in Python3, and is ready to run and launch.
Output: The application should display a 100x100 squares map (a two-dimensional grid). Each drone will be represented as a digit in a single square, and move only along X and Y axis (diagonal movement is not allowed). 

Input: Drone ID and an action.
We have two types of drones with the following properties:

- Hunter: 
	- ID (digit in range of 1-9)
	- Maximum flight speed (squares per second)

- Wolverine:
  - ID (digit in range of 1-9)
  - Maximum flight speed (squares per second)
  - Current payload weight (grams)
	
The weight of the payload affects the maximum flight speed
Each drone should have the following functionality:
- Get location – returns the current drone location (X, Y)
- Set location – set drone location (X, Y)
- Set action – set an action that a drone will execute (Takeoff, GoTo, Land)

GoTo: the function should receive a desired location - (X, Y)

# Tech Stack
-   Application Type: Python Console Application
-   Python 3.8

# Run
 In order to run tha application open a Terminal and write:
 ```python
 python3 DroneApp.py
 ```

