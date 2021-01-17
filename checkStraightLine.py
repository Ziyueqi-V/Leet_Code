class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]):
        key = True
        A = coordinates[1][1] - coordinates[0][1]
        B = coordinates[0][0] - coordinates[1][0]
        C = coordinates[1][0] * coordinates[0][1] - coordinates[0][0] * coordinates[1][1]
        for item in coordinates:
                if A * item[0] + B * item[1] + C != 0:
                    key = False
                    break
        return key