class Box:
    count = 0.0
    length = 0.0
    breadth = 0.0
    height = 0.0
    area = 0.0
    volume = 0.0

    def __init__(self, *args):
        if len(args) == 1:
            self.length = args[0]
            self.count = 0
        elif len(args) == 2:
            self.length = args[0]
            self.height = args[1]
            self.count = 1
        elif len(args) == 3:
            self.length = args[0]
            self.breadth = args[1]
            self.height = args[2]
            self.count = 2
        else:
            print("Constructor out of scope ")

    def area_volume(self):   # member function to calculate area
        if (self.count == 0):
            self.area = 6*self.length**2
            self.volume = self.length ** 3
        elif (self.count == 1):
            self.area = (2*self.length**2)+(4*self.length*self.height)
            self.volume = (self.length ** 2) * self.height
        elif (self.count == 2):
            self.area = 2*(self.breadth*self.length+self.height*self.length+self.height*self.breadth)
            self.volume = self.length * self.breadth * self.height
        else:
            print("Something went worry")

    def display(self):
        print("\tArea :", self.area)
        print("\tVolume : ", self.volume)


cube = Box(10)
cube.area_volume()
cube.display()

sq_prism = Box(10, 5)
sq_prism.area_volume()
sq_prism.display()

rect_prism = Box(10, 11, 12)
rect_prism.area_volume()
rect_prism.display()