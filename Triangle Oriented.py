"""

Triangle(A (5, 30) B (27, 43) C (18, 8) )
Area: 326.5
Perimeter: 87.24635135590786
Longest side: 36.138621999185304
Classify by Side Length: Isosceles
Is Right Triangle: True
Centroid: (16.666666666666668, 27.0)

"""

from math import sqrt
import math



def test_Triangle():
    t = Triangle((5,30), (27,43), (18,8))
    computed_area = t.area()
    computed_perimeter = t.perimeter()
    computed_longestside = t.LongestSide()
    EIS = t.ClassifyBySideLength()
    right_triangle = t.IsRightTriangle()
    centroid = t.Centroid()


class Triangle(object):

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        print("Triangle(A",A,"B",B,"C",C,")")

    def area(self):
        Ax, Ay = self.A
        Bx, By = self.B
        Cx, Cy = self.C
        area = 1/2*(abs(Ax*By - Ax*Cy + Bx*Cy - Bx*Ay + Cx*Ay - Cx*By))
        print("Area:",area)


    def perimeter(self):
        Ax, Ay = self.A
        Bx, By = self.B
        Cx, Cy = self.C
        AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
        BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
        AC = sqrt((Cx - Ax)**2 + (Cy - Ay)**2)
        perimeter = AB + BC + AC
        print("Perimeter:",perimeter)

    def LongestSide(self):
        Ax, Ay = self.A
        Bx, By = self.B
        Cx, Cy = self.C
        AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
        BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
        AC = sqrt((Cx - Ax)**2 + (Cy - Ay)**2)

        if BC <= AB >= AC:
            if AB == AC:
                print("Longest side:", AB)
            elif AB == BC:
                print("Longest side:", AB)
            else:
                print("Longest side:", AB)

        if BC <= AC >= AB:
            if AC == BC:
                print("Longest side:", AC)
            else:
                print("Longest side:", AC)

        if AB < BC > AC:
            print("Longest side:", BC)

    def ClassifyBySideLength(self):
        Ax, Ay = self.A
        Bx, By = self.B
        Cx, Cy = self.C
        AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
        BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
        AC = sqrt((Cx - Ax)**2 + (Cy - Ay)**2)

        if AB == AC == BC:
            print("Classify by Side Length: Equilateral")
        elif AB == AC:
            print("Classify by Side Length: Isosceles")
        elif AB == BC:
            print("Classify by Side Length: Isosceles")
        elif AC == BC:
            print("Classify by Side Length: Isosceles")
        else:
            print("Classify by Side Length: Scalene")

    def IsRightTriangle(self):
        Ax, Ay = self.A
        Bx, By = self.B
        Cx, Cy = self.C
        AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
        BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
        AC = sqrt((Cx - Ax)**2 + (Cy - Ay)**2)

        if AB <= BC >= AC:
            if BC**2 == (AB**2 + AC**2):
                print("Is Right Triangle:",True)
            else:
                print("Is Right Triangle:", False)
        if BC <= AB >= AC:
            if AB**2 == (AC**2 + BC**2):
                print("Is Right Triangle:", True)
            else:
                print("Is Right Triangle:", False)
        if AB <= AC >= BC:
            if AC**2 == (AB ** 2 + BC ** 2):
                print("Is Right Triangle:", True)
            else:
                print("Is Right Triangle:", False)

    def Centroid(self):
        Ax, Ay = self.A
        Bx, By = self.B
        Cx, Cy = self.C

        Ox = (Ax + Bx + Cx) / 3
        Oy = (Ay + By + Cy) / 3

        centroid = (Ox,Oy)

        print("Centroid:",centroid)



test_Triangle()
