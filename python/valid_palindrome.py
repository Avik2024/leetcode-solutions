class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a palindrome considering only alphanumeric characters
        and ignoring case differences.

        Time Complexity: O(n), where n is the length of the string.
          - We traverse the string once.
        Space Complexity: O(1), as we use constant extra space for two pointers.

        :param s: str - Input string
        :return: bool - True if s is a palindrome, else False
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters after converting to lowercase
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
