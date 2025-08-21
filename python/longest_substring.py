class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Time Complexity: O(n), where n is the length of the string.
          - Each character is visited at most twice.
        Space Complexity: O(min(m, n)), where m is the size of the charset/alphabet.

        :param s: str - input string
        :return: int - length of the longest substring without repeating characters
        """
        char_index_map = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

