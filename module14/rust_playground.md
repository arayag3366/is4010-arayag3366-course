# Week 14: Multithreaded Applications - Rust Playground Examples

**Note:** Some threading examples may have limited functionality in Rust Playground due to browser environment restrictions. For full threading capabilities, use a local Rust installation.

---

## Example 1: Spawning Threads - Basic Concurrency

**What it demonstrates:** Creating and running concurrent threads with thread::spawn.

**The code:**
```rust
use std::thread;
use std::time::Duration;

fn main() {
    // Spawn a new thread
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("Thread: count {}", i);
            thread::sleep(Duration::from_millis(50));
        }
    });

    // Main thread continues
    for i in 1..5 {
        println!("Main: count {}", i);
        thread::sleep(Duration::from_millis(50));
    }

    // Wait for spawned thread to finish
    handle.join().unwrap();
    println!("Thread finished!");
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**What you'll see:** Output from both threads interleaved - demonstrating concurrent execution.

**Challenge:**
1. Spawn 3 threads that each print different messages
2. Store all join handles and wait for all threads
3. Observe how execution order is non-deterministic
4. Explain why we need to call .join()

---

## Example 2: Move Semantics with Threads

**What it demonstrates:** Using `move` keyword to transfer ownership into thread closures.

**The code:**
```rust
use std::thread;

fn main() {
    let data = vec![1, 2, 3, 4, 5];

    // ❌ This won't compile - closure might outlive 'data'
    // let handle = thread::spawn(|| {
    //     println!("Data: {:?}", data);
    // });

    // ✅ Use 'move' to transfer ownership
    let handle = thread::spawn(move || {
        println!("Thread owns data: {:?}", data);
        let sum: i32 = data.iter().sum();
        println!("Sum: {}", sum);
        sum  // Return value from thread
    });

    // data is no longer accessible here - moved into thread

    // Get result from thread
    let result = handle.join().unwrap();
    println!("Thread returned: {}", result);

    // Multiple threads with cloned data
    let numbers = vec![10, 20, 30];

    let handles: Vec<_> = (0..3)
        .map(|i| {
            let nums = numbers.clone();  // Clone for each thread
            thread::spawn(move || {
                println!("Thread {}: {:?}", i, nums);
            })
        })
        .collect();

    // Wait for all threads
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Try removing `move` and observe the compiler error
2. Create 5 threads, each printing a different portion of a string
3. Return different values from each thread and collect them
4. Explain why threads need to own their data

---

## Example 3: Message Passing with Channels

**What it demonstrates:** Thread communication using channels (mpsc - multi-producer, single-consumer).

**The code:**
```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    // Create a channel
    let (tx, rx) = mpsc::channel();

    // Spawn thread that sends messages
    thread::spawn(move || {
        let messages = vec![
            String::from("Hello"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for msg in messages {
            tx.send(msg).unwrap();
            thread::sleep(Duration::from_millis(100));
        }
    });

    // Receive messages in main thread
    for received in rx {
        println!("Received: {}", received);
    }

    println!("\n=== Multiple senders ===");

    // Multiple senders, one receiver
    let (tx, rx) = mpsc::channel();

    for i in 0..3 {
        let tx_clone = tx.clone();
        thread::spawn(move || {
            let msg = format!("Message from thread {}", i);
            tx_clone.send(msg).unwrap();
        });
    }

    // Drop original sender so loop knows when to end
    drop(tx);

    // Receive all messages
    for received in rx {
        println!("Got: {}", received);
    }
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a worker thread that processes numbers sent via channel
2. Send a shutdown signal through the channel
3. Use try_recv() for non-blocking receive
4. Create multiple sender threads and one receiver

---

## Example 4: Shared State with Arc<Mutex<T>>

**What it demonstrates:** Thread-safe shared mutable state using Arc (Atomic Reference Counting) and Mutex.

**The code:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Create shared counter wrapped in Arc<Mutex<>>
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for i in 0..10 {
        // Clone Arc (increments reference count)
        let counter_clone = Arc::clone(&counter);

        let handle = thread::spawn(move || {
            // Lock mutex to access data
            let mut num = counter_clone.lock().unwrap();
            *num += 1;

            println!("Thread {} incremented to {}", i, *num);
        });  // Lock automatically released when 'num' goes out of scope

        handles.push(handle);
    }

    // Wait for all threads
    for handle in handles {
        handle.join().unwrap();
    }

    // Check final value
    println!("Final counter: {}", *counter.lock().unwrap());

    println!("\n=== Shared Vec example ===");

    let data = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];

    for i in 0..5 {
        let data_clone = Arc::clone(&data);
        let handle = thread::spawn(move || {
            let mut vec = data_clone.lock().unwrap();
            vec.push(i * 10);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Shared vec: {:?}", *data.lock().unwrap());
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a shared HashMap that multiple threads insert into
2. Use Arc<Mutex<>> to share a String that threads append to
3. Try using Rc instead of Arc - observe the error
4. Explain why we need both Arc AND Mutex

---

## Example 5: Parallel Computation Pattern

**What it demonstrates:** Dividing work among threads for parallel processing.

**The code:**
```rust
use std::thread;

fn main() {
    let numbers: Vec<i32> = (1..=100).collect();

    // Split work among threads
    let chunk_size = numbers.len() / 4;
    let mut handles = vec![];

    for i in 0..4 {
        let start = i * chunk_size;
        let end = if i == 3 {
            numbers.len()  // Last chunk gets remainder
        } else {
            (i + 1) * chunk_size
        };

        let chunk: Vec<i32> = numbers[start..end].to_vec();

        let handle = thread::spawn(move || {
            let sum: i32 = chunk.iter().sum();
            println!("Thread {} sum: {}", i, sum);
            sum  // Return sum from thread
        });

        handles.push(handle);
    }

    // Collect results from all threads
    let mut total = 0;
    for handle in handles {
        total += handle.join().unwrap();
    }

    println!("Total sum: {}", total);

    // Verify with single-threaded version
    let expected: i32 = numbers.iter().sum();
    println!("Expected: {}", expected);
    assert_eq!(total, expected);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Find the maximum value in parallel
2. Count how many numbers are even using multiple threads
3. Search for a specific value in parallel
4. Measure theoretical speedup (single-thread vs multi-thread time)

---

## Example 6: Thread Pool Pattern (Conceptual)

**What it demonstrates:** Reusing threads with a work queue pattern.

**The code:**
```rust
use std::sync::{mpsc, Arc, Mutex};
use std::thread;

enum Message {
    NewJob(i32),
    Terminate,
}

fn main() {
    let (sender, receiver) = mpsc::channel();
    let receiver = Arc::new(Mutex::new(receiver));
    let mut workers = vec![];

    // Spawn worker threads
    for id in 0..4 {
        let receiver = Arc::clone(&receiver);

        let worker = thread::spawn(move || {
            loop {
                // Lock mutex to receive job
                let message = receiver.lock().unwrap().recv().unwrap();

                match message {
                    Message::NewJob(job) => {
                        println!("Worker {} processing job {}", id, job);
                        // Simulate work
                        thread::sleep(std::time::Duration::from_millis(100));
                        println!("Worker {} finished job {}", id, job);
                    }
                    Message::Terminate => {
                        println!("Worker {} shutting down", id);
                        break;
                    }
                }
            }
        });

        workers.push(worker);
    }

    // Send jobs to workers
    for job in 0..10 {
        sender.send(Message::NewJob(job)).unwrap();
    }

    // Send shutdown signal to all workers
    for _ in 0..4 {
        sender.send(Message::Terminate).unwrap();
    }

    // Wait for all workers to finish
    for worker in workers {
        worker.join().unwrap();
    }

    println!("All workers finished!");
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Add a job counter to track how many jobs each worker processes
2. Implement priority jobs (process certain jobs first)
3. Add graceful shutdown that waits for in-progress jobs
4. Explain why this pattern is more efficient than spawning threads per job

---

## Conceptual Examples (May not run in Playground)

These patterns demonstrate important concurrency concepts but may require a local Rust installation:

### Pattern 1: Preventing Data Races
```rust
// ❌ Won't compile - prevents data race!
let mut data = vec![1, 2, 3];
thread::spawn(|| {
    data.push(4);  // ERROR: can't send mutable reference to thread
});
data.push(5);  // Would cause data race

// ✅ Correct - use Arc<Mutex<>>
let data = Arc::new(Mutex::new(vec![1, 2, 3]));
// Now safe to share across threads
```

### Pattern 2: Deadlock Prevention
```rust
// ❌ Potential deadlock
// Thread 1: lock A, then lock B
// Thread 2: lock B, then lock A
// → Circular dependency!

// ✅ Solution: Always acquire locks in same order
// Both threads: lock A first, then lock B
```

### Pattern 3: Channel vs Shared State
```rust
// Channels: Transfer ownership
tx.send(data);  // Data moved to receiver

// Shared state: Multiple owners
let data = Arc::new(Mutex::new(value));
// All threads can access, one at a time
```

---

## Pro Tips for Concurrent Rust

**Choosing between channels and Arc<Mutex<>>:**
- **Use channels when:** Ownership transfer makes sense, producer-consumer patterns
- **Use Arc<Mutex<>> when:** Multiple threads need read/write access to same data

**Remember: Rust prevents data races at compile time!**
- Can't have `&T` and `&mut T` simultaneously
- Can't share mutable references across threads
- Mutex ensures only one thread accesses data at a time

**Common patterns:**
```rust
// Parallel processing
let handles: Vec<_> = chunks
    .into_iter()
    .map(|chunk| thread::spawn(move || process(chunk)))
    .collect();

// Shared counter
Arc::new(Mutex::new(0))

// Work queue
let (tx, rx) = mpsc::channel();
```

**Performance considerations:**
- Thread creation has overhead (~100μs)
- Lock acquisition has overhead
- Only parallelize if work is substantial
- Measure actual speedup - don't assume!

---

## Important Note About Playground Limitations

**Rust Playground restrictions:**
- Limited thread execution time
- May not show true parallelism (browser environment)
- Some examples may timeout or behave differently than local

**For full threading experience:**
```bash
# Install Rust locally
rustup install stable

# Create project
cargo new threading_examples
cd threading_examples

# Run examples
cargo run
```

---

## Next Steps

**After mastering these concepts:**
1. Complete **Lab 14** - Parallel File Processor
2. Practice with local threading (not in Playground)
3. Explore async/await for asynchronous programming
4. Learn about atomic operations and lock-free data structures

**Resources:**
- [The Rust Book - Ch 16: Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)
- [std::thread documentation](https://doc.rust-lang.org/std/thread/)
- [std::sync::mpsc](https://doc.rust-lang.org/std/sync/mpsc/)
- [Arc documentation](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [Mutex documentation](https://doc.rust-lang.org/std/sync/struct.Mutex.html)

**The Rust advantage:** Fearless concurrency - if it compiles, it's thread-safe!
