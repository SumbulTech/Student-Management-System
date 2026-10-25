# Live Demonstration Script
## Student Management System — 3 to 5 Minute Presentation

*Read this script aloud a few times before your demo.
Run the program in a terminal while presenting.*

---

## BEFORE YOU START

1. Open a terminal (Command Prompt or PowerShell)
2. Navigate to the `src` folder:
   ```
   cd "c:\Users\DELL\OneDrive\Desktop\Student Management System using java\src"
   ```
3. Have the code open in VS Code or a text editor as a backup reference
4. Take a breath — you know this project!

---

## THE SCRIPT

---

### OPENING (30 seconds)

*Stand straight, make eye contact, speak clearly.*

"Good morning, respected faculty.
My name is [Your Name], Roll Number [Your Roll No.], from the CSE AI&ML department.

Today I will demonstrate my OOP lab case study project:
a **Student Management System** built using Core Java.

This system can add, display, search, update, and delete student records.
It also calculates grades automatically and saves all data permanently using
file handling — so records are not lost when the program closes.

Let me run it now."

---

### STEP 1 — RUN THE PROGRAM (20 seconds)

*Type the command and let the welcome banner appear.*

```
java StudentManagementSystem
```

"When I run this command, the program loads any previously saved student data
from a file called `students.dat` and shows this welcome menu.

You can see 8 options here. The menu is driven by numbers — the user simply types
a number and presses Enter."

---

### STEP 2 — ADD A STUDENT (45 seconds)

*Choose option 1.*

"I'll start by adding a student. I press 1 and hit Enter."

*Enter:*
- Student ID: `S001`
- Name: `Ravi Kumar`
- Department: `CSE-AIML`
- Year: `2`
- Marks: `88`

"Notice that the program asks for each field one at a time.
The `year` field only accepts 1 to 4 — if I type 5 it will reject it.
The `marks` field only accepts 0 to 100.

This input validation is handled in our `InputValidator` class using
`try-catch` blocks — that is our Exception Handling in action.

The record is now saved. Let me add one more student."

*Add second student:*
- ID: `S002`, Name: `Priya Sharma`, Dept: `CSE-AIML`, Year: `3`, Marks: `55`

---

### STEP 3 — DISPLAY ALL (30 seconds)

*Choose option 2.*

"I press 2 to display all students.
You can see both students listed in a table with their IDs, names, departments,
year, marks, and automatically calculated grades.

Ravi got 88 marks — that is **A+ Excellent**.
Priya got 55 marks — that is **B+ Good**.

The grade calculation is inside the `calculateGrade()` method of the `Student`
class. This is a behaviour specific to the Student — a clear example of
**Encapsulation**, where data and behaviour are bundled together."

---

### STEP 4 — SEARCH A STUDENT (30 seconds)

*Choose option 3.*

"Now I'll search for Ravi using his student ID S001."

*Enter: S001*

"The program displays a formatted profile card.
Notice this is the output of `getDisplayInfo()` — a method that is declared
`abstract` in the `Person` class and **overridden** in `Student`.

This is **Polymorphism** — the method behaves differently depending on whether
it is called on a Student or (in a future version) a Faculty object.
Java decides which version to call at runtime."

---

### STEP 5 — UPDATE A STUDENT (30 seconds)

*Choose option 4.*

"Let me update Priya's marks."

*Enter: S002, then new values: same name, same dept, same year, new marks = 72*

"Updated successfully. If I display all students now, Priya's grade will have
changed from B+ Good to A Very Good.

This change is also saved to file immediately — the `saveToFile()` method in
`StudentManager` is called every time a record is added, updated, or deleted."

---

### STEP 6 — SHOW OOP STRUCTURE (40 seconds)

*Point to the terminal or switch to VS Code.*

"Let me quickly explain the class structure:

- `StudentOperations` is an **interface** — it lists all the operations the system must support.
  This is **Abstraction**: we define WHAT operations exist without saying HOW.

- `Person` is an **abstract class** — it holds the common fields: id, name, department.
  `Student extends Person` — this is **Inheritance**. Student reuses those fields
  and adds year and marks.

- `StudentManager implements StudentOperations` — it provides the actual code
  for add, search, update, delete, and handles file reading and writing.

- `InputValidator` is a utility class that uses **Exception Handling** to make sure
  the user cannot enter letters when a number is expected."

---

### STEP 7 — DELETE AND PERSISTENCE (30 seconds)

*Choose option 5.*

"Finally, let me delete Priya's record."

*Enter: S002, confirm with y*

"Deleted. Now I'll exit the program..."

*Choose option 8.*

"...and run it again."

```
java StudentManagementSystem
```

*Choose option 2.*

"You can see that Ravi's record is still here even after restarting.
That is our **File Handling** — all data is serialized and saved to `students.dat`.
On startup, `StudentManager` loads it back automatically using `ObjectInputStream`."

---

### CLOSING (20 seconds)

"To summarise:
- The project uses **Encapsulation** to protect student data through private fields.
- **Inheritance** through Person and Student to reuse common code.
- **Polymorphism** through `getDisplayInfo()` and `toString()` overrides.
- **Abstraction** through the `StudentOperations` interface.
- **Exception Handling** to prevent crashes from bad input.
- **File Handling** for persistent data storage.

Thank you. I am ready for your questions."

---

## TIMING GUIDE

| Section           | Time     |
|-------------------|----------|
| Opening           | 30 sec   |
| Run program       | 20 sec   |
| Add students      | 45 sec   |
| Display all       | 30 sec   |
| Search            | 30 sec   |
| Update            | 30 sec   |
| OOP explanation   | 40 sec   |
| Delete + persist  | 30 sec   |
| Closing           | 20 sec   |
| **TOTAL**         | ~4.5 min |

---

## TIPS FOR THE DEMO

- Speak slowly and clearly. Faculty want to hear you, not just watch the screen.
- If something goes wrong (typo, wrong option), stay calm and say "Let me redo that."
- If asked a question mid-demo, answer it and then continue from where you left off.
- Know which class each feature is in — faculty often ask "where is this code?"
- The key phrases to use: "This demonstrates...", "Notice how...", "That is because..."
