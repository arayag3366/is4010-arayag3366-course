# Week 10: Ownership & Borrowing - Rust Playground Examples

Try these interactive examples in your browser—no installation needed!

---

## Example 1: Move Semantics - Ownership Transfer

**What it demonstrates:** How ownership moves from one variable to another with heap-allocated types.

**The code:**
```rust
fn main() {
    // Create a String (heap-allocated)
    let s1 = String::from("hello");
    println!("s1: {}", s1);

    // Ownership moves from s1 to s2
    let s2 = s1;
    println!("s2: {}", s2);

    // ❌ Uncommenting this line causes a compile error:
    // println!("s1: {}", s1);  // ERROR: value borrowed after move

    // Compare with Copy types (stack-only)
    let x = 5;
    let y = x;  // x is copied, not moved

    println!("x: {}, y: {}", x, y);  // ✅ Both valid!
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Uncomment the line trying to use `s1` and read the compiler error
2. Create two String variables and move one to the other
3. Try to use the original variable and observe the error
4. Explain why integers copy but Strings move

---

## Example 2: Clone to Create Deep Copies

**What it demonstrates:** Using `.clone()` to explicitly create a deep copy instead of moving.

**The code:**
```rust
fn main() {
    let s1 = String::from("hello");

    // Clone creates a deep copy - both variables now own separate data
    let s2 = s1.clone();

    // Now both are valid!
    println!("s1 = {}, s2 = {}", s1, s2);

    // Clone is explicit - you see the cost
    let data = vec![1, 2, 3, 4, 5];
    let data_copy = data.clone();

    println!("Original: {:?}", data);
    println!("Clone: {:?}", data_copy);

    // Performance note: Clone is expensive!
    // Only use when you actually need separate ownership
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a String and clone it 3 times
2. Modify one of the clones (hint: make it `mut` first)
3. Show that the original and other clones are unchanged
4. Think about when you'd want clone vs move

---

## Example 3: Immutable References (&T)

**What it demonstrates:** Borrowing data with immutable references - read access without taking ownership.

**The code:**
```rust
fn main() {
    let s = String::from("hello world");

    // Borrow s immutably (read-only access)
    let len = calculate_length(&s);

    // s is still valid because we only borrowed it!
    println!("The length of '{}' is {}", s, len);

    // Multiple immutable borrows are allowed
    let r1 = &s;
    let r2 = &s;
    let r3 = &s;

    println!("{}, {}, {}", r1, r2, r3);  // All valid!
}

// Function takes a reference (borrows, doesn't own)
fn calculate_length(some_string: &String) -> usize {
    some_string.len()
}  // some_string goes out of scope, but doesn't drop the data (it doesn't own it!)
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Write a function `first_word` that takes `&String` and returns the first word length
2. Create multiple immutable references to the same string
3. Show that all references can be used simultaneously
4. Explain why references don't take ownership

---

## Example 4: Mutable References (&mut T)

**What it demonstrates:** Borrowing data with mutable references - write access without taking ownership.

**The code:**
```rust
fn main() {
    // Must be mut to create mutable references
    let mut s = String::from("hello");

    // Borrow s mutably
    change(&mut s);

    println!("Modified: {}", s);  // "hello, world"

    // Important: Only ONE mutable reference at a time!
    let r1 = &mut s;
    r1.push_str("!");

    // ❌ Can't have two mutable references:
    // let r2 = &mut s;  // ERROR: cannot borrow as mutable more than once

    println!("Final: {}", r1);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Uncomment the second mutable reference and observe the error
2. Write a function that takes `&mut Vec<i32>` and doubles all elements
3. Create a mutable String and pass it to multiple functions that modify it
4. Explain why Rust only allows one mutable reference at a time

---

## Example 5: String vs &str

**What it demonstrates:** The difference between owned `String` and borrowed `&str` types.

**The code:**
```rust
fn main() {
    // String - owned, growable, heap-allocated
    let mut owned = String::from("Hello");
    owned.push_str(", Rust!");
    println!("Owned String: {}", owned);

    // &str - borrowed string slice, immutable view
    let slice: &str = &owned[0..5];  // "Hello"
    println!("String slice: {}", slice);

    // String literals are &str with 'static lifetime
    let literal: &str = "I'm a string literal";
    println!("Literal: {}", literal);

    // Convert between types
    let from_str: String = literal.to_string();
    let to_str: &str = &owned;

    println!("Converted: {}", from_str);
    println!("Borrowed: {}", to_str);

    // Functions should generally accept &str (more flexible)
    print_string("Works with literals");
    print_string(&owned);  // Also works with String references
}

// Accept &str instead of String for flexibility
fn print_string(s: &str) {
    println!("Printing: {}", s);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a String and take various slices of it
2. Write a function that accepts `&str` and returns the length
3. Call it with both string literals and String references
4. Explain when to use String vs &str as parameter types

---

## Example 6: Fixing Borrow Checker Errors

**What it demonstrates:** Common borrow checker errors and how to fix them.

**The code:**
```rust
fn main() {
    println!("=== Example 1: Can't mix mutable and immutable ===");
    let mut s = String::from("hello");

    let r1 = &s;     // Immutable borrow
    let r2 = &s;     // Another immutable borrow (OK!)
    println!("{} and {}", r1, r2);
    // r1 and r2 are no longer used after this point

    let r3 = &mut s; // Mutable borrow (OK - no immutable borrows active)
    r3.push_str(" world");
    println!("{}", r3);

    println!("\n=== Example 2: Scope limits borrow lifetime ===");
    let mut data = vec![1, 2, 3];

    {
        let r = &mut data;
        r.push(4);
    } // r goes out of scope here

    // Now we can borrow again
    let r2 = &mut data;
    r2.push(5);
    println!("Data: {:?}", r2);

    println!("\n=== Example 3: Return owned data, not references ===");
    let result = no_dangle();
    println!("Result: {}", result);
}

// ✅ CORRECT: Return owned value
fn no_dangle() -> String {
    let s = String::from("hello");
    s  // Move ownership out
}

// ❌ WRONG: Can't return reference to local variable
// fn dangle() -> &String {
//     let s = String::from("hello");
//     &s  // ERROR: s will be dropped, reference would be invalid
// }
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Uncomment the `dangle` function and read the compiler error
2. Try to create two mutable references in the same scope
3. Fix it by using separate scopes `{}`
4. Create a function that tries to return a reference to a local variable and fix it

---

## Pro Tips for Understanding Ownership

**Visualize ownership:**
```rust
fn main() {
    let s1 = String::from("data");  // s1 owns "data"
    let s2 = s1;                     // s2 now owns "data", s1 invalidated
    // let s3 = s1;                  // ❌ ERROR: s1 no longer valid

    let s3 = s2.clone();             // s3 owns separate copy
    // Both s2 and s3 valid           ✅ OK
}
```

**Remember the rules:**
1. Each value has ONE owner
2. When owner goes out of scope, value is dropped
3. Either one `&mut` OR many `&` at a time
4. References must always be valid

**Read compiler errors carefully:**
- Rust's error messages explain exactly what's wrong
- They often suggest the fix
- Trust the borrow checker - it's preventing bugs!

---

## Common Patterns to Practice

**Pattern 1: Pass by reference, not by value**
```rust
fn process(data: &String) { /* ... */ }  // ✅ Borrows
// Not: fn process(data: String) { /* ... */ }  // ❌ Takes ownership
```

**Pattern 2: Return owned data**
```rust
fn create() -> String { String::from("data") }  // ✅ Transfers ownership out
```

**Pattern 3: Limit mutable borrow scope**
```rust
{
    let r = &mut data;
    // use r
}  // r dropped here
// Can create new reference now
```

---

## Next Steps

**After mastering these concepts:**
1. Complete **Lab 10** - The Borrow Checker Game
2. Practice fixing ownership violations
3. Learn about lifetimes (Week 11)
4. Understand when to use `Box`, `Rc`, `Arc` (Week 13)

**Resources:**
- [The Rust Book - Chapter 4: Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [Rust by Example - Ownership](https://doc.rust-lang.org/rust-by-example/scope.html)
- [Rustlings - Move Semantics Exercises](https://github.com/rust-lang/rustlings/)

**The key to mastering ownership:** Practice reading compiler errors and understanding WHY the rules exist (preventing memory bugs!).
