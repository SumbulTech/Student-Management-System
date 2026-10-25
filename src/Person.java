/**
 * Person.java
 * 
 * This is an ABSTRACT BASE CLASS (Inheritance + Abstraction).
 * A real-world college has many types of people: students, faculty, staff.
 * All of them share some common properties: id, name, department.
 * We capture that shared structure here.
 * 
 * OOP Concept Demonstrated: ABSTRACTION + INHERITANCE (base class)
 * 
 * "abstract" means you cannot create a Person object directly —
 * you must create a specific type like Student.
 */
public abstract class Person {

    // Private fields — only accessible through getters/setters (Encapsulation)
    private String id;
    private String name;
    private String department;

    // Constructor — called when creating a subclass object
    public Person(String id, String name, String department) {
        this.id = id;
        this.name = name;
        this.department = department;
    }

    // --- Getters ---
    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getDepartment() {
        return department;
    }

    // --- Setters ---
    public void setId(String id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    /**
     * Abstract method — every subclass MUST provide its own version.
     * This is how we achieve polymorphism through method overriding.
     */
    public abstract String getDisplayInfo();

    /**
     * toString() is overridden here to give a readable description.
     * OOP Concept: Polymorphism (method overriding from Object class)
     */
    @Override
    public String toString() {
        return "ID: " + id + " | Name: " + name + " | Department: " + department;
    }
}
