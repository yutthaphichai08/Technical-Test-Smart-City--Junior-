def find_busiest_intersections(intersections):

    # หาค่าจำนวนรถสูงสุด
    max_vehicles = max(intersections.values())

    busiest_intersections = [intersection for intersection, count in intersections.items() if count == max_vehicles]

    return busiest_intersections


print(find_busiest_intersections())
