#!/usr/bin/env python3

# https://www.codeproject.com/Articles/1104747/Introduction-to-Genetic-Algorithms-with-Python-Hel
# https://medium.com/@gabogarza/simple-genetic-algorithm-6d6aafcc310a

import numpy as np
from operator import itemgetter # to sort list of tuples by "column"
import random # to select random elements 
import string
from bike import Bike


def main():
    """
        Outer loop to test GA
    """
    # This is declared in the first iteration of GenAlg
    #   ... updates with new max_x reached in each iteration of GenAlg
    #   ... use to test convergence
    max_distance = 0
    # Extra counter to check number of GA iterations
    ga_counter = 0
    conv = False

    #initialise bike rack if not passed from SIM module
    # Default case for testing with input == number of bike objects to generate
    parents = generate_bike_rack(20)
    print("First bike rack of parents made")


    while conv == False:
        max_distance, ga_counter, conv, parents = full_GA(max_distance, ga_counter, conv, parents)
        print("New generation produced!")
        print("Convergnce?")
        print(conv)
        



def full_GA(max_distance, ga_counter, conv, parents):
    # # Default case for testing with input == number of bike objects to generate
    # parents = generate_bike_rack(20)
        
    # Check distances:
    # [x.distance_made  for x in parents]

    # (3) sort dictionary list by fitness
    parents = test_fitness(parents)
        
    # [x.distance_made  for x in parents]

    # (4) update max distance
    max_distance = update_max_x(parents)

    # (5) select parents for new generaion (LABELS ONLY)
    fittest_parents = select_parents(parents)

    # (6) pair two randon parents (LABELS ONLY)
    # couple_labels = choose_parents(parent_labels)
    couples = [choose_parents(fittest_parents) for x in list(range(len(parents)))]
        
    # [x.distance_made  for x in couples[1]]
    # [x.distance_made  for x in couples[15]]
    # [x.distance_made  for x in couples[18]]

    # (7) create new child for every random couple
    children = [create_child(couples[x]) for x in list(range(len(parents)))]        
    # [x.distance_made  for x in children] # should be "none"
    # [x.locations  for x in children]
        
    # (7 - tmp)
    # # do default child as back-up setting in case GA algorithm doesn't work
    # default_child()

    # (8) Introduce mutations
    children = [add_mutation(x) for x in children]
    # [x.locations  for x in children]
    
    # (9) Convergence checks
    if ga_counter == 10:
        conv = True
    else:
        ga_counter = ga_counter + 1
    # check_convergence()
    # check_counter()
    return (max_distance, ga_counter, conv, children)

def generate_bike_rack(N):
    # Test bikes:
    bike_rack = [Bike("random") for x in range(N)]
    for i in range(len(bike_rack)):
        bike_rack[i].distance_made =  random.sample(range(23), 1)
    return bike_rack


def test_fitness(obj_list):
    """
    Rank fitness according to max x-distance reached by each bicycle-like object.
        
    Input:
        Gene list of objects

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


def update_max_x(obj_list):
    """
    Input 
        Sorted gene dictionary
    Returns
        Updates GLOBAL x reached
    """
    return max([x.distance_made  for x in obj_list])


def select_parents(obj_list):
    """
    Select [how?] set of parents to keep for next generation.

    Input:
        Gene dictionary

    Return:
        Subset gene dictionary
    """
    n = 4   #Choose *n* fittest genes
    return obj_list[:n]


def choose_parents(obj_list):
    """
    Combinations of selected parents.
    Input:
        Subset gene dictionary

    Return:
        Permutation list? Necessary?
    """
    return random.sample(set(obj_list), 2)


def default_child():
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
def create_child(parent_couple):
    """
    How to combine [average?] between two parents.
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
def add_mutation(Bike_input):
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



        # 
# def check_convergence()
#     """
#     Check for some or other defined convergence test.

#     Returns
#         True/False
#     """    

if __name__== "__main__":  
    main()