score=0
def add_points(points):
    global score
    score = score + points
    return score

add_points(10)
add_points(20)
print("score:",score)