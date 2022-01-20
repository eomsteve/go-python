import collections

input_list = ["eat","tea","tan","ate","nat","bat"]

anagrams = collections.defaultdict(list)

for word in input_list:
    anagrams[''.join(sorted(word))].append(word)
    print(list(anagrams.values()))
