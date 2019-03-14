

from bike import Bike
import geneticAlg
import random
import numpy as np


def main():
    """
        Main loop to connect bike simulation, visualisation and genetic algorithm.
    """
    # Change number of bikes here:
    n_bikes = 20
    # Set max number allowed GA iterations
    max_iter = 100
    # Print some output after each GA call?
    print_output = True

    # Initialise variables to track 
    iteration = 0
    max_distance_ever = 0
    conv = False

    # Create list of bike objects
    bike_list = _create_bike_rack(n_bikes)

    # *CALL BIKE SIMULATION
    # Output: updated bike_list with new values for each Bike.distance_made
    # bike_list = simulate_bike(bike_list)

    while conv == False:
        # Tmp: choose random values instead of bike simulation
        bike_list = _update_bike_distance(bike_list, iteration)
        
        # *GENETIC ALGORITHM
        bike_list, max_distance_ever, iteration, conv = geneticAlg.call_ga(bike_list, max_distance_ever, iteration, print_output)

        # Optional output:
        if print_output:
            print("Convergence --  ", conv)
            print("Iteration number --  ", iteration)
            # print("Maximum distance made on last iteration --  ", current_max_distance)
            print("Maximum distance ...ever...  --  ", max_distance_ever)
            print("--\n")

        # Check max iterations: if not met, advance iterations
        if _check_iterations(iteration, max_iter):
            conv = True
            print("Convergence reached: max. number of allowed iterations -.  ", iteration)
        else:
            iteration = iteration + 1

        


def _create_bike_rack(N):
    """
        Generate a random bike rack. 
        Bike.distance_made = "None" (default).
        Input:
            N: number of bike objects
        Output:
            List of N bike objects.
    """
    return [Bike("random") for x in range(N)]


def _update_bike_distance(obj_list, iteration):
    """
        Only called if SIM module is not connected.
        Update next generation with randomly assigned values forBike.distance_made
        Input:
            N: number of bike objects, iteration: number of GA iterations
        Output:
            List of N bike objects.
    """
    if iteration == 0:
        for i in range(len(obj_list)):
            obj_list[i].distance_made = random.uniform(0, 20)
    else:
        for i in range(len(obj_list)):
            obj_list[i].distance_made = random.uniform(22, 80)
        
    return obj_list


def _check_iterations(iters, max_iters):
    """
    Escape hatch if no convergence...
    Input: 
        number of GA iterations
    Output:
        True / False
    """
    if iters == max_iters:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
