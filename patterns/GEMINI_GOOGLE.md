1st study this:
This format is designed for **study and memorization**. I have broken the 16 patterns down into logical categories.

Each card contains the **Signal** (when to use it), the **Code Skeleton** (memorize this), and the **Battleground** (problems to practice).

***

# THE ULTIMATE DSA PATTERNS CHEAT SHEET
**Python Edition • 2025 Final Version**

---

## PART 1: ARRAYS & POINTERS
*The bread and butter of interviews. Master these first.*

### 1. Fast & Slow Pointers (The Tortoise & Hare)
**The Signal:** Linked List cycles, finding the middle node, finding the start of a cycle, "Happy Number".
```python
def fast_slow(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True # Cycle detected
            
    return False
```
**The Battleground:** 141, 142, 287, 876, 202

### 2. Two Pointers (Opposite Ends)
**The Signal:** Sorted arrays, "Two Sum" in sorted array, reversing strings, checking palindromes.
```python
def two_pointers(nums, target):
    l, r = 0, len(nums) - 1
    
    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return [l, r]
        elif curr < target:
            l += 1
        else:
            r -= 1
    return []
```
**The Battleground:** 167, 15, 11, 125, 344, 977

### 3. Sliding Window (Variable Size)
**The Signal:** "Longest substring/subarray with condition", "Max consecutive ones", "Fruit into baskets".
```python
def sliding_window(s):
    l = 0
    ans = 0
    count = {} # Or a simple integer for sums
    
    for r in range(len(s)):
        # 1. Add right element
        count[s[r]] = count.get(s[r], 0) + 1
        
        # 2. Shrink left if invalid
        while not_valid_condition(count):
            count[s[l]] -= 1
            if count[s[l]] == 0: del count[s[l]]
            l += 1
            
        # 3. Update answer
        ans = max(ans, r - l + 1)
    return ans
```
**The Battleground:** 3, 76, 424, 209, 1004, 904

### 4. Prefix Sum + Hash Map
**The Signal:** "Subarray sum equals K", "Number of subarrays with sum...", continuous subarray problems.
```python
def subarray_sum(nums, k):
    prefix_map = {0: 1} # Base case: sum 0 happens once
    curr_sum = 0
    count = 0
    
    for num in nums:
        curr_sum += num
        # If (curr_sum - k) exists, we found a valid subarray ending here
        if (curr_sum - k) in prefix_map:
            count += prefix_map[curr_sum - k]
        
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
        
    return count
```
**The Battleground:** 560, 974, 525, 930, 437 (Tree version)

---

## PART 2: SEARCHING & SORTING
*Finding the needle in the haystack.*

### 5. Binary Search on Answer Space
**The Signal:** "Minimize the maximum", "Koko eating bananas", "Capacity to ship packages", "Smallest divisor".
**Note:** You are not searching the array; you are searching the range of possible answers (e.g., 1 to 10^9).
```python
def solve():
    def feasible(val):
        # Return True if 'val' is sufficient/possible
        pass

    l, r = 1, 10**9 
    while l < r:
        mid = (l + r) // 2
        if feasible(mid):
            r = mid # Try smaller
        else:
            l = mid + 1 # Need bigger
    return l
```
**The Battleground:** 875, 1011, 410, 1482, 1283

### 6. Modified Binary Search (Rotated/Tricky)
**The Signal:** Sorted array that was rotated, searching in a mountain array.
```python
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target: return mid
        
        # Check if Left side is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]: r = mid - 1
            else: l = mid + 1
        # Otherwise Right side is sorted
        else:
            if nums[mid] < target <= nums[r]: l = mid + 1
            else: r = mid - 1
    return -1
```
**The Battleground:** 33, 81, 153, 162 (Peak Element)

### 7. Top 'K' Elements (Heaps)
**The Signal:** "Find K largest/smallest", "Top K frequent", "Merge K sorted lists".
```python
import heapq

def find_k_largest(nums, k):
    heap = [] # Min-heap by default
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap) # Remove smallest of the bunch
            
    return heap[0] # The Kth largest
```
**The Battleground:** 215, 347, 23, 973, 692

---

## PART 3: TREES & GRAPHS
*The most common "Hard" patterns.*

### 8. BFS (Level Order Traversal)
**The Signal:** "Shortest path in unweighted graph", "Level order", "Nearest gate/rotting orange".
```python
from collections import deque

def bfs(root):
    if not root: return []
    q = deque([root])
    result = []
    
    while q:
        level = []
        for _ in range(len(q)): # Snapshot current level size
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result
```
**The Battleground:** 102, 107, 994 (Rotting Oranges), 127 (Word Ladder)

### 9. DFS (Recursive Backtracking)
**The Signal:** "Generate all subsets", "Permutations", "Combination Sum", "Sudoku".
```python
def backtrack(start, path):
    if is_solution(path):
        res.append(path[:]) # Copy path
        return

    for i in range(start, len(nums)):
        path.append(nums[i]) # 1. Choose
        backtrack(i + 1, path) # 2. Explore
        path.pop() # 3. Un-choose (Backtrack)
```
**The Battleground:** 46, 78, 39, 79 (Word Search), 51 (N-Queens)

### 10. DFS on Trees (Bottom-Up State)
**The Signal:** "Diameter of tree", "Is Balanced", "Max Path Sum".
**Key:** Ask child for info, process it, return info to parent.
```python
def max_path_sum(root):
    global_max = float('-inf')
    
    def dfs(node):
        nonlocal global_max
        if not node: return 0
        
        left = max(dfs(node.left), 0) # Ignore negative paths
        right = max(dfs(node.right), 0)
        
        # Update global maximum (the "Split" point)
        global_max = max(global_max, node.val + left + right)
        
        # Return max path extending down ONE side
        return node.val + max(left, right)
        
    dfs(root)
    return global_max
```
**The Battleground:** 124, 543, 110, 104

### 11. Topological Sort (Kahn's Algorithm)
**The Signal:** "Course Schedule", "Project Dependencies", "Build order", "Alien Dictionary".
```python
def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(n)}
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
        
    q = deque([node for node in indegree if indegree[node] == 0])
    result = []
    
    while q:
        node = q.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
                
    return result if len(result) == n else [] # Cycle detection
```
**The Battleground:** 207, 210, 269, 310
### Short Notes: Topological Sort (Kahn’s Algorithm)

**Edge `u → v`**  
- Means: **u must finish before v** starts  
- v depends on u → **only v’s indegree increases**

**Indegree[v]**  
- Number of incoming edges to v  
- Meaning: **“How many nodes must finish before v can start?”**  
- indegree = 0 → node is ready (no dependency)

**Why separate indegree map?**  
- Fast O(1) access & update  
- Needed for real-time decrement when a prerequisite finishes  
- Counting from graph each time would be O(n²) → too slow

**Queue (q)**  
- Initially contains all nodes with indegree == 0 (independent nodes)  
- While processing a node, reduce indegree of its neighbors  
- When any neighbor’s indegree becomes 0 → add to queue

**Result list**  
- Stores nodes in valid topological order

**Cycle Detection**  
```python
return result if len(result) == n else []
```
- If graph has a cycle → some nodes never get indegree 0  
- len(result) < n → cycle exists → return empty list  
- len(result) == n → valid DAG → return the order

**Summary in one line**  
Start with nodes having zero dependencies, keep freeing dependent nodes as their prerequisites finish. If all nodes get processed → valid order, else → cycle.

### 12. Union Find (Disjoint Set Union)
**The Signal:** "Connected components", "Number of Islands 2", "Redundant Connection", "Graph Valid Tree".
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]] # Path compression
            p = self.parent[p]
        return p
        
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True
```
**The Battleground:** 547, 684, 200, 305, 721

---

## PART 4: ADVANCED DATA STRUCTURES & DP
*The difference between L4 and L5/L6.*

### 13. Monotonic Stack
**The Signal:** "Next Greater Element", "Next Smaller Element", "Largest Rectangle in Histogram", "Daily Temperatures".
```python
def next_greater_element(nums):
    stack = [] # Stores indices
    res = [-1] * len(nums)
    
    for i, num in enumerate(nums):
        # While current num is greater than stack top
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            res[index] = num
        stack.append(i)
        
    return res
```
**The Battleground:** 739, 496, 503, 84, 42 (Trapping Rain Water)

### 14. Trie (Prefix Tree)
**The Signal:** "Autocomplete", "Word Search II", "Prefix matching".
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
```
**The Battleground:** 208, 211, 212, 1268

### 15. DP: 0/1 Knapsack (Subsets)
**The Signal:** "Partition Equal Subset Sum", "Target Sum", "Coin Change 2".
```python
def knapsack(nums, target):
    # dp[i] = can we sum to 'i'?
    dp = [False] * (target + 1)
    dp[0] = True # Base case
    
    for num in nums:
        # Iterate BACKWARDS to avoid using same item twice
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    return dp[target]
```
**The Battleground:** 416, 494, 322, 518

### 16. DP: Grid Paths
**The Signal:** "Unique Paths", "Min Path Sum", "Gold Miner".
```python
def grid_dp(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Fill first row/col based on logic
    # Iterate
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            
    return dp[m-1][n-1]
```
**The Battleground:** 62, 63, 64, 120, 221

***

# THE PLAN OF ATTACK

1.  **Don't memorize problems.** Memorize the **Signals** (When to use) and the **Templates** (Code skeletons above).
2.  **Order of Operations:**
    *   Week 1: Patterns 1, 2, 3 (Arrays)
    *   Week 2: Patterns 8, 9, 10 (Trees/Graphs)
    *   Week 3: Patterns 5, 6 (Search) + 7 (Heaps)
    *   Week 4: The rest.
3.  **The "Stuck" Rule:** If you can't solve a problem in 20 minutes, **STOP**. Look at the solution, identify which of the 16 patterns it uses, and write that down.


You now have the source code for the interview. Good luck.
