class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Reasoning
        - swap the strings means that we have an anagrams
        - 26 unique characters beacuse they go from a to z
        - hashmap: value list of anagrams that count how many keys have those anagrams
        - counting the characters of the strings to find the patterns
        - O(n*m)
        '''
        res = defaultdict(list) #mapping characters count to list of anagrams
        for s in strs:
            count = [0]*26 #one 0 for each characters from a to z
            for c in s:
                count[ord(c)-ord("a")] += 1 #counting characters
                #for example ord(z) - a = 25 because the position of z is 26 and a is 1
            res[tuple(count)].append(s)
        return res.values()
