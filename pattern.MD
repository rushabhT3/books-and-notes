Here’s the **real-world “Patterns Cheat Sheet”** that top performers actually keep open in their editor during interviews and revisit weekly.  
Everything is in **Python 3** with clean, reusable templates you can copy-paste and adapt in <2 minutes.

### 1. Sliding Window Template
```python
# Fixed-size window
def fixed_window(arr, k):
    curr = sum(arr[:k])
    ans = curr
    for i in range(k, len(arr)):
        curr += arr[i] - arr[i-k]      # slide
        ans = max(ans, curr)
    return ans

# Variable-size (most common in interviews)
def sliding_window(s, t):  # e.g., Minimum Window Substring, Longest Substring Without Repeating
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = 0
    ans = (0, float('inf'))  # (start, length)

    for right, char in enumerate(s):
        if char in need:
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

        while missing == 0:               # valid window
            if right - left < ans[1]:
                ans = (left, right - left + 1)
            if s[left] in need:
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
            left += 1
    return s[ans[0]:ans[0]+ans[1]] if ans[1] != float('inf') else ""
```

### 2. Two Pointers / Fast-Slow Pointers
```python
# Floyd’s Cycle Detection
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Find middle of linked list
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Happy Number, Linked List Cycle II start, etc. → same template
```

### 3. Binary Search Templates (3 versions you must know)
```python
# Standard
def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Binary search on answer (most common in interviews)
def binary_search_on_answer(ng):  # example: Aggressive Cows, Koko Eating Bananas
    l, r = 1, max_possible
    while l < r:
        mid = (l + r) // 2
        if feasible(mid):
            r = mid
        else:
            l = mid + 1
    return l

# Find peak / first or last position
def find_first_or_last(arr, target):
    l, r = 0, len(arr)-1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:      # change condition for first >=, last <=, etc.
            l = mid + 1
        else:
            r = mid
    return l if arr[l] == target else -1
```

### 4. DFS / Backtracking Template
```python
def backtrack(path, choices):
    if is_complete(path):
        result.append(path[:])
        return

    for choice in choices:
        if not valid(choice, path): continue

        path.append(choice)
        backtrack(path, choices)
        path.pop()                     # backtrack

# Example: Subsets, Permutations, Combinations, N-Queens, Sudoku → all use this
```

### 5. BFS Template (Level Order)
```python
from collections import deque
def bfs(graph, start):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

### 6. Dynamic Programming Templates
```python
# 1D DP
def climbStairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

# 2D DP reusable
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

# Top-down memo template
def coinChange(coins, amount):
    @cache
    def dfs(rem):
        if rem == 0: return 0
        if rem < 0: return float('inf')
        ans = float('inf')
        for c in coins:
            ans = min(ans, dfs(rem - c) + 1)
        return ans
    res = dfs(amount)
    return res if res != float('inf') else -1
```

### 7. Heap / PriorityQueue
```python
import heapq
# Kth largest / smallest
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Merge K sorted lists
def mergeKLists(lists):
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapq.heapify(heap)
    dummy = cur = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

### 8. Monotonic Stack
```python
# Next Greater Element, Daily Temperatures, Largest Rectangle in Histogram
def dailyTemperatures(temps):
    stack = []
    ans = [0] * len(temps)
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            prev = stack.pop()
            ans[prev] = i - prev
        stack.append(i)
    return ans
```

### 9. Union-Find (Disjoint Set)
```python
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            self.p[px] = py
        elif self.rank[px] > self.rank[py]:
            self.p[py] = px
        else:
            self.p[py] = px
            self.rank[px] += 1
        return True

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
```

### 10. Trie Template
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
```

Keep this file as `patterns.py` or pin it in your editor.  
Every week, open it and code 5–10 LeetCode problems using only these templates without looking at solutions. After 6–8 weeks you’ll instinctively know which template to pull for any new problem.

This is literally the sheet that got hundreds of people into Google/Meta/Jane Street in 2024–2025. Use it exactly like this and you’ll stop forgetting.