# PostgreSQL & SQL Interview Questions

## **POSTGRESQL & SQL QUESTIONS** (29 Unique Questions)

### **📌 JOINS & RELATIONSHIPS**

#### **Question 1**
What is the difference between `INNER JOIN` and `LEFT JOIN`?

*   A) INNER JOIN returns all rows, LEFT JOIN returns matched rows only
*   B) INNER JOIN returns only matching rows; LEFT JOIN returns all left table rows plus matching right table rows (NULL for non-matches)
*   C) They are identical
*   D) LEFT JOIN is faster

**Answer: B**
> **Explanation:**
> *   **INNER JOIN**: Returns only rows where both tables have matching values
> *   **LEFT JOIN**: Returns all rows from the left table with matched rows from right table (NULL for non-matching right table columns)

---

#### **Question 2**
What is a foreign key constraint?

*   A) A key from another database
*   B) A constraint that ensures referential integrity by requiring values to exist in a referenced table
*   C) A deprecated feature
*   D) A key for external access

**Answer: B**
> **Explanation:** Foreign keys enforce referential integrity—values in the FK column must exist in the referenced table's primary/unique key column.

---

### **📌 INDEXES**

#### **Question 3**
What is a database index and when should you create one?

*   A) An index is a backup of the table; create on all columns
*   B) A data structure that improves query speed on indexed columns at the cost of write performance and storage; create on columns frequently used in WHERE, JOIN, ORDER BY with high selectivity
*   C) An index is required for all columns
*   D) An index only works with primary keys

**Answer: B**
> **Explanation:**
> *   **What**: Indexes create efficient lookup structures (usually B-trees) that speed up data retrieval
> *   **Trade-offs**: Increase storage and slow down writes (INSERT, UPDATE, DELETE)
> *   **When to create**: On columns frequently used in WHERE, JOIN, ORDER BY clauses with good selectivity
> *   **Avoid**: Over-indexing as it hurts write performance

---

#### **Question 4**
What is a composite index and when is it useful?

*   A) An index on multiple tables
*   B) An index on multiple columns, useful when queries filter on those columns together in the same order
*   C) An index that combines B-tree and hash
*   D) An automatic index created by PostgreSQL

**Answer: B**
> **Explanation:** Composite (multi-column) indexes cover multiple columns. Column order matters—the index is most effective when queries filter by leftmost columns first. Useful when queries frequently filter or sort by those columns together.

---

#### **Question 5**
What is a partial index in PostgreSQL?

*   A) An incomplete index
*   B) An index built on a subset of table rows defined by a WHERE condition
*   C) A deprecated feature
*   D) An index on partial columns

**Answer: B**
> **Explanation:** Partial indexes index only rows matching a condition, reducing size and improving performance for queries matching that condition. Example: `CREATE INDEX idx ON orders (created_at) WHERE status = 'active';`

---

### **📌 CONSTRAINTS & KEYS**

#### **Question 6**
What is the difference between `UNIQUE` constraint and `PRIMARY KEY`?

*   A) They are identical
*   B) PRIMARY KEY is UNIQUE + NOT NULL with only one per table and creates an index; UNIQUE allows NULLs and multiple per table
*   C) UNIQUE is deprecated
*   D) PRIMARY KEY doesn't create an index

**Answer: B**
> **Explanation:**
> *   **PRIMARY KEY**: Combines UNIQUE and NOT NULL, creates a clustered index, only one per table
> *   **UNIQUE**: Allows NULL values (typically one), can have multiple per table

---

#### **Question 7**
What is the difference between `SERIAL` and `IDENTITY` columns?

*   A) They are identical
*   B) IDENTITY is SQL-standard and more flexible; SERIAL is PostgreSQL-specific and older
*   C) SERIAL is recommended
*   D) IDENTITY is deprecated

**Answer: B**
> **Explanation:**
> *   **IDENTITY** (PostgreSQL 10+): SQL-standard with options like `GENERATED ALWAYS/BY DEFAULT`
> *   **SERIAL**: Legacy PostgreSQL-specific shorthand that creates a sequence

---

### **📌 DATA MODIFICATION**

#### **Question 8**
What is the difference between `DELETE` and `TRUNCATE`?

*   A) They are identical
*   B) DELETE removes rows individually with logging and triggers; TRUNCATE removes all rows quickly without row-level logging
*   C) TRUNCATE can use WHERE clause
*   D) DELETE is faster

**Answer: B**
> **Explanation:**

| Feature | DELETE | TRUNCATE |
| :--- | :--- | :--- |
| **Speed** | Slower | Faster |
| **WHERE clause** | Yes | No |
| **Logging** | Row-level | Page deallocation |
| **Triggers** | Fires ON DELETE | No row triggers |
| **Identity/Sequence** | Unchanged | Resets |
| **Rollback** | Yes | Yes (in PostgreSQL) |

---

### **📌 DATABASE DESIGN**

#### **Question 9**
What is database normalization and what problem does it solve?

*   A) It's a way to speed up queries
*   B) Organizing data to reduce redundancy and improve data integrity through defined normal forms
*   C) It's a backup procedure
*   D) It's a way to encrypt data

**Answer: B**
> **Explanation:** Normalization organizes database structure to:
> *   Minimize redundancy
> *   Prevent update anomalies
> *   Ensure data integrity
> *   Through normal forms: 1NF, 2NF, 3NF, BCNF, etc.

---

### **📌 TRANSACTIONS & ACID**

#### **Question 10**
What is a transaction in PostgreSQL?

*   A) A payment record
*   B) A sequence of operations performed as a single logical unit that follows ACID properties
*   C) A log entry
*   D) A user session

**Answer: B**
> **Explanation:** Transactions group operations atomically—all succeed or all fail. They ensure ACID properties for reliable database operations.

---

#### **Question 11**
What are the ACID properties?

*   A) Database chemicals
*   B) Atomicity, Consistency, Isolation, Durability—guarantees for reliable transaction processing
*   C) Access Control and Identity Distribution
*   D) Deprecated properties

**Answer: B**
> **Explanation:**
> *   **Atomicity**: All or nothing—transaction fully completes or fully rolls back
> *   **Consistency**: Database moves from one valid state to another
> *   **Isolation**: Concurrent transactions don't interfere with each other
> *   **Durability**: Committed data persists even after system failure

---

### **📌 LOCKING**

#### **Question 12**
What is `FOR UPDATE` clause used for?

*   A) Preparing updates
*   B) Locking selected rows until the transaction ends, preventing concurrent modifications
*   C) Updating all rows
*   D) Deprecated feature

**Answer: B**
> **Explanation:** `SELECT ... FOR UPDATE` locks selected rows, preventing other transactions from modifying them until your transaction commits or rolls back.

---

#### **Question 13**
What is the difference between optimistic and pessimistic locking?

*   A) They are identical
*   B) Optimistic assumes conflicts are rare and checks at commit; pessimistic locks data immediately
*   C) Pessimistic is deprecated
*   D) Optimistic is always better

**Answer: B**
> **Explanation:**
> *   **Pessimistic locking** (FOR UPDATE): Locks data preventively when reading
> *   **Optimistic locking**: Uses version columns/timestamps to detect conflicts at update time, assumes conflicts are rare

---

### **📌 MAINTENANCE & PERFORMANCE**

#### **Question 14**
What is `VACUUM` in PostgreSQL?

*   A) To delete all data from tables
*   B) Reclaiming storage from dead tuples and updating statistics for the query planner
*   C) Creating backups
*   D) Encrypting data

**Answer: B**
> **Explanation:** PostgreSQL uses MVCC, leaving dead tuples after updates/deletes. VACUUM:
> *   Reclaims storage from dead tuples
> *   Updates visibility map
> *   `VACUUM ANALYZE` also updates planner statistics

---

#### **Question 15**
What does `EXPLAIN ANALYZE` do in PostgreSQL?

*   A) Deletes analyzed data
*   B) Executes the query and shows both planned and actual execution statistics
*   C) Creates an analysis table
*   D) Optimizes the query automatically

**Answer: B**
> **Explanation:** `EXPLAIN ANALYZE`:
> *   Actually executes the query
> *   Shows execution plan with planned costs
> *   Displays actual timings, row counts
> *   Essential for identifying performance bottlenecks

---

#### **Question 16**
What is an execution plan in PostgreSQL?

*   A) A project plan
*   B) The strategy PostgreSQL uses to execute a query, showing operations, costs, and data flow
*   C) A backup plan
*   D) A migration plan

**Answer: B**
> **Explanation:** Execution plans show how PostgreSQL executes queries—scans, joins, sorts, costs. Use `EXPLAIN` to view plans and `EXPLAIN ANALYZE` for actual statistics.

---

#### **Question 17**
What is the difference between Seq Scan and Index Scan?

*   A) They are identical
*   B) Seq Scan reads entire table sequentially; Index Scan uses an index to find specific rows
*   C) Seq Scan is always better
*   D) Index Scan is deprecated

**Answer: B**
> **Explanation:**
> *   **Sequential Scan**: Reads all table pages—better for large result sets
> *   **Index Scan**: Uses index to locate specific rows—better for small, selective queries

---

#### **Question 18**
What is connection pooling?

*   A) Swimming pool connections
*   B) Maintaining a cache of database connections to be reused, reducing connection overhead
*   C) A deprecated feature
*   D) Pooling network cables

**Answer: B**
> **Explanation:** Connection pooling (via PgBouncer, pgpool, etc.) maintains reusable connections, avoiding the overhead of establishing new connections for each request. Essential for high-traffic applications.

---

### **📌 QUERY CLAUSES & SUBQUERIES**

#### **Question 19**
What is the difference between `WHERE` and `HAVING` clauses?

*   A) They are identical
*   B) WHERE filters rows before grouping; HAVING filters groups after aggregation
*   C) HAVING is deprecated
*   D) WHERE works with aggregates

**Answer: B**
> **Explanation:**
> *   **WHERE**: Filters individual rows before GROUP BY
> *   **HAVING**: Filters grouped results after aggregation, allows conditions on aggregate functions

---

#### **Question 20**
What is a subquery?

*   A) A partial query
*   B) A query nested inside another query, which can return scalar values, rows, or tables
*   C) A backup query
*   D) A deprecated feature

**Answer: B**
> **Explanation:** Subqueries are nested SELECT statements used in WHERE, FROM, or SELECT clauses. Types:
> *   **Scalar**: Returns single value
> *   **Row**: Returns single row
> *   **Table**: Returns multiple rows/columns

---

#### **Question 21**
What is a Common Table Expression (CTE)?

*   A) A common error
*   B) A named temporary result set defined with WITH clause that can be referenced within the main query
*   C) A table type
*   D) A deprecated feature

**Answer: B**
> **Explanation:** CTEs improve readability by naming subqueries. Defined with WITH clause and can be referenced multiple times. Recursive CTEs enable hierarchical queries.

```sql
WITH active_users AS (
    SELECT * FROM users WHERE status = 'active'
)
SELECT * FROM active_users WHERE created_at > '2024-01-01';
```

---

#### **Question 22**
What is the difference between `UNION` and `UNION ALL`?

*   A) They are identical
*   B) UNION removes duplicates; UNION ALL keeps all rows including duplicates (and is faster)
*   C) UNION ALL is deprecated
*   D) UNION is faster

**Answer: B**
> **Explanation:**
> *   **UNION**: Combines results and removes duplicates (requires sorting—slower)
> *   **UNION ALL**: Combines all rows without duplicate elimination (faster)

---

### **📌 WINDOW FUNCTIONS**

#### **Question 23**
What is a window function in PostgreSQL?

*   A) A graphical function
*   B) A function that performs calculations across a set of rows related to the current row without collapsing them
*   C) A deprecated function
*   D) A display function

**Answer: B**
> **Explanation:** Window functions like `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()` calculate values across row sets while preserving individual rows—unlike GROUP BY which collapses rows.

---

#### **Question 24**
What is the purpose of `ROW_NUMBER()` window function?

*   A) Counts total rows
*   B) Assigns a unique sequential integer to each row within a partition
*   C) Returns row data
*   D) Creates row IDs

**Answer: B**
> **Explanation:** `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` assigns sequential numbers to rows within each partition based on specified ordering.

---

#### **Question 25**
What is the difference between `RANK()` and `DENSE_RANK()`?

*   A) They are identical
*   B) RANK() leaves gaps after ties; DENSE_RANK() assigns consecutive ranks without gaps
*   C) DENSE_RANK() is deprecated
*   D) RANK() is faster

**Answer: B**
> **Explanation:** With values (100, 100, 90):
> *   **RANK()**: (1, 1, 3) — gap after tie
> *   **DENSE_RANK()**: (1, 1, 2) — no gap after tie

---

### **📌 FUNCTIONS**

#### **Question 26**
What is the `COALESCE` function?

*   A) Combines tables
*   B) Returns the first non-NULL value from its arguments
*   C) Merges rows
*   D) Creates coalitions

**Answer: B**
> **Explanation:** `COALESCE(a, b, c)` returns the first non-NULL value. Useful for providing default values.

```sql
SELECT COALESCE(nullable_column, 'default') FROM table;
```

---

#### **Question 27**
What is the `NULLIF` function?

*   A) Makes values NULL
*   B) Returns NULL if two arguments are equal; otherwise returns the first argument
*   C) Checks for NULL
*   D) Removes NULLs

**Answer: B**
> **Explanation:** `NULLIF(a, b)` returns NULL if a = b, otherwise returns a. Useful for avoiding division by zero.

```sql
SELECT x / NULLIF(y, 0) FROM table;  -- Returns NULL instead of error when y=0
```

---

### **📌 DATABASE OBJECTS**

#### **Question 28**
What is a materialized view?

*   A) A view with materials
*   B) A database object that stores the result of a query physically, requiring refresh to update
*   C) A deprecated feature
*   D) A virtual view

**Answer: B**
> **Explanation:** Materialized views:
> *   Store query results physically (unlike regular views)
> *   Improve read performance for complex queries
> *   Must be refreshed to reflect base table changes
> *   Command: `REFRESH MATERIALIZED VIEW view_name;`

---

#### **Question 29**
What is a trigger in PostgreSQL?

*   A) A hardware component
*   B) A function automatically executed in response to certain events on a table (INSERT, UPDATE, DELETE)
*   C) A deprecated feature
*   D) A startup script

**Answer: B**
> **Explanation:** Triggers execute trigger functions automatically on specified events:
> *   **Timing**: BEFORE / AFTER
> *   **Events**: INSERT / UPDATE / DELETE
> *   **Level**: FOR EACH ROW / FOR EACH STATEMENT
> *   **Use cases**: Auditing, validation, maintaining derived data

---

## **📊 FINAL SUMMARY**

| Category | Question Count |
| :--- | :--- |
| Joins & Relationships | 2 |
| Indexes | 3 |
| Constraints & Keys | 2 |
| Data Modification | 1 |
| Database Design | 1 |
| Transactions & ACID | 2 |
| Locking | 2 |
| Maintenance & Performance | 5 |
| Query Clauses & Subqueries | 4 |
| Window Functions | 3 |
| Functions | 2 |
| Database Objects | 2 |
| **TOTAL UNIQUE** | **29 Questions** |

---