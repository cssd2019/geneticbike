# geneticbike

## Submodules
**Bike** is the central object that gets passed around in the workflow and is the carrier of the exchanged information. It contains the locations of the points in the bike and a variable for distance traveled. Bike('random') initializes a completely random bike.
**Movement** contains the simulation of the bike's ride along the road. The distance made is written onto the bike object.
**Visuals** visualizes the bike's position at given time points.
**Random_surface** generates the road and reads it into a 2D numpy array.
**GeneticAlg** contains the genetic algorithm that takes a generation of bikes and the distances they travelled and generates a new generation of bikes.
