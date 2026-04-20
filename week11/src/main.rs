mod student;
use student::{Student, Grade, CourseGrade, StudentDatabase};

fn main() {
    let mut db = StudentDatabase::new();

    // Create and add students
    let mut alice = Student::new(
        String::from("S001"),
        String::from("Alice Johnson"),
        String::from("alice@example.com"),
    );
    alice.add_grade(CourseGrade::new(
        String::from("IS4010"),
        String::from("App Dev with AI"),
        3,
        Grade::A,
    ));

    let mut bob = Student::new(
        String::from("S002"),
        String::from("Bob Smith"),
        String::from("bob@example.com"),
    );
    bob.add_grade(CourseGrade::new(
        String::from("IS3050"),
        String::from("Database Design"),
        3,
        Grade::B,
    ));

    // Add students to database
    match db.add_student(alice) {
        Ok(()) => println!("Added Alice"),
        Err(e) => println!("Error: {}", e),
    }

    match db.add_student(bob) {
        Ok(()) => println!("Added Bob"),
        Err(e) => println!("Error: {}", e),
    }

    // Database statistics
    println!("\nDatabase Statistics:");
    println!("Total students: {}", db.student_count());
    println!("Average GPA: {:.2}", db.average_gpa());

    // List all students
    println!("\nAll Students:");
    for student in db.list_students() {
        println!("  {} - {} (GPA: {:.2})",
            student.id,
            student.name,
            student.calculate_gpa(),
        );
    }

    // Find specific student
    if let Some(student) = db.find_student("S001") {
        println!("\nFound student: {}", student.name);
        println!("  Email: {}", student.email);
        println!("  Credits: {}", student.credits_earned);
        println!("  GPA: {:.2}", student.calculate_gpa());
    }
}