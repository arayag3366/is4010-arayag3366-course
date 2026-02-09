# Lab 04: Data Structures
## Problem 1: Finding Common Items
**My Prompt**
I have two very large lists of product IDs from two different suppliers, and I need to find out which product IDs are present in both lists. The order of the final list does not matter. Can you recommend the best Python data structure for this problem?

**AI's Recommendation and Reasoning**
Yep — this is a classic case where **Python sets** shine ✨

### Best choice: `set`

If you have two large lists and you want to find which product IDs appear in **both**, converting them to sets and using **set intersection** is the fastest and most memory-efficient approach in Python.

Why sets?

* **O(1)** average-time membership checks
* Built-in, highly optimized intersection operations
* Order doesn’t matter (which you said is fine)

### How it looks in practice

```python
supplier_a_ids = set(list_a)
supplier_b_ids = set(list_b)

common_ids = supplier_a_ids & supplier_b_ids
```

Or, if you prefer it spelled out:

```python
common_ids = supplier_a_ids.intersection(supplier_b_ids)
```

### Performance intuition

* Lists → checking membership is **O(n)** each time (slow for large data)
* Sets → membership checks are **O(1)** on average
* Intersection runs in **O(min(len(a), len(b)))**

That’s about as good as it gets for this problem.

### One small note

If your product IDs are already unique in each list, you’re golden.
If they *aren’t*, converting to a set will automatically de-duplicate them — which is usually what you want when comparing IDs.

If you want, I can also show how this scales compared to a list-based approach, or how to handle cases where you need to keep counts or metadata 👀

## Problem 2: User Profile Lookup
**My Prompt**
Please help me determine what data structure is best to use in a scenario wherein an application loads a list of user profiles from a database where each user has a unique username, an age, and an email address. A user's complete profile is frequently looked up by using their username. Optimized performance is critical.

**AI's Recommendation and Reasoning**
Given your requirements, the best fit here is a **hash-based map/dictionary keyed by username**.

### Why a hash map (dictionary)?

* **Unique key**: Usernames are guaranteed to be unique → perfect as keys.
* **Frequent lookups by username**: Hash maps provide **O(1) average-time** lookups.
* **Performance-critical**: This is about as fast as it gets for in-memory access.

### What it looks like conceptually

* **Key**: `username` (string)
* **Value**: a `UserProfile` object/struct containing `age` and `email`

Example (Python-style for clarity):

```python
users = {
    "alice123": {"age": 25, "email": "alice@example.com"},
    "bob_smith": {"age": 32, "email": "bob@example.com"}
}

profile = users["alice123"]  # O(1) average time
```

### Why not other data structures?

* **List / array**: Would require O(n) search to find a user by username — too slow at scale.
* **Tree (BST, balanced tree)**: O(log n) lookups are good, but still slower than a hash map when exact-key lookup is the dominant operation.
* **Set**: Doesn’t work well because you need to retrieve associated profile data, not just check existence.

### Memory vs. speed trade-off

Hash maps use a bit more memory than lists or trees, but in a performance-critical system where lookups dominate, this trade-off is almost always worth it.

### Final recommendation

Use a **dictionary (hash map)** where:

* `username` → key
* `user profile data (age, email, etc.)` → value

This gives you **fast, direct access**, excellent scalability, and clean, readable code.

## Problem 3: Listing Even Numbers In Order
**My Prompt**
What is the best Python data structure to use in a situation where I am given a list of integers representing sensor readings and need to produce a report that contains only the even-numbered readings presented in the exact same order they were received?

**AI's Recommendation and Reasoning**
You don’t need anything fancy here—the best data structure is just a **list**. 👍

### Why a list is the right choice

* **Preserves order**: Lists keep elements in the exact order they’re added, which is a hard requirement in your case.
* **Simple filtering**: You can easily select only the even readings.
* **Efficient enough**: For typical sensor data sizes, list operations are fast and idiomatic.

### Idiomatic Python approach

Use a list comprehension to filter the even numbers while maintaining order:

```python
even_readings = [reading for reading in sensor_readings if reading % 2 == 0]
```

This:

* Iterates once over the input
* Keeps only even integers
* Preserves the original sequence exactly

### When you might consider something else

* **Very large or streaming data**: A generator expression could be useful if you want to process readings lazily.
* **Need fast membership checks**: A `set` would help—but it would *not* preserve order, so it’s not appropriate here.

### Bottom line

For “filter these values and keep their original order,” a **list** is the most Pythonic and correct data structure. Clean, readable, and purpose-built for this task. 🐍✨