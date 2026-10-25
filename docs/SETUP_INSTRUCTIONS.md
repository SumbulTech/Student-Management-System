# Setup & Run Instructions
## Student Management System — B V C College of Engineering

---

## Step 1: Verify Java is Installed

Open a terminal (Command Prompt or PowerShell) and type:

```
java --version
javac --version
```

You should see a version number like `java 17.x.x` or higher.
If you see an error, download JDK from: https://adoptium.net/

---

## Step 2: Locate the Source Files

All `.java` files are inside the `src` folder:

```
Student Management System using java/
├── src/
│   ├── StudentOperations.java
│   ├── Person.java
│   ├── Student.java
│   ├── InputValidator.java
│   ├── StudentManager.java
│   └── StudentManagementSystem.java
└── docs/
```

---

## Step 3: Compile the Code

Open Command Prompt or PowerShell and navigate to the `src` folder:

```
cd "c:\Users\DELL\OneDrive\Desktop\Student Management System using java\src"
```

Then compile all files with one command:

```
javac *.java
```

If compilation succeeds, you will see NO error messages.
Six `.class` files will appear in the `src` folder.

---

## Step 4: Run the Application

From the same `src` folder, run:

```
java StudentManagementSystem
```

The welcome banner will appear and the main menu will be displayed.

---

## Step 5: Test Every Feature

### Test 1 — Add a Student
- Choose option 1
- Enter: ID = `S001`, Name = `Ravi Kumar`, Dept = `CSE-AIML`, Year = `2`, Marks = `88`
- Expected: "Student added successfully!"

### Test 2 — Add Another Student
- ID = `S002`, Name = `Priya Sharma`, Dept = `CSE-AIML`, Year = `3`, Marks = `55`

### Test 3 — Display All Students
- Choose option 2
- Expected: Both students listed in a table with grades

### Test 4 — Search a Student
- Choose option 3, enter `S001`
- Expected: Full profile card for Ravi Kumar, Grade = A+ (Excellent)

### Test 5 — Update a Student
- Choose option 4, enter `S002`
- Change marks to `72`
- Expected: "Student updated successfully!"

### Test 6 — View Grade
- Choose option 6, enter `S002`
- Expected: Grade = A (Very Good) for marks 72

### Test 7 — Delete a Student
- Choose option 5, enter `S002`, confirm with `y`
- Expected: "Student record deleted successfully."

### Test 8 — Duplicate ID Check
- Try adding a student with ID `S001` again
- Expected: "A student with ID 'S001' already exists."

### Test 9 — Invalid Marks
- When asked for marks, type `150`
- Expected: "Please enter a value between 0.0 and 100.0."

### Test 10 — Persistent Storage
- Exit the program (option 8)
- Run it again: `java StudentManagementSystem`
- Choose option 2 — previously added students should still appear

---

## Grade Scale Reference

| Marks     | Grade              |
|-----------|--------------------|
| 90 – 100  | O  (Outstanding)   |
| 75 – 89   | A+ (Excellent)     |
| 60 – 74   | A  (Very Good)     |
| 50 – 59   | B+ (Good)          |
| 40 – 49   | B  (Average)       |
| Below 40  | F  (Fail)          |

---

## Using VS Code (Optional)

1. Open VS Code
2. Install the **Extension Pack for Java** (Microsoft)
3. Open the `src` folder
4. Open `StudentManagementSystem.java`
5. Click the **Run** button (▶) at the top right
6. Input/output appears in the integrated terminal

---

## Data Storage

Student records are saved in a file called `students.dat` in the same folder
where you run the program. This file is created automatically on first use.
Do not delete it if you want to keep your data.
