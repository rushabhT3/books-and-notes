# Node.js Interview Questions:
## Below questions + Interview Bit questions (https://www.interviewbit.com/node-js-interview-questions/)

### **1. The "Crucial" Question: Priority & Event Loop**

**Q: Explain the exact priority between `process.nextTick()`, `setImmediate()`, and `setTimeout(fn, 0)`.**

**The Reality:**
Contrary to the names, `setImmediate()` is **not** immediate, and `nextTick()` does **not** fire on the "next" tick (iteration)—it fires at the end of the *current* operation.

* **Priority 1: `process.nextTick()` (Highest)**
* It is **not** part of the libuv event loop phases.
* Callbacks are stored in the `nextTickQueue`. This queue is drained **immediately** after the current operation completes, regardless of the current phase of the event loop.
* *Warning:* Recursively calling `nextTick` will starve the event loop (it will never move to the next phase).


* **Priority 2: `Microtasks` (Promises)**
* Resolved after `nextTickQueue` but before the event loop continues to the next phase.


* **Priority 3: `setTimeout(fn, 0)` vs `setImmediate()**`
* **Inside an I/O cycle:** `setImmediate` is guaranteed to run first because the `poll` phase (I/O) is followed immediately by the `check` phase (where `setImmediate` lives).
* **Main Module (Random):** If called in the main script, the order is non-deterministic (depends on process performance).



---

### **2. Junior Level (Fundamentals)**

**Q: Why is Node.js single-threaded but still handles 10k+ concurrent connections?**

* **A:** Node.js is single-threaded for **JavaScript execution only**. It offloads I/O tasks (file system, network, DNS) to **Libuv’s thread pool** (usually 4 threads) or the Operating System kernel. This allows the main thread to remain free to handle new incoming requests.

**Q: What is the difference between `__dirname` and `process.cwd()`?**

* **A:** `__dirname` is the absolute path to the **directory of the file** being executed. `process.cwd()` is the absolute path to the **directory from which you launched** the node process.

---

### **3. Intermediate Level (Development & Patterns)**

**Q: What is "Backpressure" in Streams and how do you handle it?**

* **A:** Backpressure occurs when the **Readable** stream produces data faster than the **Writable** stream can consume it (filling the buffer).
* **Handling:** Use `.pipe()` which manages backpressure automatically. If manual, listen for the `drain` event on the Writable stream before resuming the Readable stream.

**Q: Difference between `fork()` and `spawn()`?**

* **A:** * `spawn()`: Starts a process and streams data. Best for large data or system commands (like `ls` or `grep`).
* `fork()`: A special case of `spawn` that creates a new V8 instance and an **IPC (Inter-Process Communication)** channel. Best for offloading heavy JS calculations.



---

### **4. Senior Level (Scaling & Reliability)**

**Q: How do you handle a CPU-intensive task in Node without blocking the event loop?**

* **A:** 1.  **Worker Threads:** (Recommended) Runs JS in parallel on a separate thread (sharing memory via `SharedArrayBuffer`).
2.  **Child Process (`fork`):** Runs a separate process with its own memory.
3.  **Partitioning:** Breaking the task into smaller chunks using `setImmediate()` to allow the event loop to breathe between iterations.

**Q: Explain the "Reactor Pattern" in Node.js.**

* **A:** It’s the heart of Node. It involves a **Demultiplexer** (handles I/O requests), an **Event Queue**, and the **Event Loop**. When an I/O request is made, it’s sent to the Demultiplexer with a handler. Once the I/O is done, the Demultiplexer pushes the handler to the Event Queue for the Loop to execute.

---

### **5. Architect Level (Optimization & Infrastructure)**

**Q: How would you debug a Memory Leak in production?**

* **A:**
1. **Trigger Heap Dumps:** Use the `v8` module or `node --inspect`.
2. **Comparison:** Take two snapshots (one at start, one after load) and look for objects that aren't being garbage collected (usually global variables, forgotten timers, or closures).
3. **Tools:** Use **Clinic.js (Heapprofiler)** or **Chrome DevTools**.



**Q: What are the best strategies for optimizing Node.js performance?**

* **A:**
* **V8 Optimization:** Avoid "Hidden Class" changes (always initialize objects with the same properties in the same order).
* **Infrastructure:** Use a Reverse Proxy (Nginx) for SSL termination and static file serving to keep Node focused on logic.
* **Clustering:** Use the `cluster` module or **PM2** to run one process per CPU core.
* **Zero-Copy:** Use `Buffer.allocUnsafe()` for performance if you are immediately overwriting the data (avoiding the cost of zero-filling).



---

### **Summary Cheat Sheet: Timing Order**

If you run this code, the order will always be:

1. `Sync Code`
2. `process.nextTick`
3. `Promise.then` (Microtask)
4. `setTimeout 0` OR `setImmediate` (depending on the phase)

```javascript
console.log('1. Sync');
setTimeout(() => console.log('4. Timeout'), 0);
setImmediate(() => console.log('5. Immediate'));
process.nextTick(() => console.log('2. NextTick'));
Promise.resolve().then(() => console.log('3. Promise'));

```

▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄

---

### **1. The Core Internals (The "Architect" Level)**

**Q: Explain the Libuv Thread Pool. When is it used, and how do you scale it?**

* **A:** Node.js uses Libuv for asynchronous I/O. While network I/O is handled via OS epoll/kqueue (non-blocking), other tasks are offloaded to a **Thread Pool**.
* **Tasks using the Thread Pool:** `fs` (File System), `crypto`, `zlib`, and `dns.lookup`.
* **Scaling:** By default, the pool size is **4**. For heavy apps, this is a bottleneck. You can increase it using: `process.env.UV_THREADPOOL_SIZE = 64`.

**Q: How does the Event Loop handle Microtasks vs. Macrotasks?**

* **A:** The Event Loop has phases (Timers, Pending, Poll, Check, Close).
* **The Nuance:** Microtasks (`process.nextTick` and `Promises`) are executed **between every phase** of the event loop and even between individual callbacks within a phase.
* **Priority:** `process.nextTick` > `Promise` callbacks > `setImmediate/setTimeout`.

---

### **2. Performance & Optimization**

**Q: What is "Garbage Collection" (GC) in Node.js, and how can you trigger it manually?**

* **A:** Node uses the V8 engine’s "Mark-and-Sweep" algorithm. It has two main areas: **New Space** (short-lived objects) and **Old Space** (long-lived objects).
* **Manual Trigger:** Start Node with `--expose-gc` and call `global.gc()`.
* **Optimization:** Avoid "Memory Leaks" by clearing intervals, nullifying large objects, and avoiding global variables.

**Q: How do you handle "Hot Path" optimization in Node.js?**

* **A:** A Hot Path is a section of code executed frequently (e.g., a loop in a request handler).
* **Optimization Techniques:**
* **Inlining:** Keep functions small so V8 can inline them.
* **Hidden Classes:** Always initialize object properties in the same order so V8 doesn't have to re-create the "hidden class" of the object.
* **Avoid 'Delete':** Using `delete obj.prop` changes the hidden class and makes it "generic," slowing down execution. Set it to `undefined` instead.



---

### **3. Streams & Buffers (Data Handling)**

**Q: Explain the difference between `Buffer.alloc()` and `Buffer.allocUnsafe()`.**

* **A:** * `alloc(size)`: Creates a buffer and **zero-fills** it (secure but slower).
* `allocUnsafe(size)`: Grabs a chunk of memory **without cleaning it**. It may contain sensitive old data, but it is significantly faster. Use it only if you are immediately filling the buffer with new data.



**Q: What is a "Transform Stream" and when would you use it?**

* **A:** It is a type of Duplex stream where the output is computed from the input.
* **Example:** Compressing a file (`zlib.createGzip()`) or encrypting data on the fly as it is being uploaded.

---

### **4. Security & Scaling**

**Q: How do you protect a Node.js API from "Event Loop Blocking" attacks?**

* **A:** 1.  **Validation:** Limit the size of incoming JSON payloads (`body-parser` limits).
2.  **Offloading:** Use `Worker Threads` for heavy computation (e.g., Bcrypt hashing).
3.  **Rate Limiting:** Use `express-rate-limit` to prevent DoS.
4.  **Avoid RegEx pitfalls:** Don't use "Evil Regex" (Nested quantifiers) that cause exponential backtracking.

**Q: Compare "Clustering" vs "Worker Threads".**

| Feature | Clustering | Worker Threads |
| --- | --- | --- |
| **Model** | Multi-process | Multi-thread |
| **Memory** | Isolated (High overhead) | Shared (Low overhead) |
| **Best for** | Scaling network servers (Nginx-style) | CPU-intensive tasks (image processing) |
| **Communication** | IPC (Serialization) | SharedArrayBuffer (Fast) |

---

### **5. Advanced Design Patterns**

**Q: What is the "Dependency Injection" pattern in Node, and why use it?**

* **A:** Instead of `require`-ing a database connection inside a service, you pass the connection as a parameter to the constructor/function.
* **Benefit:** It makes **Unit Testing** much easier because you can inject a "Mock" database instead of a real one.

**Q: How does the `EventEmitter` work, and what is a "Memory Leak" risk associated with it?**

* **A:** It’s an implementation of the Observer pattern.
* **The Risk:** If you add a listener (`on('event')`) inside a function that runs repeatedly and never call `removeListener()` or `off()`, the listeners array grows indefinitely, causing a memory leak.

---

### **Summary of "The Priority" (The SetImmediate vs NextTick code challenge)**

If an interviewer asks you to predict the output of this code, this is the "Golden Standard" answer:

```javascript
const fs = require('fs');

fs.readFile(__filename, () => {
    setTimeout(() => console.log('Timeout'), 0);
    setImmediate(() => console.log('Immediate'));
    process.nextTick(() => console.log('NextTick'));
});

```

**Output:**

1. **NextTick**: Because it executes immediately after the I/O callback finishes but before the loop continues.
2. **Immediate**: Because the I/O callback is in the **Poll Phase**, and the **Check Phase** (where `setImmediate` sits) comes immediately after.
3. **Timeout**: Because the loop has to wrap all the way around to the **Timers Phase** in the next iteration.

**Would you like me to create a specific set of "Architecture" scenario questions, such as "How would you design a real-time chat system with 1 million concurrent Node.js users"?**


▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄

---

### **1. Advanced Event Loop Scenarios**

**Q: If you have a `while(true)` loop in your code, will a `setTimeout` or `process.nextTick` ever fire?**

* **A:** **No.** Because the JavaScript execution thread is occupied by the `while` loop, the Event Loop is "blocked." It can never finish the current "poll" or "execution" phase to move on to check the timer or nextTick queues. This is why you must never perform heavy CPU tasks on the main thread.

**Q: In the Poll Phase, what happens if the queue is empty?**

* **A:** If the queue is empty, the loop will:
1. Check if there are any `setImmediate` scripts. If yes, it moves to the **Check Phase**.
2. If no `setImmediate`, it will **wait** (block) for I/O events to be added to the queue, then execute them immediately.
3. If there are expired timers, it wraps back to the **Timers Phase**.



---

### **2. System Design & Security**

**Q: How would you design a "Distributed Lock" in Node.js for a microservices architecture?**

* **A:** Since Node is single-threaded, a local variable works as a lock for one instance. But for multiple instances, you need a shared store like **Redis** using the `Redlock` algorithm. This prevents two different microservices from processing the same piece of data (like a bank withdrawal) at the exact same time.

**Q: What is a "Re-DoS" (Regular Expression Denial of Service) attack?**

* **A:** This happens when a complex Regex (like `(a+)+$`) is run against a specific string that causes "exponential backtracking." The V8 engine will spend 100% CPU trying to match it, blocking the event loop for everyone.
* **Fix:** Use the `safe-regex` library to check your patterns.

---

### **3. Memory & Performance Tuning**

**Q: What is the "V8 Hidden Class" optimization, and how do you write code to take advantage of it?**

* **A:** V8 creates "hidden classes" for objects to speed up property access.
* **The Rule:** Always initialize all object properties in the **constructor** and in the **same order**.
* *Bad:* Creating `obj.a = 1` then later `obj.b = 2` in some cases, but `obj.b` then `obj.a` in others. This forces V8 to create multiple hidden classes, slowing down the code.



**Q: How do you handle 1GB of data processing in a 512MB RAM container?**

* **A:** **Streams.** You must never use `fs.readFile` or `JSON.parse` on the whole file. Instead, use `fs.createReadStream`, pipe it through a `Transform` stream (like `csv-parser` or `zlib`), and write it out using a `Writable` stream. This keeps the memory usage constant (around 30-50MB) regardless of file size.

---

### **4. Error Handling at Scale**

**Q: Why is `process.on('uncaughtException')` dangerous?**

* **A:** It should only be used as a last resort for logging. When an uncaught exception occurs, the application state becomes **unreliable** (variables might be half-set, sockets might be leaked).
* **Best Practice:** Log the error, then use `process.exit(1)` and let a process manager like **PM2** or **Kubernetes** restart the instance.

---

### **The Final Checklist**

To be 100% sure, verify you know these "one-liner" concepts:

* **REPL:** Read-Eval-Print-Loop (The interactive Node shell).
* **WASI:** WebAssembly System Interface (Running high-performance C++/Rust code in Node).
* **CommonJS vs ESM:** `require` (synchronous) vs `import` (asynchronous/static).
* **Cluster vs Worker Threads:** Cluster = multiple processes (scaling throughput); Workers = multiple threads (scaling heavy math).

### **Conclusion**

If you have read the InterviewBit guide and these two responses, you have covered:

1. **Architecture** (Event Loop, Libuv, V8)
2. **Concurrency** (nextTick, setImmediate, Promises, Workers)
3. **Data handling** (Streams, Buffers, Backpressure)
4. **Scaling** (Clustering, PM2, Microservices)
5. **Optimization** (Memory leaks, Hidden classes, CPU blocking)

**Would you like me to simulate a "Mock Interview" where I ask you 3 difficult questions and then grade your answers?**


▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄