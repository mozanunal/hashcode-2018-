


def calcStep(a,b):
    return abs(a.x - b.x ) + abs(a.y - b.y)


class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Map(object):
    def __init__(self,R,C):
        self.R = R
        self.C = C
