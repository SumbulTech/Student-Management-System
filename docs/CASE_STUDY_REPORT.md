# CASE STUDY REPORT

---

**Title:** Student Management System Using Java

**Subject:** Object-Oriented Programming Through Java Laboratory

**Department:** Computer Science and Engineering (AI & ML)

**Institution:** B V C College of Engineering

**Submission Date:** 26 October 2026

---

---

## 1. COVER PAGE

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│           B V C COLLEGE OF ENGINEERING                          │
│                                                                  │
│     Department of Computer Science & Engineering (AI & ML)      │
│                                                                  │
│    ──────────────────────────────────────────────────────────   │
│                                                                  │
│         OBJECT-ORIENTED PROGRAMMING THROUGH JAVA                │
│                    LABORATORY                                    │
│                                                                  │
│    ──────────────────────────────────────────────────────────   │
│                                                                  │
│              CASE STUDY REPORT                                   │
│                                                                  │
│         STUDENT MANAGEMENT SYSTEM USING JAVA                    │
│                                                                  │
│    ──────────────────────────────────────────────────────────   │
│                                                                  │
│    Submitted By : [Your Name]                                   │
│    Roll No.     : [Your Roll Number]                            │
│    Section      : [Your Section]                                │
│    Semester     : [Current Semester]                            │
│                                                                  │
│    Submitted To : [Faculty Name]                                │
│    Date         : 26 October 2026                               │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. ABSTRACT

This case study presents the design and implementation of a **Student Management
System** developed using Core Java. The system is a console-based application
that allows users to add, view, search, update, and delete student records.
It uses Object-Oriented Programming (OOP) principles — Encapsulation,
Inheritance, Polymorphism, and Abstraction — to structure the codebase cleanly
and maintainably.

Student data is persisted to a binary file using Java's serialization mechanism,
ensuring that records survive across program sessions. Input validation and
exception handling prevent crashes from invalid user input. The project
demonstrates practical application of core OOP and Java file handling concepts
in a real-world scenario.

---

## 3. INTRODUCTION

Managing student information is a fundamental administrative task in any
educational institution. Traditionally this was done using paper registers or
simple spreadsheets — both of which are difficult to search, update, or
maintain at scale. A software-based system offers faster operations, reduced
errors, and permanent structured storage.

Java is a widely-used, platform-independent object-oriented language that
provides rich support for file handling, exception management, and data
structures. This project uses Java to build a practical, menu-driven Student
Management System that any user can operate from a command-line terminal
without requiring internet access, a database server, or paid tools.

---

## 4. PROBLEM STATEMENT

Educational institutions maintain large volumes of student data: names, IDs,
departments, years of study, and academic performance. Managing this data
manually is error-prone and slow. The specific problems addressed by this
project are:

1. No structured mechanism to add and store student records.
2. Difficulty searching for a specific student among hundreds of records.
3. No automated grade calculation from raw marks.
4. Records are lost when the program is closed (no persistence).
5. Errors from invalid input (e.g., marks > 100) can crash naive programs.
6. Duplicate student IDs create confusion in records.

---

## 5. OBJECTIVES

1. Build a functional Student Management System using Core Java.
2. Implement all four OOP pillars: Encapsulation, Inheritance, Polymorphism,
   and Abstraction.
3. Allow CRUD operations: Create, Read, Update, Delete on student records.
4. Automatically calculate student grades based on marks.
5. Persist all records to a file so data is retained after the program closes.
6. Validate all user inputs and handle exceptions gracefully.
7. Prevent duplicate student IDs in the system.
8. Keep the codebase modular, readable, and beginner-friendly.

---

## 6. EXISTING SYSTEM AND ITS LIMITATIONS

### Existing Systems

- **Paper registers**: Student data written in physical books.
- **MS Excel spreadsheets**: Data stored in rows and columns.
- **Basic text files**: Data saved as plain text without structure.

### Limitations of Existing Systems

| Limitation               | Paper Register | Excel Sheet  |
|--------------------------|---------------|--------------|
| Fast search              | ✗ (Manual)   | Partial      |
| Automated grade calc     | ✗            | Partial      |
| Duplicate ID prevention  | ✗            | ✗           |
| Input validation         | ✗            | ✗           |
| Platform independent     | ✗            | ✗ (paid)    |
| Programmatic access      | ✗            | ✗           |
| No external dependency   | ✓            | ✗           |

---

## 7. PROPOSED SYSTEM

The proposed system is a **Java-based console application** that:

- Provides a numbered menu for all operations.
- Validates every input before accepting it.
- Stores all records in a binary `.dat` file using Java Serialization.
- Loads saved records automatically every time the program starts.
- Calculates grades in real time based on marks entered.
- Prevents duplicate student IDs at the point of entry.
- Uses OOP principles to keep the code modular and extensible.

### System Features

| Feature                        | Supported |
|-------------------------------|-----------|
| Add student                   | ✓        |
| Display all students          | ✓        |
| Search by student ID          | ✓        |
| Update student details        | ✓        |
| Delete student record         | ✓        |
| Automatic grade calculation   | ✓        |
| Total student count           | ✓        |
| Persistent file storage       | ✓        |
| Input validation              | ✓        |
| Duplicate ID check            | ✓        |
| No database/internet required | ✓        |

---

## 8. HARDWARE AND SOFTWARE REQUIREMENTS

### Hardware Requirements (Minimum)

| Component   | Requirement              |
|-------------|--------------------------|
| Processor   | Intel Core i3 or above   |
| RAM         | 2 GB or above            |
| Storage     | 100 MB free disk space   |
| Display     | Any standard monitor     |
| Input       | Keyboard                 |

### Software Requirements

| Component          | Requirement                            |
|--------------------|----------------------------------------|
| Operating System   | Windows 10/11, Linux, or macOS        |
| JDK Version        | Java 17 or later (tested on Java 25)  |
| IDE (optional)     | VS Code with Java Extension Pack      |
|                    | OR IntelliJ IDEA Community Edition    |
| Terminal           | Command Prompt, PowerShell, or Bash   |
| External Libraries | None required                         |
| Database           | None required                         |

---

## 9. SYSTEM DESIGN AND UML CLASS DIAGRAM

### Project File Structure

```
Student Management System using java/
├── src/
│   ├── StudentOperations.java   ← Interface (Abstraction)
│   ├── Person.java              ← Abstract base class (Inheritance)
│   ├── Student.java             ← Concrete class (all OOP concepts)
│   ├── InputValidator.java      ← Utility class (Encapsulation)
│   ├── StudentManager.java      ← Business logic (implements interface)
│   └── StudentManagementSystem.java  ← Main class (entry point)
├── docs/
│   ├── SETUP_INSTRUCTIONS.md
│   ├── CASE_STUDY_REPORT.md
│   ├── PPT_CONTENT.md
│   ├── VIVA_QA.md
│   └── DEMO_SCRIPT.md
└── src/students.dat             ← Auto-generated data file
```

### UML Class Diagram (Text Representation)

```
«interface»
StudentOperations
─────────────────────────────
+ addStudent(student)
+ displayAllStudents()
+ searchStudent(id) : Student
+ updateStudent(...) : boolean
+ deleteStudent(id) : boolean
+ getTotalStudents() : int
         ▲
         │ implements
         │
«abstract»                         «class»
Person                             InputValidator
──────────────────────             ──────────────────────
- id : String         ◄────        - scanner : Scanner
- name : String       inherits     + readString(prompt) : String
- department : String              + readInt(...) : int
──────────────────────             + readDouble(...) : double
+ getId() : String                 + readConfirmation(...) : boolean
+ getName() : String               + close()
+ getDepartment() : String
+ setId(id)
+ setName(name)
+ setDepartment(dept)
+ getDisplayInfo() : String  ← abstract
+ toString() : String
         ▲
         │ extends
         │
«class»
Student  (also Serializable)
──────────────────────────────
- year : int
- marks : double
──────────────────────────────
+ Student(id, name, dept, year, marks)
+ getYear() : int
+ getMarks() : double
+ setYear(year)
+ setMarks(marks)
+ calculateGrade() : String
+ getDisplayInfo() : String   ← overrides Person
+ toString() : String         ← overrides Object

«class»
StudentManager  (implements StudentOperations)
──────────────────────────────────────────────
- FILE_NAME : String = "students.dat"
- studentList : ArrayList<Student>
──────────────────────────────────────────────
+ StudentManager()
+ addStudent(student)
+ displayAllStudents()
+ searchStudent(id) : Student
+ updateStudent(...) : boolean
+ deleteStudent(id) : boolean
+ getTotalStudents() : int
- saveToFile()
- loadFromFile() : ArrayList<Student>

«class»
StudentManagementSystem
──────────────────────────────
+ main(args)
- handleAddStudent(...)
- handleDisplayAll(...)
- handleSearch(...)
- handleUpdate(...)
- handleDelete(...)
- handleGrade(...)
- handleCount(...)
- printWelcome()
- printMenu()
```

---

## 10. OOP CONCEPTS EXPLAINED

### 10.1 Encapsulation

**Definition:** Wrapping data (variables) and code (methods) together into a
single unit (class), and restricting direct access to the data by making fields
`private`.

**Where used in this project:**
- In `Person.java`: `id`, `name`, `department` are all `private`.
- Access is only through `getId()`, `getName()`, `setName()`, etc.
- In `StudentManager.java`: The `studentList` ArrayList is `private`.
  Outside code cannot directly manipulate the list — it must go through methods
  like `addStudent()` or `deleteStudent()`.

```java
// Example from Person.java
private String id;        // Cannot be accessed directly from outside

public String getId() {   // Must use this getter
    return id;
}
```

**Benefit:** Protects data integrity. No code outside the class can accidentally
corrupt the student ID.

---

### 10.2 Inheritance

**Definition:** A mechanism where a child class acquires the properties and
behaviors of a parent class using the `extends` keyword.

**Where used in this project:**
- `Student extends Person`
- `Student` inherits `id`, `name`, `department`, and all getters/setters from
  `Person` without rewriting them.
- `Student` adds its own fields: `year` and `marks`.

```java
// Person is the parent
public abstract class Person { ... }

// Student is the child — inherits all of Person's fields and methods
public class Student extends Person implements Serializable {
    public Student(String studentId, String name, String department,
                   int year, double marks) {
        super(studentId, name, department);  // Calls Person's constructor
        this.year = year;
        this.marks = marks;
    }
}
```

**Benefit:** Code reuse. Common person attributes are written once in `Person`
and shared by `Student` (and could be shared by `Faculty`, `Staff`, etc. in
a future extension).

---

### 10.3 Polymorphism

**Definition:** The ability for the same method name to behave differently
depending on the object it is called on.

**Where used in this project (Method Overriding):**
- `Person` declares `getDisplayInfo()` as `abstract`.
- `Student` provides its own implementation — a formatted profile card.
- `toString()` is overridden in both `Person` and `Student` (originally from
  Java's `Object` class).

```java
// In Person.java — abstract declaration (no body)
public abstract String getDisplayInfo();

// In Student.java — overrides with specific Student behaviour
@Override
public String getDisplayInfo() {
    return "Student ID: " + getId() + "\nGrade: " + calculateGrade() + ...;
}
```

When `found.getDisplayInfo()` is called in `StudentManagementSystem.java`, Java
automatically runs the `Student` version, not the `Person` version.

**Benefit:** Flexibility. If we add a `Faculty` class later, it provides its own
`getDisplayInfo()`, and the same calling code works without changes.

---

### 10.4 Abstraction

**Definition:** Hiding implementation details and showing only the essential
features. Achieved using abstract classes and interfaces.

**Where used in this project:**
1. **Abstract class `Person`**: Cannot be instantiated directly. Forces all
   subclasses to implement `getDisplayInfo()`.
2. **Interface `StudentOperations`**: Defines the contract (what operations
   must exist) without specifying how they work. `StudentManager` provides
   the actual implementation.

```java
// Interface — defines WHAT, not HOW
public interface StudentOperations {
    void addStudent(Student student);
    Student searchStudent(String studentId);
    // ...
}

// StudentManager provides the HOW
public class StudentManager implements StudentOperations {
    @Override
    public void addStudent(Student student) {
        // Actual code here
    }
}
```

**Benefit:** Separation of concerns. The `main` class only knows the interface,
not the internal details of how records are stored.

---

### 10.5 Exception Handling

**Definition:** A mechanism to handle runtime errors gracefully without
crashing the program, using `try`, `catch`, and `finally` blocks.

**Where used in this project:**
- `InputValidator.java`: Catches `NumberFormatException` when the user types
  text instead of a number.
- `StudentManager.java`: Catches `IOException`, `FileNotFoundException`, and
  `ClassNotFoundException` during file read/write.

```java
try {
    value = Integer.parseInt(line.trim());
} catch (NumberFormatException e) {
    System.out.println("Invalid input. Please enter a whole number.");
}
```

---

## 11. ALGORITHM AND PROGRAM IMPLEMENTATION

### 11.1 Main Algorithm (Pseudocode)

```
START
  Load students from file into ArrayList
  REPEAT
    Display menu (options 1–8)
    Read user choice
    SWITCH choice:
      1 → Read id, name, dept, year, marks → Create Student → Add to list → Save
      2 → Iterate list → Print each student
      3 → Read id → Search list → Print profile or "Not Found"
      4 → Read id → Find student → Read new values → Update → Save
      5 → Read id → Find student → Confirm → Remove → Save
      6 → Read id → Find student → Print grade
      7 → Print list size
      8 → Exit loop
  UNTIL choice == 8
  Close scanner
END
```

### 11.2 Grade Calculation Algorithm

```
INPUT: marks (0–100)
IF marks >= 90  → Grade = "O  (Outstanding)"
ELSE IF >= 75   → Grade = "A+ (Excellent)"
ELSE IF >= 60   → Grade = "A  (Very Good)"
ELSE IF >= 50   → Grade = "B+ (Good)"
ELSE IF >= 40   → Grade = "B  (Average)"
ELSE            → Grade = "F  (Fail)"
OUTPUT: Grade string
```

### 11.3 File Persistence

Data is saved using **Java Object Serialization**:
- `ObjectOutputStream` writes the entire `ArrayList<Student>` to `students.dat`
- `ObjectInputStream` reads it back when the program starts
- `Student` implements `Serializable` to enable this

---

## 12. SAMPLE OUTPUT

### Welcome Screen
```
  ╔══════════════════════════════════════════════╗
  ║      STUDENT MANAGEMENT SYSTEM               ║
  ║      B V C College of Engineering            ║
  ║      CSE – AI & ML Department                ║
  ╚══════════════════════════════════════════════╝
```

### Adding a Student
```
  ══════════ ADD NEW STUDENT ══════════
  Student ID   : S001
  Full Name    : Ravi Kumar
  Department   : CSE-AIML
  Year (1-4)   : 2
  Marks (0-100): 88
  [✔] Student added successfully!
```

### Display All Students
```
  Total registered students: 2
  ─────────────────────────────────────────────────────────────────
  Student ID   Name                 Department       Year  Marks    Grade
  ─────────────────────────────────────────────────────────────────
  S001         Ravi Kumar           CSE-AIML         Year: 2  Marks: 88.00  Grade: A+ (Excellent)
  S002         Priya Sharma         CSE-AIML         Year: 3  Marks: 55.00  Grade: B+ (Good)
  ─────────────────────────────────────────────────────────────────
```

### Search Result
```
  ══════════ SEARCH STUDENT ══════════
  Enter Student ID to search: S001

  ┌─────────────────────────────────────────┐
  │  Student ID  : S001
  │  Name        : Ravi Kumar
  │  Department  : CSE-AIML
  │  Year        : 2
  │  Marks       : 88.0
  │  Grade       : A+ (Excellent)
  └─────────────────────────────────────────┘
```

### Duplicate ID Error
```
  Student ID   : S001
  [!] A student with ID 'S001' already exists. Duplicate IDs are not allowed.
```

### Invalid Marks Error
```
  Marks (0-100): 150
  [!] Please enter a value between 0.0 and 100.0.
```

---

## 13. TEST CASES AND RESULTS

| Test # | Action            | Input                      | Expected Result                          | Result |
|--------|-------------------|----------------------------|------------------------------------------|--------|
| TC-01  | Add student       | S001, Ravi, CSE, 2, 88     | "Student added successfully!"           | PASS   |
| TC-02  | Add student       | S002, Priya, CSE, 3, 55    | "Student added successfully!"           | PASS   |
| TC-03  | Duplicate ID      | S001 (again)               | "Duplicate IDs are not allowed."        | PASS   |
| TC-04  | Invalid marks     | 150                        | "Please enter a value between 0 and 100"| PASS   |
| TC-05  | Invalid marks     | -5                         | "Please enter a value between 0 and 100"| PASS   |
| TC-06  | Invalid year      | 5                          | "Please enter a number between 1 and 4" | PASS   |
| TC-07  | Display all       | (2 students added)         | Table with 2 rows                       | PASS   |
| TC-08  | Search found      | S001                       | Profile card for Ravi Kumar             | PASS   |
| TC-09  | Search not found  | S999                       | "No student found with ID: S999"        | PASS   |
| TC-10  | Update student    | S002, new marks = 72       | "Student updated successfully!"         | PASS   |
| TC-11  | Grade for 88      | (from TC-01)               | A+ (Excellent)                          | PASS   |
| TC-12  | Grade for 72      | (after TC-10)              | A  (Very Good)                          | PASS   |
| TC-13  | Delete confirmed  | S002, confirm y            | "Student record deleted."               | PASS   |
| TC-14  | Delete cancelled  | S001, confirm n            | "Deletion cancelled."                   | PASS   |
| TC-15  | Persistence       | Exit + restart             | S001 still shows in display             | PASS   |

---

## 14. ADVANTAGES AND LIMITATIONS

### Advantages

1. **No external dependencies** — only JDK required, no database, no internet.
2. **Platform independent** — runs on Windows, Linux, or macOS.
3. **Clean OOP structure** — all four pillars demonstrated clearly.
4. **Persistent storage** — data survives program restarts.
5. **Robust input validation** — handles wrong types and out-of-range values.
6. **Duplicate prevention** — student IDs are unique.
7. **Beginner-friendly code** — well-commented with clear method names.

### Limitations

1. **Console only** — no graphical user interface.
2. **No sorting** — students are displayed in insertion order only.
3. **No partial search** — search requires the exact student ID.
4. **Single user** — no concurrent multi-user support.
5. **Binary file format** — `students.dat` cannot be opened in a text editor.
6. **No backup** — if `students.dat` is deleted, all data is lost.

---

## 15. FUTURE ENHANCEMENTS

1. **GUI** — Add a JavaFX or Swing graphical interface.
2. **Database integration** — Use SQLite or MySQL for structured storage.
3. **Name-based search** — Allow searching by partial name.
4. **Sorting** — Sort students by name, marks, or year.
5. **Export to CSV/PDF** — Generate printable reports.
6. **Multi-subject marks** — Store marks per subject and compute average.
7. **Login system** — Add admin authentication before access.
8. **Faculty class** — Extend the `Person` hierarchy with a `Faculty` class.

---

## 16. CONCLUSION

This project successfully implements a Student Management System using Core Java,
demonstrating all four Object-Oriented Programming principles in a meaningful,
practical context. Encapsulation protects student data, Inheritance enables code
reuse through the Person–Student hierarchy, Polymorphism allows flexible method
behaviour via overriding, and Abstraction separates the interface contract from
its implementation.

The system handles persistent file storage, validates all user input, prevents
duplicate records, and provides a clean console interface. It was designed to
be simple enough for a beginner to understand and extend, while still
following professional Java coding practices.

---

## 17. REFERENCES

1. Herbert Schildt, *Java: The Complete Reference*, 12th Edition, McGraw-Hill, 2021.
2. Oracle Java Documentation — https://docs.oracle.com/en/java/
3. GeeksforGeeks Java OOP Concepts — https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/
4. Javatpoint Java Tutorial — https://www.javatpoint.com/java-tutorial
5. W3Schools Java — https://www.w3schools.com/java/
6. Baeldung — Java Serialization — https://www.baeldung.com/java-serialization
