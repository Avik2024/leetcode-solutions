class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if string t is an anagram of string s.

        Time Complexity: O(n), where n is the length of the strings.
          - Counting characters in each string takes linear time.
        Space Complexity: O(1), as the character count dictionaries' size
          is bounded by the character set (e.g., ASCII or Unicode).

        :param s: str - First string
        :param t: str - Second string
        :return: bool - True if t is an anagram of s, else False
        """
        if len(s) != len(t):
            return False 
        
        countS, countT = {}, {}
        
        for char in s:
            countS[char] = 1 + countS.get(char, 0)
        
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        return countS == countT
