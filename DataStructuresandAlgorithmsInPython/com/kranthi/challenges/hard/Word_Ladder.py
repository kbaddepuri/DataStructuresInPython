"""
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation
sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation:
"hit" → "hot" → "dot" → "dog" → "cog"

Concept	Details
Graph Traversal	Think of each word as a node in a graph. An edge exists if two words differ by 1 letter.
BFS	Since we want the shortest transformation, use Breadth-First Search.
HashSet	Use it to check if words exist in the dictionary.
Queue	For level-order traversal (BFS).

💡 Approach
🔹 Step-by-step:
Add wordList to a HashSet for O(1) lookup.

Use a queue to do BFS from beginWord.

For each word, try changing each character from 'a' to 'z':

If the new word is in the wordSet and hasn't been visited, enqueue it.

Track the number of levels in BFS — this gives the shortest path length.

"""
from collections import deque

def wordLadder(beginWord, endWord, wordList):
    wordList = set(wordList)

    if endWord not in wordList:
        return 0

    


