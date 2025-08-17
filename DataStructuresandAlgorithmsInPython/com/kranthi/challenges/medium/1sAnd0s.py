"""
generate-binary-permutations-1s-0s-every-point-permutations
enerate all permutations of given length such that every permutation has more or equal 1’s than 0’s in all
prefixes of the permutation.
Examples:

Input: len = 4
Output: 1111 1110 1101 1100 1011 1010
Note that a permutation like 0101 can not be in output because
there are more 0's from index 0 to 2 in this permutation.

Input: len = 3
Output: 111 110 101

Input: len = 2
Output: 11 10

[1,27,1,4,5,6,4,3,2,23434556,5566778,2,3,4,5,6,7,8]
k = 4
"""





def generate(ones, zeros, st, len1):
    if len(st) == len1:
        print(st, end=" ")
        return

    #append a 1 and recur
    generate(ones+1, zeros, st+"1", len1)

    # check if there are more 1's and append 0 as well and recur
    if ones > zeros:
        generate(ones, zeros+1, st+"0", len1)



st = ""
generate(0, 0, st, 4)