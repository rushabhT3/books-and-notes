2nd study this:
# THE ULTIMATE DSA PATTERN BIBLE  
**Python Edition • Final Clean Version • 2025+**

This is the cleanest, most beautiful, and most complete version you'll ever see.  
Designed to be your lifelong reference. Save it, print it, live by it.

────────────────────────────────────────

### 1. Fast & Slow Pointers (Floyd's Cycle Detection)
**When:** Linked List cycle, find middle, palindrome, loop detection, Happy Number  
**Template:**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        # cycle detected or compute distance
        break
return slow  # or True/False
```
**Must Do:** 141, 142, 287, 876, 202, 457

### 2. Two Pointers (Opposite Ends)
**When:** Sorted array, Two Sum, Container With Most Water, Trapping Rain  
**Template:**
```python
l, r = 0, len(nums) - 1
while l < r:
    if nums[l] + nums[r] == target:
        return [l, r]
    elif nums[l] + nums[r] < target:
        l += 1
    else:
        r -= 1
```
**Must Do:** 167, 15, 16, 11, 42, 977

### 3. Sliding Window
**When:** Longest/shortest substring/subarray with constraint  
**Gold Template (Handles 99% cases):**
```python
from collections import Counter
l = best = 0
count = Counter()
for r, char in enumerate(s):
    count[char] += 1
    while len(count) > k:  # or any invalid condition
        count[s[l]] -= 1
        if count[s[l]] == 0:
            del count[s[l]]
        l += 1
    best = max(best, r - l + 1)
```
**Must Do:** 3, 76, 424, 340, 1004, 239, 295

### 4. Prefix Sum + Hash Map
**When:** Subarray sum equals k, count subarrays with sum/property  
**Template:**
```python
seen = {0: 1}
curr = ans = 0
for num in nums:
    curr += num
    ans += seen.get(curr - k, 0)
    seen[curr] = seen.get(curr, 0) + 1
```
**Must Do:** 560, 930, 974, 437, 525, 1074

### 5. Binary Search on Answer (Decision Boundary)
**When:** Minimize maximum, Koko, Ship packages, Split array  
**Template:**
```python
def can_do(mid):
    # return True if possible with mid

l, r = 1, max_possible  # usually 10**9
while l < r:
    mid = (l + r) // 2
    if can_do(mid):
        r = mid
    else:
        l = mid + 1
return l
```
**Must Do:** 875, 1011, 410, 1482, 778, 1552

### 6. BFS (Level Order / Shortest Path)
**When:** Shortest path in unweighted graph, rotten oranges, word ladder  
**Template:**
```python
from collections import deque
q = deque([(start, 0)])
visited = {start}
while q:
    node, dist = q.popleft()
    if node == target:
        return dist
    for nei in neighbors(node):
        if nei not in visited:
            visited.add(nei)
            q.append((nei, dist + 1))
```
**Must Do:** 994, 127, 126, 542, 286, 1091

### 7. DFS + Backtracking
**When:** Permutations, Combinations, Subsets, N-Queens, Sudoku  
**Template:**
```python
def backtrack(start, path):
    if len(path) == target:
        result.append(path[:])
        return
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue  # skip duplicates
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```
**Must Do:** 46, 47, 78, 90, 39, 40, 77, 51, 79

### 8. Tree DFS with State Return (Bottom-Up DP)
**When:** Diameter, Max Path Sum, Balanced Tree, LCA  
**Template (Exactly like 110 Balanced Tree):**
```python
def dfs(node):
    if not node: return 0
    
    left = dfs(node.left)
    right = dfs(node.right)
    
    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1
        
    return 1 + max(left, right)

return dfs(root) != -1
```
**Must Do:** 124, 543, 110, 236, 687, 337

### 9. Topological Sort (Kahn's Algorithm)
**When:** Course Schedule, Alien Dictionary  
**Template:**
```python
from collections import deque
indegree = [0] * n
for a, b in prerequisites:
    indegree[b] += 1

q = deque([i for i in range(n) if indegree[i] == 0])
count = 0
while q:
    node = q.popleft()
    count += 1
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)
return count == n
```
**Must Do:** 207, 210, 269, 310

### 10. Union Find (DSU) with Path Compression + Rank
**When:** Connected components, redundant connection, islands  
**Ultimate Template:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True
```
**Must Do:** 200, 547, 684, 128, 721, 399

### 11. Monotonic Stack
**When:** Next Greater, Largest Rectangle, Trapped Rain  
**Template:**
```python
stack = []
for i, h in enumerate(heights + [0]):
    while stack and heights[stack[-1]] > h:
        height = heights[stack.pop()]
        width = i - stack[-1] - 1 if stack else i
        area = height * width
        max_area = max(max_area, area)
    stack.append(i)
```
**Must Do:** 84, 42, 739, 496, 503, 901

### 12. Heap / Priority Queue
**When:** Merge K sorted, Top K, Median, Scheduling  
**Template:**
```python
import heapq
heap = []
for item in items:
    heapq.heappush(heap, (priority, item))
    if len(heap) > k:
        heapq.heappop(heap)
```
**Must Do:** 23, 295, 973, 355, 253, 218

### 13. Trie (Prefix Tree)
**When:** Word Search II, Autocomplete, Max XOR  
**Template:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
```
**Must Do:** 208, 212, 211, 421, 720

### 14. Binary Search on Rotated / Tricky Cases
**When:** Search in Rotated Sorted Array, Find Peak  
**Template:**
```python
l, r = 0, len(nums) - 1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    if nums[l] <= nums[mid]:  # left half sorted
        if nums[l] <= target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:  # right half sorted
        if nums[mid] < target <= nums[r]:
            l = mid + 1
        else:
            r = mid - 1
```
**Must Do:** 33, 153, 154, 162, 852

────────────────────────────────────────

### FINAL WORDS (Tattoo This)

> "Every LeetCode problem ever created is just 2 of the above patterns holding hands."

Master these 14.  
Do 20 problems each.  
Then close your laptop and go touch grass.

You are now officially dangerous.

Go collect offers like Pokémon cards.  
You've earned it.