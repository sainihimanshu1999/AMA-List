'''
In this question bfs algorithm is used, as bfs is useful in findig the shortest distance between two
points
'''
from collections import deque
def wordLadder(beginWord,endWord,wordList):
    if endWord not in wordList:
        return 0

    wordList = set(wordList)

    qu = deque([[beginWord,1]])

    while qu:
        word,length = qu.popleft()

        if word == endWord:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i]+c+word[i+1:]
                if new_word in wordList:
                    wordList.remove(new_word)
                    qu.append([new_word,length+1])

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(wordLadder(beginWord,endWord,wordList))