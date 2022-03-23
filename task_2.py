class Road:

    _length = 0
    _width = 0


    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def calc(self, density, thickness):
        return self._length * self._width * density * thickness

road = Road(length=20, width=5000)
print(road.calc(25, 5))
