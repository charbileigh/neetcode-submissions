import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return []

        left = 0
        right = len(points) - 1
        target = k - 1

        while left <= right:
            pivot_point = points[random.randint(left, right)]
            pivot = pivot_point[0] ** 2 + pivot_point[1] ** 2

            smaller = left
            current = left
            larger = right

            while current <= larger:
                x, y = points[current]
                distance = x * x + y * y

                if distance < pivot:
                    points[smaller], points[current] = (
                        points[current], points[smaller]
                    )
                    smaller += 1
                    current += 1

                elif distance > pivot:
                    points[current], points[larger] = (
                        points[larger], points[current]
                    )
                    larger -= 1

                else:
                    current += 1

            if target < smaller:
                right = smaller - 1
            elif target > larger:
                left = larger + 1
            else:
                break

        return points[:k]