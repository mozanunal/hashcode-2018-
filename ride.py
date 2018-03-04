
from mapH import *

class Ride(object):
    def __init__(self, ride_id, start_intersection, finish_intersection, earliest_start, latest_finish):
        self.id = ride_id
        self.start_intersection = start_intersection
        self.finish_intersection = finish_intersection
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.stepSize = calcStep(start_intersection,finish_intersection)
        self.earliest_finish = self.earliest_start + self.stepSize
        self.latest_start =  self.latest_finish - self.stepSize
        self.status = 0

    def printRide(self):
        print "-----Ride id: ", self.id
        print "-start ", self.start_intersection.x, self.start_intersection.y
        print "-finish: ", self.finish_intersection.x, self.finish_intersection.y
        print "-start steps: ", self.earliest_start, self.latest_start
        print "-distance: ", self.stepSize
        print "-finish steps: ", self.earliest_finish, self.latest_finish