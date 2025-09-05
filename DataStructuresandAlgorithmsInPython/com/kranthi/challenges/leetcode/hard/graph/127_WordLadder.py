"""
You are given beginWord, endWord, and a word list.

Transform beginWord → endWord by changing one letter at a time.

Each transformed word must exist in the word list.

Return the minimum number of transformations needed (including begin + end).

If no transformation is possible → return 0.

Example:

Input: beginWord = "hit", endWord = "cog",
       wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

"""
from collections import deque
def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)

    # Base check
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])  # (word, depth)

    while queue:
        word, depth = queue.popleft()
        if word == endWord:
            return depth

        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i+1:]
                if newWord in wordSet:
                    queue.append((newWord, depth + 1))
                    wordSet.remove(newWord)  # mark visited

    return 0


# driving code
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))