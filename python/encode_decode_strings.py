from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string with length delimiters.

        Each string is encoded as <length>#<string> concatenated together.

        Time Complexity: O(n), where n is the total length of all strings.
          - Each character is processed once during encoding.
        Space Complexity: O(n), for the resulting encoded string.

        :param strs: List[str] - list of strings to encode
        :return: str - encoded string
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into a list of strings using length delimiters.

        Time Complexity: O(n), where n is the length of the encoded string.
          - Each character is visited at most once during decoding.
        Space Complexity: O(n), for storing all decoded strings.

        :param s: str - encoded string
        :return: List[str] - decoded list of strings
        """
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

