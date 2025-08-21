from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find the k most frequent elements in nums using bucket sort.

        Time Complexity: O(n), where n is the length of nums.
          - Counting frequencies and distributing into buckets each take O(n).
          - Collecting top k elements is also O(n) in worst case.
        Space Complexity: O(n), for frequency dictionary and buckets.

        :param nums: List[int] - Input list of integers
        :param k: int - Number of top frequent elements to return
        :return: List[int] - List of k most frequent integers
        """
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Count frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Place numbers into buckets based on frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # Gather top k frequent elements from highest frequency bucket down
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
