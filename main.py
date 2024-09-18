import unittest

def find_busiest_intersections(intersections):
    # เช็คค่าว่าง
    if not intersections:
        return []

    # หาค่าจำนวนรถสูงสุด
    max_vehicles = max(intersections.values())
    busiest_intersections = [intersection for intersection, count in intersections.items() if count == max_vehicles]

    return busiest_intersections

class TestFindBusiestIntersections(unittest.TestCase):
    
    # intersection มีค่าต่างกัน
    def test_normal_case(self):
        intersections_data = {
            "Intersection A": 120,
            "Intersection B": 150,
            "Intersection C": 150,
            "Intersection D": 100
        }
        result = find_busiest_intersections(intersections_data)
        expected = ["Intersection B", "Intersection C"]
        self.assertEqual(result, expected)
        
    # กรณีที่ dictionary ได้
    def test_empty_dictionary(self):
        intersections_data = {}
        result = find_busiest_intersections(intersections_data)
        expected = []
        self.assertEqual(result, expected)
        
    # intersection เดียว
    def test_single_intersection(self):
        intersections_data = {
            "Intersection A": 120
        }
        result = find_busiest_intersections(intersections_data)
        expected = ["Intersection A"]
        self.assertEqual(result, expected)
        
    # มีค่าจำนวนรถเท่ากัน
    def test_all_same_values(self):
        intersections_data = {
            "Intersection A": 150,
            "Intersection B": 150,
            "Intersection C": 150
        }
        result = find_busiest_intersections(intersections_data)
        expected = ["Intersection A", "Intersection B", "Intersection C"]
        self.assertEqual(result, expected)
        
    # จำนวนรถสูงสุดเท่ากัน
    def test_multiple_maximum_values(self): 
        intersections_data = {
            "Intersection A": 120,
            "Intersection B": 150,
            "Intersection C": 150,
            "Intersection D": 150
        }
        result = find_busiest_intersections(intersections_data)
        expected = ["Intersection B", "Intersection C", "Intersection D"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
