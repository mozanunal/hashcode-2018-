

from ride import *
from car import *
from mapH import *

#"data/c_no_hurry.in"
#"data/b_should_be_easy.in"
#"data/a_example.in"
#"data/d_metropolis.in"
FILENAME = "data/d_metropolis.in"
Rides = []
Cars = []

file = open(FILENAME)

line1 = file.readline()

# R number of rows of the grid
# C number of columns of the grid
# F number of vehicles in the fleet
# N number of rides
# B per-ride bonus for starting the ride on time
# T number of steps in the simulation

values = line1.split(" ")
number_of_rows, number_of_columns, number_of_vehicles, number_of_rides, per_ride_bonus, number_of_steps = [int(v) for v in values]

print 'number_of_rows', 'number_of_columns', 'number_of_vehicles', 'number_of_rides', 'per_ride_bonus', 'number_of_steps'
print number_of_rows, number_of_columns, number_of_vehicles, number_of_rides, per_ride_bonus, number_of_steps


id = 0
for line in file.readlines():
    x1, y1, x2, y2, start, end = [int(i) for i in line.split(" ")]
    startPoint = Point(x1, y1)
    endPoint = Point(x2, y2)
    curRide = Ride(id, startPoint, endPoint, start, end)
    #curRide.printRide()
    Rides.append( curRide )
    id = id+1

for i in range(number_of_vehicles):
    Cars.append( Car(i) )


def solve():
    for i in range(number_of_steps):
        stepNow = i
        if i % 1000 is 0:
            print "Sim step", stepNow
        for car in Cars:
            if car.willBeIdleTime <= stepNow:
                car.findRide(Rides,stepNow)

def printResult():
    print "RESULT_________"
    result=""
    for car in Cars:
        line = str(len(car.rides))
        for i in car.rides:
            line+=" "+str(i)
        line+="\n"
        result+=line
    print result
    file = open(FILENAME+ ".out","w+")
    file.write(result)
    file.close()
    print "done"


solve()
printResult()