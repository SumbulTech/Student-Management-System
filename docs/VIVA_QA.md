# Viva Questions and Answers
## Student Management System — OOP Through Java Lab

*Prepare these 25 questions. Read each answer aloud at least twice before your viva.*

---

### SECTION A: Java Basics

**Q1. What is Java?**
Java is a high-level, object-oriented, platform-independent programming language
developed by Sun Microsystems (now Oracle). It follows the "write once, run anywhere"
principle — Java code compiles to bytecode that runs on any machine with a JVM
(Java Virtual Machine).

---

**Q2. What is the JVM, JDK, and JRE? How are they different?**
- **JDK (Java Development Kit):** The full package for developers — includes the
  compiler (javac), JRE, and development tools. You need this to write and compile Java.
- **JRE (Java Runtime Environment):** Needed to run Java programs. Includes the JVM.
- **JVM (Java Virtual Machine):** The engine that actually executes Java bytecode.

*Simple way to remember: JDK > JRE > JVM — each one is inside the next.*

---

**Q3. What is the difference between `javac` and `java`?**
- `javac` is the **compiler** — it converts `.java` source code into `.class` bytecode.
- `java` is the **runtime** — it runs the compiled `.class` file using the JVM.

---

**Q4. What is `public static void main(String[] args)`?**
This is the entry point of every Java program.
- `public` — accessible from anywhere
- `static` — belongs to the class, not an object (JVM calls it without creating an object)
- `void` — returns nothing
- `main` — the required name for the entry method
- `String[] args` — command-line arguments passed to the program

---

### SECTION B: Classes and Objects

**Q5. What is a class in Java?**
A class is a blueprint or template that defines the structure and behaviour of objects.
It contains fields (data) and methods (actions).
In our project, `Student` is a class that defines what properties a student has
(id, name, marks) and what actions are possible (calculateGrade, getDisplayInfo).

---

**Q6. What is an object in Java?**
An object is an instance of a class — a real, concrete entity created from the blueprint.

```java
Student s = new Student("S001", "Ravi", "CSE", 2, 88);
```

Here `s` is an object of the `Student` class. Each object has its own separate data.

---

**Q7. What is a constructor?**
A constructor is a special method that is called automatically when an object is
created using `new`. It initialises the object's fields.
- Same name as the class
- No return type

In our project, `Student(id, name, dept, year, marks)` is the constructor.

---

### SECTION C: Encapsulation

**Q8. What is Encapsulation?**
Encapsulation means wrapping data and methods together in a class and restricting
direct access to the data by making fields `private`. Access is provided only
through public getters and setters.

---

**Q9. How did you implement Encapsulation in your project?**
In `Person.java`, the fields `id`, `name`, and `department` are all `private`.
No code outside the class can directly write `person.id = "S001"`. Instead,
they must use `person.setId("S001")` or read it with `person.getId()`.

---

**Q10. What is the difference between `private`, `public`, and `protected`?**
- `private` — accessible only within the same class
- `public` — accessible from anywhere
- `protected` — accessible within the same class, subclasses, and same package

---

### SECTION D: Inheritance

**Q11. What is Inheritance?**
Inheritance is the mechanism by which a child class (subclass) acquires the
properties and methods of a parent class (superclass). It promotes code reuse.

---

**Q12. How did you use Inheritance in your project?**
`Student extends Person`. The `Student` class automatically gets `id`, `name`,
`department`, and all their getters/setters from `Person` without rewriting them.
`Student` adds its own `year` and `marks` fields on top.

---

**Q13. What is the `super` keyword?**
`super` refers to the parent class. In `Student`'s constructor, we use
`super(studentId, name, department)` to call `Person`'s constructor and
initialise the inherited fields. Without `super`, the parent's constructor
would not be called.

---

**Q14. What is an abstract class?**
An abstract class is a class that cannot be instantiated directly — you cannot
write `new Person()`. It may contain abstract methods (methods with no body)
that must be implemented by subclasses.

In our project, `Person` is abstract. It forces all subclasses to implement
`getDisplayInfo()`.

---

### SECTION E: Polymorphism

**Q15. What is Polymorphism?**
Polymorphism means "many forms." In Java, the same method name can behave
differently depending on the object. There are two types:
- **Method Overriding** (runtime polymorphism) — subclass provides its own version
- **Method Overloading** (compile-time) — same name, different parameters

---

**Q16. How did you demonstrate Polymorphism in your project?**
`Person` declares `getDisplayInfo()` as abstract. `Student` overrides it to
produce a formatted profile card with the student's marks and grade.

When the code runs `found.getDisplayInfo()`, Java automatically calls the
`Student` version — this is runtime polymorphism (also called dynamic dispatch).

---

**Q17. What is the `@Override` annotation?**
`@Override` tells the compiler "this method is meant to override a method from
the parent class." If you accidentally misspell the method name, the compiler
will give an error instead of silently creating a new method. It is a safety check.

---

### SECTION F: Abstraction

**Q18. What is Abstraction?**
Abstraction means hiding the internal implementation and showing only what is
necessary. It focuses on WHAT something does, not HOW it does it.

---

**Q19. What is an Interface in Java?**
An interface is a contract — it defines method signatures that a class must
implement, but contains no implementation code itself (in traditional Java).
A class implements an interface using the `implements` keyword.

---

**Q20. How did you use Abstraction in your project?**
The `StudentOperations` interface defines six method signatures: `addStudent`,
`displayAllStudents`, `searchStudent`, `updateStudent`, `deleteStudent`,
`getTotalStudents`. `StudentManager` provides the actual implementation.
The `main` class interacts with `StudentManager` through this interface contract,
without caring about the internal file handling details.

---

### SECTION G: ArrayList

**Q21. What is an ArrayList in Java?**
`ArrayList` is a resizable array from the `java.util` package. Unlike a regular
array with fixed size, ArrayList grows automatically when elements are added.
It provides methods like `add()`, `remove()`, `get()`, and `size()`.

---

**Q22. How did you use ArrayList in your project?**
In `StudentManager.java`, we use `ArrayList<Student> studentList` to store all
student objects in memory. When we add a student, `studentList.add(student)` is
called. When we delete one, `studentList.remove(s)` is called. The entire list
is saved to file using serialization.

---

### SECTION H: File Handling

**Q23. How does your project save data permanently?**
We use Java Object Serialization:
- `Student implements Serializable` — marks the class as saveable
- `ObjectOutputStream` writes the entire `ArrayList<Student>` to `students.dat`
- `ObjectInputStream` reads it back when the program starts
- This happens automatically every time the user adds, updates, or deletes a record

---

### SECTION I: Exception Handling

**Q24. What is Exception Handling?**
Exception handling is the mechanism to catch and respond to runtime errors
(exceptions) so the program does not crash. It uses:
- `try` — the block of code that might throw an exception
- `catch` — what to do if an exception occurs
- `finally` — code that always runs (optional)

---

**Q25. What exceptions does your project handle?**
1. `NumberFormatException` — when the user types letters instead of a number
   (handled in `InputValidator.java`)
2. `FileNotFoundException` — when the data file doesn't exist yet on first run
3. `IOException` — disk or permission error during file read/write
4. `ClassNotFoundException` — file is corrupted or from an incompatible version
   (all three handled in `StudentManager.java`'s `loadFromFile` method)

---

### BONUS QUESTIONS (if the faculty goes deeper)

**Q. What is Serialization?**
Converting a Java object into a byte stream so it can be saved to a file or
sent over a network. The reverse process is Deserialization — reading bytes back
into an object. The class must implement `java.io.Serializable`.

**Q. Why do you have `serialVersionUID` in Student.java?**
It is a unique version number for the serialized class. If you change the class
later and the `serialVersionUID` differs from what's in the file, Java throws an
`InvalidClassException` to prevent loading incompatible data.

**Q. What is the difference between an abstract class and an interface?**
| Feature | Abstract Class | Interface |
|---|---|---|
| Can have constructor | Yes | No |
| Can have instance fields | Yes | No (only constants) |
| Supports multiple inheritance | No | Yes (a class can implement many) |
| Methods with body | Yes | Only default/static (Java 8+) |

**Q. What does `implements Serializable` mean?**
It is a marker interface — it has no methods. Implementing it tells the JVM
that objects of this class can be serialized (converted to bytes and saved).
