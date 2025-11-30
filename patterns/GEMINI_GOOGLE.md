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

**Time and Space Complexity:** 
You're absolutely right in the **no-cycle** case — here's the short truth:

- **Without cycle** (e.g. finding middle - LeetCode 876):  
  They meet (or fast reaches end) when slow has moved **~n/2 steps** → fast moved **~n steps** → visited **~n nodes** (not 2n). So actually **O(n)** total work.

- **With cycle** (e.g. cycle detection - LeetCode 141/142):  
  In the **worst case**, slow enters the cycle and they meet only after slow traveled almost the full cycle length → fast may have lapped multiple times → in rare cases fast can visit up to **~2n nodes** before meeting.

**Bottom line (2 lines):**  
In the average/no-cycle case, fast visits ~n nodes → O(n).  
But the proven **worst-case upper bound** across all inputs is ≤ 2n node visits → we safely say **O(n)** time.  


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

**Time: O(n), Space: O(1)** — one pointer moves per iteration, at most n−1 moves total, using only two indices.

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

**TC (Time Complexity):**  
**O(n)** → each element is visited at most twice (once by `r`, once by `l`)

**SC (Space Complexity):**  
**O(k)** → where `k` is the size of the sliding window dictionary (at most `min(n, alphabet_size)`)

**Note (for dictionary):**
O(k): (k = max distinct chars allowed or alphabet size) (if we change [k] * 5 to dict it would be O(1) like that even though it's {k: 5})

Short form:  
**TC: O(n) | SC: O(k)**

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

**Core Idea:** If two prefix sums differ by exactly k, the elements between those two points add up to k.

**TC: O(n)** – one pass, hashmap ops are O(1)  
**SC: O(n)** – worst-case stores n different prefix sums

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

**📝Note:** 
- Finding a specific number? → `while l <= r`  
- Finding minimum possible value? → `while l < r` → return `l`  

That’s it. 2 rules. Forever. Done.

**THE ONE SENTENCE THAT ENDS ALL CONFUSION FOREVER:**  
> If `mid` could be the final answer → you do `r = mid`  
> If `mid` is definitely NOT the answer → you do `mid - 1` or `mid + 1`

**TC: O(log N)** × (cost of `feasible`)  
**SC: O(1)**

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

**TC: O(log N)**
**SC: O(1)**

### 7. Top 'K' Elements (Heaps)
**The Signal:** "Find K largest/smallest", "Top K frequent", "Merge K sorted lists".
```python
import heapq

def find_k_largest(nums, k):
    heap = [] # Min-heap by default
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:  # clever trick to heapq to have particular length
            heapq.heappop(heap) # Remove smallest of the bunch
            
    return heap[0] # The Kth largest
```
**The Battleground:** 215, 347, 23, 973, 692

**📝 Note:**

(here, k: numbers already inside the heapq, n: total number about to entered or pop)

- Every `heappush` → **O(log k)** (because current `n ≤ k+1`)
- Every `heappop` → **O(log k)**

That’s why we confidently say:  
> **Time Complexity = O(N log k)** for entering N elements in the heapq

⚠️ Warning: Inside a min-heap, only one thing is guaranteed: `heap[0]` is the smallest element. Everything else has no guaranteed order.  
That is why we cannot simply return `heap[k]`❌ after filling the heap.

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)
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

**📝 Reason to use `for _ in range(len(q))`:**

You’ll process nodes in correct order, but you won’t know where one level ends and the next begins, because children are added while you're still processing the current level.

So, basically where the for loop ends is the boundary for that row.

**Time Complexity:** O(N)  
**Space Complexity:** O(W) → where W is the maximum width of the tree (maximum number of nodes at any level)

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

📝**Note:**
From n elements you can form **2ⁿ** subsets.
For each of the n elements, you have exactly two choices when forming a subset:
- Include the element in the subset
- Exclude the element from the subset

Total number of subsets = 2 × 2 × 2 × … × 2 (n times) = **2ⁿ**

```python
res.append(path[:])          # This line costs O(len(path)) = O(n) in worst case
backtrack(i + 1, path)       # This is going deep and deep → that is why we are multiplying and not adding
```

**Time complexity: O(n × 2ⁿ)**

**Space complexity: O(n)**  
The path list can grow to a maximum size of n (if the subset includes all elements from nums). The recursion depth is also at most n.

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

### Time Complexity: O(n)
- **Every node is visited exactly once** during the DFS traversal.

### Space Complexity: O(h) where h = height of tree
- The recursion uses the **call stack**.
- The maximum depth of the recursion stack is equal to the **height of the tree**.

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

```python
def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(n)}    # O(V) space
    
    # Building graph and indegree → O(E) time, O(E) space
    for u, v in edges:                     # loops E times
        graph[u].append(v)                 # total edges stored = E
        indegree[v] += 1                   # each edge increases one count
    
    # Queue starts with all nodes having indegree 0 → O(V) time to scan
    q = deque([node for node in indegree if indegree[node] == 0])
    result = []
    
    # Main BFS loop
    while q:
        node = q.popleft()                 # each node processed once → O(V)
        result.append(node)
        
        for nei in graph[node]:            # total times this runs = E (all edges)
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)              # each node added to queue once → O(V)
    
    # Final check: if cycle exists, not all nodes were visited
    return result if len(result) == n else []   # O(1)
```
```python
# Time Complexity  : O(V + E)
#   → Every vertex is processed exactly once        → O(V)
#   → Every edge is looked at exactly once           → O(E)
#   → Total = O(V + E)

# Space Complexity : O(V + E)
#   → graph stores all edges                         → O(E)
#   → indegree dictionary has one entry per node     → O(V)
#   → queue can hold up to V nodes in worst case     → O(V)
#   → Total = O(V + E)
```
**Time Complexity**  **O(V + E)**  Each vertex and edge processed exactly once 

**Space Complexity** **O(V + E)**  Adjacency list dominates 

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
            self.parent[p] = self.parent[self.parent[p]] 
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

Here's a shortened version with all important details preserved:

---

**Union-Find Code Explained**
[https://youtu.be/ayW5B2W9hfo](url)

```python
class UnionFind:
    def __init__(self, n):
        # Each node is initially its own parent (isolated trees)
        self.parent = list(range(n))  # index: child and the value at that index: parent 
        # Rank tracks tree depth for balancing
        self.rank = [1] * n
        
    def find(self, n):  # root of the node 
        # Find the root representative of n's set
        p = self.parent[n]
        
        # Traverse up until finding a node that is its own parent (root)
        while p != self.parent[p]:                        # keep going until we reach the root
            # PATH COMPRESSION: Point to grandparent to shorten path
            self.parent[p] = self.parent[self.parent[p]]  # path compression step (kind of like linkedlist where connection index is connected to next value)
            p = self.parent[p]                            # move one step forward
        return p
        
    def union(self, n1, n2):  # if both nodes in same set or NOT
        # Merge sets containing n1 and n2
        p1, p2 = self.find(n1), self.find(n2)
        
        # Already in same set
        if p1 == p2: return False
        
        # UNION BY RANK: Attach shorter tree to taller tree
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True
```

**Key Optimizations:**

1. **Path Compression** (`self.parent[p] = self.parent[self.parent[p]]`):
   - Skips intermediate nodes by pointing to grandparent
   - Flattens tree structure over time through repeated applications
   - Reduces future lookups from O(N) to nearly O(1)
   - Works via while loop - doesn't need grandparent to be root, just closer to it

2. **Union by Rank**:
   - Attaches shorter tree to taller tree
   - Keeps maximum height logarithmic O(log N)
   - Prevents long linked-list structures

**Why Path Compression Works:**
- Even if grandparent isn't the root, the while loop continues climbing
- Example: Chain 0→1→2→3→4 (root)
  - Iteration 1: 0 points to 2 (skips 1)
  - Iteration 2: 2 points to 4 (skips 3)
  - Result: Path reduced from 4 to 2 hops
- Can't miss the root - worst case is pointing to root itself. Since the root's parent is the root itself (`parent[root] == root`), the while loop condition `p != self.parent[p]` will stop exactly at the root, ensuring we never skip past it.

**Complexity:** O(α(N)) where α is the Inverse Ackermann function - effectively O(1) constant time for all practical purposes.

---

## PART 4: ADVANCED DATA STRUCTURES & DP
*The difference between L4 and L5/L6.*

### 13. Monotonic Stack
**The Signal:** "Next Greater Element", "Next Smaller Element", "Largest Rectangle in Histogram", "Daily Temperatures".
```python
def next_greater_element(nums):
    stack = [] # Stores indices (here, it's like decreasing array element indices)
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

**Explanation:**
*Trie structure (shares common prefixes):*
```text
root
 ├── c
 │    ├── a
 │    │    ├── t → (end of "cat")
 │    │    └── r → (end of "car")
 │    │         └── t → (end of "cart")
 └── d
      └── o
           └── g → (end of "dog")
```
```python
def insert(self, word):
    curr = self.root             # Start from root
    for char in word:            # Go letter by letter
        if char not in curr.children:
            curr.children[char] = TrieNode()  # Create new branch
        curr = curr.children[char]            # Move down
    curr.is_end = True           # Mark: a word ends here!
```

### 15. DP: 0/1 Knapsack (Subsets: following solution is NOT real KnapSack problem: but it's special version)
**The Signal:** "Partition Equal Subset Sum", "Target Sum", "Coin Change 2".
```python
def knapsack(nums, target):
    # dp[i] = can we sum to 'i'?
    dp = [False] * (target + 1)       # target + 1: because we care about upto target values NOT len(nums)
    dp[0] = True # Base case
    
    for num in nums:
        # Iterate BACKWARDS to avoid using same item twice
        for i in range(target, num - 1, -1):      # target to num range as going further down would be less than 0 
            if dp[i - num]:
                dp[i] = True
    return dp[target]
```
**The Battleground:** 416, 494, 322, 518

The knapsack problem is a `classic optimization problem where you must choose items with a certain weight and profit to include in a knapsack with a limited weight capacity, with the goal of maximizing the total profit`. It involves deciding which items to pack to get the most value without exceeding the weight limit. Common variations include the 0-1 knapsack problem, where each item can either be included or not, and the fractional knapsack problem, where you can take parts of items. 

## Why Reverse Iteration (“Inverse Propagation”) in 0/1 Knapsack Prevents Duplicate Use (but in unbounded it's different way)

1. **DP State Setup**

   * Suppose you use a 1D dp array: `dp[w]` = maximum value you can get with capacity exactly `w`.
   * You iterate through each item `i` and for each capacity `w`, you consider whether to take that item or not.

2. **Risk if You Iterate Forwards**

   * If you do:

     ```python
     for each item i:  
       for w = wt[i] to W:  
         dp[w] = max(dp[w], dp[w - wt[i]] + val[i]);  
     ```
   * Here, when you compute `dp[w]`, `dp[w - wt[i]]` **might have already been updated in the same iteration** of item `i`. That means you could be reusing the same item `i` more than once in this item’s iteration → Leading to duplicate usage, which is **not allowed** in 0/1 knapsack.
   * This is precisely why for 0/1 knapsack, you should loop capacity in reverse.

3. **Reverse Loop Fixes This**

   * Instead, do:

     ```python
     for each item i:  
       for (w = W; w >= wt[i]; w--) {  
         dp[w] = max(dp[w], dp[w - wt[i]] + val[i]);  
       }  
     ```
   * Because you're going from high `w` down to `wt[i]`, when you refer to `dp[w - wt[i]]`, that value is from **before** this iteration of `i` (i.e., from the “previous item state”), not something you may have just modified.
   * This ensures **each item is used at most once** in that iteration, thereby correctly implementing 0/1 knapsack. ([thealgorists.com][1])

4. **In Unbounded Knapsack (Duplicates Allowed)**

   * When duplicates are allowed (unbounded knapsack), you can (and do) iterate forwards:

     ```python
     for each item i:  
       for (w = wt[i]; w <= W; w++) {  
         dp[w] = max(dp[w], dp[w - wt[i]] + val[i]);  
       }  
     ```
   * Here, using `dp[w - wt[i]]` is okay because you **want** to be able to reuse the same item multiple times — forward iteration helps “propagate” the value, allowing multiple picks. ([Astik Anand][2])

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

**More Generic Template:**
```python
def solve_grid(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # STEP 1: BASE CASE
    # (Initialize the starting point)
    dp[0][0] = ... 

    # STEP 2: HANDLE EDGES 
    # (The first row and first column usually have restricted movement)
    for i in range(1, m): ...
    for j in range(1, n): ...

    # STEP 3: THE CORE LOGIC
    # (The generic formula for the rest of the grid)
    for i in range(1, m):
        for j in range(1, n):
             # This is the only line that changes based on the problem
             dp[i][j] = ... 
             
    return dp[-1][-1]
```

***

## PART 5: THE "GOOGLE" GAPS
*Patterns specifically for optimization, scheduling, and system design components.*

### 17. Dijkstra’s Algorithm (Weighted Shortest Path)
**The Signal:** "Shortest path" in a graph with **weights** (time, cost, distance). BFS only works for unweighted graphs.
**Note:** If weights are negative, you need Bellman-Ford (rare).
```python
import heapq

def dijkstra(n, edges, start_node):
    # 1. Build Graph: u -> (v, weight)
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        
    # 2. Min-Heap: (current_dist, node)
    min_heap = [(0, start_node)]
    
    # 3. Track shortest distances
    shortest = {} # or [float('inf')] * n
    
    while min_heap:
        w1, n1 = heapq.heappop(min_heap)
        
        if n1 in shortest: continue # Already processed
        shortest[n1] = w1
        
        for n2, w2 in graph[n1]:
            if n2 not in shortest:
                heapq.heappush(min_heap, (w1 + w2, n2))
                
    return shortest
```
**The Battleground:** 743 (Network Delay), 787 (Cheapest Flights), 1631, 1514

### 18. Merge Intervals (Sweeping Line)
**The Signal:** "Meeting Rooms," "Calendar conflicts," "Merge overlapping intervals."
**Key:** Always sort by start time first.
```python
def merge_intervals(intervals):
    # 1. Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_end = merged[-1][1]
        current_start, current_end = current
        
        # 2. Overlap detected -> Merge
        if current_start <= last_end:
            merged[-1][1] = max(last_end, current_end)
        else:
            # 3. No overlap -> Add new interval
            merged.append(current)
            
    return merged
```
**The Battleground:** 56, 57, 435, 252 (Premium), 253 (Premium)

### 19. Design Data Structures (LRU Cache)
**The Signal:** "Design a data structure that supports..." (Usually O(1) get and put).
**Key:** Combine a **Hash Map** (for lookup) with a **Doubly Linked List** (for ordering).
```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # Map key -> Node
        # Dummy head and tail to avoid edge cases
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Helper: Remove node from List
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper: Insert at Right (Most Recent)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # Evict LRU (Left-most real node)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```
**The Battleground:** 146 (LRU), 460 (LFU), 380 (Insert Delete GetRandom), 155 (Min Stack)

---

## PART 6: SPECIALIST TRICKS
*Math, Bits, and Queues. High ROI for low code volume.*

### 20. Bit Manipulation (XOR Tricks)
**The Signal:** "Find the single number in array of duplicates," "Missing number," "Sum of two integers without +".

**Concept:** `n ^ n = 0` and `n ^ 0 = n` (since, $n \oplus 0 = n \cdot 1 + \overline{n} \cdot 0$ so, $\overline{n} \cdot 0$ becomes 0)
```python
def find_single_number(nums):
    xor = 0
    for n in nums:
        xor ^= n
    return xor
```
**The Battleground:** 136, 268, 371, 191, 338

### 21. Monotonic Queue (Sliding Window Max)
**The Signal:** "Maximum value in a sliding window of size K." (Note: Standard sliding window finds sums/counts; this finds Max/Min).
```python
from collections import deque

def max_sliding_window(nums, k):
    output = []
    q = deque() # Stores INDICES
    
    for r in range(len(nums)):
        # 1. Pop smaller values from back (they are useless now)
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        # 2. Remove value from front if it's out of window
        if q[0] < r - k + 1:   
            q.popleft()
            
        # 3. Add to output (front is always the max)
        if r + 1 >= k:                # "Have we seen at least k elements yet?"
            output.append(nums[q[0]])
            
    return output
```
**The Battleground:** 239, 1438, 862

### why use r - k + 1 and NOT r - k for the block space: Suppose `k = 3`, and we’re at index `r = 4`

The current window should be indices: **2, 3, 4**

Now answer this:

| Formula             | Result | Is this the correct left index? |

|---------------------|--------|---------------------------------|

| `r - k`   → 4 - 3   | 1      | No! Index 1 is **not** in the current window anymore |

| `r - k + 1` → 4 - 3 + 1 | 2  | Yes! This is exactly the first index of the current window |

So:

- `r - k`     → gives **one index too early** (the one that just slid out)

- `r - k + 1` → gives the **correct start** of the current window

### 22. Reservoir Sampling (Probabilistic)
**The Signal:** "Select K random elements from a stream," "Linked List too large for memory," "Random Pick Index."
```python
import random

def pick_random(head):
    scope = 1
    chosen_value = 0
    curr = head
    
    while curr:
        # Probability of picking current node is 1/scope
        if random.random() < (1 / scope): 
            chosen_value = curr.val
        curr = curr.next
        scope += 1
    return chosen_value
```
**The Battleground:** 382, 398

For this line: `if random.random() < (1 / scope):`  
The trick is that we keep one candidate, and as we walk through the list, we give the current node a chance to replace the candidate.

***

### UPDATED STUDY PLAN (The "Complete" 22)

To be "Google Ready," you must rearrange the study order slightly to prioritize these new patterns:

1.  **Phase 1 (Core):** Arrays & Two Pointers (Patterns 1, 2, 3, 13)
2.  **Phase 2 (Structure):** Trees, Graphs & **Design** (Patterns 8, 9, 10, 19)
3.  **Phase 3 (Search):** Binary Search & Heaps & **Dijkstra** (Patterns 5, 6, 7, 17)
4.  **Phase 4 (Optimization):** DP, Greedy & **Intervals** (Patterns 15, 16, 18)
5.  **Phase 5 (Niche):** Bit Manipulation & Reservoir Sampling (Patterns 20, 22)

**Final Warning:**
If you see a problem involving **"Range Sum Updates"** (where values in the array change and you need the sum of a range repeatedly), you need a **Segment Tree**. This is Pattern #23. It is rare. If you have time, look up `LeetCode 307`. If you are short on time, skip it—you can pass without it, but you cannot pass without the 22 above.


















