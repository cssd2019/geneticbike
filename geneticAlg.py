#!/usr/bin/env python3

# https://www.codeproject.com/Articles/1104747/Introduction-to-Genetic-Algorithms-with-Python-Hel
# https://medium.com/@gabogarza/simple-genetic-algorithm-6d6aafcc310a

import numpy as np
import pdb
from operator import itemgetter # to sort list of tuples by "column"
import random # to select random elements 
import string
from bike import Bike


def call_ga(bike_input_list, max_all, ga_iter, print_output):
    """
    MAIN CONNECTION
    Inputs:
        bike_input_list (list of bike objects with each having
            Bike.displacement_made >= 0, 
            ie. not "None".)
        max_all: keep track of max x reached over all iterations
        ga_iter: kep track of # of GA iterations
        print_output: True / False
    Outputs:
        list of new generation bike objects.
        For each, bike.displacement = "None".

        iteration counter
        total max distance reached
        conv
    """
    conv = False
    max_all, current_max_distance, ga_iter, conv, bike_output_list = _full_GA(max_all, ga_iter, conv, bike_input_list)
    
    # Convergence checks
    conv = _check_convergence(max_all, current_max_distance, ga_iter)

    return (bike_output_list, max_all, ga_iter, conv)


def _test_local_main():
    """
        Outer loop to test GA:
            This must be modified to link with SIMULATION module.

        --- For module linkage --- 

            Input
                list of bike objects
                    where each bike object has Bike.distance_made >= 0
                    !TODO: don't assume this, include in test and set default distance_made == 0
            Returns
                list of next-generation bike objects
                    *Note: Bike.distance_made == "None" for these.
    """
    # This is declared in the first iteration of GenAlg
    #   ... updates with new max_x reached in each iteration of GenAlg
    #   ... use to test convergence
    max_distance = 0.0
    last_max_distance = 0.0
    # Extra counter to check number of GA iterations
    ga_counter = 0
    conv = False

    #initialise bike rack if not passed from SIM module
    # Default case for testing with input == number of bike objects to generate
    parents = _generate_bike_rack(20)
    print("First bike rack of parents made\n")

    while conv == False:
        max_distance, last_max_distance, ga_counter, conv, parents = _full_GA(max_distance, ga_counter, conv, parents)
        
        # pdb.set_<trace()
        print("New generation produced!")
        print("Convergence --  ", conv)
        # print(conv)
        print("Iteration number --  ", ga_counter)
        print("Maximum distance made on last iteration --  ", last_max_distance)
        print("Maximum distance ...ever...  --  ", max_distance)
        print("--\n")
        if conv == False:
            update_children_x(parents)
    
    print("END!")
        



def _full_GA(max_distance, ga_counter, conv, parents):
    # # Default case for testing with input == number of bike objects to generate
    # parents = generate_bike_rack(20)
        
    # Check distances:
    # [x.distance_made  for x in parents]

    # (3) sort dictionary list by fitness
    parents = _test_fitness(parents)
        
    # [x.distance_made  for x in parents]

    # (4) update max distances
    max_distance, last_max_distance = _update_max_x(max_distance, parents)

    # (5) select parents for new generaion (LABELS ONLY)
    fittest_parents = _select_parents(parents)

    # (6) pair two randon parents (LABELS ONLY)
    # couple_labels = choose_parents(parent_labels)
    couples = [_choose_parents(fittest_parents) for x in list(range(len(parents)))]
        
    # [x.distance_made  for x in couples[1]]
    # [x.distance_made  for x in couples[15]]
    # [x.distance_made  for x in couples[18]]

    # (7) create new child for every random couple
    children = [_create_child(couples[x]) for x in list(range(len(parents)))]        
    # [x.distance_made  for x in children] # should be "none"
    # [x.locations  for x in children]
        
    # (7 - tmp)
    # # do default child as back-up setting in case GA algorithm doesn't work
    # default_child()

    # (8) Introduce mutations
    children = [_add_mutation(x) for x in children]
    # [x.locations  for x in children]
    
    # (9) Convergence checks
    conv = _check_convergence(max_distance, last_max_distance, ga_counter)
    
    # (10) BACK-UP CONVERGENCE! Max iterations
    if ga_counter == 1000:
        conv = True
    else:
        ga_counter = ga_counter + 1
    return (max_distance, last_max_distance, ga_counter, conv, children)



def _generate_bike_rack(N):
    """
        Only called if SIM module is not connected.

        Generate a random bike rack with 
        a set of N bike objects and randomly assigned values for
        Bike.distance_made
    """
    # Test bikes:
    bike_rack = [Bike("random") for x in range(N)]
    for i in range(len(bike_rack)):
        bike_rack[i].distance_made =  random.uniform(0, 25)
    return bike_rack

def _update_children_x(obj_list):
    """
        Only called if SIM module is not connected.

        Update next generation with randomly assigned values for
        Bike.distance_made
    """
    # Test bikes:
    for i in range(len(obj_list)):
        obj_list[i].distance_made =  random.uniform(15, 80)
    return obj_list    


def _test_fitness(obj_list):
    """
    Rank fitness according to max x-distance reached by each bicycle-like object.
        
    Input:
        List of objects

    Return:
        Sorted list of objects
    """
    # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    #     # To sort the list in place...
    # ut.sort(key=lambda x: x.count, reverse=True)
    # # To return a new list, use the sorted() built-in function...
    # newlist = sorted(ut, key=lambda x: x.count, reverse=True)
    # input_list.sort(key=lambda x: x.distance_made, reverse=True)
    # newlist = sorted(ut, key=lambda x: x.distance_made, reverse=True)
    return sorted(obj_list, key = lambda x: x.distance_made, reverse=True)


def _update_max_x(max_tot, obj_list):
    """
    Input 
        Maximum x reached (ever), list of objects
    Returns
        Maximum x reached (ever), current max x reached 
    """
    # max_current = max([x.distance_made  for x in obj_list])[0]
    max_current = max([x.distance_made  for x in obj_list])
    # pdb.set_trace()
    # max_current = 
    # pdb.set_trace()
    if max_current > max_tot:
        max_tot = max_current
    return (max_tot, max_current)


def _select_parents(obj_list):
    """
    Select [how?] set of parents to keep for next generation.

    Input:
        Object list

    Return:
        Subset object list
    """
    n = 4   #Choose *n* fittest genes
    return obj_list[:n]


def _choose_parents(obj_list):
    """
    Random combinations of selected parent objects.

    Input:
        Subset of fittest object list.

    Return:
        Two objects as tuple
    """
    return random.sample(set(obj_list), 2)


def _default_child():
    """
    Define random default output so that 
    entire toolchain "works" to some degree
    Input:
        Nothing(?)
    Returns:
        One random baby bicycle object
    """
    default_baby_Bike = Bike("random")
    return default_baby_Bike


        # 
def _create_child(parent_couple):
    """
    How to combine [currently: average] between two parents.
    Inputs:
        Two bicycle objects
    Returns:
        One shiny new baby bicycle object
    """
    parent1 = parent_couple[0]
    parent2 = parent_couple[1]
    parent1_loc = parent1.locations
    parent2_loc = parent2.locations
    baby_loc = ( parent1_loc + parent2_loc ) * 0.5
    # return numpy array of x and y average value of newgen baby
    Baby_Bike = Bike(np.array(baby_loc))
    return Baby_Bike



        # This last step of our genetic algorithm is the natural mutation of an individual. 
        # After the breeding, each individual must have a small probability 
        # to see their DNA change a little bit. 
        # The goal of this operation is to prevent the algorithm to be blocked in a local minimum.
def _add_mutation(Bike_input):
    """
    Add natural mutation.
    Input:
        One bike object
    Returns:
        Slightly mutated bike object
    """
    # mutate the location of both wheels with 0-20 % random increase or decrease
    rand_mutate     = random.uniform( -0.2, 0.2 )
    bike_loc = Bike_input.locations
    bike_loc[0][:2] = (1 + rand_mutate) * bike_loc[0][:2]
    bike_loc[1][:2] = ( 1 + rand_mutate ) * bike_loc[1][:2]
    Baby_mutated = Bike(bike_loc)
    return Baby_mutated



def _check_convergence(max_tot, max_current, iteration):
    """
    Check for some or other defined convergence test.
    At the moment:
        convergence if
            current max_x - total max x <= delta_x (as defined here)
    Returns
        True if convergence criterium reached
        False if convergence not reached
    """
    local_conv = False
    # check if after subsequent iterations the values does not change more then Delta_X value
    delta_x = 0.001
    # global mean_x_GAiter
    
    if iteration > 1:
        if ( max_current - max_tot ) <= delta_x:
            local_conv = True
    return local_conv


# if __name__== "__main__":  
#     main()