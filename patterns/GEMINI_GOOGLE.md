1st study this:
This format is designed for **study and memorization**. I have broken the 16 patterns down into logical categories.

Each card contains the **Signal** (when to use it), the **Code Skeleton** (memorize this), and the **Battleground** (problems to practice).

## Flashcards: [Notebook llm](https://notebooklm.google.com/notebook/980f76e7-a7da-4b8d-b842-99d54549447b)

# THE ULTIMATE DSA PATTERNS CHEAT SHEET
**Python Edition • 2026 Final Version**

---

## PART 1: ARRAYS & POINTERS

### Reverse Linked List:
```python
prev, curr = None, head
while curr:
    next_temp = curr.next   # save the curr.next point as that will be eliminated
    curr.next = prev
    prev, curr = curr, next_temp
return prev
```
or,
```python
prev, curr = None, head
while curr:
    curr.next, prev, curr = prev, curr, curr.next  #⚠️DON'T change the sequence
return prev
```

*The bread and butter of interviews. Master these first.*

### 1. Fast & Slow Pointers (The Tortoise & Hare)
**The Signal:** Linked List cycles, finding the middle node, finding the start of a cycle, "Happy Number".
```python
def fast_slow(head):
    slow, fast = head, head    
    
    while fast and fast.next:   # fast and fast.next both needed; checking only fast.next it may crash since fast may NOT be present 
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
**The Signal:** "Longest substring/subarray with condition", "Max consecutive ones", "Fruit into baskets". The Goal: Finding "Extreme Limits" (The Longest, The Shortest, The Maximum).
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
**The Signal:** "Subarray sum equals K", "Number of subarrays with sum...", continuous subarray problems. The Goal: Finding "Exact Targets" (Count how many, or find a specific sum).
```python
def subarray_sum(nums, k):
    prefix_map = {0: 1} # This handles the base case where a subarray starting from index 0 has the required sum `k`.
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

**Core Idea:** 
### The Analogy: The "Road Trip"

<img width="593" height="286" alt="image" src="https://github.com/user-attachments/assets/72106273-b1f6-4dc3-b519-ec5b01f8cab5" />

Imagine driving down a highway and wanting to find sections that are exactly **100 miles long**. 

Instead of measuring each section, you track your total distance from the start using `curr_sum`. 

At 1:00 PM, your odometer reads 50 miles. At 3:00 PM, it reads 150 miles. 

Since 150 - 50 = 100, you've found a section that is exactly 100 miles long.

So `curr_sum - prev_sum = k` becomes the `curr_sum - k` and hence something must exist.

**TC: O(n)** – one pass, hashmap ops are O(1)  
**SC: O(n)** – worst-case stores n different prefix sums

📝 Note: **Sliding Window finds the optimal *range* (Max/Min), whereas Prefix Sum uses a historical *map* to count every instance where the exact "gap" to your target (k) exists.**
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
        mid = l + (r - l) // 2
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

**The Essential Binary Search "Muscle Memory"**

In interviews, prefer `mid = low + (high - low) / 2` over `mid = (low + high) / 2`.

**1. The Bug: Integer Overflow (Java/C++)**
Languages like Java and C++ have fixed integer limits (~2.14 Billion).
*   **Scenario:** If `low` = 2B and `high` = 2.1B, `low + high` = 4.1B. This overflows to a negative number, causing a crash.

**2. The Fix: The Safe Formula**
`mid = low + (high - low) / 2` calculates the distance first.
*   `high - low` is small (0.1B), avoiding overflow.
*   **Python Note:** Python handles arbitrarily large integers automatically, so it will **not** overflow or crash with the "bad" formula. However, using the "safe" formula is still recommended to show you understand low-level constraints.

**3. Math vs. Computers**
Algebraically identical, but computationally distinct. The "safe" formula respects hardware limits.

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

### Median from Data Stream (Two Heaps Pattern)

Signal phrases:

* **"Find median"**
* **"Middle element in stream"**
* **"Balance two halves"**
* **"Kth largest in stream"** (variation)

📝 **Imagine:** Min-heap stores the "Top Half" ($> \text{median}$), Max-heap stores the "Bottom Half" ($\le \text{median}$); keep Small size $\ge$ Large size.

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (stores smaller half, negate values)
        self.large = []  # Min heap (stores larger half)
    
    def addNum(self, num):
        # Step 1: Add to max heap (small half)
        heapq.heappush(self.small, -num)
        
        # Step 2: Balance - move largest of small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 3: Keep sizes balanced (small >= large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

```

### Complexity Analysis

| Operation | Time Complexity | Reason |
| --- | --- | --- |
| **addNum** | $O(\log n)$ | Multiple heap pushes/pops. |
| **findMedian** | $O(1)$ | Accessing top elements `self.small[0]` or `self.large[0]`. |
| **Space** | $O(n)$ | Storing all  elements from the stream. |

---

## PART 3: TREES & GRAPHS

### Validate BST:

> left: boundary (minimum), root: (the middle), right: boundary (maximum)

```python
# ⚠️ In Python, you cannot put a "regular" argument (like root) after an argument with a default value (like left=float('-inf')).
# => def isValidBST(left=float('-inf'), root, right=float('inf')): is WRONG ❌

def isValidBST(root, left=float('-inf'), right=float('inf')):
    # 1️⃣ base condition 
    if not root:
        return True
    # 2️⃣ for that particular node/level condition 
    if not (left < root.val < right):
        return False
    # 3️⃣ propogate it further
    return (isValidBST(root.left, left, root.val) and 
            isValidBST(root.right, root.val, right))
```

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

### Combinations: 
**The Signal:** "Generate all subsets", "Combination Sum", "Sudoku".
Example: Input: [1, 2, 3] → Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

```python
def subsets(nums):
    res = []
    
    def backtrack(start, path):
        # 1️⃣ base condition
        if is_solution(path):
            res.append(path[:]) 
            return
        
        for i in range(start, len(nums)):
            # 2️⃣ Choose 
            path.append(nums[i])
            # 3️⃣ Explore: Move to the next index
            backtrack(i + 1, path)
            # 4️⃣ Unchoose: Backtrack to try the next number at this position
            path.pop()             

    # 📝 start from the empty array or the 0 index
    backtrack(0, [])
    return res

subsets([1, 2, 3])
```
**The Battleground:** 46, 78, 39, 79 (Word Search), 51 (N-Queens)

```python
def subsets(nums):
    res = []
    
    def backtrack(start, path):
        if is_solution(path):
            res.append(path[:]) # Must copy! Otherwise all reference same list
            return
        
        for i in range(start, len(nums)): # start to prevent going backward
            path.append(nums[i])   # Modify the ONE path # 1. Choose
            backtrack(i + 1, path) # Pass same path deeper  # 2. Explore
            path.pop()             # Undo modification # 3. Un-choose (Backtrack)
    
    backtrack(0, [])
    return res

subsets([1, 2, 3])
```

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

---

### Permutations: 
**The Signal**: "All possible arrangements", "Rankings".
Example: Input: [1, 2, 3] → Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

```python
def permutations(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if is_satisfied():
            result.append(path[:])
            return

        for i in range(len(nums)):
            # since we start from the start only we can repeat and this is for so that it won't repeat
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            backtrack(path)

            path.pop()
            used[i] = False

    # ⚠️ backtrack from start NOT backtrack from nums we gotta build the result from start
    backtrack([])
    return result
```
1. **Time Complexity (TC)**: $O(n \cdot n!)$
   $n!$: There are $n$ factorial total permutations. For example, if $n=3$, there are $3 \times 2 \times 1 = 6$ results.
   
   $n$: For each of those $n!$ results, you perform a path[:] copy, which takes $O(n)$ time.
   
   Total: $O(n \cdot n!)$. This grows much faster than $O(2^n)$.
3. **Space Complexity (SC)**: $O(n)$ Recursion Stack: The maximum depth of the "tree" is $n$

---

### Grid Pattern:

**The Signal:** "Word Search", "Number of Islands", "Unique Paths", "Snake/Maze".
**Example:** Can you find "ABCCED" in the 2D matrix?

```python
def grid_search(grid, word):
    rows, cols = len(grid), len(grid[0])
    
    def backtrack(r, c, index):
        # 1️⃣ Success Base Case: We found all characters
        if index == len(word):
            return True
            
        # 2️⃣ Constraint Base Case: Out of bounds, wrong char, or already visited
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] != word[index]):
            return False
        
        # 3️⃣ Choose: Mark as visited so we don't use the same cell twice in one path
        temp = grid[r][c]
        grid[r][c] = "#" 
        
        # 4️⃣ Explore: Move in 4 directions (Down, Up, Right, Left)
        # In grid patterns, we usually use 'or' to stop early if we find the path
        found = (backtrack(r + 1, c, index + 1) or 
                 backtrack(r - 1, c, index + 1) or 
                 backtrack(r, c + 1, index + 1) or 
                 backtrack(r, c - 1, index + 1))
        
        # 5️⃣ Un-choose: Backtrack by restoring the cell for other starting points
        grid[r][c] = temp
        
        return found

    # Start the search from every possible cell in the grid
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False
```

### 📊 Complexity Analysis for Grid

1. **Time Complexity (TC): $O(N \cdot M \cdot 3^L)$**

- $N \cdot M$: We start a search from every cell in the grid.
- $3^L$: From each cell, we explore 4 directions initially, then 3 directions (since we don't go back to where we just came from) up to length $L$ of the word.

2. **Space Complexity (SC): $O(L)$**

- $L$: The maximum depth of the recursion stack is the length of the word/path. If you use a separate visited matrix, it would be $O(N \cdot M)$, but the "in-place mark" (#) keeps it at $O(L)$.

### 📝 Note: In backtracking, the arguments placed in the functions are those which changes like index and path in combinations, the path in the permutations and the (r,c) and the index or current_word_length in the grid pattern.

---

### 10. DFS on Trees (Bottom-Up State)
**The Signal:** "Diameter of tree", "Is Balanced", "Max Path Sum".
**Key:** Ask child for info, process it, return info to parent.
```python
def max_path_sum(root):
    global_max = float('-inf')
    
    def dfs(node): # dfs: for get_weighted_height
        nonlocal global_max
        if not node: return 0
        
        left = max(dfs(node.left), 0) # Ignore negative paths 
        right = max(dfs(node.right), 0)
        
        # Update global maximum (the "Split" point)
        global_max = max(global_max, node.val + left + right) # when it not weighted we use 1 instead of node.val
        
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

---

### Python Scoping: Reassignment vs. Mutation

In Python, you can **read** any variable from an outer scope. However, if you want to **modify** it, the rules change based on the data type:

* **Primitives (Immutable):** For types like `int`, `float`, `str`, or `tuple`, you must use the `nonlocal` keyword. Without it, using the `=` operator creates a new **local** variable instead of updating the one outside.
* **Non-Primitives (Mutable):** For types like `list` or `dict`, you do **not** need `nonlocal` to modify their contents. Since you are **mutating** the object (e.g., `arr[0] = val`) rather than **reassigning** the variable name itself, Python allows the change directly.

---

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
    def __init__(self, n): # here, n: number of nodes
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, n1):  # here, n1: node whose parent has to be found
        while n1 != self.parent[n1]:
            self.parent[n1] = self.parent[self.parent[n1]] 
            n1 = self.parent[n1]
        return n1
        
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

| Line                                           | What it does                                                  | Result                  |
|------------------------------------------------|---------------------------------------------------------------|-------------------------|
| `self.parent[p] = self.parent[self.parent[p]]` | Changes where node `p` points → **skip one middleman**        | `parent[2]` becomes `0` |
| `p = self.parent[p]`                           | Now move `p` to the **new place** (grandparent)               | `p` jumps from `2 → 0`  |

```python
class UnionFind:
    def __init__(self, n):
        # Each node is initially its own parent (isolated trees)
        self.parent = list(range(n))  # index: child and the value at that index: parent 
        # Rank tracks tree depth for balancing
        self.rank = [1] * n
        
    def find(self, n):  # root of the node 
        # Find the root representative of n's set
        # Traverse up until finding a node that is its own parent (root)
        while n1 != self.parent[n1]:                        # keep going until we reach the root
            # PATH COMPRESSION: Point to grandparent to shorten path
            self.parent[n1] = self.parent[self.parent[n1]]  # path compression step (kind of like linkedlist where connection index is connected to next value)
            n1 = self.parent[n1]                            # move one step forward
            # ⚠️ confusion: n1 = self.parent[n1] so it should stop as it became it's parent but in next loop it'll check if it's currently it's own parent so this is how it's getting forwarded
        return n1
        
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

1. **Path Compression** (`self.parent[n1] = self.parent[self.parent[n1]]`):
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

**Time and Space Complexity:** O(α(N)) where α is the Inverse Ackermann function - effectively O(1) constant time for all practical purposes.

---

## PART 4: ADVANCED DATA STRUCTURES & DP
*The difference between L4 and L5/L6.*

### 13. Monotonic Stack
**The Signal:** "Next Greater Element", "Next Smaller Element", "Largest Rectangle in Histogram", "Daily Temperatures".
```python
def next_greater_element(nums):
    stack = [] # Stores indices (here, it's like decreasing array element indices)
    res = [-1] * len(nums)  # stores value of next greater element
    
    for i, num in enumerate(nums):
        # While current num is greater than stack top
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            res[index] = num
        stack.append(i)
        
    return res
```
**The Battleground:** 739, 496, 503, 84, 42 (Trapping Rain Water)

| Aspect            | Complexity | Reason                                                            |
|-------------------|------------|-------------------------------------------------------------------|
| Time Complexity   | O(n)       | Each element is pushed and popped from the stack at most once     |
| Space Complexity  | O(n)       | Output array + stack (worst case: all elements stored in stack)  |

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
```python
curr = curr.children['a']
```
→ curr now points to the 'a' node.
search and startwith functions NOT so different.

### Trie Complexity Analysis
| Operation          | Time Complexity          | Space Complexity                  | Notes |
|--------------------|--------------------------|-----------------------------------|-------|
| `insert(word)`     | **O(L)**                 | **O(L)** (worst case)             | L = length of the word <br> No new nodes if word already exists (O(1) space in that case) |
| `search(word)`     | **O(L)**                 | **O(1)**                          | Only traverses existing nodes |
| `startsWith(prefix)` | **O(P)**               | **O(1)**                          | P = length of prefix |
| Overall storage (N words, avg length L) | -              | **O(N × L)**                      | Total nodes ≈ total characters across all words |

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
            dp[i] = dp[i] or dp[i - num]  
    return dp[target]
```
**The Battleground:** 416, 494, 322, 518

 **Why `dp[i]` is in the RHS (`dp[i] = dp[i] or ...`)**: This preserves existing "True" values. If a sum was already possible using previous items, we don't want to overwrite it with False just because the current item can't form it.

The **Knapsack problem** maximizes value within a weight limit. **0/1 Knapsack** allows taking an item once or not at all, while **Unbounded Knapsack** allows using an item infinite times.

## Why Reverse Iteration Prevents Duplicates (0/1 Knapsack)

1.  **Forward Iteration Risk (Unbounded)**:
    If you loop `w` from `wt[i]` to `W`, the check `dp[w - wt[i]]` accesses the value you *just updated* earlier in the same loop. This creates a "chain reaction" where item `i` is used repeatedly to build larger sums. This effectively solves the **Unbounded Knapsack** problem.

2.  **Reverse Loop Fix (0/1)**:
    Looping `w` from `W` down to `wt[i]` guarantees that `dp[w - wt[i]]` reads the state from the **previous** item's iteration (before the current item was touched). This ensures the item is added at most once.

### Scenario A: The Mistake (Looping Forwards)
Let's look at what happens if we write `for i in range(2, 5)`:

1.  **i = 2**:
    *   Code: `dp[2] = dp[2] or dp[2 - 2]`
    *   Check: `dp[0]` is **True**.
    *   Result: `dp[2]` becomes **True**.
    *   *Meaning: "We have used the number 2 to make sum 2."*

2.  **i = 3**:
    *   Code: `dp[3] = dp[3] or dp[3 - 2]`
    *   Check: `dp[1]` is False.
    *   Result: `dp[3]` stays False.

3.  **i = 4**:
    *   Code: `dp[4] = dp[4] or dp[4 - 2]`
    *   **THE BUG:** It looks at `dp[2]`. We **just made** `dp[2]` True in step 1!
    *   Result: `dp[4]` becomes **True**.
  
      
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
**Time Complexity: O(m × n)
Space Complexity: O(m × n)**
We visit each cell exactly once → m rows × n columns = O(mn) operations.

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
                new_dist = w1 + w2
                heapq.heappush(min_heap, (new_dist, n2))
                
    return shortest
```
<details>
<summary><h3>↕️ Show/Hide Dijkstra’s Algorithm Explanation</h3></summary>

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, start_node):
    """
    Implements Dijkstra's algorithm to find the shortest path distances
    from a single start_node to all other nodes in a graph with non-negative weights.
    
    Parameters:
        n:          Number of nodes (usually 0 to n-1 or 1 to n, depending on input)
        edges:      List of tuples (u, v, w) meaning there is a directed edge from u to v with weight w
        start_node: The node from which to start computing shortest paths
    
    Returns:
        shortest:   Dictionary {node: distance} containing the shortest distance from start_node
                    to each reachable node. Unreachable nodes are not included.
    """
    
    # Step 1: Build the adjacency list representation of the graph
    # graph[u] will contain a list of tuples (v, w) meaning "from u you can go to v with cost w"
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))  # Directed edge: u -> v with weight w
        # If the graph is undirected, you would also add: graph[v].append((u, w))
    
    # Step 2: Initialize the priority queue (min-heap)
    # We store tuples (current_known_distance, node)
    # heapq will always give us the node with the smallest known distance first
    min_heap = [(0, start_node)]  # Distance to start_node is 0
    
    # Step 3: Dictionary to store the final shortest distance to each node
    # Once a node is added here, we know its shortest distance has been found
    shortest = {}  # Will map node -> shortest distance from start_node
    # Alternative: you could use a list of size n initialized with float('inf')
    
    # Main loop: continue until we have processed all reachable nodes
    while min_heap:
        # Pop the node with the smallest current known distance
        w1, n1 = heapq.heappop(min_heap)  # w1 = distance to n1, n1 = current node
        
        # Optimization: if we already found a better (or equal) path to n1 earlier,
        # we can skip processing this outdated entry
        if n1 in shortest:
            continue  # This entry is obsolete; we already processed this node
        
        # We have now found the true shortest distance to n1
        # Record it (this node is now "settled")
        shortest[n1] = w1
        
        # Explore all neighbors of the current node n1
        for n2, w2 in graph[n1]:  # n2 = neighbor, w2 = edge weight from n1 to n2
            # Only consider neighbors that haven't been settled yet
            if n2 not in shortest:
                # New candidate distance to n2: distance to n1 + edge weight
                new_distance = w1 + w2
                # Push this possibility into the heap
                # Note: we may push multiple entries for the same node with different distances
                # That's okay — the first time we pop the best one, we settle it and ignore later worse ones
                heapq.heappush(min_heap, (new_distance, n2))
    
    # At the end, shortest contains the minimal distance from start_node to every reachable node
    return shortest
```

Oh so it's kind of greedy algorithm; since we are choosing the least ones it is not possible to that point have the shortest in future.

</details>

**The Battleground:** 743 (Network Delay), 787 (Cheapest Flights), 1631, 1514

**TC and SC:**
The complexity depends on which data structure you use to find the nearest vertex. Let $V$ be the number of vertices and $E$ be the number of edges.

| Implementation Type | Time Complexity | Space Complexity | Best For |
| :--- | :--- | :--- | :--- |
| **Priority Queue (Binary Heap)** | **$O(E \log V)$** | **$O(V + E)$** | **Sparse Graphs** |
| **Linear Array (No Heap)** | **$O(V^2)$** | **$O(V + E)$** | **Dense Graphs** |
| **Fibonacci Heap** (Theoretical) | $O(E + V \log V)$ | $O(V + E)$ | Extremely Large/Complex |

<details>
    <summary>
        <h3>↕️ Show/Hide Dijkstra’s Algorithm TC and SC</h3>
    </summary>

Here are the Time Complexity (TC) and Space Complexity (SC) for Dijkstra’s Algorithm, followed by an explanation of why your intuition regarding the Priority Queue and dense graphs is correct.

### 1. Complexities

The complexity depends on which data structure you use to find the nearest vertex. Let $V$ be the number of vertices and $E$ be the number of edges.

| Implementation Type | Time Complexity | Space Complexity | Best For |
| :--- | :--- | :--- | :--- |
| **Priority Queue (Binary Heap)** | **$O(E \log V)$** | **$O(V + E)$** | **Sparse Graphs** |
| **Linear Array (No Heap)** | **$O(V^2)$** | **$O(V + E)$** | **Dense Graphs** |
| **Fibonacci Heap** (Theoretical) | $O(E + V \log V)$ | $O(V + E)$ | Extremely Large/Complex |

*(Note: In most standard libraries like C++ STL or Python `heapq`, the actual time is $O(E \log E)$, but since $E \le V^2$, $\log E \approx 2 \log V$, so it simplifies to $O(E \log V)$. Space is $O(V+E)$ because we store the graph ($V+E$) and the distance array/queue ($V$ or $E$ depending on implementation).)*

---

### 2. Is the Priority Queue (PQ) only good when it's not dense?

**Yes, you are absolutely correct.**

Using a Priority Queue (Binary Heap) is actually **slower** than a simple array if the graph is very dense.

#### Here is the math behind why:

A **Dense Graph** is one where the number of edges is close to the maximum possible number of edges ($E \approx V^2$).

Let's compare the operations:

**A. Using a Simple Array (Linear Scan):**
*   **Logic:** For every vertex, we iterate through all other vertices to find the minimum distance.
*   **Math:** $O(V^2)$
*   **Result:** Even if $E = V^2$, the complexity remains **$O(V^2)$**.

**B. Using a Priority Queue (Binary Heap):**
*   **Logic:** Every time we relax an edge, we push/update the heap. A heap operation costs logarithmic time.
*   **Math:** $O(E \log V)$
*   **Result in a Dense Graph ($E \approx V^2$):**
    Substitute $V^2$ for $E$:
    $$O(V^2 \log V)$$

#### The Comparison:
*   **Linear Array:** $V^2$
*   **Priority Queue:** $V^2 \times \log V$

Since $\log V \ge 1$, **$V^2 \log V$ is greater than $V^2$**.

### Summary
*   **Sparse Graph ($E \approx V$):** The Priority Queue is much faster ($V \log V$ vs $V^2$).
*   **Dense Graph ($E \approx V^2$):** The Priority Queue is slower because of the overhead of sorting/maintaining the heap structure for so many edges. The simple array scan wins here.
---
This is the standard **"Lazy" Dijkstra** implementation using a Priority Queue. This is the most common version you will write in an interview.

Here is the line-by-line breakdown of the **Time Complexity (TC)** and **Space Complexity (SC)**.

### Summary
*   **Time Complexity:** $O(E \log E)$ which simplifies to **$O(E \log V)$**
*   **Space Complexity:** **$O(V + E)$**

---

### Detailed Breakdown

#### 1. Building the Graph
```python
# 1. Build Graph
graph = defaultdict(list)
for u, v, w in edges:       # Loops E times
    graph[u].append((v, w)) # O(1) operation
```
*   **TC:** **$O(E)$**. We iterate through the list of edges once.
*   **SC:** **$O(V + E)$**. We store $V$ keys (nodes) and a total of $E$ items inside the lists.

#### 2. The Main Loop (The Heavy Lifter)
```python
while min_heap:  # Can run up to E times (Worst case)
    w1, n1 = heapq.heappop(min_heap)
```
*   **TC:** **$O(E \log E)$**
    *   In this "Lazy" implementation, we don't update priorities inside the heap; we just add duplicates.
    *   Worst case: The heap contains every edge ($E$) in the graph.
    *   `heappop` takes logarithmic time relative to the size of the heap: $O(\log E)$.
    *   We might pop up to $E$ times. Total: $E \times \log E$.

*(Note: Since $E \le V^2$, mathematically $\log E$ is effectively the same as $2 \log V$. So we usually write $O(E \log V)$. Both are correct.)*

#### 3. The Lazy Check
```python
    if n1 in shortest: continue # O(1) average lookup
    shortest[n1] = w1           # O(1)
```
*   **TC:** $O(1)$.
*   **Logic:** This is crucial. This line ensures we don't process the same node twice. Even if the heap has duplicates, we skip them here.

#### 4. The Neighbors Loop
```python
    for n2, w2 in graph[n1]:    # Iterates over neighbors
        if n2 not in shortest:
            new_dist = w1 + w2
            heapq.heappush(min_heap, (new_dist, n2))
```
*   **TC:** **$O(E \log E)$**
    *   **The Loop:** Across the entire lifespan of the algorithm, this inner loop runs exactly **$E$** times (once for every edge in the graph).
    *   **The Push:** `heapq.heappush` takes $O(\log E)$ (log of current heap size).
    *   **Total:** We push into the heap at most $E$ times. Total: $E \times \log E$.

---

### Space Complexity Analysis

1.  **`graph` Dictionary:**
    *   Holds all nodes and edges.
    *   **$O(V + E)$**

2.  **`shortest` Dictionary:**
    *   Holds the final distance for every node.
    *   **$O(V)$**

3.  **`min_heap`:**
    *   This is the tricky one. In a "perfect" theoretical Dijkstra, the heap size is $V$.
    *   But in this **Python "Lazy" Dijkstra**, we do not delete old paths. If we find a shorter path to a node, we just add a *new* entry to the heap.
    *   Therefore, the heap can grow to store every edge in the graph in the worst case.
    *   **$O(E)$**

**Total Space:** $O(V + E + V + E) \approx$ **$O(V + E)$**.

### Why is this efficient?
Even though the heap grows to size $E$ (making it slightly larger than the theoretical $V$), the logic `if n1 in shortest: continue` ensures we ignore the "bad" duplicates instantly. The ease of writing this code outweighs the minor space overhead compared to writing a complex Indexed Priority Queue.


</details>

[Visualize Dijkshtra's Algo](https://youtu.be/bZkzH5x0SKU ) 

[Dijkstra's Algorithm - Why PQ and not Q](https://www.youtube.com/watch?v=3dINsjyfooY)


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
**Time Complexity: O(n log n)  # sorting the interval
Space Complexity: O(n)**


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

    # Helper: Remove node from List (just in the linked list not the cache dictionary)
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper: Insert at Right (Most Recent) (just in the linked list not the cache dictionary)
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

### Explanation: 
**The dictionary answers “WHERE is the node?”**

**The linked list answers “IN WHAT ORDER is the node?”**

<img width="975" height="789" alt="Screenshot 2025-12-14 181547" src="https://github.com/user-attachments/assets/1cf10cb5-9980-4e56-a4ae-ba050c5450e3" />

| | Time Complexity | Space Complexity |
|--|-----------------|------------------|
| `get()` | **O(1)** | - |
| `put()` | **O(1)** | - |
| Overall | - | **O(n)** where n = capacity |

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
Time Complexity: O(n)
Space Complexity: O(1)

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

### How to Compute the Left Index of a Sliding Window of Size `k`

| Formula       | Example (`r=4`, `k=3`) | Result | Is this the correct left index?                       |
|---------------|-------------------------|--------|-------------------------------------------------------|
| `r - k`       | 4 - 3                   | 1      | No! Index 1 is **not** in the current window anymore  |
| `r - k + 1`   | 4 - 3 + 1               | 2      | Yes! This is exactly the first index of the window    |

**Summary:**
- `r - k` → gives **one index too early** (the one that just slid out)
- `r - k + 1` → gives the **correct start** of the current window of size `k`

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

<details>
    <summary> <h3>↕️ Show/Hide Probability Explanation </h3></summary>

## Calculate Final Probability for Each Element

### Element A (position 1)

```
P(A is final) = P(pick A) × P(survive step 2) × P(survive step 3) × P(survive step 4)

             = 1/1 × (1 - 1/2) × (1 - 1/3) × (1 - 1/4)
               ↓        ↓           ↓           ↓
             = 1   ×   1/2    ×    2/3    ×    3/4
             
             = 1/4  ✓
```

### Element B (position 2)

```
P(B is final) = P(pick B) × P(survive step 3) × P(survive step 4)

             = 1/2 × (1 - 1/3) × (1 - 1/4)
               ↓        ↓           ↓
             = 1/2  ×  2/3    ×    3/4
             
             = 1/4  ✓
```

### Element C (position 3)

```
P(C is final) = P(pick C) × P(survive step 4)

             = 1/3 × (1 - 1/4)
               ↓        ↓
             = 1/3  ×  3/4
             
             = 1/4  ✓
```

### Element D (position 4)

```
P(D is final) = P(pick D)    ← No future steps to survive!

             = 1/4  ✓
```

### why choosing 1 - 1/n as the survivor of the probability?

Think only like this (super simple):

You have 4 elements: A B C D

For A to win in the end, A must survive 3 attacks:

- When B comes → B must NOT kick A out → probability = 1 - 1/2 = 1/2  
  (B gets only 50% chance to replace)

- When C comes → C must NOT kick A out → probability = 1 - 1/3 = 2/3  
  (C gets only ~33% chance)

- When D comes → D must NOT kick A out → probability = 1 - 1/4 = 3/4  
  (D gets only 25% chance)

So A’s total chance = 1 × (1/2) × (2/3) × (3/4) = 1/4

The “1 - 1/scope” is just “chance the new guy fails to kick out the current champion”.

Every element gets exactly the same fair 1/n chance because the later elements have higher chance to get picked first but lower chance to survive the remaining attacks — everything cancels out perfectly.

the old one is not going to change but individually they only have power like 1/n to remove is that why?
---

## Visual Summary

```
Element   PICK prob    SURVIVAL prob           FINAL prob
────────────────────────────────────────────────────────────
   A        1/1    ×   1/2 × 2/3 × 3/4    =      1/4
   B        1/2    ×   2/3 × 3/4          =      1/4
   C        1/3    ×   3/4                =      1/4
   D        1/4    ×   (nothing)          =      1/4
────────────────────────────────────────────────────────────
                                    ALL EQUAL! ✓
```

## Even without explicit multiplication like above how it's working?
### Now Focus on Just Element A

For A to be the FINAL answer, what must happen?

```
Step 1:  chosen = A         ← A enters the box

Step 2:  If random() < 0.5  → B kicks A out! GAME OVER for A
         If random() >= 0.5 → A stays in box ✓

Step 3:  If random() < 0.33 → C kicks A out! GAME OVER for A  
         If random() >= 0.33→ A stays in box ✓

Step 4:  If random() < 0.25 → D kicks A out! GAME OVER for A
         If random() >= 0.25→ A stays in box ✓
```
***
# Can We Use `>` Instead of `<`?

## Short Answer: NOT directly, but with modification YES

---

## Let's See What Happens with Direct Change

### Original: `random.random() < (1/scope)`

```
scope=1:  random() < 1.0   →  100% chance to pick  ✓
scope=2:  random() < 0.5   →  50% chance to pick   ✓
scope=3:  random() < 0.33  →  33% chance to pick   ✓
scope=4:  random() < 0.25  →  25% chance to pick   ✓
```

### Changed: `random.random() > (1/scope)`

```
scope=1:  random() > 1.0   →  0% chance to pick    ✗ NEVER PICKS FIRST!
scope=2:  random() > 0.5   →  50% chance to pick
scope=3:  random() > 0.33  →  67% chance to pick   ✗ WRONG!
scope=4:  random() > 0.25  →  75% chance to pick   ✗ WRONG!
```

**This is COMPLETELY BROKEN!**

---

## The Fix: Change the Threshold

To use `>`, we need to flip the threshold:

```
Original:    random() < (1/scope)
Equivalent:  random() > (1 - 1/scope)
             random() > ((scope - 1) / scope)
```

### Verify the Math

```
scope=1:  random() > (1-1)/1 = 0    →  ~100% chance  ✓
scope=2:  random() > (2-1)/2 = 0.5  →  50% chance    ✓
scope=3:  random() > (3-1)/3 = 0.67 →  33% chance    ✓
scope=4:  random() > (4-1)/4 = 0.75 →  25% chance    ✓
```

---

## Working Code with `>`

```python
import random

def pick_random(head):
    scope = 1
    chosen_value = 0
    curr = head
    
    while curr:
        # Changed: using > with flipped threshold
        if random.random() > ((scope - 1) / scope): 
            chosen_value = curr.val
        curr = curr.next
        scope += 1
    return chosen_value
```

---

## Side-by-Side Comparison

```
┌─────────────────────────────────────────────────────────────┐
│  ORIGINAL                    EQUIVALENT WITH >              │
├─────────────────────────────────────────────────────────────┤
│  random() < (1/scope)   ═══  random() > ((scope-1)/scope)  │
├─────────────────────────────────────────────────────────────┤
│  scope=1: < 1.0              scope=1: > 0.0                 │
│  scope=2: < 0.5              scope=2: > 0.5                 │
│  scope=3: < 0.33             scope=3: > 0.67                │
│  scope=4: < 0.25             scope=4: > 0.75                │
├─────────────────────────────────────────────────────────────┤
│  SAME PROBABILITIES!                                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Visual Proof

```
random() returns value in [0, 1)

Using < (1/scope):
    |████████|          |  scope=1: 100% (all values work)
    |████|              |  scope=2: 50%  
    |███|               |  scope=3: 33%
    |██|                |  scope=4: 25%
    0        0.5        1

Using > ((scope-1)/scope):
    |████████|          |  scope=1: 100% (all values work)  
    |        |████|     |  scope=2: 50%
    |            |███|  |  scope=3: 33%
    |              |██| |  scope=4: 25%
    0        0.5        1
    
Different regions, SAME sizes!
```

---

## Summary

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ✗  random() > (1/scope)         →  BROKEN                 │
│                                                             │
│  ✓  random() > ((scope-1)/scope) →  WORKS (equivalent)     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</details>

### UPDATED STUDY PLAN (The "Complete" 22)

To be "Google Ready," you must rearrange the study order slightly to prioritize these new patterns:

1.  **Phase 1 (Core):** Arrays & Two Pointers (Patterns 1, 2, 3, 13)
2.  **Phase 2 (Structure):** Trees, Graphs & **Design** (Patterns 8, 9, 10, 19)
3.  **Phase 3 (Search):** Binary Search & Heaps & **Dijkstra** (Patterns 5, 6, 7, 17)
4.  **Phase 4 (Optimization):** DP, Greedy & **Intervals** (Patterns 15, 16, 18)
5.  **Phase 5 (Niche):** Bit Manipulation & Reservoir Sampling (Patterns 20, 22)

**Final Warning:**
If you see a problem involving **"Range Sum Updates"** (where values in the array change and you need the sum of a range repeatedly), you need a **Segment Tree**. This is Pattern #23. It is rare. If you have time, look up `LeetCode 307`. If you are short on time, skip it—you can pass without it, but you cannot pass without the 22 above.

Here is the **Tier 2 (The Google/Uber Standard)** and **Tier 3 (The Specialist/Niche)** extension.

If you are aiming for L4/L5 at Google or SDE-2 at Uber, **Tier 2 is mandatory**. You cannot skip it. Tier 3 is your insurance policy.


### 23. Advanced Graphs: Kruskal’s (MST) & Union-Find
**The Signal:** "Connect all points with minimum cost." "Min Cost to Connect Points."
**Concept:** Sort all edges by weight. Add them if they don't form a cycle (using Union-Find).
```python
def min_cost_connect_points(points):
    n = len(points)
    edges = []
    # 1. Build all edges (dist, u, v)
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))
    
    edges.sort() # Key step: Process smallest edges first
    
    uf = UnionFind(n) # Use standard UnionFind class
    cost = 0
    edges_used = 0
    
    for w, u, v in edges:
        if uf.union(u, v):
            cost += w
            edges_used += 1
            if edges_used == n - 1: break
            
    return cost
```
**The Battleground:** 1584, 1135
<img width="1100" height="778" alt="Producer" src="https://github.com/user-attachments/assets/cfb234c4-2b00-4e03-99cd-e871ca8ffc8b" />

<details>
  <summary><h3>↕️ Show/Hide Explanation</h3></summary>

```python
def min_cost_connect_points(points):
    """
    Returns the minimum cost to connect all points using Manhattan distance.
    This is a classic Minimum Spanning Tree (MST) problem solved using Kruskal's algorithm.
    
    Args:
        points: List of [x, y] coordinates (list of lists)
    
    Returns:
        Minimum total cost to connect all points
    """
    n = len(points)
    if n == 1:
        return 0  # Edge case: single point needs no connections
    
    edges = []
    
    # Step 1: Generate all possible edges between points
    # For every pair of points (i, j), compute Manhattan distance and store as (distance, i, j)
    for i in range(n):
        for j in range(i + 1, n):  # Avoid duplicates and self-loops
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))  # Tuple: (weight, vertex1, vertex2)
    
    # Step 2: Sort edges by weight (distance) in ascending order
    # This is crucial for Kruskal's algorithm — we always consider cheapest edges first
    edges.sort()
    
    # Step 3: Initialize Union-Find (Disjoint Set Union) data structure
    # Helps detect cycles efficiently and merge connected components
    uf = UnionFind(n)
    
    cost = 0           # Total cost of the MST
    edges_used = 0     # Number of edges added to the MST
    
    # Step 4: Iterate through sorted edges and add them if they don't form a cycle
    for weight, u, v in edges:
        # Try to union the two points (connect them)
        if uf.union(u, v):  # Returns True only if u and v were NOT already connected
            cost += weight         # Add this edge's cost to total
            edges_used += 1         # One more valid edge in MST
            
            # Early termination: MST for n nodes has exactly n-1 edges
            if edges_used == n - 1:
                break
    
    return cost
```
</details>

**Time:** $O(E \log E)$ = $O(n^2 \log n)$  
**Space:** $O(E)$ = $O(n^2)$

<details>
  <summary><h3>↕️ Show/Hide TC, SC Explanation</h3></summary>

```python
def min_cost_connect_points(points):
    """
    Solves "Min Cost to Connect Points" using Kruskal's algorithm with Manhattan distance.
    
    Time Complexity:  O(n² log n)
    Space Complexity: O(n²)
    """
    n = len(points)
    
    # Edge case: If 0 or 1 point, no connections needed → cost is 0
    # TC: O(1) | SC: O(1)
    if n <= 1:
        return 0
    
    edges = []  # Will store all possible unique edges as (distance, i, j)
    
    # Step 1: Generate all possible UNIQUE edges between pairs of points
    # Since the graph is undirected, we use i < j to avoid duplicates
    # Exact number of edges: n(n-1)/2 → This is quadratic in n
    # In Big-O notation: O(n²) edges generated and stored
    # TC: O(n²) [nested loops + O(1) Manhattan distance calculation per pair]
    # SC: O(n²) [we store all n(n-1)/2 edges in the list]
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))  # (weight, vertex_u, vertex_v)
    
    # Step 2: Sort all edges by distance (weight) in ascending order
    # This is the key greedy step in Kruskal's algorithm
    # Number of edges E = n(n-1)/2 = O(n²)
    # Sorting cost: O(E log E) = O(n² log n) ← Dominates overall time complexity
    # SC: O(1) extra
    edges.sort()
    
    # Step 3: Initialize Union-Find (Disjoint Set Union) for efficient cycle detection
    # SC: O(n) [parent and rank/size arrays of size n]
    uf = UnionFind(n)
    
    cost = 0         # Total minimum cost of the MST
    edges_used = 0   # Number of edges added to the MST
    
    # Step 4: Process edges in order of increasing weight
    # Add an edge only if it connects two different components (no cycle)
    # In worst case we may check all edges → O(n²) iterations
    # Each union/find is amortized nearly O(1) → total Union-Find cost nearly O(n)
    # Overall TC remains O(n² log n) due to sorting
    for weight, u, v in edges:
        if uf.union(u, v):  # Returns True only if u and v were not already connected
            cost += weight
            edges_used += 1
            
            # MST is complete when we have exactly (n-1) edges → early exit
            if edges_used == n - 1:
                break
    
    return cost
```

</details>

---

# TIER 2: THE "HARD" STANDARD
*Used in Google, Uber, and High-Frequency Trading (HFT) interviews. These solve problems where $N$ is huge or constraints are weird.*

### 24. Bitmask Dynamic Programming
**The Signal:** $N$ is extremely small ($N \le 20$). "Assign N workers to N jobs." "Visit all cities (TSP)."
**Concept:** Use an integer (e.g., `10110`) to represent a set `{1, 2, 4}`.
```python
def solve_bitmask(n, costs):
    # dp[mask] = min cost to assign workers represented by mask
    memo = {}
    target = (1 << n) - 1 # All 1s (everyone assigned)

    def dfs(i, mask):
        if i == n: return 0 # All workers assigned
        if mask in memo: return memo[mask]
        
        res = float('inf')
        for job in range(n):
            # Check if 'job' bit is NOT set in mask
            if not (mask & (1 << job)):
                res = min(res, costs[i][job] + dfs(i + 1, mask | (1 << job)))
        
        memo[mask] = res
        return res

    return dfs(0, 0)
```
**The Battleground:** 1879, 698, 473, 847
**Time:** $O(N \cdot 2^N)$. This is why $N$ must be small.

### 25. Trie with XOR Logic
**The Signal:** "Find maximum XOR of two numbers in an array."
**Concept:** To maximize XOR, you want opposite bits ($0 \oplus 1 = 1$). Walk the Trie; if current bit is `1`, try to go to `0` child.
```python
def find_max_xor(nums):
    # Standard Trie Insert omitted for brevity
    # Logic for query:
    max_xor = 0
    for num in nums:
        curr = root
        curr_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Want opposite bit
            if 1 - bit in curr.children:
                curr_xor |= (1 << i)
                curr = curr.children[1 - bit]
            else:
                curr = curr.children[bit]
        max_xor = max(max_xor, curr_xor)
    return max_xor
```
**The Battleground:** 421 (Max XOR of Two Numbers), 1707

---

# TIER 3: THE "NICHE" SPECIALISTS
*Study these only after mastering Tier 2. These appear in specific hard rounds or at Uber/Google when they want to filter candidates. OA rounds rarely in the face to face interviews*

### 26. Segment Tree (Range Queries & Updates)
**The Signal:** "Find sum/max of range `[L, R]`" AND "Update value at index `i`".
**Why Prefix Sum Fails:** Prefix sum is $O(N)$ to update. Segment Tree is $O(\log N)$ for both.
```python
class SegmentTree:
    def __init__(self, data, func=sum):
        self.n = len(data)
        self.func = func # sum, max, min, etc.
        self.tree = [0] * (2 * self.n)
        # Build tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func([self.tree[2 * i], self.tree[2 * i + 1]])

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.func([self.tree[2 * i], self.tree[2 * i + 1]])

    def query(self, l, r): # Range [l, r)
        l += self.n; r += self.n
        res = None
        while l < r:
            if l % 2 == 1:
                res = self.tree[l] if res is None else self.func([res, self.tree[l]])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.tree[r] if res is None else self.func([res, self.tree[r]])
            l //= 2; r //= 2
        return res
```
**The Battleground:** 307 (Range Sum Mutable), 315, 327
**Time:** $O(\log N)$ for query and update.
**Space:** $O(N)$.


### 27. Digit DP
**The Signal:** "Count numbers between range `L` and `R` that satisfy property X." (e.g., no consecutive ones).
**Concept:** Build the number digit by digit.
**State:** `dp(index, tight_constraint, is_leading_zero, state_variable)`
*   `tight`: Are we restricted by the digits of R?
*   `leading_zero`: Can we place a 0 here?
```python
def count_numbers(s): # s is string of R
    @cache
    def dfs(i, tight, leading_zero, prev_digit):
        if i == len(s): return 1
        
        limit = int(s[i]) if tight else 9
        res = 0
        
        for digit in range(limit + 1):
            new_tight = tight and (digit == limit)
            new_leading = leading_zero and (digit == 0)
            
            # Custom Logic (Example: No consecutive ones)
            if not new_leading and prev_digit == 1 and digit == 1:
                continue 
                
            res += dfs(i + 1, new_tight, new_leading, digit)
        return res
    return dfs(0, True, True, -1)
```
**The Battleground:** 233, 902, 600, 1012

### 28. Rolling Hash (Rabin-Karp)
**The Signal:** "Longest Duplicate Substring." Standard KMP is too complex to implement quickly.
**Concept:** Treat a string as a number in base 26 (or 31). Slide the window, update hash in $O(1)$.
```python
def rolling_hash(s, length):
    base = 26
    mod = 2**63 - 1 # Large prime helps avoid collision
    current_hash = 0
    
    # Initial window
    for i in range(length):
        current_hash = (current_hash * base + ord(s[i])) % mod
    
    seen = {current_hash}
    power = pow(base, length, mod) # Precompute removal factor
    
    for i in range(1, len(s) - length + 1):
        # Remove leading char, Shift left, Add new char
        current_hash = (current_hash * base - ord(s[i-1]) * power + ord(s[i+length-1])) % mod
        if current_hash in seen:
            return s[i : i+length]
        seen.add(current_hash)
    return None
```
**The Battleground:** 1044, 187, 718

### 29. Critical Connections (Tarjan’s Bridge Finding)
**The Signal:** "Find edge which, if removed, disconnects the graph." "Critical network connections."
**Concept:** Track `discovery_time` and `low_link` value. If `low[child] > disc[parent]`, the edge `parent-child` is a bridge.
```python
def find_bridges(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v); graph[v].append(u)
        
    disc = [-1] * n; low = [-1] * n
    time = 0
    res = []
    
    def dfs(u, p=-1):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        
        for v in graph[u]:
            if v == p: continue
            if disc[v] != -1:
                low[u] = min(low[u], disc[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    res.append([u, v])
                    
    dfs(0)
    return res
```
**The Battleground:** 1192 (Critical Connections)

### 30. Convex Hull (Monotone Chain)
**The Signal:** "Erect the fence," "Enclose all trees." Geometry problems.
**Concept:** Sort points by X. Build upper hull, build lower hull using "Cross Product" to check turn direction.
```python
def outerTrees(points):
    points.sort()
    
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
        
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)
        
    return list(set(map(tuple, lower + upper)))
```
**The Battleground:** 587 (Erect the Fence)

---

### Final "Cheat Sheet" Summary for FAANG

1.  **If the problem asks for Range Sums:**
    *   Static Array → Prefix Sum.
    *   Mutable Array (Updates) → **Segment Tree (Tier 2)**.
2.  **If N is tiny (< 20):**
    *   **Bitmask DP (Tier 2)**.
3.  **If it's about connecting things cheaply:**
    *   Graph → **Kruskal's / Union Find (Tier 2)**.
4.  **If it's about Numbers/Digits:**
    *   Count in range → **Digit DP (Tier 3)**.
    *   Max XOR → **Trie (Tier 2)**.
5.  **If it's String Matching:**
    *   Simple → Two Pointers.
    *   Longest Duplicate → **Rolling Hash (Tier 3)**.

Memorize Tier 2. Keep Tier 3 codes handy in your brain just in case.

---

# PART 7: POST-GRIND 75 PATTERNS
*The patterns that separate "good enough" from "actually ready." These appear in backend, platform, and data-heavy interviews.*

---

## SECTION A: ADVANCED TREE PATTERNS

### 31. Tree Flattening (Euler Tour)
**The Signal:** "Subtree queries," "Count nodes in subtree with property X," "Subtree sum updates."
**Concept:** Convert a tree to an array using DFS. Each subtree becomes a **contiguous range**.
```python
def euler_tour(root, adj):
    """
    Flatten tree into array where each subtree is a contiguous range.
    tin[node] = entry time (start of subtree range)
    tout[node] = exit time (end of subtree range)
    """
    tin = {}    # Entry time for each node
    tout = {}   # Exit time for each node
    euler = []  # The flattened array
    timer = 0
    
    def dfs(node, parent):
        nonlocal timer
        tin[node] = timer
        euler.append(node)
        timer += 1
        
        for child in adj[node]:
            if child != parent:
                dfs(child, node)
        
        tout[node] = timer - 1  # Last index in subtree
    
    dfs(root, -1)
    return tin, tout, euler

# Usage: Check if 'a' is ancestor of 'b'
def is_ancestor(a, b, tin, tout):
    return tin[a] <= tin[b] <= tout[a]

# Usage: Get subtree range for range queries
def get_subtree_range(node, tin, tout):
    return (tin[node], tout[node])  # Use with prefix sum or segment tree
```
**The Battleground:** 1022, 1026, 508, 1339

**Key Insight:** After flattening:
- Subtree of node `X` = `euler[tin[X] : tout[X] + 1]`
- Ancestor check = O(1)
- Subtree queries become **range queries** on array

**Time:** O(N) to build | O(1) for ancestor check
**Space:** O(N)

---

### 32. Binary Lifting (LCA & Kth Ancestor)
**The Signal:** "Lowest Common Ancestor," "Kth ancestor of node," "Distance between two nodes in tree."
**Concept:** Precompute 2^i-th ancestors for each node. Jump in powers of 2.
```python
import math

class BinaryLifting:
    def __init__(self, n, parent):
        """
        n: number of nodes (0-indexed)
        parent: parent[i] = parent of node i (-1 for root)
        """
        self.n = n
        self.LOG = max(1, int(math.log2(n)) + 1)
        self.depth = [0] * n
        
        # up[i][j] = 2^j-th ancestor of node i
        self.up = [[-1] * self.LOG for _ in range(n)]
        
        # Build sparse table
        for i in range(n):
            self.up[i][0] = parent[i]
        
        for j in range(1, self.LOG):
            for i in range(n):
                if self.up[i][j-1] != -1:
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]
    
    def kth_ancestor(self, node, k):
        """Return k-th ancestor of node, or -1 if doesn't exist."""
        for j in range(self.LOG):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node
    
    def lca(self, a, b):
        """Return Lowest Common Ancestor of nodes a and b."""
        # First, bring both to same depth
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        
        diff = self.depth[a] - self.depth[b]
        a = self.kth_ancestor(a, diff)
        
        if a == b:
            return a
        
        # Binary search for LCA
        for j in range(self.LOG - 1, -1, -1):
            if self.up[a][j] != self.up[b][j]:
                a = self.up[a][j]
                b = self.up[b][j]
        
        return self.up[a][0]
```
**The Battleground:** 1483 (Kth Ancestor), 236 (LCA), 1740, 2846

**Time:** O(N log N) preprocess | O(log N) per query
**Space:** O(N log N)

---

### 33. Tree DP (Subtree DP)
**The Signal:** "Maximum independent set on tree," "Count paths with property," "Best assignment in tree structure."
**Concept:** Process children first, then combine results at parent.
```python
def tree_dp(root, adj):
    """
    Example: Maximum Independent Set
    dp[node][0] = max size NOT including node
    dp[node][1] = max size INCLUDING node
    """
    n = len(adj)
    dp = [[0, 0] for _ in range(n)]
    
    def dfs(node, parent):
        dp[node][1] = 1  # Include this node
        
        for child in adj[node]:
            if child != parent:
                dfs(child, node)
                
                # If we DON'T take node, children can be taken or not
                dp[node][0] += max(dp[child][0], dp[child][1])
                
                # If we TAKE node, children must NOT be taken
                dp[node][1] += dp[child][0]
    
    dfs(root, -1)
    return max(dp[root][0], dp[root][1])
```

**Common Tree DP Patterns:**
```python
# Pattern 1: Path counting
def count_paths(node, parent, adj, target):
    """Count paths that sum to target."""
    count = defaultdict(int)
    count[0] = 1
    result = 0
    
    def dfs(node, parent, curr_sum):
        nonlocal result
        curr_sum += values[node]
        result += count[curr_sum - target]
        count[curr_sum] += 1
        
        for child in adj[node]:
            if child != parent:
                dfs(child, node, curr_sum)
        
        count[curr_sum] -= 1  # Backtrack
    
    dfs(node, parent, 0)
    return result

# Pattern 2: Diameter
def diameter(root, adj):
    ans = 0
    def dfs(node, parent):
        nonlocal ans
        max1 = max2 = 0
        for child in adj[node]:
            if child != parent:
                d = dfs(child, node) + 1
                if d > max1:
                    max1, max2 = d, max1
                elif d > max2:
                    max2 = d
        ans = max(ans, max1 + max2)
        return max1
    dfs(root, -1)
    return ans
```
**The Battleground:** 337 (House Robber III), 543, 124, 1372, 968

**Time:** O(N) 
**Space:** O(N) for DP table + O(H) recursion stack

---

### 34. Re-rooting DP
**The Signal:** "Answer for every node as root," "Sum of distances to all nodes," "Find best root."
**Concept:** Compute answer for one root, then "shift" the root to neighbors in O(1).
```python
def reroot_dp(n, adj):
    """
    Example: Sum of distances from each node to all other nodes (LC 834)
    
    Phase 1: Root at node 0, compute subtree sizes and distance sum
    Phase 2: Shift root to each node using the formula
    """
    # Phase 1: DFS from node 0
    subtree_size = [1] * n
    dist_sum = [0] * n  # dist_sum[0] = sum of distances from 0 to all nodes
    
    def dfs1(node, parent, depth):
        dist_sum[0] += depth
        for child in adj[node]:
            if child != parent:
                dfs1(child, node, depth + 1)
                subtree_size[node] += subtree_size[child]
    
    dfs1(0, -1, 0)
    
    # Phase 2: Re-root
    # When moving root from parent to child:
    # - subtree_size[child] nodes get 1 closer
    # - (n - subtree_size[child]) nodes get 1 farther
    def dfs2(node, parent):
        for child in adj[node]:
            if child != parent:
                dist_sum[child] = dist_sum[node] - subtree_size[child] + (n - subtree_size[child])
                dfs2(child, node)
    
    dfs2(0, -1)
    return dist_sum
```
**The Battleground:** 834 (Sum of Distances), 310, 2581

**Time:** O(N)
**Space:** O(N)

---

## SECTION B: ADVANCED GRAPH PATTERNS

### 35. Multi-Source BFS
**The Signal:** "Nearest distance from any of K sources," "Spreading from multiple starting points," "01 Matrix."
**Concept:** Start BFS from ALL sources simultaneously.
```python
from collections import deque

def multi_source_bfs(grid, sources):
    """
    Find shortest distance from any source to every cell.
    Sources: list of (row, col) starting points
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    q = deque()
    
    # Add ALL sources to queue at once
    for r, c in sources:
        dist[r][c] = 0
        q.append((r, c))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    
    return dist
```
**The Battleground:** 542 (01 Matrix), 994 (Rotting Oranges), 286, 1162

**Time:** O(M × N)
**Space:** O(M × N)

---

### 36. Topological DP
**The Signal:** "Minimum cost to complete all tasks with dependencies," "Longest path in DAG," "Count paths in DAG."
**Concept:** Process nodes in topological order. DP depends only on already-processed nodes.
```python
from collections import deque, defaultdict

def topo_dp(n, edges, values):
    """
    Example: Longest path in DAG with node values
    """
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # dp[i] = longest path ending at node i
    dp = [values[i] for i in range(n)]
    
    q = deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []
    
    while q:
        node = q.popleft()
        topo_order.append(node)
        for nei in graph[node]:
            # Relaxation: update dp before reducing indegree
            dp[nei] = max(dp[nei], dp[node] + values[nei])
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    return max(dp) if len(topo_order) == n else -1  # -1 if cycle
```

**Count Paths Variant:**
```python
def count_paths_dag(n, edges, start, end):
    """Count all paths from start to end in DAG."""
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # paths[i] = number of paths from start to node i
    paths = [0] * n
    paths[start] = 1
    
    q = deque([i for i in range(n) if indegree[i] == 0])
    
    while q:
        node = q.popleft()
        for nei in graph[node]:
            paths[nei] += paths[node]
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    return paths[end]
```
**The Battleground:** 2050 (Parallel Courses III), 1857, 329, 1976

**Time:** O(V + E)
**Space:** O(V + E)

---

## SECTION C: ARRAY & RANGE PATTERNS

### 37. Difference Array
**The Signal:** "Add value to range [L, R] multiple times," "Range increment queries," then "final array state."
**Concept:** Instead of updating each element, mark only boundaries.
```python
def difference_array(n, updates):
    """
    updates: list of (left, right, value) meaning add 'value' to range [left, right]
    Returns final array after all updates.
    """
    diff = [0] * (n + 1)  # Extra space to avoid boundary checks
    
    for left, right, val in updates:
        diff[left] += val       # Start adding here
        diff[right + 1] -= val  # Stop adding after right
    
    # Reconstruct array with prefix sum
    result = []
    curr = 0
    for i in range(n):
        curr += diff[i]
        result.append(curr)
    
    return result

# Example: n=5, updates = [(1,3,2), (2,4,3), (0,2,-1)]
# Initial:  [0, 0, 0, 0, 0]
# Final:    [-1, 1, 4, 5, 3]
```

**2D Difference Array:**
```python
def difference_2d(m, n, updates):
    """
    updates: list of (r1, c1, r2, c2, val)
    Add 'val' to submatrix from (r1,c1) to (r2,c2)
    """
    diff = [[0] * (n + 2) for _ in range(m + 2)]
    
    for r1, c1, r2, c2, val in updates:
        diff[r1][c1] += val
        diff[r1][c2 + 1] -= val
        diff[r2 + 1][c1] -= val
        diff[r2 + 1][c2 + 1] += val
    
    # Reconstruct with 2D prefix sum
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            diff[i][j] += (diff[i-1][j] if i > 0 else 0) + \
                          (diff[i][j-1] if j > 0 else 0) - \
                          (diff[i-1][j-1] if i > 0 and j > 0 else 0)
            result[i][j] = diff[i][j]
    
    return result
```
**The Battleground:** 370 (Range Addition), 1109, 2381, 2536

**Time:** O(K) for K updates + O(N) to reconstruct
**Space:** O(N)

---

### 38. Coordinate Compression
**The Signal:** Values up to 10⁹ but only 10⁵ unique values. "Discretize," "Map to smaller range."
**Concept:** Map large values to consecutive integers 0, 1, 2, ...
```python
def coordinate_compress(arr):
    """
    Compress large values to indices 0, 1, 2, ...
    Returns: compressed array and mapping dictionaries
    """
    # Get sorted unique values
    sorted_unique = sorted(set(arr))
    
    # Create mappings
    val_to_idx = {v: i for i, v in enumerate(sorted_unique)}
    idx_to_val = {i: v for i, v in enumerate(sorted_unique)}
    
    # Compress the array
    compressed = [val_to_idx[x] for x in arr]
    
    return compressed, val_to_idx, idx_to_val

# Example usage: Count inversions with values up to 10^9
def count_smaller_after_self(nums):
    """LC 315: Count of Smaller Numbers After Self"""
    # Compress coordinates
    sorted_unique = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}  # 1-indexed for BIT
    
    # Use BIT/Fenwick tree on compressed values
    n = len(sorted_unique)
    bit = [0] * (n + 1)
    
    def update(i):
        while i <= n:
            bit[i] += 1
            i += i & (-i)
    
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
    
    result = []
    for num in reversed(nums):
        r = rank[num]
        result.append(query(r - 1))  # Count elements smaller than current
        update(r)
    
    return result[::-1]
```
**The Battleground:** 315, 493, 327, 2926

**📝 When to Use:**
- Value range is huge (10⁹) but count is small (10⁵)
- Need to use values as array indices
- Segment tree / BIT with large value range

**Time:** O(N log N) for sorting
**Space:** O(N)

---

### 39. Prefix Frequency Array
**The Signal:** "Count occurrences in substring," "Character frequency in range [L, R]."
**Concept:** For each position, store cumulative frequency of each character.
```python
def prefix_frequency(s):
    """
    Build prefix frequency for string queries.
    prefix[i][c] = count of character c in s[0:i]
    """
    n = len(s)
    # For lowercase letters only
    prefix = [[0] * 26 for _ in range(n + 1)]
    
    for i, char in enumerate(s):
        # Copy previous counts
        for c in range(26):
            prefix[i + 1][c] = prefix[i][c]
        # Increment current char
        prefix[i + 1][ord(char) - ord('a')] += 1
    
    return prefix

def query_frequency(prefix, left, right, char):
    """Count of 'char' in s[left:right+1]"""
    c = ord(char) - ord('a')
    return prefix[right + 1][c] - prefix[left][c]

# Optimized version using dictionary (for sparse alphabets)
def prefix_frequency_sparse(s):
    from collections import defaultdict
    n = len(s)
    # prefix[char] = list of positions where char appears
    positions = defaultdict(list)
    
    for i, char in enumerate(s):
        positions[char].append(i)
    
    return positions

def query_sparse(positions, left, right, char):
    """Count of 'char' in s[left:right+1] using binary search"""
    import bisect
    if char not in positions:
        return 0
    pos_list = positions[char]
    return bisect.bisect_right(pos_list, right) - bisect.bisect_left(pos_list, left)
```
**The Battleground:** 1177, 2559, 1915

**Time:** O(N × A) build, O(1) or O(log N) query (A = alphabet size)
**Space:** O(N × A) or O(N)

---

## SECTION D: ADVANCED DP PATTERNS

### 40. Interval DP
**The Signal:** "Optimal way to merge/split intervals," "Minimum cost to combine," "Burst balloons."
**Concept:** `dp[i][j]` = optimal value for interval `[i, j]`. Try all split points `k`.
```python
def interval_dp(arr):
    """
    Example: Minimum cost to merge stones (simplified)
    dp[i][j] = minimum cost to process interval [i, j]
    """
    n = len(arr)
    # Precompute prefix sums for range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    def range_sum(i, j):
        return prefix[j + 1] - prefix[i]
    
    # dp[i][j] = min cost for interval [i, j]
    dp = [[0] * n for _ in range(n)]
    
    # Iterate by interval length
    for length in range(2, n + 1):  # length of interval
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # Try all split points
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + range_sum(i, j)
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

# Classic: Burst Balloons (LC 312)
def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                # k is the LAST balloon to burst in (left, right)
                coins = nums[left] * nums[k] * nums[right]
                coins += dp[left][k] + dp[k][right]
                dp[left][right] = max(dp[left][right], coins)
    
    return dp[0][n - 1]
```
**The Battleground:** 312 (Burst Balloons), 1039, 1547, 516, 1246

**Time:** O(N³)
**Space:** O(N²)

---

### 41. Monotonic Stack/Queue DP Optimization
**The Signal:** "DP transition depends on max/min in sliding range," "Jump Game variants."
**Concept:** Use monotonic structure to optimize O(N²) DP to O(N).
```python
from collections import deque

def optimized_dp_with_monotonic_queue(nums, k):
    """
    Example: Maximum sum of at most k consecutive elements ending at each position
    dp[i] = max(dp[j] + sum(nums[j+1:i+1])) for j in [i-k, i-1]
    
    Naive: O(N*K)
    Optimized: O(N) using monotonic deque
    """
    n = len(nums)
    
    # prefix sum for range sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    # dp[i] = best answer ending at index i
    dp = [0] * (n + 1)
    
    # Monotonic deque stores indices
    # We want max(dp[j] - prefix[j]) for j in valid range
    q = deque([0])  # Store indices
    
    def value(j):
        return dp[j] - prefix[j]
    
    for i in range(1, n + 1):
        # Remove out-of-window elements
        while q and q[0] < i - k:
            q.popleft()
        
        # Best j is at front of deque
        j = q[0]
        dp[i] = value(j) + prefix[i]
        
        # Maintain monotonic property (decreasing by value)
        while q and value(q[-1]) <= value(i):
            q.pop()
        q.append(i)
    
    return max(dp)
```

**Jump Game VII Pattern:**
```python
def canReach(s, minJump, maxJump):
    """LC 1871: Jump Game VII"""
    n = len(s)
    if s[-1] == '1':
        return False
    
    dp = [False] * n
    dp[0] = True
    
    # Count of True values in sliding window [i-maxJump, i-minJump]
    reachable = 0
    
    for i in range(minJump, n):
        if i - minJump >= 0 and dp[i - minJump]:
            reachable += 1
        if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
            reachable -= 1
        
        if s[i] == '0' and reachable > 0:
            dp[i] = True
    
    return dp[n - 1]
```
**The Battleground:** 1425, 1696, 1871, 2944

**Time:** O(N)
**Space:** O(N)

---

## SECTION E: STRING PATTERNS

### 42. Canonical Form (Normalization)
**The Signal:** "Group equivalent strings," "Check if two structures are the same," "Isomorphic strings."
**Concept:** Convert to a standard form where equivalent items become identical.
```python
def canonical_form_string(s):
    """
    Convert string to canonical form based on first occurrence.
    "egg" -> "abb" (e=a, g=b)
    "add" -> "abb" (a=a, d=b)
    Both are equivalent!
    """
    mapping = {}
    next_char = 0
    result = []
    
    for char in s:
        if char not in mapping:
            mapping[char] = chr(ord('a') + next_char)
            next_char += 1
        result.append(mapping[char])
    
    return ''.join(result)

def group_isomorphic(words):
    """Group words by their canonical form."""
    from collections import defaultdict
    groups = defaultdict(list)
    
    for word in words:
        canonical = canonical_form_string(word)
        groups[canonical].append(word)
    
    return list(groups.values())

# Tree canonical form (for tree isomorphism)
def tree_canonical(node, adj, parent=-1):
    """
    Create canonical string representation of tree rooted at node.
    Two trees are isomorphic iff their canonical forms are equal.
    """
    children_forms = []
    
    for child in adj[node]:
        if child != parent:
            children_forms.append(tree_canonical(child, adj, node))
    
    children_forms.sort()  # Key: sort to make canonical
    return "(" + "".join(children_forms) + ")"
```
**The Battleground:** 205, 290, 1460, 652 (Duplicate Subtrees)

**Time:** O(N) for strings, O(N log N) for trees (due to sorting)
**Space:** O(N)

---

### 43. Z-Algorithm (Linear Pattern Matching)
**The Signal:** "Find all occurrences of pattern in text," "Longest prefix that is also suffix."
**Concept:** z[i] = length of longest substring starting at i that matches prefix of string.
```python
def z_function(s):
    """
    z[i] = length of longest substring starting at position i
           that is also a prefix of s
    
    Example: s = "aabxaab"
    z = [7, 1, 0, 0, 3, 1, 0]
         ^  a matches prefix "a"
               ^  "aab" matches prefix "aab"
    """
    n = len(s)
    z = [0] * n
    z[0] = n  # Convention: z[0] = length of string
    
    l, r = 0, 0  # Current rightmost match window [l, r]
    
    for i in range(1, n):
        if i < r:
            # We're inside a known match window
            z[i] = min(r - i, z[i - l])
        
        # Extend match naively
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        # Update window
        if i + z[i] > r:
            l, r = i, i + z[i]
    
    return z

def find_pattern(text, pattern):
    """Find all occurrences of pattern in text."""
    combined = pattern + "$" + text
    z = z_function(combined)
    
    result = []
    pattern_len = len(pattern)
    
    for i in range(pattern_len + 1, len(combined)):
        if z[i] == pattern_len:
            result.append(i - pattern_len - 1)  # Position in original text
    
    return result
```
**The Battleground:** 28, 214, 1392

**Time:** O(N)
**Space:** O(N)

---

## SECTION F: DATA STRUCTURE COMBINATIONS

### 44. Two-Structure Pairing
**The Signal:** "O(1) for two different operations that seem incompatible," "Min Stack," "Max Queue."
**Concept:** Combine two data structures where each handles one operation efficiently.
```python
# Pattern 1: Stack + Auxiliary Stack (Min Stack)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Parallel stack tracking minimums
    
    def push(self, val):
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def getMin(self):
        return self.min_stack[-1]

# Pattern 2: Queue with Max (using two stacks)
class MaxQueue:
    """
    Queue with O(1) amortized push, pop, and getMax.
    Uses two stacks to implement queue + monotonic tracking.
    """
    def __init__(self):
        self.push_stack = []  # (value, max_so_far in this stack)
        self.pop_stack = []
    
    def push(self, val):
        max_val = max(val, self.push_stack[-1][1] if self.push_stack else val)
        self.push_stack.append((val, max_val))
    
    def pop(self):
        if not self.pop_stack:
            while self.push_stack:
                val, _ = self.push_stack.pop()
                max_val = max(val, self.pop_stack[-1][1] if self.pop_stack else val)
                self.pop_stack.append((val, max_val))
        return self.pop_stack.pop()[0]
    
    def getMax(self):
        max_val = float('-inf')
        if self.push_stack:
            max_val = max(max_val, self.push_stack[-1][1])
        if self.pop_stack:
            max_val = max(max_val, self.pop_stack[-1][1])
        return max_val

# Pattern 3: HashMap + Doubly Linked List (LRU Cache - already covered)

# Pattern 4: HashMap + Heap (for delete from middle)
class HeapWithDelete:
    """Heap that supports lazy deletion."""
    def __init__(self):
        self.heap = []
        self.deleted = {}  # Count of deleted elements
    
    def push(self, val):
        heapq.heappush(self.heap, val)
    
    def delete(self, val):
        self.deleted[val] = self.deleted.get(val, 0) + 1
    
    def top(self):
        self._clean()
        return self.heap[0] if self.heap else None
    
    def pop(self):
        self._clean()
        return heapq.heappop(self.heap) if self.heap else None
    
    def _clean(self):
        while self.heap and self.deleted.get(self.heap[0], 0) > 0:
            self.deleted[self.heap[0]] -= 1
            heapq.heappop(self.heap)
```
**The Battleground:** 155, 716, 895, 432, 480

**Time:** Usually O(1) or O(log N) per operation
**Space:** O(N)

---

### 45. Lazy Propagation (Conceptual)
**The Signal:** "Range updates + range queries," "Too many updates to apply individually."
**Concept:** Delay applying updates until absolutely necessary.
```python
class LazySegmentTree:
    """
    Segment Tree with Lazy Propagation.
    Supports: Range Add, Range Sum Query
    """
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)
    
    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2*node+1, start, mid)
            self._build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def _push_down(self, node, start, end):
        """Push lazy value to children."""
        if self.lazy[node] != 0:
            mid = (start + end) // 2
            # Update children
            self.tree[2*node+1] += self.lazy[node] * (mid - start + 1)
            self.tree[2*node+2] += self.lazy[node] * (end - mid)
            # Pass lazy to children
            self.lazy[2*node+1] += self.lazy[node]
            self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0
    
    def update_range(self, node, start, end, l, r, val):
        """Add val to all elements in range [l, r]."""
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] += val * (end - start + 1)
            self.lazy[node] += val
            return
        
        self._push_down(node, start, end)
        mid = (start + end) // 2
        self.update_range(2*node+1, start, mid, l, r, val)
        self.update_range(2*node+2, mid+1, end, l, r, val)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query_range(self, node, start, end, l, r):
        """Get sum of range [l, r]."""
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        self._push_down(node, start, end)
        mid = (start + end) // 2
        return (self.query_range(2*node+1, start, mid, l, r) +
                self.query_range(2*node+2, mid+1, end, l, r))
```
**The Battleground:** 699, 715, 732

**Time:** O(log N) per operation
**Space:** O(N)

---

## SECTION G: META-PATTERNS (Thinking Habits)

### 46. Preprocessing vs Query Tradeoff
**The Signal:** Many queries on same data structure. "Answer Q queries."
```python
"""
THE DECISION FRAMEWORK:

1. Count queries (Q) vs data size (N)

2. If Q is large relative to N:
   → Heavy preprocess, O(1) query
   
3. If Q is small:
   → Light/no preprocess, O(X) per query

4. Common tradeoffs:
   | Approach          | Preprocess | Query    | When to use           |
   |-------------------|------------|----------|------------------------|
   | No preprocess     | O(1)       | O(N)     | Q << N                |
   | Prefix Sum        | O(N)       | O(1)     | Sum queries           |
   | Sparse Table      | O(N log N) | O(1)     | Static RMQ            |
   | Segment Tree      | O(N)       | O(log N) | Dynamic + queries     |
   | Mo's Algorithm    | O(N√N)     | O(√N)    | Offline range queries |
"""

# Example: Sparse Table for Range Minimum Query (RMQ)
import math

class SparseTable:
    """O(N log N) build, O(1) query for range min/max."""
    def __init__(self, arr):
        n = len(arr)
        self.LOG = int(math.log2(n)) + 1
        # sparse[i][j] = min of range starting at i with length 2^j
        self.sparse = [[0] * self.LOG for _ in range(n)]
        self.log_table = [0] * (n + 1)
        
        # Precompute log values
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
        
        # Initialize
        for i in range(n):
            self.sparse[i][0] = arr[i]
        
        # Build
        for j in range(1, self.LOG):
            for i in range(n - (1 << j) + 1):
                self.sparse[i][j] = min(
                    self.sparse[i][j-1],
                    self.sparse[i + (1 << (j-1))][j-1]
                )
    
    def query(self, l, r):
        """Min in range [l, r]."""
        length = r - l + 1
        k = self.log_table[length]
        return min(self.sparse[l][k], self.sparse[r - (1 << k) + 1][k])
```

---

### 47. Constraint Analysis Thinking
**The Signal:** Before writing code, analyze constraints to determine algorithm.
```python
"""
THE CONSTRAINT CHEAT SHEET:

N ≤ 10        → O(N!) brute force OK         → Try all permutations
N ≤ 20        → O(2^N) bitmask DP OK         → Subset enumeration
N ≤ 500       → O(N³) OK                      → Matrix DP, Floyd-Warshall
N ≤ 5000      → O(N²) OK                      → Nested loops, 2D DP
N ≤ 10^5      → O(N log N) needed            → Sorting, Binary Search, Segment Tree
N ≤ 10^6      → O(N) or O(N log N) needed    → Linear scan, efficient DS
N ≤ 10^8      → O(N) barely OK, O(log N) preferred → Math, binary search
N ≤ 10^12     → O(√N) or O(log N) needed     → Math tricks, binary search

SPACE:
N ≤ 10^6      → O(N) array OK
N ≤ 10^8      → O(N) might TLE or MLE, consider streaming

COMBINATIONS:
- "N ≤ 20 with combinations" → Bitmask DP
- "N ≤ 10^5 with range queries" → Segment Tree or BIT
- "N ≤ 10^5 but values up to 10^9" → Coordinate Compression
- "Tree with N ≤ 10^5" → O(N) or O(N log N) tree algos
- "Graph with N,E ≤ 10^5" → Dijkstra, Union Find OK
"""

def analyze_constraints(n, time_limit=1):
    """
    Helper to estimate maximum complexity allowed.
    Assumes ~10^8 operations per second.
    """
    max_ops = time_limit * 10**8
    
    if n <= 10:
        return "O(N!) OK - brute force all permutations"
    elif n <= 20:
        return "O(2^N) OK - bitmask DP"
    elif n <= 500:
        return "O(N³) OK - cubic algorithms"
    elif n <= 5000:
        return "O(N²) OK - quadratic algorithms"
    elif n <= 10**5:
        return "O(N log N) needed - sorting/binary search"
    elif n <= 10**6:
        return "O(N) or O(N log N) - linear algorithms"
    elif n <= 10**8:
        return "O(N) barely, prefer O(log N) - optimize heavily"
    else:
        return "O(√N) or O(log N) needed - math/binary search"
```

---

### 48. Offline vs Online Query Processing
**The Signal:** "All queries known in advance" = offline. "Queries come one by one" = online.
```python
"""
OFFLINE ADVANTAGES:
1. Sort queries to process efficiently
2. Process in a specific order (e.g., by right endpoint)
3. Mo's algorithm becomes possible
4. Can use simpler data structures

ONLINE REQUIREMENTS:
1. Must answer query before seeing next
2. Need persistent or dynamic data structures
3. Usually more complex
"""

# Example: Offline processing with sorting
def answer_queries_offline(nums, queries):
    """
    queries = [(left, right, query_id), ...]
    Process sorted by right endpoint for efficiency.
    """
    n = len(nums)
    q = len(queries)
    
    # Add original indices to queries
    indexed_queries = [(l, r, i) for i, (l, r) in enumerate(queries)]
    
    # Sort by right endpoint
    indexed_queries.sort(key=lambda x: x[1])
    
    answers = [0] * q
    j = 0  # Pointer in nums
    
    # Some data structure being built incrementally
    data_structure = []
    
    for l, r, idx in indexed_queries:
        # Extend data structure up to r
        while j <= r:
            data_structure.append(nums[j])  # Or update as needed
            j += 1
        
        # Answer query using data structure
        answers[idx] = process_query(data_structure, l, r)
    
    return answers
```

---

## STUDY PRIORITY ORDER

**Phase 1 (Immediately useful):**
1. Tree Flattening (#31)
2. Difference Array (#37)
3. Coordinate Compression (#38)
4. Multi-Source BFS (#35)

**Phase 2 (Common in harder interviews):**
5. Binary Lifting (#32)
6. Tree DP (#33)
7. Topological DP (#36)
8. Prefix Frequency (#39)

**Phase 3 (For senior/staff level):**
9. Re-rooting DP (#34)
10. Interval DP (#40)
11. Monotonic DP Optimization (#41)

**Phase 4 (Specialist/Competitive):**
12. Canonical Form (#42)
13. Z-Algorithm (#43)
14. Two-Structure Patterns (#44)
15. Lazy Propagation (#45)
16. Sparse Table (#46)

---

## QUICK REFERENCE: WHEN TO USE WHAT

| Problem Type | Pattern | Section |
|-------------|---------|---------|
| Subtree queries | Tree Flattening | A |
| Kth ancestor / LCA | Binary Lifting | A |
| Max independent set on tree | Tree DP | A |
| Answer changes with root | Re-rooting | A |
| Distance from multiple sources | Multi-Source BFS | B |
| Longest path in DAG | Topological DP | B |
| Range increment queries | Difference Array | C |
| Values too large for array | Coordinate Compression | C |
| Character count in substring | Prefix Frequency | C |
| Merge/split intervals optimally | Interval DP | D |
| DP with sliding window optimization | Monotonic DP | D |
| Group equivalent structures | Canonical Form | E |
| Fast pattern matching | Z-Algorithm | E |
| O(1) for conflicting operations | Two-Structure | F |
| Range update + range query | Lazy Propagation | F |






















































