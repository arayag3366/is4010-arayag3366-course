# Week 11: Structuring Code and Data - Rust Playground Examples

Try these interactive examples in your browser—no installation needed!

---

## Example 1: Defining and Using Structs

**What it demonstrates:** Creating custom data types with named fields using structs.

**The code:**
```rust
// Define a struct to represent a student
struct Student {
    name: String,
    id: u32,
    gpa: f64,
    is_enrolled: bool,
}

fn main() {
    // Create an instance
    let student1 = Student {
        name: String::from("Alice Smith"),
        id: 12345,
        gpa: 3.8,
        is_enrolled: true,
    };

    // Access fields with dot notation
    println!("Name: {}", student1.name);
    println!("ID: {}", student1.id);
    println!("GPA: {:.2}", student1.gpa);
    println!("Enrolled: {}", student1.is_enrolled);

    // Mutable struct - can change fields
    let mut student2 = Student {
        name: String::from("Bob Jones"),
        id: 67890,
        gpa: 3.5,
        is_enrolled: true,
    };

    // Update a field
    student2.gpa = 3.7;
    println!("\n{}'s new GPA: {:.2}", student2.name, student2.gpa);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a `Book` struct with fields: title, author, pages, is_fiction
2. Instantiate two books
3. Make one mutable and change the number of pages
4. Print all book information

---

## Example 2: Struct Methods with `impl` Blocks

**What it demonstrates:** Adding behavior to structs using implementation blocks.

**The code:**
```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Method - takes &self as first parameter
    fn area(&self) -> u32 {
        self.width * self.height
    }

    // Method that borrows mutably
    fn scale(&mut self, factor: u32) {
        self.width *= factor;
        self.height *= factor;
    }

    // Associated function (like a constructor) - no self
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }

    // Method with additional parameters
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let mut rect = Rectangle { width: 30, height: 50 };

    println!("Area: {} square pixels", rect.area());

    // Call method with &mut self
    rect.scale(2);
    println!("After scaling: {}x{}", rect.width, rect.height);

    // Call associated function with ::
    let sq = Rectangle::square(25);
    println!("Square: {}x{}", sq.width, sq.height);

    // Compare rectangles
    println!("Can rect hold square? {}", rect.can_hold(&sq));
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Add a `perimeter` method to Rectangle
2. Add an `is_square` method that returns true if width == height
3. Create a `Circle` struct with methods for area and circumference
4. Add a constructor method `new(radius: f64) -> Circle`

---

## Example 3: Enums for Modeling Choices

**What it demonstrates:** Using enums to represent mutually exclusive states with associated data.

**The code:**
```rust
// Enum with different variants holding different types of data
enum WebEvent {
    PageLoad,                      // No data
    PageUnload,                    // No data
    KeyPress(char),                // Holds a character
    Click { x: i32, y: i32 },     // Holds named fields
    Paste(String),                 // Holds a String
}

fn inspect_event(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("Page loaded"),
        WebEvent::PageUnload => println!("Page unloaded"),
        WebEvent::KeyPress(c) => println!("Key pressed: '{}'", c),
        WebEvent::Click { x, y } => println!("Clicked at x={}, y={}", x, y),
        WebEvent::Paste(text) => println!("Pasted text: {}", text),
    }
}

fn main() {
    let load = WebEvent::PageLoad;
    let press = WebEvent::KeyPress('x');
    let click = WebEvent::Click { x: 20, y: 80 };
    let paste = WebEvent::Paste(String::from("Hello!"));

    inspect_event(load);
    inspect_event(press);
    inspect_event(click);
    inspect_event(paste);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a `Message` enum with variants: Quit, Move{x,y}, Write(String), ChangeColor(i32,i32,i32)
2. Write a function that processes each message type
3. Create instances of all four variants and process them
4. Add a new variant and handle it in your match statement

---

## Example 4: Pattern Matching with `match`

**What it demonstrates:** Using `match` expressions to exhaustively handle enum variants.

**The code:**
```rust
enum TrafficLight {
    Red,
    Yellow,
    Green,
}

impl TrafficLight {
    fn duration(&self) -> u32 {
        match self {
            TrafficLight::Red => 60,
            TrafficLight::Yellow => 10,
            TrafficLight::Green => 45,
        }
    }

    fn action(&self) -> &str {
        match self {
            TrafficLight::Red => "Stop!",
            TrafficLight::Yellow => "Prepare to stop",
            TrafficLight::Green => "Go!",
        }
    }
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(String), // Quarter variant holds state name
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("Quarter from {}!", state);
            25
        }
    }
}

fn main() {
    let light = TrafficLight::Red;
    println!("{} (wait {} seconds)", light.action(), light.duration());

    let coin = Coin::Quarter(String::from("Alaska"));
    println!("Value: {} cents", value_in_cents(coin));
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a `Direction` enum (North, South, East, West)
2. Write a function that returns the opposite direction
3. Create a `Temperature` enum that can be Celsius(f64) or Fahrenheit(f64)
4. Write a function that converts any Temperature to Celsius

---

## Example 5: Option<T> - Handling Absence

**What it demonstrates:** Using `Option<T>` to represent values that might not exist (Rust's null replacement).

**The code:**
```rust
fn divide(numerator: f64, denominator: f64) -> Option<f64> {
    if denominator == 0.0 {
        None  // Return None for division by zero
    } else {
        Some(numerator / denominator)  // Return Some with result
    }
}

fn find_item(items: &[&str], search: &str) -> Option<usize> {
    for (index, &item) in items.iter().enumerate() {
        if item == search {
            return Some(index);
        }
    }
    None  // Not found
}

fn main() {
    // Using match to handle Option
    match divide(10.0, 2.0) {
        Some(result) => println!("Result: {}", result),
        None => println!("Cannot divide by zero!"),
    }

    match divide(10.0, 0.0) {
        Some(result) => println!("Result: {}", result),
        None => println!("Cannot divide by zero!"),
    }

    // Using if let for cleaner code when only interested in Some
    let items = ["apple", "banana", "cherry"];

    if let Some(index) = find_item(&items, "banana") {
        println!("Found banana at index {}", index);
    } else {
        println!("Item not found");
    }

    // unwrap_or provides a default value
    let result = divide(10.0, 0.0).unwrap_or(0.0);
    println!("Result with default: {}", result);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Write a function that finds the first even number in a Vec<i32>, returning Option<i32>
2. Write a function that gets the nth element from a slice, returning Option<T>
3. Use `match`, `if let`, and `unwrap_or` to handle the results differently
4. Explain why Option is better than using null

---

## Example 6: Result<T, E> - Recoverable Errors

**What it demonstrates:** Using `Result<T, E>` for operations that can fail with specific error information.

**The code:**
```rust
#[derive(Debug)]
enum MathError {
    DivisionByZero,
    NegativeSquareRoot,
}

fn safe_divide(numerator: f64, denominator: f64) -> Result<f64, MathError> {
    if denominator == 0.0 {
        Err(MathError::DivisionByZero)
    } else {
        Ok(numerator / denominator)
    }
}

fn square_root(number: f64) -> Result<f64, MathError> {
    if number < 0.0 {
        Err(MathError::NegativeSquareRoot)
    } else {
        Ok(number.sqrt())
    }
}

fn main() {
    // Handle Result with match
    match safe_divide(10.0, 2.0) {
        Ok(result) => println!("10 / 2 = {}", result),
        Err(e) => println!("Error: {:?}", e),
    }

    match safe_divide(10.0, 0.0) {
        Ok(result) => println!("Result: {}", result),
        Err(MathError::DivisionByZero) => println!("Cannot divide by zero!"),
        Err(e) => println!("Other error: {:?}", e),
    }

    // Chain operations that might fail
    let result = safe_divide(20.0, 4.0)
        .and_then(|x| square_root(x));

    match result {
        Ok(val) => println!("sqrt(20/4) = {}", val),
        Err(e) => println!("Error in chain: {:?}", e),
    }

    // unwrap_or_else with custom error handling
    let value = square_root(-4.0).unwrap_or_else(|e| {
        println!("Handling error: {:?}", e);
        0.0  // Default value
    });
    println!("Value: {}", value);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a `ParseError` enum with variants for EmptyString and InvalidFormat
2. Write a function that parses a string to an integer, returning Result<i32, ParseError>
3. Use `and_then` to chain two Result-returning operations
4. Compare error handling with Result vs panicking with unwrap()

---

## Pro Tips for Structs, Enums, and Error Handling

**When to use struct vs enum:**
```rust
// Struct - represents data that has ALL these fields
struct Person { name: String, age: u32 }

// Enum - represents data that is ONE OF these variants
enum Status { Active, Inactive, Pending }
```

**Pattern matching is exhaustive:**
```rust
// ✅ Compiler ensures you handle all cases
match coin {
    Coin::Penny => 1,
    Coin::Nickel => 5,
    // Forgetting Dime or Quarter causes compile error!
}
```

**Option vs Result:**
- `Option<T>`: Value might not exist (find, get, parse)
- `Result<T, E>`: Operation might fail with specific error (I/O, validation)

**Derive useful traits:**
```rust
#[derive(Debug, Clone, PartialEq)]  // Auto-implement common traits
struct Point { x: i32, y: i32 }
```

---

## Next Steps

**After mastering these concepts:**
1. Complete **Lab 11** - Student Management System
2. Practice modeling real-world domains with structs and enums
3. Learn about generics and traits (Week 12)
4. Explore advanced error handling patterns

**Resources:**
- [The Rust Book - Chapter 5: Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [The Rust Book - Chapter 6: Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [The Rust Book - Chapter 9: Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [Rust by Example - Custom Types](https://doc.rust-lang.org/rust-by-example/custom_types.html)

**The key insight:** Rust's type system lets you make illegal states unrepresentable!
