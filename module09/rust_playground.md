# Week 09: Welcome to Rust - Rust Playground Examples

Try these interactive examples in your browser—no installation needed!

---

## Example 1: Hello, Rust!

**What it demonstrates:** Your first Rust program using the `println!` macro and basic syntax.

**The code:**
```rust
fn main() {
    println!("Hello, Rust!");
    println!("Welcome to systems programming!");

    // Variables store values
    let language = "Rust";
    let year = 2015;

    println!("{} was first released in {}", language, year);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:** Add three more `println!` statements that print:
- Your name
- Your favorite programming language
- What you're excited to learn about Rust

---

## Example 2: Variables and Mutability

**What it demonstrates:** The difference between `let` (immutable) and `let mut` (mutable) variables.

**The code:**
```rust
fn main() {
    // Immutable by default - this is Rust's philosophy!
    let x = 5;
    println!("x = {}", x);

    // This would cause an error:
    // x = 6;  // ❌ ERROR: cannot assign twice to immutable variable

    // Use 'mut' keyword to allow changes
    let mut y = 10;
    println!("y = {}", y);

    y = 15;  // ✅ This works because y is mutable
    println!("y is now {}", y);

    // Constants are ALWAYS immutable and require type annotation
    const MAX_POINTS: u32 = 100_000;
    println!("Max points: {}", MAX_POINTS);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Try uncommenting the `x = 6;` line to see the compiler error
2. Create a mutable variable `count` starting at 0, then increment it three times by 1
3. Create a constant for PI with value 3.14159

---

## Example 3: Basic Data Types

**What it demonstrates:** Rust's scalar types (integers, floats, booleans, characters).

**The code:**
```rust
fn main() {
    // Integers (default is i32)
    let age: i32 = 25;
    let temperature: i8 = -15;  // Small signed integer
    let population: u64 = 8_000_000_000;  // Large unsigned integer

    println!("Age: {}, Temperature: {}°C, Population: {}", age, temperature, population);

    // Floating-point numbers (default is f64)
    let pi: f64 = 3.14159;
    let price: f32 = 19.99;

    println!("Pi: {:.2}, Price: ${:.2}", pi, price);

    // Booleans
    let is_learning: bool = true;
    let is_expert: bool = false;

    println!("Learning? {}, Expert? {}", is_learning, is_expert);

    // Characters (single Unicode character, use single quotes!)
    let letter: char = 'R';
    let emoji: char = '🦀';  // Ferris the crab - Rust's mascot!

    println!("Letter: {}, Mascot: {}", letter, emoji);
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Declare your height as a float in meters
2. Create a boolean for "is_raining" and set it appropriately
3. Store your favorite emoji in a char variable
4. Print all three with descriptive messages

---

## Example 4: Tuples and Arrays

**What it demonstrates:** Compound types that group multiple values together.

**The code:**
```rust
fn main() {
    // Tuples - fixed size, different types allowed
    let person: (String, i32, bool) = (String::from("Alice"), 30, true);

    // Access tuple elements by index
    println!("Name: {}", person.0);
    println!("Age: {}", person.1);
    println!("Active: {}", person.2);

    // Destructure tuple into individual variables
    let (name, age, active) = person;
    println!("\nDestructured: {} is {} years old, active: {}", name, age, active);

    // Arrays - fixed size, same type required
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    println!("\nFirst number: {}", numbers[0]);
    println!("Last number: {}", numbers[4]);

    // Create array with repeated value
    let zeros = [0; 10];  // Ten zeros
    println!("Array length: {}", zeros.len());

    // Accessing with indices
    for i in 0..numbers.len() {
        println!("numbers[{}] = {}", i, numbers[i]);
    }
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Create a tuple representing a book: (title, author, pages, is_fiction)
2. Create an array of your 5 favorite numbers
3. Use destructuring to extract the book's title and author
4. Print the sum of your favorite numbers

---

## Example 5: Functions with Type Annotations

**What it demonstrates:** Defining functions with parameters and return values.

**The code:**
```rust
fn main() {
    // Call functions
    greet("World");

    let sum = add(5, 7);
    println!("5 + 7 = {}", sum);

    let area = calculate_rectangle_area(10.5, 6.0);
    println!("Rectangle area: {:.2} square units", area);

    // Functions can return tuples
    let (min, max) = min_max(42, 17);
    println!("Min: {}, Max: {}", min, max);
}

// Function with no return value
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

// Function returning a value (explicit return type)
fn add(a: i32, b: i32) -> i32 {
    a + b  // No semicolon = return value (expression)
    // Same as: return a + b;
}

// Function with floating-point parameters and return
fn calculate_rectangle_area(width: f64, height: f64) -> f64 {
    width * height
}

// Function returning a tuple
fn min_max(a: i32, b: i32) -> (i32, i32) {
    if a < b {
        (a, b)  // a is min, b is max
    } else {
        (b, a)  // b is min, a is max
    }
}
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Write a `multiply` function that takes two i32 values and returns their product
2. Write a `fahrenheit_to_celsius` function that converts temperature (hint: formula is (f - 32) * 5/9)
3. Write a function that takes three integers and returns them sorted in a tuple (small, medium, large)
4. Call all your functions from main() and print the results

---

## Example 6: Function Returning a Value

**What it demonstrates:** Expression-based return values (no semicolon means return).

**The code:**
```rust
fn main() {
    let result1 = square(5);
    let result2 = cube(3);
    let result3 = is_even(10);

    println!("5² = {}", result1);
    println!("3³ = {}", result2);
    println!("Is 10 even? {}", result3);

    // Demonstrate statement vs expression
    let value = {
        let x = 10;
        let y = 20;
        x + y  // No semicolon - this is an expression that returns
    };
    println!("Value from block: {}", value);
}

// Return value without 'return' keyword
fn square(n: i32) -> i32 {
    n * n  // Expression - no semicolon!
}

fn cube(n: i32) -> i32 {
    n * n * n
}

// Return a boolean
fn is_even(n: i32) -> bool {
    n % 2 == 0
}

// ⚠️ Common mistake - adding semicolon changes meaning!
// fn broken_square(n: i32) -> i32 {
//     n * n;  // ❌ Semicolon makes this a statement, not expression
//             // Returns () (unit type), not i32!
// }
```

**Try it:** Copy this code to [https://play.rust-lang.org/](https://play.rust-lang.org/) and click "Run"

**Challenge:**
1. Uncomment the `broken_square` function and try to compile - read the error message!
2. Write a `double` function that returns n * 2
3. Write an `is_positive` function that returns true if n > 0
4. Write a function that returns the absolute value of a number (hint: use if/else)

---

## Pro Tips for the Playground

**Sharing your work:**
- Click the "Share" button at the top
- Copy the generated link
- This link saves your code permanently

**Viewing compiler output:**
- Errors show in red at the bottom
- Warnings show in yellow
- Read them carefully - Rust's error messages are incredibly helpful!

**Trying different Rust editions:**
- Top right dropdown lets you select Rust edition (2021 is latest)
- For this course, always use edition 2021

**Using the formatting tool:**
- Click "Tools" → "Rustfmt" to auto-format your code
- This follows Rust community style guidelines

---

## Next Steps

After mastering these Playground examples:

1. **Install Rust locally** following the [SETUP_GUIDE.md](../../resources/SETUP_GUIDE.md)
2. **Create your first Cargo project** with `cargo new`
3. **Complete Lab 09** to practice these concepts with testing
4. **Move on to Week 10** to learn ownership and borrowing

**Resources:**
- [The Rust Programming Language Book - Chapter 3](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Rustlings](https://github.com/rust-lang/rustlings/) - Small exercises

**Keep experimenting!** The Playground is perfect for testing ideas before putting them in your projects.
