class TimeMap:
    def __init__(self):
        # keyStore maps each key to a list of [value, timestamp] pairs
        # Space Complexity: O(m * n) where m = number of unique keys, n = number of total set operations
        self.keyStore = {}  # key: List of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key with the value along with a timestamp.
        Time Complexity: O(1)
        """
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieve the value such that the given key was set at the largest timestamp <= given timestamp.
        Time Complexity: O(log n) where n is the number of pairs for the key (due to binary search)
        """
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                res = values[m]
                l = m + 1
            else:
                r = m - 1
        return res
