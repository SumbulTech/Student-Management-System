import java.io.*;
import java.util.ArrayList;

/**
 * StudentManager.java
 * 
 * This class IMPLEMENTS the StudentOperations interface.
 * It manages the list of students and handles all file I/O.
 * 
 * OOP Concepts Demonstrated:
 *  - ENCAPSULATION:  The ArrayList is private; outside code uses methods only.
 *  - ABSTRACTION:    Implements the StudentOperations interface.
 *  - EXCEPTION HANDLING: All file operations are wrapped in try-catch.
 */
public class StudentManager implements StudentOperations {

    // The file where student records are saved between sessions
    private static final String FILE_NAME = "students.dat";

    // Internal list that holds all Student objects in memory
    private ArrayList<Student> studentList;

    /**
     * Constructor — loads any previously saved students from the file.
     * If no file exists yet (first run), starts with an empty list.
     */
    public StudentManager() {
        studentList = loadFromFile();
    }

    // =========================================================
    //  ADD
    // =========================================================

    /**
     * Adds a new student to the list, preventing duplicate IDs.
     * Saves to file immediately after adding.
     */
    @Override
    public void addStudent(Student student) {
        // Check for duplicate ID (case-insensitive)
        if (searchStudent(student.getId()) != null) {
            System.out.println("  [!] A student with ID '" + student.getId()
                    + "' already exists. Duplicate IDs are not allowed.");
            return;
        }
        studentList.add(student);
        saveToFile();
        System.out.println("  [✔] Student added successfully!");
    }

    // =========================================================
    //  DISPLAY ALL
    // =========================================================

    /**
     * Prints all students in a formatted table.
     */
    @Override
    public void displayAllStudents() {
        if (studentList.isEmpty()) {
            System.out.println("  [!] No students registered yet.");
            return;
        }

        System.out.println("\n  Total registered students: " + studentList.size());
        System.out.println("  " + "─".repeat(85));
        System.out.printf("  %-12s %-20s %-15s %-6s %-8s %s%n",
                "Student ID", "Name", "Department", "Year", "Marks", "Grade");
        System.out.println("  " + "─".repeat(85));

        for (Student s : studentList) {
            System.out.println("  " + s.toString());
        }
        System.out.println("  " + "─".repeat(85));
    }

    // =========================================================
    //  SEARCH
    // =========================================================

    /**
     * Returns the Student whose ID matches, or null if not found.
     * OOP Concept: Linear search on an ArrayList of objects.
     */
    @Override
    public Student searchStudent(String studentId) {
        for (Student s : studentList) {
            if (s.getId().equalsIgnoreCase(studentId)) {
                return s;
            }
        }
        return null;
    }

    // =========================================================
    //  UPDATE
    // =========================================================

    /**
     * Updates all fields of an existing student.
     * Returns true if the student was found and updated, false otherwise.
     */
    @Override
    public boolean updateStudent(String studentId, String name,
                                  String department, int year, double marks) {
        Student s = searchStudent(studentId);
        if (s == null) {
            return false;
        }
        s.setName(name);
        s.setDepartment(department);
        s.setYear(year);
        s.setMarks(marks);
        saveToFile();
        return true;
    }

    // =========================================================
    //  DELETE
    // =========================================================

    /**
     * Removes a student by ID.
     * Returns true if found and deleted, false otherwise.
     */
    @Override
    public boolean deleteStudent(String studentId) {
        Student s = searchStudent(studentId);
        if (s == null) {
            return false;
        }
        studentList.remove(s);
        saveToFile();
        return true;
    }

    // =========================================================
    //  COUNT
    // =========================================================

    @Override
    public int getTotalStudents() {
        return studentList.size();
    }

    // =========================================================
    //  FILE HANDLING — SAVE
    // =========================================================

    /**
     * Serializes the entire ArrayList to a binary file.
     * OOP + File Handling: ObjectOutputStream writes Java objects as bytes.
     */
    private void saveToFile() {
        try (ObjectOutputStream oos =
                     new ObjectOutputStream(new FileOutputStream(FILE_NAME))) {
            oos.writeObject(studentList);
        } catch (IOException e) {
            System.out.println("  [!] Error saving data: " + e.getMessage());
        }
    }

    // =========================================================
    //  FILE HANDLING — LOAD
    // =========================================================

    /**
     * Deserializes the ArrayList from the binary file.
     * If the file does not exist (first run), returns an empty list.
     * 
     * OOP + Exception Handling:
     *   - FileNotFoundException  → file doesn't exist yet (normal on first run)
     *   - IOException            → disk/permission error
     *   - ClassNotFoundException → file is corrupted or from a different version
     */
    @SuppressWarnings("unchecked")
    private ArrayList<Student> loadFromFile() {
        File file = new File(FILE_NAME);

        // First run — no file yet, that's perfectly fine
        if (!file.exists()) {
            return new ArrayList<>();
        }

        try (ObjectInputStream ois =
                     new ObjectInputStream(new FileInputStream(FILE_NAME))) {
            return (ArrayList<Student>) ois.readObject();
        } catch (FileNotFoundException e) {
            // File vanished between the exists() check and open — still fine
            return new ArrayList<>();
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("  [!] Could not load saved data: "
                    + e.getMessage()
                    + "\n  Starting with an empty student list.");
            return new ArrayList<>();
        }
    }
}
