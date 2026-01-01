# Django Interview Questions:
## Below questions + Interview Bit questions (https://www.interviewbit.com/django-interview-questions/)

### **1. The Advanced Internals: ORM & Database Tuning**

**Q: Explain the "N+1 Problem" in the Django ORM and the exact technical difference between `select_related` and `prefetch_related`.**

* **A:** The N+1 problem occurs when you fetch a list of objects and then perform an additional database query for each object to get related data (e.g., getting the author for 50 different blog posts).

* **`select_related`:** Uses a **SQL JOIN** to fetch the related data in a single query. It is best for "one-to-one" or "many-to-one" (foreign key) relationships.

* **`prefetch_related`:** Performs a separate query for each table and then **joins the results in Python memory**. It is the only way to optimize "many-to-many" or "many-to-one" (reverse foreign key) relationships where a single SQL JOIN would result in a massive, redundant result set.

**Q: How does Django's QuerySet evaluation work? When is it actually "hit"?**

* **A:** Django QuerySets are **lazy**. They don't touch the database until you iterate over them, slice them (without a step), or call functions like `len()`, `list()`, or `bool()`.
* **Optimization Tip:** Use `.exists()` instead of `if queryset:` if you only need to check for presence, as `.exists()` executes a much faster `SELECT (1) AS "a" ... LIMIT 1` query.

---

### **2. Architecture & Concurrency**

**Q: When should you use `Celery` vs. `Django Channels` for background or real-time tasks?**

* **A:** 
  * **Celery:** Used for **long-running background tasks** (e.g., generating 1,000 invoices or processing 1000x faster OCR logic). It uses a message broker like Redis to handle tasks asynchronously outside the request-response cycle.
  * **Django Channels:** Extends Django to handle **WebSockets and long-lived connections**. Use this for real-time features like chat apps, live notifications, or a real-time trading order book.

**Q: How do you handle "Race Conditions" in Django?**

* **A:** Use **`select_for_update()`**. When you retrieve an object using this method, Django locks the row in the database until the end of the transaction. This prevents other processes from modifying that specific record simultaneously (e.g., preventing two users from spending the same wallet balance at once).

---

### **3. Senior Performance Optimization**

**Q: How do you debug and optimize a slow Django view?**

* **A:**
  1. **Profiling:** Use `django-debug-toolbar` to see exactly which SQL queries are slow or duplicated.
  2. **Indexing:** Ensure columns used in `filter()`, `exclude()`, and `order_by()` are indexed in the database.
  3. **Database Level:** Use `.values()` or `.only()` to fetch only the specific columns you need, reducing memory and bandwidth.
  4. **Caching:** Implement **Redis** for expensive data that doesn't change often. Use the cache framework at the site, view, or template fragment level.

**Q: What is the difference between `F()` expressions and `Func()` expressions?**

* **A:** 
  * **`F()` expressions:** Allow you to perform database operations (like incrementing a counter) **on the database server** without loading the object into Python memory. This avoids race conditions and is faster.
  * **`Func()` expressions:** Allow you to call **database-native functions** (like `COALESCE`, `LOWER`, or custom SQL functions) directly within your ORM queries.

---

### **4. Security & Deployment (Architect Level)**

**Q: How do you protect a Django app against SQL Injection if you *must* use raw SQL?**

* **A:** Never use string formatting (f-strings) to build queries. Always use **parameterized queries** where the database driver handles the escaping:
  ```python
  # WRONG
  Manager.objects.raw(f"SELECT * FROM table WHERE id = {user_id}") 
  # RIGHT
  Manager.objects.raw("SELECT * FROM table WHERE id = %s", [user_id])
  ```

**Q: Describe a "Zero-Downtime" deployment strategy for a Django app with database migrations.**

* **A:** 
  1. **Deploy code that is compatible with BOTH old and new schemas.**
  2. **Apply migrations** (ensuring they are non-breaking, like adding a nullable column).
  3. **Rolling restart** of your application servers (e.g., Gunicorn/Nginx).
  4. **Clean up** old code/columns once the transition is complete.

---

### **Summary of Key Professional Experience (The "Pro" edge)**

If asked about your specific high-level contributions, you can reference your work:

* **Infrastructure:** Enhanced systems using **Docker** and **AWS SDK** for cloud scaling.
* **Optimization:** Achieved **1000x faster OCR processing** by implementing targeted conditional logic rather than relying on standard library defaults.
* **Real-time:** Built event-driven systems handling **high-throughput requests** using Node.js and Django microservices.

---

▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄

---

### **1. The Execution Layer: WSGI vs. ASGI**

**Q: Explain the evolution from WSGI to ASGI. Why does it matter for modern Django?**

* **WSGI (Web Server Gateway Interface):** The traditional standard. It is **synchronous** and follows a "request-in, response-out" pattern. One thread handles one request. If that request waits for an external API, the thread is blocked.
* **ASGI (Asynchronous Server Gateway Interface):** The successor to WSGI. It allows Django to handle **asynchronous** protocols (WebSockets, HTTP/2) and `async/await` syntax.
* **Comparison:**
* **WSGI:** Best for standard CRUD apps. Examples: Gunicorn, uWSGI.
* **ASGI:** Required for real-time features (Chat, Notifications) using **Django Channels**. Examples: Daphne, Uvicorn.



---

### **2. Deep-Dive ORM (The "N+1" Mastery)**

**Q: You mentioned N+1. How do you detect it in a production environment without manual checking?**

* **A:** Use tools like `nplusone` (a Python library) or `django-debug-toolbar` in staging. In production, use **APM tools** like Sentry or New Relic, which flag "Database Spans" that look repetitive.

**Q: Explain `prefetch_related` objects (Prefetch objects).**

* **A:** Standard `prefetch_related` fetches all related objects. If you only want a *filtered* subset of related objects (e.g., only "Active" comments for a list of Posts), you use the `Prefetch` object:
```python
# This avoids fetching every single comment into memory
Post.objects.prefetch_related(
    Prefetch('comments', queryset=Comment.objects.filter(is_active=True))
)

```



---

### **3. Intermediate & Senior Level Concepts**

**Q: What is the difference between `Middleware` and `Context Processors`?**

* **A:** * **Middleware:** Operates at the **Request/Response** level. It can modify the request before it hits the view or the response before it leaves the server (e.g., Authentication, Gzip compression).
* **Context Processors:** Operate at the **Template** level. They allow you to make data available to *every* template automatically (e.g., the current user or site settings) without passing it in every view.



**Q: How do you handle a "Fat Model" vs. "Service Layer" architecture?**

* **A:** * **Fat Models:** Put logic in model methods. Good for small apps but leads to unmaintainable code.
* **Service Layer:** Move complex business logic (e.g., "Process Order and Send Email") into separate `services.py` modules. This keeps models for data structure and views for request handling, making the code much easier to unit test.



---

### **4. Advanced Optimization & Security**

**Q: How do you optimize `count()` on a table with 10 million rows?**

* **A:** PostgreSQL and MySQL get slow with `SELECT COUNT(*)` on large tables because they scan the whole table.
* **Solution:** 1.  **Cache the count** in Redis and update it on `save()` and `delete()`.
2.  Use **Database Statistics** (approximate count) if exact precision isn't required (e.g., "About 10,000 results").

**Q: What are "Signals" and why should you avoid them in large systems?**

* **A:** Signals (`post_save`, `pre_delete`) allow decoupled applications to get notified when actions occur.
* **The Problem:** They make code execution **implicit**. It becomes hard to track why a certain database change happened. In large systems, it is better to override the `.save()` method or use a **Service Layer** to keep logic explicit.

---

### **5. Architecture Level: Multi-Database & Multi-Tenancy**

**Q: How do you implement Multi-Tenancy in Django?**

* **A:** 1.  **Shared Database, Shared Schema:** Every table has a `tenant_id`. (Simplest, most scalable).
2.  **Shared Database, Isolated Schemas:** One database, but different Postgres Schemas per client. (Good balance).
3.  **Isolated Databases:** Separate DB per client. (Most secure, hardest to manage).
* Use a **Database Router** in Django to decide which DB to read/write to based on the request.



---

### **6. Deployment & Performance**

**Q: What is the "Thundering Herd" problem in Django caching?**

* **A:** This happens when a heavily used cache key expires, and 1,000 concurrent requests all see a cache miss and try to re-calculate the data from the DB at the same time.
* **Fix:** Use **Probabilistic Early Recomputation** or a "Lock" (using Redis) so only one request regenerates the cache while the others wait or see old data briefly.

---

### **Summary Checklist for your Interview:**

* **WSGI/ASGI:** Know the difference between synchronous and asynchronous serving.
* **N+1:** Master `select_related` (JOIN) vs `prefetch_related` (separate query).
* **F and Q objects:** For complex queries and atomic updates.
* **Transactions:** Use `transaction.atomic` to ensure data integrity.
* **Security:** Understand CSRF, XSS, and SQL Injection protections built into Django.

**Would you like me to walk through a system design scenario, like "How to design a scalable Notification System using Django and Celery"?**


▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄


To wrap up your preparation, these are the **"Architectural Deep-Dive"** questions. These are rarely found on basic interview sites because they test your knowledge of how Django interacts with the underlying OS, the Database engine, and modern distributed systems.

---

### **1. The "Under the Hood" Level**

**Q: Explain the lifecycle of a request in Django when using an ASGI server (like Uvicorn) vs. a WSGI server (like Gunicorn).**

* **A:** * **WSGI:** The server receives the HTTP request and calls the Django callable. It's a synchronous, blocking process. One request = One worker thread/process.
* **ASGI:** The server receives an "Event." The connection is handled via an "Application Instance." This allows for long-polling and WebSockets because the connection doesn't block the worker while waiting for data.
* **Key Internals:** In both cases, the request passes through `SecurityMiddleware`  `SessionMiddleware`  `AuthenticationMiddleware`  `URL Router`  `View`.



**Q: Why does Django's ORM use "Single Inheritance" by default for Multi-table inheritance, and what are the performance costs?**

* **A:** When you inherit a model from a non-abstract base class, Django creates a separate table for each and links them via a `OneToOneField`.
* **The Cost:** Every time you query the child model, Django performs an implicit **INNER JOIN** on the parent table. If you have deep inheritance (3+ levels), your "simple" queries become massive JOIN-heavy operations that kill performance.
* **Solution:** Use **Abstract Base Classes** unless you specifically need to query the parent table independently.

---

### **2. Scaling & High-Performance Level**

**Q: You have a view that needs to generate a 50MB PDF. How do you serve this without blocking other users or crashing the server's RAM?**

* **A:**
1. **Don't generate it in the view:** Offload the generation to a **Celery Worker**.
2. **Streaming:** If you must generate it in-line, use `StreamingHttpResponse`. This sends the data to the user in chunks as it’s generated, keeping the memory footprint low.
3. **Storage:** Store the result in S3 and redirect the user to a pre-signed URL rather than serving the bytes through Python/Django.



**Q: How do you handle "Database Sharding" in Django?**

* **A:** Django doesn't support automatic sharding, but you implement it using **Database Routers**. You define logic in `db_for_read` and `db_for_write` to direct traffic based on a "shard key" (like `tenant_id` or `user_id_prefix`).

---

### **3. The "Gotcha" Questions (Senior Specialty)**

**Q: What is the "Transaction Isolation Level" in Django, and why does it matter?**

* **A:** By default, Django uses the level set by your DB (usually **Read Committed**).
* **The Risk:** In "Read Committed," if you read a value, and another transaction updates it before you finish, you might get "Non-repeatable reads."
* **The Fix:** For critical financial logic, use `select_for_update()` to lock the row, ensuring no other process can touch it until your transaction commits.

**Q: Explain the "Hidden" cost of `GenericForeignKey`.**

* **A:** `GenericForeignKey` allows a model to link to *any* other model.
* **The Problem:** It is **not** a real database constraint. You lose "Referential Integrity" (you can delete the target object and the link stays broken). Furthermore, you cannot use `select_related` on generic keys, leading to massive **N+1 problems** that are hard to fix.

---

### **4. System Design: The Final Boss**

**Q: Design a "Global Rate Limiter" for a Django API that spans 10 server nodes.**

* **A:** You cannot use local memory. You must use a centralized **Redis** store.
1. Use the **Fixed Window** or **Sliding Window Log** algorithm.
2. In a Django Middleware, use `cache.incr(key)` with a TTL (Time to Live).
3. If the count exceeds the threshold, return `HTTP 429 Too Many Requests`.
4. To optimize, use a Lua script in Redis to make the "Check + Increment" operation atomic.



---

### **Final Pro-Tip for your Interview**

When they ask you a question, don't just give the definition. Give the **trade-off**.

* *Instead of:* "Middleware processes requests."
* *Say:* "Middleware is powerful for global logic like Auth, but adding too many custom middlewares increases the latency of **every single request** in the system, even for static heartbeat checks."


▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄


### **1. Database Transaction Mastery**

A senior developer must know how to prevent data corruption during crashes or concurrent writes.

**Q: Explain the difference between `atomic()`, `select_for_update()`, and `savepoints`.**

* **`transaction.atomic()`:** A decorator or context manager that ensures a block of code is a single database transaction. If an error occurs, every change in that block is rolled back.
* **`select_for_update()`:** A QuerySet method that locks the rows until the transaction ends.
* *Scenario:* If you are building a banking app, you **must** use this. Otherwise, two requests could read a $100 balance, subtract $50 simultaneously, and both save the balance as $50 (leaving $50 instead of $0).


* **Savepoints:** These allow you to "partially" roll back a transaction to a specific point without failing the entire transaction.

**Q: What is "Database Connection Pooling" and why doesn't Django do it by default?**

* **A:** Django opens a new connection for every request and closes it at the end (by default). This is slow for high-traffic apps.
* **Solution:** Use **Connexion Pooling** (via `CONN_MAX_AGE` in settings or an external tool like **PgBouncer**). This keeps connections "warm" and reused across multiple requests, drastically reducing latency.

---

### **2. Deployment & Security Architecture**

This is where "Junior" vs "Architecture" is decided.

**Q: What is the "Security Middleware" and why is `ALLOWED_HOSTS` critical?**

* **A:** `SecurityMiddleware` enforces HTTPS, HSTS, and X-Content-Type options.
* **`ALLOWED_HOSTS`:** This is a security measure to prevent **HTTP Host Header attacks**. Without it, an attacker can spoof the host header to lead users to malicious password reset links or cache-poisoning results.

**Q: How do you handle "Media" files in a scaled production environment?**

* **A:** You **never** serve media files (user uploads) via Django in production.
* **Architectural Flow:** 1. User uploads to Django.
2. Django sends the file to **AWS S3** or **Google Cloud Storage**.
3. The file is served to other users via a **CDN (CloudFront/Cloudflare)**.
* *Why?* Serving files through Python is slow and consumes memory that should be used for processing logic.



---

### **3. The "New" Async Django (3.1+ and 4.0+)**

Interviewers in 2026 will expect you to know the modern async capabilities.

**Q: Can you use `async def` and `sync` ORM calls together? What is the "Thread Sensitive" trap?**

* **A:** Yes, but it’s risky. Django's ORM is currently **synchronous**. If you call a sync ORM method inside an `async def` view, it will block the entire event loop.
* **The Fix:** Use `sync_to_async` wrapper or the newer `await MyModel.objects.aget(id=1)` (the `a` prefix methods) which are designed for async contexts.

**Q: Explain "Context Processors" vs "Middleware" execution order.**

* **A:** 1. **Middleware (Request):** Top to bottom.
2. **View:** Business logic.
3. **Context Processors:** Run *after* the view but *before* the template renders to inject global variables (like `{{ request.user }}`).
4. **Middleware (Response):** Bottom to top.

---

### **4. System Design: The "Million User" Problem**

**Q: How would you design a real-time notification system (e.g., Like/Comment alerts) for 1 million users?**

* **Architecture:**
* **Database:** Store notifications in a relational DB for history.
* **Broker:** Use **Redis** with **Django Channels**.
* **Layer:** Use the **Channel Layer** to "group_send" messages to specific user groups.
* **Interface:** Use an **ASGI** server (Daphne/Uvicorn) to handle the long-lived WebSocket connections.



---

### **Summary Table: The "Cheat Sheet"**

| Feature | Best For | Technical Note |
| --- | --- | --- |
| **select_related** | Foreign Key (1-to-1) | One SQL JOIN |
| **prefetch_related** | Many-to-Many | Two separate queries + Python join |
| **F() Expression** | Atomic Updates | Avoids Race Conditions (DB level math) |
| **Q() Object** | Complex Queries | Allows `OR` and `NOT` logic in filters |
| **Middleware** | Global Logic | Runs on every request/response |
