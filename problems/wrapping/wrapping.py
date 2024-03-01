from math import sin, cos, radians

def cross_product(o, a, b):
  return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Monotone chain algorithm
def convex_hull(points):
  # First, sort the points by x coordinate, then by y coordinate
  # Also remove duplicates
  points = sorted(set(points))

  # Edge case: 1 or less unique points
  if len(points) <= 1:
    return points

  # Build lower hull
  lower = []
  for p in points:
    while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
      lower.pop()
    lower.append(p)

  # Build upper hull
  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
      upper.pop()
    upper.append(p)

  # Combine the two hulls
  return lower[:-1] + upper[:-1]

def polygon_area(points):
  # calculate the area with shoe-lace formula
  m = len(points)
  area = 0
  for i in range(m):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % m]
    area += x1*y2 - x2*y1
  return area / 2

# Thanks ChatGPT
def rotate(x, y, ox, oy, theta):
    # Translate the point to the origin
    translated_x = x - ox
    translated_y = y - oy

    # Perform rotation
    rotated_x = translated_x * cos(theta) - translated_y * sin(theta)
    rotated_y = translated_x * sin(theta) + translated_y * cos(theta)

    # Translate the point back
    final_x = rotated_x + ox
    final_y = rotated_y + oy

    return final_x, final_y

def main():
    big_n = int(input())

    for i in range(big_n):
        n = int(input())
        board_area = 0
        total_area = 0

        points = []

        for j in range(n):
            x,y,w,h,v = map(float, input().split())
            w /= 2
            h /= 2
            v = radians(-v)

            p1 = rotate(x-w, y-h, x, y, v)
            p2 = rotate(x+w, y-h, x, y, v)
            p3 = rotate(x+w, y+h, x, y, v)
            p4 = rotate(x-w, y+h, x, y, v)

            board = [p1, p2, p3, p4]

            board_area += polygon_area(board)

            points += board

        total_area = polygon_area(convex_hull(points))

        ratio = board_area / total_area * 100

        print(round(ratio, 1), "%")

main()