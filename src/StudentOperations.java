/**
 * StudentOperations.java
 * 
 * This is an INTERFACE (Abstraction).
 * An interface defines a contract — it lists what operations must be available,
 * but does not say HOW they are done. Any class that "implements" this interface
 * must provide the actual code for each method.
 * 
 * OOP Concept Demonstrated: ABSTRACTION
 * We hide the implementation details and only expose the required operations.
 */
public interface StudentOperations {

    // Add a new student to the system
    void addStudent(Student student);

    // Display all students currently stored
    void displayAllStudents();

    // Search for a student by their ID; returns null if not found
    Student searchStudent(String studentId);

    // Update an existing student's details
    boolean updateStudent(String studentId, String name, String department,
                          int year, double marks);

    // Delete a student record by ID
    boolean deleteStudent(String studentId);

    // Get total count of registered students
    int getTotalStudents();
}
