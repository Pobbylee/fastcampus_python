# Triangle

def move_triangle(point0x, point0y, point1x, point1y, point2x, point2y):
    point0x += 1
    point0y += 1
    point1x += 1
    point1y += 1
    point2x += 1
    point2y += 1

# making triangle0
triangle0_name = "tri0"
triangle0_0x = 0
triangle0_0y = 0
triangle0_1x = 2
triangle0_1y = 0
triangle0_2x = 1
triangle0_2y = 2

# making triangle1
triangle1_name = "tri1"
triangle1_0x = 5
triangle1_0y = 5
triangle1_1x = 7
triangle1_1y = 5
triangle1_2x = 6
triangle1_2y = 7

move_triangle(triangle0_0x, triangle0_0y, triangle0_1x,
                triangle0_1y, triangle0_2x, triangle0_2y)

move_triangle(triangle1_0x, triangle1_0y, triangle1_1x,
                triangle1_1y, triangle1_2x, triangle1_2y)

print triangle0_2x
