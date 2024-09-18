def find_busiest_intersections(intersections):
    # เช็คค่าว่าง
    if not intersections:
        return []

    # หาค่าจำนวนรถสูงสุด
    max_vehicles = max(intersections.values())

    busiest_intersections = [intersection for intersection, count in intersections.items() if count == max_vehicles]

    return busiest_intersections

# ข้อมูลตัวอย่าง
intersections_data = {
    "Intersection A": 120,
    "Intersection B": 150,
    "Intersection C": 150,
    "Intersection D": 100
}

print(find_busiest_intersections(intersections_data))
