"""
Find maximum depth of nested parenthesis in a string
Last Updated: 30-10-2020
We are given a string having parenthesis like below
     “( ((X)) (((Y))) )”
We need to find the maximum depth of balanced parenthesis, like 4 in the above example. Since ‘Y’
is surrounded by 4 balanced parentheses.
If parenthesis is unbalanced then return -1.
Examples :


Input : S = "( a(b) (c) (d(e(f)g)h) I (j(k)l)m)";
Output : 4

Input : S = "( p((q)) ((s)t) )";
Output : 3

Input : S = "";
Output : 0

Input : S = "b) (c) ()";
Output : -1

Input : S = "(b) ((c) ()"
Output : -1
"""

def maxDepth(S:str) -> int:
    cur_max = 0
    depth = 0

    for i in S:
        if i == '(':
            cur_max += 1
            if depth < cur_max:
                depth = cur_max
        elif i == ')':
            if cur_max > 0:
                cur_max -= 1
            else:
                return -1

    return depth


s = "(((X))(((Y))))"
print (maxDepth(s))
