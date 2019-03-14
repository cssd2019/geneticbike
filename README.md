# geneticbike

What is this: a genetic evolution of a bicycle that converges to a better bicycle that can reach the greatest distance.


#### What is a bicycle in our world?

An object with 4 defined points: two handlebar points and two wheel centers.  
One wheel is an active, driving wheel.  
There are springs attaching all four points to each other.  

##### What happens?
Initially, a bicycle is defined by setting four random coordinates for each of these points.  
The bicycle drops onto a defined surface and moves along this surface according to the relevant physics, hopefully. 
The bicycle drives along until at least one of the handle bars touches the surface.  
At this point, the bike has fallen over and is broken.

A genetic algorithm is used to evolve 20 such random bicycles, with the evolution step concentrated on the greatest x-distance reached by a generation of bicylces.


## Implementation: go_genetic_bike.py

**Bike** is the central object that gets passed around in the workflow and is the carrier of the exchanged information. It contains the locations of the points in the bike and a variable for distance traveled. Bike('random') initializes a completely random bike.  

**Movement** contains the simulation of the bike's ride along the road. The distance made is written onto the bike object.  

**Visuals** visualizes the bike's position at given time points.  

**Random_surface** generates the road and reads it into a 2D numpy array.  

**GeneticAlg** contains the genetic algorithm that takes a generation of bikes and the distances they travelled and generates a new generation of bikes.  

##### Brought to you by the Genetic Bikers...
Türküler, Roland, Pat, Elsa
