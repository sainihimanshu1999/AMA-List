'''
In general cases of grouping and searchinf for the similar hash map/dictionaries usually occurs
'''

def anagrams(strs):
    maps = {}
    for key in strs:
        word = tuple(sorted(key))
        maps[word] = maps.get(word,[])+[key]
    return maps.values()