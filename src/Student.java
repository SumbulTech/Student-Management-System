import java.io.Serializable;

/**
 * Student.java
 * 
 * This class EXTENDS Person (Inheritance) and IMPLEMENTS StudentOperations is
 * not needed here — Student is just the data model.
 * 
 * OOP Concepts Demonstrated:
 *  - ENCAPSULATION: All fields are private; access is through getters/setters.
 *  - INHERITANCE:   Extends Person, inheriting id, name, department.
 *  - POLYMORPHISM:  Overrides getDisplayInfo() and toString().
 * 
 * Serializable allows Java to convert this object into bytes and save it to
 * a file — that is how we achieve persistent file storage.
 */
public class Student extends Person implements Serializable {

    // Required for Serializable — keeps file format stable
    private static final long serialVersionUID = 1L;

    // Additional fields specific to a Student (private = Encapsulation)
    private int year;       // Academic year: 1, 2, 3, or 4
    private double marks;   // Marks out of 100

    /**
     * Constructor — creates a fully populated Student object.
     * Calls the parent (Person) constructor using super().
     */
    public Student(String studentId, String name, String department,
                   int year, double marks) {
        super(studentId, name, department);   // Calls Person's constructor
        this.year = year;
        this.marks = marks;
    }

    // --- Getters ---
    public int getYear() {
        return year;
    }

    public double getMarks() {
        return marks;
    }

    // --- Setters ---
    public void setYear(int year) {
        this.year = year;
    }

    public void setMarks(double marks) {
        this.marks = marks;
    }

    /**
     * calculateGrade() — determines a letter grade based on marks.
     * OOP Concept: A behaviour specific to Student.
     */
    public String calculateGrade() {
        if (marks >= 90) return "O  (Outstanding)";
        else if (marks >= 75) return "A+ (Excellent)";
        else if (marks >= 60) return "A  (Very Good)";
        else if (marks >= 50) return "B+ (Good)";
        else if (marks >= 40) return "B  (Average)";
        else                  return "F  (Fail)";
    }

    /**
     * getDisplayInfo() — provides a formatted multi-line student profile.
     * OOP Concept: POLYMORPHISM — overrides the abstract method in Person.
     */
    @Override
    public String getDisplayInfo() {
        return "┌─────────────────────────────────────────┐\n" +
               "│  Student ID  : " + getId()         + "\n" +
               "│  Name        : " + getName()       + "\n" +
               "│  Department  : " + getDepartment() + "\n" +
               "│  Year        : " + year            + "\n" +
               "│  Marks       : " + marks           + "\n" +
               "│  Grade       : " + calculateGrade()+ "\n" +
               "└─────────────────────────────────────────┘";
    }

    /**
     * toString() — compact single-line representation.
     * OOP Concept: POLYMORPHISM — overrides toString() from Object.
     */
    @Override
    public String toString() {
        return String.format("%-12s %-20s %-15s  Year: %d  Marks: %-6.2f  Grade: %s",
                getId(), getName(), getDepartment(), year, marks, calculateGrade());
    }
}
