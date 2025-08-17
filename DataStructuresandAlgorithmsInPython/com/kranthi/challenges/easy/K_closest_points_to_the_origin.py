"""
Given a list of points on the 2-D plane and an integer K. The task is to find K closest points to the origin and
print them.
Note: The distance between two points on a plane is the Euclidean distance.

Input : point = [[3, 3], [5, -1], [-2, 4]], K = 2
Output : [[3, 3], [-2, 4]]
Square of Distance of origin from this point is
(3, 3) = 18
(5, -1) = 26
(-2, 4) = 20
So rhe closest two points are [3, 3], [-2, 4].

Input : point = [[1, 3], [-2, 2]], K  = 1
Output : [[-2, 2]]
Square of Distance of origin from this point is
(1, 3) = 10
(-2, 2) = 8
So the closest point to origin is (-2, 2)


Approach: The idea is to calculate the Euclidean distance from the origin for every given point and sort the array
according to the Euclidean distance found. Print the first k closest points from the list.

Algorithm :
Consider two points with coordinates as (x1, y1) and (x2, y2) respectively. The Euclidean distance between these two
points will be:

√{(x2-x1)2 + (y2-y1)2}
Sort the points by distance using the Euclidean distance formula.
Select first K points form the list
Print the points obtained in any order.

Complexity Analysis:

Time Complexity: O(n log n).
Time complexity to find the distance from the origin for every point is O(n) and to sort the array is O(n log n)
Space Complexity: O(n).
As we are making an array to store distance from the origin for each point.

"""

def kClosestPoints(points, K):
    if not points:
        return -1

    points.sort(key = lambda point: point[0]**2 + point[1]**2)
    return points[:K]

print(kClosestPoints([[3, 3], [5, -1], [-2, 4]], 2))