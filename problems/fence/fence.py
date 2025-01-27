import math
def polygon_perimeter(points):
    perimeter = 0.0
    num_points = len(points)
    
    for i in range(num_points):
        # Get the current point and the next point (wrapping around to the first point)
        x1, y1,_,__ = points[i]
        x2, y2,_,__ = points[(i + 1) % num_points]
        
        # Calculate the distance between the points
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    
    return perimeter

def convex_hull(points): # O(n log n) complexity.
    # Remove duplicates to detect the case we have just one unique point.
    # points = sorted(set(points))
    if len(points) <= 1: #no points or a single point, possibly repeated multiple times
        return points
    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product. Returns a positive value, if OAB makes a counter-clockwise turn,negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = [] # Build lower hull 
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = [] # Build upper hull
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))
import itertools
while 1:
    n = ii()
    if n == 0:
        break

    trees = []
    for _ in range(n):
        x, y, v, l = mii()
        trees.append((x, y, v, l))
    
    trees.sort()

    best = float('inf')

    for i in range(1<= perim:
            # print("\t", perim, wood, cost)
            best = min(best, cost)
    
    print(f'The lost value is {best}.')