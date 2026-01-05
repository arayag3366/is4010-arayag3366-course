# Week 13: Idiomatic Rust - Rust Playground Examples

Try these interactive examples in your browser—no installation needed!

---

## Example 1: Iterator Methods - map, filter, collect

**What it demonstrates:** Functional-style data processing with iterator chains.

**The code:**
```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // Old way: manual loop
    let mut evens = Vec::new();
    for &n in &numbers {
        if n % 2 == 0 {
            evens.push(n * n);
        }
    }
    println!("Manual loop: {:?}", evens);

    // Idiomatic way: iterator chain
    let evens: Vec<i32> = numbers
        .iter()                      // Create iterator
        .filter(|&&n| n % 2 == 0)   // Keep only evens
        .map(|&n| n * n)             // Square each number
        .collect();                  // Gather into Vec

    println!("Iterator chain: {:?}", evens);

    // More examples
    let sum: i32 = numbers.iter().sum();
    println!("Sum: {}", sum);

    let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();
    println!("Doubled: {:?}", doubled);

    // Find first element matching condition
    let first_large = numbers.iter().find(|&&x| x > 5);
    println!("First > 5: {:?}", first_large);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Filter numbers divisible by 3, cube them, and sum the results
2. Find all strings starting with 'a' in a Vec<String> and uppercase them
3. Use `.take(5)` to get only the first 5 even squares
4. Compare performance perception of loops vs iterators

---

## Example 2: Closures - Capturing Environment

**What it demonstrates:** Anonymous functions that can capture variables from their environment.

**The code:**
```rust
fn main() {
    // Simple closure
    let add_one = |x: i32| x + 1;
    println!("5 + 1 = {}", add_one(5));

    // Type inference - compiler figures out types
    let square = |x| x * x;
    println!("4² = {}", square(4));

    // Closure capturing environment (immutable borrow)
    let threshold = 10;
    let is_large = |x: i32| x > threshold;  // Captures 'threshold'
    println!("Is 15 large? {}", is_large(15));
    println!("Is 5 large? {}", is_large(5));

    // Mutable closure
    let mut count = 0;
    let mut increment = || {
        count += 1;
        count
    };
    println!("Count: {}", increment());
    println!("Count: {}", increment());
    println!("Count: {}", increment());

    // Using closures with iterators
    let numbers = vec![1, 2, 3, 4, 5];
    let multiplier = 10;

    let result: Vec<i32> = numbers
        .iter()
        .map(|x| x * multiplier)  // Closure captures 'multiplier'
        .collect();

    println!("Multiplied: {:?}", result);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a closure that captures a String and checks if a word contains it
2. Write a closure that captures a mutable counter and increments it
3. Use a closure with `.filter()` to keep only numbers in a specific range
4. Explain the difference between Fn, FnMut, and FnOnce

---

## Example 3: Closure Traits - Fn, FnMut, FnOnce

**What it demonstrates:** How closures capture variables in different ways.

**The code:**
```rust
fn main() {
    println!("=== Fn - Immutable Borrow ===");
    let x = 10;
    let print_x = || println!("x = {}", x);  // Borrows x immutably
    print_x();
    print_x();  // Can call multiple times
    println!("x still accessible: {}", x);

    println!("\n=== FnMut - Mutable Borrow ===");
    let mut counter = 0;
    let mut increment = || {
        counter += 1;  // Mutably borrows counter
        counter
    };
    println!("Counter: {}", increment());
    println!("Counter: {}", increment());
    // Can't use 'counter' here - borrowed mutably by closure

    println!("\n=== FnOnce - Takes Ownership ===");
    let data = vec![1, 2, 3];
    let consume = || {
        let _owned = data;  // Takes ownership
        println!("Consumed data");
    };
    consume();
    // Can only call once - data moved into closure
    // consume();  // ❌ ERROR: use of moved value

    println!("\n=== Using 'move' keyword ===");
    let message = String::from("Hello");
    let print_message = move || println!("{}", message);  // Forces ownership transfer
    print_message();
    // message no longer accessible here
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Try calling the `consume` closure twice - observe the error
2. Create a closure that modifies a Vec<i32> (FnMut)
3. Use `move` to transfer ownership of a String into a closure
4. Explain when each closure type is needed

---

## Example 4: Smart Pointers - Box, Rc, RefCell

**What it demonstrates:** Flexible memory management with Box<T> for heap allocation.

**The code:**
```rust
#[derive(Debug)]
enum List<T> {
    Cons(T, Box<List<T>>),  // Box enables recursion!
    Nil,
}

use List::{Cons, Nil};

fn main() {
    // Box<T> - Heap allocation
    let boxed = Box::new(5);
    println!("Boxed value: {}", boxed);

    // Recursive type - only works with Box
    let list = Cons(1,
        Box::new(Cons(2,
            Box::new(Cons(3,
                Box::new(Nil))))));

    println!("List: {:?}", list);

    // Box automatically derefs
    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);  // Dereference with *

    // Use case: Large data on heap
    let large_array = Box::new([0; 1000]);
    println!("Large array on heap (first element): {}", large_array[0]);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a binary tree using Box<T>
2. Build a linked list with Box
3. Box a large struct and pass it around without copying
4. Explain why Box is needed for recursive types

---

## Example 5: Result and the ? Operator

**What it demonstrates:** Idiomatic error handling with `?` for propagation.

**The code:**
```rust
#[derive(Debug)]
enum MathError {
    DivisionByZero,
    NegativeSquareRoot,
}

fn divide(a: f64, b: f64) -> Result<f64, MathError> {
    if b == 0.0 {
        Err(MathError::DivisionByZero)
    } else {
        Ok(a / b)
    }
}

fn sqrt(x: f64) -> Result<f64, MathError> {
    if x < 0.0 {
        Err(MathError::NegativeSquareRoot)
    } else {
        Ok(x.sqrt())
    }
}

// Using ? operator to propagate errors
fn calculate(a: f64, b: f64) -> Result<f64, MathError> {
    let quotient = divide(a, b)?;  // Returns early if Err
    let result = sqrt(quotient)?;  // Returns early if Err
    Ok(result)  // Success case
}

// Without ? operator (verbose!)
fn calculate_verbose(a: f64, b: f64) -> Result<f64, MathError> {
    let quotient = match divide(a, b) {
        Ok(val) => val,
        Err(e) => return Err(e),
    };

    let result = match sqrt(quotient) {
        Ok(val) => val,
        Err(e) => return Err(e),
    };

    Ok(result)
}

fn main() {
    // Success case
    match calculate(16.0, 4.0) {
        Ok(result) => println!("sqrt(16/4) = {}", result),
        Err(e) => println!("Error: {:?}", e),
    }

    // Division by zero
    match calculate(10.0, 0.0) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => println!("Error: {:?}", e),
    }

    // Negative square root
    match calculate(-16.0, 4.0) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => println!("Error: {:?}", e),
    }
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Add a `multiply` function and chain it with ? operator
2. Create a custom error enum with 3+ variants
3. Write a function that uses ? to call multiple Result-returning functions
4. Compare code with and without ? operator

---

## Example 6: Combining Iterators, Closures, and Error Handling

**What it demonstrates:** Real-world pattern combining multiple idiomatic Rust features.

**The code:**
```rust
#[derive(Debug)]
struct Student {
    name: String,
    grade: f64,
}

#[derive(Debug)]
enum GradeError {
    InvalidGrade,
    NoStudents,
}

fn parse_grade(s: &str) -> Result<f64, GradeError> {
    s.parse::<f64>()
        .map_err(|_| GradeError::InvalidGrade)
        .and_then(|g| {
            if g >= 0.0 && g <= 100.0 {
                Ok(g)
            } else {
                Err(GradeError::InvalidGrade)
            }
        })
}

fn calculate_average(students: &[Student]) -> Result<f64, GradeError> {
    if students.is_empty() {
        return Err(GradeError::NoStudents);
    }

    let sum: f64 = students
        .iter()
        .map(|s| s.grade)
        .sum();

    Ok(sum / students.len() as f64)
}

fn main() {
    let students = vec![
        Student { name: String::from("Alice"), grade: 92.5 },
        Student { name: String::from("Bob"), grade: 78.0 },
        Student { name: String::from("Charlie"), grade: 85.5 },
        Student { name: String::from("Diana"), grade: 95.0 },
    ];

    // Filter high-performers (grade >= 80)
    let honor_roll: Vec<_> = students
        .iter()
        .filter(|s| s.grade >= 80.0)
        .map(|s| &s.name)
        .collect();

    println!("Honor roll: {:?}", honor_roll);

    // Calculate average
    match calculate_average(&students) {
        Ok(avg) => println!("Class average: {:.2}", avg),
        Err(e) => println!("Error: {:?}", e),
    }

    // Process grade strings
    let grade_strings = vec!["92.5", "invalid", "85.0"];

    let results: Vec<_> = grade_strings
        .iter()
        .map(|s| parse_grade(s))
        .collect();

    for (i, result) in results.iter().enumerate() {
        match result {
            Ok(grade) => println!("Grade {}: {:.1}", i, grade),
            Err(e) => println!("Grade {}: Error {:?}", i, e),
        }
    }
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Add a filter to find students with failing grades (< 60)
2. Use `.filter_map()` to parse and filter valid grades in one step
3. Calculate median grade using iterators
4. Chain multiple iterator operations together

---

## Pro Tips for Idiomatic Rust

**Iterator patterns to memorize:**
```rust
// Transform each element
.map(|x| x * 2)

// Filter elements
.filter(|x| x > 5)

// Transform and filter in one step
.filter_map(|x| some_fn(x).ok())

// Get first match
.find(|x| condition(x))

// Aggregate
.sum()
.fold(initial, |acc, x| acc + x)

// Collect into collection
.collect::<Vec<_>>()
```

**Error handling patterns:**
```rust
// Propagate errors up
fn foo() -> Result<T, E> {
    let x = might_fail()?;
    Ok(x)
}

// Provide default on error
let value = might_fail().unwrap_or(default);

// Chain operations
result1.and_then(|x| result2(x))
```

**When to use which smart pointer:**
```rust
Box<T>       // Single owner, heap allocation
Rc<T>        // Multiple owners (single-threaded)
Arc<T>       // Multiple owners (thread-safe)
RefCell<T>   // Interior mutability (single-threaded)
Mutex<T>     // Interior mutability (thread-safe)
```

---

## Next Steps

**After mastering these concepts:**
1. Complete **Lab 13** - Idiomatic Rust Patterns
2. Practice iterator chains in your own code
3. Learn about async/await (advanced topic)
4. Explore concurrency with threads (Week 14)

**Resources:**
- [The Rust Book - Ch 13: Functional Features](https://doc.rust-lang.org/book/ch13-00-functional-features.html)
- [The Rust Book - Ch 15: Smart Pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html)
- [Iterator documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Closure documentation](https://doc.rust-lang.org/book/ch13-01-closures.html)

**The Rust way:** Prefer iterators over loops, use ? for errors, choose the right smart pointer!
