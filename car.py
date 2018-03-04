import numpy as np
from mapH import *


class Car(object):
    def __init__(self,id):
        self.id = id
        self.currentPos = Point(0,0)
        self.rides = []
        self.willBeIdleTime = 0

    def printCar(self):
        print "-----Car id: ", self.id
        print "-pos ", self.currentPos.x, self.currentPos.y
        print "-status: ", self.status
        print "-rides", self.rides

    def findRide(self, Rides, stepNow):
        costs = []
        costs_rides = []
        for ride in Rides:
            if ride.status is 0:
                stepCost = calcStep(self.currentPos, ride.start_intersection) 
                if ( stepNow+(stepCost+ride.stepSize) ) < ride.latest_finish:
                    if (stepNow+stepCost) > ride.earliest_start: # direk al git
                        costs.append(stepCost)
                        costs_rides.append(ride)
                    else: # beklemeli cost
                        costs.append(ride.earliest_start-stepNow)
                        costs_rides.append(ride)


        if len(costs) > 0:
            darr = np.array(costs)
            selected_ride = costs_rides[darr.argmin()]
            self.rides.append(selected_ride.id)
            Rides[selected_ride.id].status = 1
            self.willBeIdleTime = stepNow+(stepCost+ride.stepSize)
        else:
            self.willBeIdleTime = 1000000