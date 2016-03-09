# Triangle

class my_triangle:
    def __init__(self, name="noname", x0=0, y0=0, x1=0, y1=0, x2=0, y2=0):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def move(self):
        self.x0 += 1
        self.y0 += 1
        self.x1 += 1
        self.y1 += 1
        self.x2 += 1
        self.y2 += 1


t0 = my_triangle("Zix", 0, 0, 2, 0, 1, 2)
t1 = my_triangle("fastcampus", 5, 5, 7, 5, 6, 7)

print "--before moving--"
print t0.name, t0.x0, t0.x1
print t1.name, t1.x0, t1.x1

t0.move()
t1.move()
print "--after moving--"
print t0.name, t0.x0, t0.x1

print t0.get_cg()
