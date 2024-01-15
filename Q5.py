class ThreeDShapes:
    volume = 0.0
    area = 0.0

    def print_volume(self):
        print("\tvolume", self.volume)

    def print_area(self):
        print("\tArea :", self.area)


class Cylinder(ThreeDShapes):
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def cal_area(self):
        self.area = 2*(22/7)*self.radius
        ThreeDShapes.print_area(self)

    def cal_volume(self):
        self.volume = 3.14 * (self.radius**2) * self.height
        ThreeDShapes.print_volume(self)


class Sphere(ThreeDShapes):
    def __init__(self,r):
        self.radius = r

    def cal_area(self):
        self.area = 4 * 3.14 * (self.radius**2)
        ThreeDShapes.print_area(self)

    def cal_volume(self):
        self.volume = (4/3) * 3.14 * (self.radius**3)
        ThreeDShapes.print_volume(self)


def main():
    print("_"*70)
    print("Cylinder : ")
    cylinderR = int(input("\tEnter Radius :"))
    cylinderH = int(input("\tEnter Height :"))
    cylinder_obj = Cylinder(cylinderR, cylinderH)
    cylinder_obj.cal_area()
    cylinder_obj.cal_volume()
    print("_" * 70)
    print("Sphere : ")
    sphereR = int(input("\tEnter Radius :"))
    sphere_obj = Sphere(sphereR)
    sphere_obj.cal_area()
    sphere_obj.cal_volume()
    print("_"*70)


main()
