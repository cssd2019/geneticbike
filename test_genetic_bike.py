import numpy as np
from bike import Bike


def main():

    max_dist = 0
    GA_iteration = 0
    con = False
    init_bike = create_init_bike(20)

    



def create_init_bike(Number_of_bike):
    """create initial bike object for simulation output"""

    bike_rack = [Bike("random") for x in range(Number_of_bike)]
    return bike_rack

main()