# Redis Interview Questions - Merged & Deduplicated

## **REDIS QUESTIONS** (30 Unique Questions)

### **📌 REDIS BASICS & OVERVIEW**

#### **Question 1**
What is Redis?

*   A) A relational database
*   B) An open-source, in-memory data structure store used as database, cache, and message broker
*   C) A file storage system
*   D) A web server

**Answer: B**
> **Explanation:** Redis (Remote Dictionary Server) stores data in memory for extremely fast access. It supports various data structures and use cases including caching, session storage, real-time analytics, and message queuing.

---

#### **Question 2**
What data structures does Redis support?

*   A) Only strings
*   B) Strings, Lists, Sets, Sorted Sets, Hashes, Streams, Bitmaps, HyperLogLogs, Geospatial indexes
*   C) Only key-value pairs
*   D) JSON only

**Answer: B**
> **Explanation:** Redis supports rich data structures beyond simple key-value, enabling efficient solutions for various use cases:
> *   **Strings**: Basic key-value
> *   **Lists**: Ordered collections (queues)
> *   **Sets**: Unique unordered elements
> *   **Sorted Sets**: Unique elements with scores
> *   **Hashes**: Field-value maps (objects)
> *   **Streams**: Append-only logs
> *   **Bitmaps, HyperLogLogs, Geo**: Specialized structures

---

### **📌 STRINGS & BASIC OPERATIONS**

#### **Question 3**
What is the difference between `SET` and `SETNX`?

*   A) They are identical
*   B) `SET` always sets the value; `SETNX` sets only if the key does not exist (Set if Not eXists)
*   C) `SETNX` is deprecated
*   D) `SET` is for numbers only

**Answer: B**
> **Explanation:** `SETNX` is atomic and sets the value only if the key doesn't exist—useful for implementing locks. Now often replaced by `SET key value NX` syntax.

---

#### **Question 4**
What is the difference between `GET` and `MGET`?

*   A) `MGET` is faster for single keys
*   B) `GET` retrieves one key's value; `MGET` retrieves multiple keys' values in a single command reducing round trips
*   C) They are identical
*   D) `MGET` is deprecated

**Answer: B**
> **Explanation:** `MGET` reduces network round trips when fetching multiple keys.
> ```bash
> MGET key1 key2 key3
> ```
> Returns all values in one command, improving performance for bulk reads.

---

#### **Question 5**
What is `INCR` command used for?

*   A) Increasing storage
*   B) Atomically incrementing a string value representing an integer by one
*   C) Creating increments
*   D) Index creation

**Answer: B**
> **Explanation:**
> *   `INCR key` atomically increments by 1
> *   `INCRBY key amount` increments by specified amount
> *   `DECR` and `DECRBY` for decrements
> *   Useful for counters, rate limiting, generating IDs

---

#### **Question 6**
What is the `TTL` command?

*   A) Time to live setting
*   B) Returns the remaining time to live of a key in seconds
*   C) Total time logged
*   D) Table to list

**Answer: B**
> **Explanation:**
> *   `TTL key` returns remaining seconds until expiration
> *   Returns -1 if key exists but has no expiration
> *   Returns -2 if key doesn't exist
> *   `PTTL key` returns remaining time in milliseconds

---

### **📌 KEY EXPIRATION**

#### **Question 7**
What is the purpose of `EXPIRE` command?

*   A) To delete expired data
*   B) To set a timeout on a key after which it will be automatically deleted
*   C) To check expiration
*   D) To extend key lifetime

**Answer: B**
> **Explanation:** `EXPIRE key seconds` sets a TTL (Time To Live). After the timeout, Redis automatically deletes the key. Related commands:
> *   `PERSIST key` removes expiration
> *   `EXPIRETIME key` returns absolute Unix timestamp of expiration

---

#### **Question 8**
What is the difference between `EXPIRE` and `EXPIREAT`?

*   A) They are identical
*   B) `EXPIRE` sets TTL in seconds from now; `EXPIREAT` sets expiration at a specific Unix timestamp
*   C) `EXPIREAT` is deprecated
*   D) `EXPIRE` only works with strings

**Answer: B**
> **Explanation:**
> *   `EXPIRE key 60` expires in 60 seconds from now
> *   `EXPIREAT key 1672531200` expires at that specific Unix timestamp
> *   Also: `PEXPIRE` (milliseconds), `PEXPIREAT` (millisecond timestamp)

---

### **📌 DATA STRUCTURES - HASHES**

#### **Question 9**
What is a Redis Hash?

*   A) A hashing algorithm
*   B) A data type that maps field-value pairs under a single key, like a small object
*   C) A password hash
*   D) A checksum

**Answer: B**
> **Explanation:** Hashes store multiple field-value pairs under one key. Efficient for representing objects.
> ```bash
> HSET user:1 name "John" age 30 email "john@example.com"
> HGET user:1 name  → "John"
> ```

---

#### **Question 10**
What commands are used with Redis Hashes?

*   A) Only GET and SET
*   B) HSET, HGET, HMSET, HMGET, HGETALL, HDEL, HINCRBY, HEXISTS, HKEYS, HVALS, etc.
*   C) Hash commands don't exist
*   D) Only HASH

**Answer: B**
> **Explanation:** Hash commands start with H:

| Command | Description |
| :--- | :--- |
| HSET | Set field(s) |
| HGET | Get one field |
| HMGET | Get multiple fields |
| HGETALL | Get all fields and values |
| HDEL | Delete field(s) |
| HINCRBY | Increment numeric field |
| HEXISTS | Check if field exists |

---

### **📌 DATA STRUCTURES - LISTS**

#### **Question 11**
What is a Redis List?

*   A) A shopping list feature
*   B) A linked list data type supporting push/pop operations from both ends
*   C) A sorted collection
*   D) A unique collection

**Answer: B**
> **Explanation:** Lists are linked lists of strings—excellent for queues and stacks.

| Command | Description |
| :--- | :--- |
| LPUSH/RPUSH | Add to left/right |
| LPOP/RPOP | Remove from left/right |
| LRANGE | Get range of elements |
| LLEN | Get length |
| BLPOP/BRPOP | Blocking pop |

---

### **📌 DATA STRUCTURES - SETS & SORTED SETS**

#### **Question 12**
What is the difference between Redis Set and Sorted Set?

*   A) They are identical
*   B) Set stores unique unordered elements; Sorted Set stores unique elements with scores for ordering
*   C) Set is deprecated
*   D) Sorted Set doesn't allow duplicates

**Answer: B**
> **Explanation:**
> *   **Sets**: Unordered unique collections (SADD, SMEMBERS, SINTER, SUNION)
> *   **Sorted Sets (ZSETs)**: Add a score to each element for ordering, enabling range queries and rankings (ZADD, ZRANGE, ZRANK)

---

#### **Question 13**
What is the use case for Sorted Sets?

*   A) Storing passwords
*   B) Leaderboards, priority queues, time-series data, rate limiting with sliding windows
*   C) File storage
*   D) Authentication only

**Answer: B**
> **Explanation:** Sorted Sets excel at:
> *   **Leaderboards**: Player scores, rankings
> *   **Priority queues**: Tasks with priorities
> *   **Time-series**: Timestamps as scores
> *   **Rate limiting**: Sliding window algorithms
> *   **Range queries**: Get items within score range

---

#### **Question 14**
What is `ZADD` command?

*   A) Adding numbers
*   B) Adds members with scores to a sorted set
*   C) Zone addition
*   D) Zip and add

**Answer: B**
> **Explanation:**
> ```bash
> ZADD leaderboard 100 "player1" 85 "player2" 92 "player3"
> ```
> Options: NX (only add new), XX (only update), GT/LT (update if greater/less than current)

---

### **📌 DATA STRUCTURES - STREAMS**

#### **Question 15**
What is Redis Stream?

*   A) A water feature
*   B) A log data structure for building message brokers, event sourcing, and real-time data pipelines
*   C) A deprecated feature
*   D) A video streaming service

**Answer: B**
> **Explanation:** Streams (Redis 5.0+) are append-only log structures featuring:
> *   Consumer groups
> *   Message acknowledgment
> *   Persistent messaging
> *   Similar to Apache Kafka
> *   Commands: XADD, XREAD, XRANGE, XGROUP

---

### **📌 PERSISTENCE**

#### **Question 16**
What is Redis persistence and what options are available?

*   A) Redis doesn't persist data
*   B) RDB (point-in-time snapshots) and AOF (append-only file logging every write operation)
*   C) Only disk storage
*   D) Only memory storage

**Answer: B**
> **Explanation:** Redis offers two persistence mechanisms:
> *   **RDB**: Periodic snapshots of dataset
> *   **AOF**: Log of every write operation
> *   Can use both together for durability with good performance

---

#### **Question 17**
What is the difference between RDB and AOF persistence?

*   A) They are identical
*   B) RDB creates snapshots at intervals (faster recovery, possible data loss); AOF logs every operation (more durable, larger files)
*   C) AOF is deprecated
*   D) RDB is more durable

**Answer: B**
> **Explanation:**

| Feature | RDB | AOF |
| :--- | :--- | :--- |
| **Method** | Point-in-time snapshots | Log every write |
| **File size** | Compact | Larger |
| **Recovery speed** | Faster | Slower |
| **Data loss risk** | Up to last snapshot | Minimal (configurable) |
| **Performance impact** | Periodic (fork) | Continuous |

> Many production setups use both together.

---

### **📌 TRANSACTIONS & ATOMICITY**

#### **Question 18**
What is Redis `MULTI/EXEC`?

*   A) Multi-user mode
*   B) Commands to start and execute a transaction where all queued commands run atomically
*   C) Multi-threading
*   D) Deprecated commands

**Answer: B**
> **Explanation:**
> ```bash
> MULTI           # Start transaction
> SET key1 "a"    # Queued
> SET key2 "b"    # Queued
> INCR counter    # Queued
> EXEC            # Execute all atomically
> ```
> Use `DISCARD` to cancel. Commands are queued, not executed until EXEC.

---

#### **Question 19**
What is `WATCH` command in Redis?

*   A) Monitoring tool
*   B) Provides optimistic locking by watching keys and aborting transaction if they change
*   C) Time tracking
*   D) Log watching

**Answer: B**
> **Explanation:**
> ```bash
> WATCH mykey           # Start watching
> val = GET mykey
> MULTI
> SET mykey newval
> EXEC                  # Aborts if mykey changed since WATCH
> ```
> Enables check-and-set (CAS) operations for optimistic locking.

---

#### **Question 20**
What is Redis pipelining?

*   A) A logging feature
*   B) Sending multiple commands to the server without waiting for replies, then reading all replies together
*   C) A data structure
*   D) A backup feature

**Answer: B**
> **Explanation:** Pipelining reduces network round trips by batching commands:
> *   Send N commands without waiting for responses
> *   Read all N replies together
> *   Significantly improves throughput (10x or more)
> *   No atomicity guarantee (unlike transactions)

---

#### **Question 21**
What is the difference between pipelining and transactions?

*   A) They are identical
*   B) Pipelining batches commands for network efficiency; transactions (MULTI/EXEC) ensure atomic execution
*   C) Transactions are faster
*   D) Pipelining is deprecated

**Answer: B**
> **Explanation:**

| Feature | Pipelining | Transactions |
| :--- | :--- | :--- |
| **Purpose** | Network optimization | Atomicity |
| **Execution** | Commands may interleave | All-or-nothing |
| **Performance** | Faster | Slight overhead |
| **Isolation** | No | Yes |

> Can combine both: pipeline multiple transactions.

---

#### **Question 22**
What is a Redis Lua script?

*   A) A programming language
*   B) A script executed atomically on the Redis server, enabling complex operations without round trips
*   C) A backup script
*   D) A deprecated feature

**Answer: B**
> **Explanation:** Lua scripts run atomically on Redis server:
> *   `EVAL script numkeys keys args` - execute script
> *   `EVALSHA sha1 numkeys keys args` - execute cached script
> *   Reduces latency (no round trips)
> *   Enables complex atomic operations
> *   Scripts block other commands while running

---

### **📌 PERFORMANCE & PATTERNS**

#### **Question 23**
What is Redis `SCAN` command and why use it over `KEYS`?

*   A) They are identical
*   B) `SCAN` iterates keys incrementally without blocking; `KEYS` blocks the server while matching all keys
*   C) `SCAN` is deprecated
*   D) `KEYS` is faster

**Answer: B**
> **Explanation:**
> *   `KEYS *` blocks Redis while scanning ALL keys—dangerous in production
> *   `SCAN cursor [MATCH pattern] [COUNT count]` iterates incrementally:
>     *   Uses cursor-based iteration
>     *   Non-blocking
>     *   May return duplicates (handle in client)
> *   Related: `SSCAN`, `HSCAN`, `ZSCAN` for sets, hashes, sorted sets

---

#### **Question 24**
What is cache-aside pattern with Redis?

*   A) Caching to the side
*   B) Application checks cache first, loads from DB on miss, and populates cache before returning data
*   C) Deprecated pattern
*   D) A Redis command

**Answer: B**
> **Explanation:** Cache-aside (lazy loading):
> 1. Check cache for data
> 2. If HIT → return cached data
> 3. If MISS → query database
> 4. Store result in cache
> 5. Return data
>
> Application controls caching logic. Most common pattern.

---

#### **Question 25**
What is write-through caching?

*   A) Writing through walls
*   B) Writing data to cache and database simultaneously/synchronously
*   C) A deprecated pattern
*   D) A Redis command

**Answer: B**
> **Explanation:** Write-through:
> 1. Write to cache
> 2. Write to database (synchronously)
> 3. Return success
>
> *   Ensures consistency (no stale data)
> *   Adds latency to writes
> *   Cache always has latest data

---

#### **Question 26**
What is cache stampede and how do you prevent it?

*   A) Animals running
*   B) Multiple requests regenerating an expired cache simultaneously; prevent with locks, early refresh, or probabilistic expiration
*   C) A Redis error
*   D) A backup issue

**Answer: B**
> **Explanation:** When a popular key expires, many requests may hit the database simultaneously. Solutions:
> *   **Mutex/Lock**: Only one request regenerates cache
> *   **Early refresh**: Refresh before expiration
> *   **Probabilistic expiration**: Stagger expiration times
> *   **Background refresh**: Async cache warming

---

### **📌 HIGH AVAILABILITY & SCALING**

#### **Question 27**
What is Redis Cluster?

*   A) A single server
*   B) A distributed implementation that automatically partitions data across multiple nodes with high availability
*   C) A backup system
*   D) A monitoring tool

**Answer: B**
> **Explanation:** Redis Cluster:
> *   Automatically shards data using 16384 hash slots
> *   Multiple master nodes, each with replicas
> *   Automatic failover when master fails
> *   Horizontal scaling
> *   Some command limitations (keys must be in same slot for multi-key ops)

---

#### **Question 28**
What is Redis Sentinel?

*   A) A security guard
*   B) A system for high availability providing monitoring, notifications, and automatic failover for Redis
*   C) A data type
*   D) A deprecated feature

**Answer: B**
> **Explanation:** Sentinel provides:
> *   **Monitoring**: Checks if masters and replicas are working
> *   **Notification**: Alerts when something goes wrong
> *   **Automatic failover**: Promotes replica to master if master fails
> *   **Service discovery**: Clients query Sentinel for current master address

---

#### **Question 29**
What is the difference between Redis Cluster and Sentinel?

*   A) They are identical
*   B) Sentinel provides HA for single master setup; Cluster provides HA and sharding across multiple masters
*   C) Cluster is deprecated
*   D) Sentinel is for clustering

**Answer: B**
> **Explanation:**

| Feature | Sentinel | Cluster |
| :--- | :--- | :--- |
| **Purpose** | High Availability | HA + Sharding |
| **Data distribution** | Single master (full dataset) | Partitioned across masters |
| **Scaling** | Vertical only | Horizontal |
| **Complexity** | Simpler | More complex |
| **Multi-key ops** | All supported | Limited to same slot |

---

### **📌 MESSAGING**

#### **Question 30**
What is Redis pub/sub and when would you use it?

*   A) A way to publish static files
*   B) A messaging paradigm where publishers send messages to channels and subscribers receive them in real-time
*   C) A database backup mechanism
*   D) A way to sort data

**Answer: B**
> **Explanation:** Redis Pub/Sub:
> *   Publishers send to channels: `PUBLISH channel message`
> *   Subscribers listen: `SUBSCRIBE channel`
> *   **Fire-and-forget**: Messages not persisted
> *   **Use cases**: Real-time notifications, chat, live updates, event broadcasting
> *   **Note**: For durable messaging, use Redis Streams instead

---

## **📊 FINAL SUMMARY**

| Category | Question Count |
| :--- | :--- |
| Redis Basics & Overview | 2 |
| Strings & Basic Operations | 4 |
| Key Expiration | 2 |
| Data Structures - Hashes | 2 |
| Data Structures - Lists | 1 |
| Data Structures - Sets & Sorted Sets | 3 |
| Data Structures - Streams | 1 |
| Persistence | 2 |
| Transactions & Atomicity | 5 |
| Performance & Patterns | 4 |
| High Availability & Scaling | 3 |
| Messaging | 1 |
| **TOTAL UNIQUE** | **30 Questions** |

---
