
# https://www.codeproject.com/Articles/1104747/Introduction-to-Genetic-Algorithms-with-Python-Hel
# https://medium.com/@gabogarza/simple-genetic-algorithm-6d6aafcc310a

import numpy as np
from operator import itemgetter # to sort list of tuples by "column"
import random # to select random elements 
import string
from bike import Bike

# This is declared in the first iteration of GenAlg
#   ... updates with new max_x reached in each iteration of GenAlg
#   ... use to test convergence
max_distance = 0
# Extra counter to check number of GA iterations
ga_counter = 0

def main()
    # Default case for testing
    input_list = generate_test_bikes()

    generation_idx  = list(range(len(input_list)))

    # (1) add alphabetic labels to bike objects in dictionary
    input_dictionary = create_labels(input_list)

    # (2) Create list of (label, distance) tuples
    current_generation = create_genes(input_dictionary)

    # (3) sort tuple list by fitness
    sorted_generation = test_fitness(current_generation)

    # (4) update max distance
    max_distance = update_max_x(sorted_generation)

    # (5) select parents for new generaion (LABELS ONLY)
    parent_labels = select_parents(sorted_generation)

    # (6) pair two randon parents (LABELS ONLY)
    # couple_labels = choose_parents(parent_labels)
    all_couples = [choose_parents(parent_labels) for x in generation_idx]

    # (7) create new child for every random couple
    # create_child()
    # new_generation = [all_couples[x] for x in generation_idx]
    # Send DICTIONARY OBJECT!!!!
    new_generation = [create_child(all_couples[x]) for x in generation_idx]
    all_couples[0][0]
    all_couples[0][1]
    input_dictionary

    [key for key, value in input_dictionary.keys() if 'A' in key.upper()]



    # (7 - tmp)
    # # do default child as back-up setting in case GA algorithm doesn't work
    # default_child()

    # (8) Introduce mutations
    # add_mutation()

    # (9) Convergence checks
    # check_convergence()
    # check_counter()

    # Most likely input: list of N bicycles

def generate_test_bikes():
    # Test bikes:
    Bike1 = Bike("random")
    Bike1.distance_made = 42
    Bike2 = Bike("random")
    Bike2.distance_made = 0
    Bike3 = Bike("random")
    Bike3.distance_made = 1
    Bike4 = Bike("random")
    Bike4.distance_made = 33
    Bike5 = Bike("random")
    Bike5.distance_made = 22.1
    Bike6 = Bike("random")
    Bike6.distance_made = 1
    Bike7 = Bike("random")
    Bike7.distance_made = 1
    Bike8 = Bike("random")
    Bike8.distance_made = 4
    Bike9 = Bike("random")
    Bike9.distance_made = 5.5
    Bike10 = Bike("random")
    Bike10.distance_made = 7
    return list[ Bike1, Bike2, Bike3, Bike4, Bike5, Bike6, Bike7, Bike8, Bike9, Bike10 ]


def create_labels(inp_list):
    """
    Take bicycle object inputs and add labels for each object

    Input: 
        bike obj

    Returns:
        dictionary with (label, bike_obj)
    """
    N = len(inp_list)
    # *Create alphabetic labels
    #   ...This will need tweaking if number of objects > len(alphabet)
    labels = list(string.ascii_uppercase)[0:N]
    return dict( zip(labels, input_list ))



def create_genes(inp_dictionary):
    """
    Take bicycle object inputs and convert to gene list of tuples with
    bicycle label:distance pairs.

    Input: 
        bike obj

    Returns:
        list of tuples (label, distance)
        [("A", 4), ....()]
    """
    # Separate input dictionary into two lists
    labels, objects = zip(*input_dictionary.items())
    # Extract distance made for each bike
    # ...list-comprehension
    distances = [x.distance_made for x in objects]
    # Default test logic
    # genes =	[ ("A", 4), ("B", 1), ("C", 9), ("D", 8), ("E", 6), ("F", 0) ]
    return list(zip(labels, distances))


def test_fitness(genes):
    """
    Rank fitness according to max x-distance reached by each bicycle-like object.
    
    Input:
        Gene list of tuples

    Return:
        Sorted list of tuples
    """
        # Using dictionary: # return sorted(genes.items(), key = operator.itemgetter(1), reverse = True)
        # return sorted([item[0] for item in genes], reverse = True)
    # https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    return sorted(genes, key = itemgetter(1), reverse = True)

def update_max_x(genes):
    """
    Input 
        Sorted gene dictionary
    Returns
        Updates GLOBAL x reached
    """
    max_x = sorted_generation[0][1]
    return max_x


def select_parents(genes):
    """
    Select [how?] set of parents to keep for next generation.

    Input:
        Gene dictionary

    Return:
        Subset gene dictionary
    """
    n = 4   #Choose *n + 1* fittest genes
    gene_labels = [i for i,j in sorted_generation]
    return gene_labels[:n]




def choose_parents(parents):
    """
    Combinations of selected parents.
    Input:
        Subset gene dictionary

    Return:
        Permutation list? Necessary?
    """
    return random.sample(set(parents), 2)


def create_child():
    """
    How to combine [average?] between two parents.

    Inputs:
        Two bicylce objects

    Returns:
        One shiny new baby bicycle object
    """
    parent1_loc = Bike1.locations
    parent2_loc = Bike2.locations

    baby_locx = ( parent1_loc + parent2_loc ) * 0.5
    baby_locy = ( parent1_loc + parent2_loc ) * 0.5
    # return numpy array of x and y average value of newgen baby

    return np.array([baby_locx, baby_locy])


    # 
def default_child()
    """
    Define random default output so that 
    entire toolchain "works" to some degree

    Input:
        Nothing(?)

    Returns:
        One random baby bicycle object
    """


    # This last step of our genetic algorithm is the natural mutation of an individual. 
    # After the breeding, each individual must have a small probability 
    # to see their DNA change a little bit. 
    # The goal of this operation is to prevent the algorithm to be blocked in a local minimum.
def add_mutation()
    """
    Add natural mutation.

    Input:
        One bike object

    Returns:
        Slightly mutated bike object
    """



    # 
def check_convergence()
    """
    Check for some or other defined convergence test.

    Returns
        True/False
    """    