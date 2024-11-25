
# We know that we contain the origin in a triangle, if the sides of the triangle intersect all of:
# (0,0) to (0,inf)
# (0,0) to (inf,0)
# (0,0) to (0,-inf)
# (0,0) to (-inf,0)
# As the points are -1000 <= x,y <= 1000, we can check just up to 1000 instead of infinity
# The formula for testing line intersection with two points is:
# t = ( (x1-x3)*(y3-y4) - (y1-y2)*(x1-x3) ) / ( (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) )
# u = ( (x1-x2)*(y1-y3) - (y1-y2)*(x1-x3) ) / ( (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) )
# If 0 <= t <= 1 and 0 <= u <= 1, the lines intersect


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Triangle:
    a: Point
    b: Point
    c: Point

    def includes_origin(self):
        pos_x = Point(1000, 0)
        neg_x = Point(-1000, 0)
        pos_y = Point(0, 1000)
        neg_y = Point(0, -1000)
        origin = Point(0, 0)

        intersect_pos_x = line_intersection(self.a, self.b, origin, pos_x) or line_intersection(self.b, self.c, origin, pos_x) or line_intersection(self.a, self.c, origin, pos_x)
        intersect_neg_x = line_intersection(self.a, self.b, origin, neg_x) or line_intersection(self.b, self.c, origin, neg_x) or line_intersection(self.a, self.c, origin, neg_x)
        intersect_pos_y = line_intersection(self.a, self.b, origin, pos_y) or line_intersection(self.b, self.c, origin, pos_y) or line_intersection(self.a, self.c, origin, pos_y)
        intersect_neg_y = line_intersection(self.a, self.b, origin, neg_y) or line_intersection(self.b, self.c, origin, neg_y) or line_intersection(self.a, self.c, origin, neg_y)

        # print(f"The triangle with points {self.a}, {self.b}, {self.c} intersects: pos_x: {intersect_pos_x}, neg_x: {intersect_neg_x}, pos_y: {intersect_pos_y}, neg_y: {intersect_neg_y}")

        return intersect_pos_x and intersect_neg_x and intersect_pos_y and intersect_neg_y
    
def line_intersection(p1, p2, p3, p4):
    t_nom = ( (p1.x-p3.x)*(p3.y-p4.y) - (p1.y-p3.y)*(p3.x-p4.x) )
    u_nom = ( (p1.x-p2.x)*(p1.y-p3.y) - (p1.y-p2.y)*(p1.x-p3.x) )
    denom = ( (p1.x-p2.x)*(p3.y-p4.y) - (p1.y-p2.y)*(p3.x-p4.x) )

    if denom == 0:
        return False
    
    return 0 <= t_nom/denom <= 1 and 0 <= u_nom/denom <= 1

triangles = []
with open("inputs/0102_triangles.txt") as f:
    for line in f:
        coords = list(map(int, line.strip().split(",")))
        triangles.append(Triangle(Point(coords[0], coords[1]), Point(coords[2], coords[3]), Point(coords[4], coords[5])))

triangles_with_origin = []
for triangle in triangles:
    if triangle.includes_origin():
        triangles_with_origin.append(triangle)

print(len(triangles_with_origin))
# Answer: 228