
# https://www.codeproject.com/Articles/1104747/Introduction-to-Genetic-Algorithms-with-Python-Hel
# https://medium.com/@gabogarza/simple-genetic-algorithm-6d6aafcc310a

import numpy as np
from operator import itemgetter # to sort list of tuples by "column"
import random # to select random elements 
from bike import Bike

# This is declared in the first iteration of GenAlg
#   ... updates with new max_x reached in each iteration of GenAlg
#   ... use to test convergence
max_distance = 0
# Extra counter to check number of GA iterations
ga_counter = 0

# Test bikes:

Bike1 = Bike("random")
Bike2 = Bike("random")
Bike3 = Bike("random")
Bike2 = Bike("random")

if __name__ == '__main__':
def main()
    current_generation = create_genes()
    sorted_generation = test_fitness(current_generation)
    max_distance = update_max_x(sorted_generation)
    parent_labels = select_parents(sorted_generation)
    couple_labels = choose_parents(parent_labels)
    # create_child()
    # # do default child as back-up setting in case GA algorithm doesn't work
    # default_child()
    # add_mutation()
    # check_convergence()
    # check_counter()


    # Bike obj:
    #     self.x = 0
	# 	self.y = 1
	# 	self.activeWheel = 0
	# 	self.passiveWheel = 1
	# 	self.handlebar1 = 2
	# 	self.handlebar2 = 3
	# 	self.distance_made = 0


def create_genes():
    """
    Take bicycle object inputs and convert to gene dictionary with
    bicycle:distance pairs.

    Input: 
        bike obj

    Returns:
        genes (dictionary with label:distgens.ance)
    """
    genes =	[ ("A", 4), ("B", 1), ("C", 9), ("D", 8), ("E", 6), ("F", 0) ]
    return genes


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