import random
total_points = int(input("Total_points: "))
points_generated =""
points_inside_circle = ""

while total_points != 0:
     x = random.randint(-1,1)
     y = random.randint(-1,1)
     if (x^2+y^2) <1:
      points_inside_circle = int(input("points_inside_ciecle: "))
     print(points_inside_circle)
if points_generated == 4 * (points_inside_circle) / (total_points):
 print(points_generated)
