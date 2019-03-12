
# https://www.codeproject.com/Articles/1104747/Introduction-to-Genetic-Algorithms-with-Python-Hel
# https://medium.com/@gabogarza/simple-genetic-algorithm-6d6aafcc310a

import numpy as np
import operator # to sort list in dictionary
from bike import Bike

# This is declared in the first iteration of GenAlg
#   ... updates with new max_x reached in each iteration of GenAlg
#   ... use to test convergence
global_max_x = 0
# Extra counter to check number of GA iterations
ga_counter = 0

Bike1 = Bike("random")
Bike2 = Bike("random")

def main():
    #gene_input = create_genes()
    #sorted_gene = test_fitness(gene_input)
    # update_max_x()
    #parents = select_parents(sorted_gene)
    # permute_parents()


    #create_child(Bike1.locations, Bike2.locations)
    Baby = create_child(Bike1, Bike2)
    print(Baby.locations)
    #print(baby_newgen_loc)

    #print(Bike1.locations)
    #print(Bike2.locations)
    #create_child()
    # # do default child as back-up setting in case GA algorithm doesn't work
    # default_child()
    # add_mutation()
    # check_convergence()
    # check_counter()



def create_genes():
    """
    Take bicycle object inputs and convert to gene dictionary with
    bicycle:distance pairs.

    Input: 
        bike obj

    Returns:
        genes (dictionary with label:distgens.ance)
    """
    # dictionary with genes and distances
    genes =	{
    "A": 4,
    "B": 1,
    "C": 9,
    "D": 8,
    "E": 6,
    "F": 0
    }
    return genes


def test_fitness(genes):
    """
    Rank fitness according to max x-distance reached by each bicycle-like object.
    
    Input:
        Gene dictionary

    Return:
        Sorted gene dictionary
    """

    return sorted(genes.items(), key = operator.itemgetter(1), reverse = True)



def update_max_x():
    """
    Input 
        Sorted gene dictionary
    Returns
        Updates GLOBAL x reached
    """

    #global_max_x = maximum x reached
    return global_max_x



def select_parents(genes):
    """
    Select [how?] set of parents to keep for next generation.

    Input:
        Gene dictionary

    Return:
        Subset gene dictionary
    """
    return genes[:10]




def permute_parents():
    """
    Combinations of selected parents.
    Input:
        Subset gene dictionary

    Return:
        Permutation list? Necessary?
    """
    pass


def create_child(parent1, parent2_loc):
    """
    How to combine [average?] between two parents.

    Inputs:
        Two bicylce objects

    Returns:
        One shiny new baby bicycle object
    """
    parent1_loc = Bike1.locations
    parent2_loc = Bike2.locations

    baby_loc = ( parent1_loc + parent2_loc ) * 0.5
    # return numpy array of x and y average value of newgen baby
    Baby_Bike = Bike(np.array(baby_loc))

    return Baby_Bike



    # 
def default_child():
    """
    Define random default output so that 
    entire toolchain "works" to some degree

    Input:
        Nothing(?)

    Returns:
        One random baby bicycle object
    """
    pass

    # This last step of our genetic algorithm is the natural mutation of an individual. 
    # After the breeding, each individual must have a small probability 
    # to see their DNA change a little bit. 
    # The goal of this operation is to prevent the algorithm to be blocked in a local minimum.
def add_mutation():
    """
    Add natural mutation.

    Input:
        One bike object

    Returns:
        Slightly mutated bike object
    """
    pass


    # 
def check_convergence():
    """
    Check for some or other defined convergence test.

    Returns
        True/False
    """
    pass

main()