"""
Add two numbers represented by linked lists | Set 1
Last Updated: 10-11-2020
Given two numbers represented by two lists, write a function that returns the sum list. The sum list is list
representation of the addition of two input numbers.

Example:

Input:
List1: 5->6->3 // represents number 365
List2: 8->4->2 // represents number 248
Output:l
Resultant list: 3->1->6 // represents number 613
Explanation: 365 + 248 = 613
Input:
List1: 7->5->9->4->6 // represents number 64957
List2: 8->4 // represents number 48
Output:
Resultant list: 5->0->0->5->6 // represents number 65005
Explanation: 64957 + 48 = 65005


Approach: Traverse both lists and One by one pick nodes of both lists and add the values.
If the sum is more than 10 then make carry as 1 and reduce sum. If one list has more elements than the other then consider remaining values of this list as 0.

The steps are:

Traverse the two linked lists from start to end
Add the two digits each from respective linked lists.
If one of the list has reached the end then take 0 as its digit.
Continue it until both the lists end.
If the sum of two digits is greater than 9 then set carry as 1 and the current digit as sum % 10
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while (first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data

            s = carry + fdata + sdata
            carry = 1 if s >= 10 else 0

            s = s if s < 10 else s%10

            temp = Node(s)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry == 1:
            temp.next = Node(carry)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next