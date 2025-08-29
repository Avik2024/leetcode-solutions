from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Build Graph and in-degree map
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}  # All unique characters

        # Step 2: Build graph edges
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            # Edge case: prefix situation, e.g., "abc" -> "ab" (invalid)
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break  # Only first difference matters

        # ✅ Step 3: Topological sorting using BFS (Kahn's Algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check for cycle (incomplete ordering)
        if len(result) != len(in_degree):
            return ""

        return ''.join(result)
# Time Complexity - O(N + V + E)
# Space Complexity - O(V + E)
# Where V is the number of unique characters, E is the number of edges, N is the sum of length of all strings.
