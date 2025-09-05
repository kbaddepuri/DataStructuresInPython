"""
Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts
and bolts. Match nuts and bolts efficiently.
Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be
compared with bolt and bolt can only be compared with a nut to see which one is bigger/smaller.
Examples:

Input : nuts[] = {'@', '#', '$', '%', '^', '&'}
        bolts[] = {'$', '%', '&', '^', '@', '#'}
Output : Matched nuts and bolts are-
        $ % & ^ @ #
        $ % & ^ @ #
"""
def nutsAndBoltMatch(nuts:list, bolts: list):

    hash = {}
    res = []
    n = len(nuts)
    for i in range(n):
        hash[nuts[i]] = nuts[i]

    # searcg for nuts for eac bolt in hashmap
    for i in range(n):
        if bolts[i] in hash:
            res.append((hash[bolts[i]], bolts[i]))

    for i in res:
        print(i, end=" ")

nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']
nutsAndBoltMatch(nuts, bolts)