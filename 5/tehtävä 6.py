import random

total_points = int(input("Syötä arvottavien pisteiden määrä: "))
if total_points <= 0:
    print("Arvottavien pisteiden määrä tulee olla positiivinen määrä: ")
else:
    points_inside_circle = 0
    points_generated = 0

    while points_generated <total_points:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2+y**2 <1:
           points_inside_circle +=1

        points_generated +=1
approximation = 4 * (points_inside_circle) / (total_points)
print(f"piin likiarvo {total_points} arvotulla pisteellä: {approximation}")