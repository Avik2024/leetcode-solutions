from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups a list of strings into anagrams.
        
        Time Complexity: O(n * k log k), where n is the number of strings and k is the max length of a string.
          - Sorting each string takes O(k log k), done n times.
        Space Complexity: O(n * k), storing all strings in the output and hashmap.
        
        :param strs: List[str] - List of input strings
        :return: List[List[str]] - List of groups of anagram strings
        """
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string to generate a key
            key = "".join(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())
