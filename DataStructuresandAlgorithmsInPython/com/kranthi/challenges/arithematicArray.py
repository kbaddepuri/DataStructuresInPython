def take_input():
    total_no_tests = int(input())

    for case in range(1, total_no_tests + 1):
        find_arithematic_array(case)


def find_arithematic_array(case: int):
    Narr = int(input())
    arr = input().split()
    arr = list(map(int, arr))
    max_length = 0
    tmp_arr = []

    i, j = 0, 1
    diff = arr[j] - arr[i]
    tmp_arr.append(arr[i])
    tmp_arr.append(arr[j])

    i, j = j, j + 1

    while j < Narr:
        if arr[j] - arr[i] == diff:
            tmp_arr.append(arr[j])
            j += 1
            i += 1

        else:
            if max_length < len(tmp_arr):
                max_length = len(tmp_arr)

            tmp_arr.clear()
            diff = arr[j] - arr[i]
            tmp_arr.append(arr[i])
            tmp_arr.append(arr[j])
            j += 1
            i += 1

    if tmp_arr:
        if max_length < len(tmp_arr):
            max_length = len(tmp_arr)

    print("Case #{}: {}".format(case, max_length))


take_input()