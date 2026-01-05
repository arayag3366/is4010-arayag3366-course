# Week 12: Generics and Traits - Rust Playground Examples

Try these interactive examples in your browser—no installation needed!

---

## Example 1: Generic Functions

**What it demonstrates:** Writing functions that work with multiple types using generics.

**The code:**
```rust
// Generic function - works with any type T
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

// Generic function with multiple type parameters
fn display_pair<T, U>(first: T, second: U)
where
    T: std::fmt::Display,
    U: std::fmt::Display,
{
    println!("Pair: ({}, {})", first, second);
}

fn main() {
    // Works with integers
    let numbers = vec![34, 50, 25, 100, 65];
    let result = largest(&numbers);
    println!("Largest number: {}", result);

    // Works with characters
    let chars = vec!['y', 'm', 'a', 'q'];
    let result = largest(&chars);
    println!("Largest char: {}", result);

    // Multiple types
    display_pair(42, "hello");
    display_pair(3.14, true);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Write a generic `swap` function that swaps two values of any type
2. Write a generic `min_max` function returning a tuple (min, max)
3. Try calling largest with strings and explain the result
4. Add a generic function that prints any displayable value

---

## Example 2: Generic Structs

**What it demonstrates:** Creating structs that can hold values of any type.

**The code:**
```rust
// Generic struct with one type parameter
struct Point<T> {
    x: T,
    y: T,
}

// Generic struct with multiple type parameters
struct Pair<T, U> {
    first: T,
    second: U,
}

impl<T> Point<T> {
    // Method on generic struct
    fn x(&self) -> &T {
        &self.x
    }
}

// Implementation only for Point<f64>
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

fn main() {
    // Point with integers
    let integer_point = Point { x: 5, y: 10 };
    println!("Integer point: ({}, {})", integer_point.x, integer_point.y);

    // Point with floats
    let float_point = Point { x: 1.5, y: 4.2 };
    println!("Float point: ({}, {})", float_point.x, float_point.y);
    println!("Distance: {:.2}", float_point.distance_from_origin());

    // Pair with different types
    let pair = Pair {
        first: String::from("hello"),
        second: 42,
    };
    println!("Pair: {} and {}", pair.first, pair.second);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a generic `Container<T>` struct that holds a value
2. Add methods `new(value: T)` and `get(&self) -> &T`
3. Create a `Triple<T, U, V>` struct with three different types
4. Try mixing types in Point (x: i32, y: f64) - what happens and why?

---

## Example 3: Trait Definitions

**What it demonstrates:** Defining shared behavior with traits (similar to interfaces).

**The code:**
```rust
// Define a trait
trait Summary {
    fn summarize(&self) -> String;

    // Default implementation
    fn summarize_short(&self) -> String {
        String::from("(Read more...)")
    }
}

struct NewsArticle {
    headline: String,
    content: String,
    author: String,
}

struct Tweet {
    username: String,
    content: String,
    retweets: u32,
}

// Implement trait for NewsArticle
impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{} by {}", self.headline, self.author)
    }

    // Override default implementation
    fn summarize_short(&self) -> String {
        format!("{}...", &self.headline[..20.min(self.headline.len())])
    }
}

// Implement trait for Tweet
impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("@{}: {} ({} retweets)", self.username, self.content, self.retweets)
    }
    // Uses default implementation for summarize_short
}

fn main() {
    let article = NewsArticle {
        headline: String::from("Rust 2.0 Released!"),
        content: String::from("The Rust team announced..."),
        author: String::from("Jane Developer"),
    };

    let tweet = Tweet {
        username: String::from("rustlang"),
        content: String::from("Check out our new features!"),
        retweets: 128,
    };

    println!("Article: {}", article.summarize());
    println!("Article (short): {}", article.summarize_short());
    println!("Tweet: {}", tweet.summarize());
    println!("Tweet (short): {}", tweet.summarize_short());
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a `Describable` trait with a `describe(&self) -> String` method
2. Implement it for two different structs
3. Add a default implementation for `brief_description`
4. Create a trait with multiple required methods

---

## Example 4: Traits as Parameters

**What it demonstrates:** Using traits to accept any type that implements specific behavior.

**The code:**
```rust
use std::fmt::Display;

trait Summary {
    fn summarize(&self) -> String;
}

struct Article {
    title: String,
    content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}: {}", self.title, self.content)
    }
}

impl Display for Article {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Article: {}", self.title)
    }
}

// Function accepting trait (impl Trait syntax)
fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

// Trait bound syntax (equivalent to above)
fn announce<T: Summary>(item: &T) {
    println!("Announcement: {}", item.summarize());
}

// Multiple trait bounds
fn print_and_summarize<T: Summary + Display>(item: &T) {
    println!("Display: {}", item);
    println!("Summary: {}", item.summarize());
}

// Where clause for complex bounds
fn complex_function<T, U>(t: &T, u: &U) -> String
where
    T: Display + Clone,
    U: Summary,
{
    format!("T: {}, U: {}", t, u.summarize())
}

fn main() {
    let article = Article {
        title: String::from("Generics in Rust"),
        content: String::from("Learn about powerful abstractions..."),
    };

    notify(&article);
    announce(&article);
    print_and_summarize(&article);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a function that accepts any type implementing Display
2. Write a function requiring both Clone and Debug traits
3. Use a where clause to make complex trait bounds readable
4. Explain when to use `impl Trait` vs `<T: Trait>`

---

## Example 5: Implementing Display Trait

**What it demonstrates:** Implementing standard library traits to customize type behavior.

**The code:**
```rust
use std::fmt;

#[derive(Debug, Clone)]  // Auto-implement Debug and Clone
struct Point {
    x: i32,
    y: i32,
}

// Manually implement Display trait
impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

struct Person {
    name: String,
    age: u32,
}

impl fmt::Display for Person {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} (age {})", self.name, self.age)
    }
}

impl fmt::Debug for Person {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.debug_struct("Person")
            .field("name", &self.name)
            .field("age", &self.age)
            .finish()
    }
}

fn main() {
    let point = Point { x: 3, y: 4 };

    // Display trait enables {} formatting
    println!("Point (Display): {}", point);

    // Debug trait enables {:?} formatting
    println!("Point (Debug): {:?}", point);

    // Clone trait enables .clone()
    let point2 = point.clone();
    println!("Cloned point: {}", point2);

    let person = Person {
        name: String::from("Alice"),
        age: 30,
    };

    println!("Person (Display): {}", person);
    println!("Person (Debug): {:?}", person);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a `Temperature` struct and implement Display showing "X°C" or "X°F"
2. Implement Debug to show internal representation
3. Derive Clone and test that it works
4. Create a struct with a custom Display format

---

## Example 6: Generic Stack Data Structure

**What it demonstrates:** Building a generic data structure (similar to Lab 12).

**The code:**
```rust
#[derive(Debug)]
struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    // Constructor
    fn new() -> Self {
        Stack { items: Vec::new() }
    }

    // Push item onto stack
    fn push(&mut self, item: T) {
        self.items.push(item);
    }

    // Pop item from stack
    fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }

    // Peek at top item without removing
    fn peek(&self) -> Option<&T> {
        self.items.last()
    }

    // Check if stack is empty
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }

    // Get stack size
    fn len(&self) -> usize {
        self.items.len()
    }
}

fn main() {
    // Stack of integers
    let mut int_stack = Stack::new();
    int_stack.push(1);
    int_stack.push(2);
    int_stack.push(3);

    println!("Int stack size: {}", int_stack.len());
    println!("Top item: {:?}", int_stack.peek());
    println!("Popped: {:?}", int_stack.pop());

    // Stack of strings
    let mut string_stack = Stack::new();
    string_stack.push(String::from("hello"));
    string_stack.push(String::from("world"));

    while let Some(item) = string_stack.pop() {
        println!("Popped: {}", item);
    }

    println!("Is empty? {}", string_stack.is_empty());
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Add a `clear()` method that empties the stack
2. Implement Display trait to show the stack contents
3. Create a Queue<T> struct with enqueue/dequeue methods
4. Add trait bounds to restrict what types can be stored

---

## Pro Tips for Generics and Traits

**Choosing between impl Trait and <T: Trait>:**
```rust
// Simple cases - use impl Trait
fn simple(item: &impl Display) { }

// Multiple parameters with same trait - use generic type
fn complex<T: Display>(a: &T, b: &T) { }

// Complex bounds - use where clause
fn very_complex<T, U>(t: &T, u: &U)
where
    T: Display + Clone,
    U: Debug + Default,
{ }
```

**Common derivable traits:**
```rust
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
struct MyType { /* fields */ }
```

**Trait bounds restrict what T can be:**
```rust
// T must implement PartialOrd to compare
fn largest<T: PartialOrd>(list: &[T]) -> &T { /* ... */ }
```

**Zero-cost abstractions:**
- Generics are monomorphized at compile time
- No runtime overhead compared to writing separate functions
- Type safety without performance cost!

---

## Next Steps

**After mastering these concepts:**
1. Complete **Lab 12** - Generic Stack Implementation
2. Practice implementing standard library traits
3. Learn about advanced trait features (Week 13)
4. Explore trait objects and dynamic dispatch

**Resources:**
- [The Rust Book - Chapter 10: Generics](https://doc.rust-lang.org/book/ch10-00-generics.html)
- [The Rust Book - Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Rust by Example - Generics](https://doc.rust-lang.org/rust-by-example/generics.html)
- [Tour of Rust's Standard Library Traits](https://github.com/pretzelhammer/rust-blog/blob/master/posts/tour-of-rusts-standard-library-traits.md)

**The power of generics:** Write once, use with any type - safely and efficiently!
