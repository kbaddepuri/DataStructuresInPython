# Python3 program to print all conflicting
# appointments in a given set of appointments

# Structure to represent an interval
class IntervalNode:
    def __init__(self, low, high):
        self.interval = (low, high)
        self.max = high
        self.left = None
        self.right = None


def insert(root, low, high):
    if not root:
        return IntervalNode(low, high)
    if low < root.interval[0]:
        root.left = insert(root.left, low, high)
    else:
        root.right = insert(root.right, low, high)

    root.max = max(root.max, high)
    return root

def doOverlap(i1, i2):
    return i1[0] <= i2[1] and i2[0] <= i1[1]

def overlapSearch(node, query, result=None):
    if result is None:
        result = []

    if node is None:
        return result
    if doOverlap(node.interval, query):
        result.append(node.interval)

    if node.left and node.left.max >= query[0]:
        overlapSearch(node.left, query, result)

    overlapSearch(node.right, query, result)
    return result


# Driver code
if __name__ == '__main__':
    # -------------------------------
    # Demo: Build the tree and query
    # -------------------------------
    intervals = [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]
    root = None
    for low, high in intervals:
        root = insert(root, low, high)

    # Search for overlapping intervals
    query_interval = (14, 16)
    overlaps = overlapSearch(root, query_interval)

    print(f"Overlapping intervals with {query_interval}: {overlaps}")