class Trie:
    def __init__(self, duplicates=False):
        self.children = {}
        self.dups = duplicates
        self.total = 0

    def add(self, word):
        current_dict = self.children
        for letter in word:
            current_dict = current_dict.setdefault(ord(letter), {})
            if self.dups:
                if ord("_") in current_dict:
                    current_dict[ord("_")] += 1
                else:
                    current_dict[ord("_")] = 1
                    self.total += 1
            else:
                current_dict[ord("_")] = 1
                self.total += 1

import sys
sys.setrecursionlimit(int(1e7))

n = int(input())
string = input()

graph = {i:[] for i in range(1,n+1)}

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

trie = Trie(True)

visited = set()
word = []
# recursive DFS to create all words from this root of the tree
def dfs(current):
    global word, visited
    word.append(string[current-1])
    visited.add(current)
    # trie.add(word)
    more = False
    for n in graph[current]:
        if n not in visited:
            more = True
            dfs(n)
    if not more:
        # print(word)
        trie.add(word)
    word.pop(-1)

# trie.add("abc")

# dfs from each node to create all possible strings
for i in range(1,n+1):
    visited = set()
    word = []
    dfs(i)

# print(trie.children)
print(trie.total)