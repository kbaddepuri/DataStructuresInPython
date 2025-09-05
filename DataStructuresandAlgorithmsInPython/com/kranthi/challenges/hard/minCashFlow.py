N = 3
def getMax(arr):
    maxInd = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[maxInd]:
            maxInd = i

    return maxInd

def getMin(arr):
    minInd = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[minInd]:
            minInd = i

    return minInd

# A utility function to
# return minimum of 2 values
def minOf2(x, y):

    return x if x < y else y


def minCashFlowRec(arr):
    maxC = getMax(arr)
    maxD = getMin(arr)

    if arr[maxD] == 0 and arr[maxD] == 0:
        return 0

    _min = minOf2(-arr[maxD], arr[maxC])
    arr[maxC] -= _min
    arr[maxD] += _min

    print(f"Person {maxD} pays {_min} amount to person {maxC}")
    minCashFlowRec(arr)

def minCashFlow(graph):
    N = len(graph)
    amount = [0 for i in range(N)]

    for p in range(N):
        for i in range(N):
            amount[p]+= (graph[i][p] - graph[p][i])

    minCashFlowRec(amount)



graph = [ [0, 1000, 2000],
         [0, 0, 5000],
         [0,0,0] ]
minCashFlow(graph)