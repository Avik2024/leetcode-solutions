class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring where you can replace
        at most k characters to make all characters the same.

        Time Complexity: O(n), where n is the length of the string.
          - One pass with sliding window.
        Space Complexity: O(1), constant space for frequency array.

        :param s: str - input string of uppercase English letters
        :param k: int - max number of replacements allowed
        :return: int - length of longest valid substring
        """
        frequency_counter = [0] * 26
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            frequency_counter[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, frequency_counter[ord(s[right]) - ord('A')])

            # If current window size minus max frequency exceeds k, shrink window
            if (right - left + 1) - max_freq > k:
                frequency_counter[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
