/**
 * StudentManagementSystem.java
 * 
 * MAIN CLASS — Entry point of the application.
 * 
 * This is a menu-driven console application that lets the user:
 *   1. Add a new student
 *   2. Display all students
 *   3. Search for a student
 *   4. Update student details
 *   5. Delete a student
 *   6. View grade of a specific student
 *   7. Display total number of students
 *   8. Exit
 * 
 * All OOP concepts (Encapsulation, Inheritance, Polymorphism, Abstraction,
 * Exception Handling, File Handling) come together here.
 */
public class StudentManagementSystem {

    // ─────────────────────────────────────────────
    //  PROGRAM ENTRY POINT
    // ─────────────────────────────────────────────
    public static void main(String[] args) {

        // Create the manager (loads saved data from file automatically)
        StudentManager manager = new StudentManager();

        // Create the input helper
        InputValidator input = new InputValidator();

        printWelcome();

        boolean running = true;

        while (running) {
            printMenu();
            int choice = input.readInt("  Enter your choice: ", 1, 8);

            switch (choice) {

                case 1 -> handleAddStudent(manager, input);
                case 2 -> handleDisplayAll(manager);
                case 3 -> handleSearch(manager, input);
                case 4 -> handleUpdate(manager, input);
                case 5 -> handleDelete(manager, input);
                case 6 -> handleGrade(manager, input);
                case 7 -> handleCount(manager);
                case 8 -> {
                    System.out.println("\n  Thank you for using the Student Management System.");
                    System.out.println("  Goodbye!\n");
                    running = false;
                }
            }
        }

        input.close();
    }

    // ─────────────────────────────────────────────
    //  MENU HANDLERS
    // ─────────────────────────────────────────────

    /** Collects student details and adds a new student. */
    private static void handleAddStudent(StudentManager manager, InputValidator input) {
        System.out.println("\n  ══════════ ADD NEW STUDENT ══════════");

        String id   = input.readString("  Student ID   : ");
        String name = input.readString("  Full Name    : ");
        String dept = input.readString("  Department   : ");
        int    year = input.readInt   ("  Year (1-4)   : ", 1, 4);
        double marks = input.readDouble("  Marks (0-100): ", 0.0, 100.0);

        // Create a Student object (uses Inheritance from Person)
        Student student = new Student(id, name, dept, year, marks);
        manager.addStudent(student);   // Calls the interface method
    }

    /** Displays the full student table. */
    private static void handleDisplayAll(StudentManager manager) {
        System.out.println("\n  ══════════ ALL STUDENTS ══════════");
        manager.displayAllStudents();
    }

    /** Searches for one student and shows their detailed profile. */
    private static void handleSearch(StudentManager manager, InputValidator input) {
        System.out.println("\n  ══════════ SEARCH STUDENT ══════════");
        String id = input.readString("  Enter Student ID to search: ");
        Student found = manager.searchStudent(id);
        if (found != null) {
            System.out.println("\n" + found.getDisplayInfo()); // Polymorphism
        } else {
            System.out.println("  [!] No student found with ID: " + id);
        }
    }

    /** Updates all details of an existing student. */
    private static void handleUpdate(StudentManager manager, InputValidator input) {
        System.out.println("\n  ══════════ UPDATE STUDENT ══════════");
        String id = input.readString("  Enter Student ID to update: ");

        // Check the student exists before asking for new values
        if (manager.searchStudent(id) == null) {
            System.out.println("  [!] No student found with ID: " + id);
            return;
        }

        System.out.println("  Student found. Enter new details (press Enter to keep existing):");
        System.out.println("  (Tip: just type the new value for each field)");

        String name  = input.readString("  New Full Name    : ");
        String dept  = input.readString("  New Department   : ");
        int    year  = input.readInt   ("  New Year (1-4)   : ", 1, 4);
        double marks = input.readDouble("  New Marks (0-100): ", 0.0, 100.0);

        boolean updated = manager.updateStudent(id, name, dept, year, marks);
        if (updated) {
            System.out.println("  [✔] Student updated successfully!");
        } else {
            System.out.println("  [!] Update failed. Please try again.");
        }
    }

    /** Deletes a student after confirmation. */
    private static void handleDelete(StudentManager manager, InputValidator input) {
        System.out.println("\n  ══════════ DELETE STUDENT ══════════");
        String id = input.readString("  Enter Student ID to delete: ");

        Student found = manager.searchStudent(id);
        if (found == null) {
            System.out.println("  [!] No student found with ID: " + id);
            return;
        }

        System.out.println("  Found: " + found.getName()
                + " (" + found.getDepartment() + ")");

        boolean confirm = input.readConfirmation("  Are you sure you want to delete this record?");
        if (confirm) {
            manager.deleteStudent(id);
            System.out.println("  [✔] Student record deleted successfully.");
        } else {
            System.out.println("  [i] Deletion cancelled.");
        }
    }

    /** Shows the grade for a specific student. */
    private static void handleGrade(StudentManager manager, InputValidator input) {
        System.out.println("\n  ══════════ STUDENT GRADE ══════════");
        String id = input.readString("  Enter Student ID: ");
        Student found = manager.searchStudent(id);
        if (found != null) {
            System.out.println("  Student  : " + found.getName());
            System.out.println("  Marks    : " + found.getMarks());
            System.out.println("  Grade    : " + found.calculateGrade());
        } else {
            System.out.println("  [!] No student found with ID: " + id);
        }
    }

    /** Prints total registered student count. */
    private static void handleCount(StudentManager manager) {
        System.out.println("\n  ══════════ STUDENT COUNT ══════════");
        System.out.println("  Total registered students: "
                + manager.getTotalStudents());
    }

    // ─────────────────────────────────────────────
    //  UI HELPERS
    // ─────────────────────────────────────────────

    private static void printWelcome() {
        System.out.println();
        System.out.println("  ╔══════════════════════════════════════════════╗");
        System.out.println("  ║      STUDENT MANAGEMENT SYSTEM               ║");
        System.out.println("  ║      B V C College of Engineering            ║");
        System.out.println("  ║      CSE – AI & ML Department                ║");
        System.out.println("  ╚══════════════════════════════════════════════╝");
        System.out.println();
    }

    private static void printMenu() {
        System.out.println();
        System.out.println("  ┌─────────────────────────────────┐");
        System.out.println("  │          MAIN MENU              │");
        System.out.println("  ├─────────────────────────────────┤");
        System.out.println("  │  1. Add New Student             │");
        System.out.println("  │  2. Display All Students        │");
        System.out.println("  │  3. Search Student              │");
        System.out.println("  │  4. Update Student Details      │");
        System.out.println("  │  5. Delete Student Record       │");
        System.out.println("  │  6. View Student Grade          │");
        System.out.println("  │  7. Total Number of Students    │");
        System.out.println("  │  8. Exit                        │");
        System.out.println("  └─────────────────────────────────┘");
    }
}
