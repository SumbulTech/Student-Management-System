# Sample Data — Student Management System
## B V C College of Engineering | CSE – AI & ML

Use this data to test all features of the application.
Enter these records one by one using **Option 1 (Add Student)**.

---

## Student Records

| # | Student ID | Full Name         | Department  | Year | Marks | Expected Grade     |
|---|------------|-------------------|-------------|------|-------|--------------------|
| 1 | S001       | Ravi Kumar        | CSE-AIML    | 2    | 92    | O — Outstanding    |
| 2 | S002       | Priya Sharma      | CSE-AIML    | 3    | 78    | A+ — Excellent     |
| 3 | S003       | Arjun Reddy       | CSE-AIML    | 1    | 65    | A — Very Good      |
| 4 | S004       | Sneha Patel       | CSE-AIML    | 4    | 54    | B+ — Good          |
| 5 | S005       | Mohammed Farhan   | CSE-AIML    | 2    | 45    | B — Average        |
| 6 | S006       | Divya Nair        | CSE-AIML    | 3    | 88    | A+ — Excellent     |
| 7 | S007       | Kiran Babu        | CSE-AIML    | 1    | 35    | F — Fail           |
| 8 | S008       | Lakshmi Devi      | CSE-AIML    | 4    | 95    | O — Outstanding    |
| 9 | S009       | Suresh Varma      | CSE-AIML    | 2    | 61    | A — Very Good      |
| 10| S010       | Anjali Menon      | CSE-AIML    | 3    | 50    | B+ — Good          |

---

## Grade Scale Reference

| Marks Range | Grade              |
|-------------|--------------------|
| 90 – 100    | O  (Outstanding)   |
| 75 – 89     | A+ (Excellent)     |
| 60 – 74     | A  (Very Good)     |
| 50 – 59     | B+ (Good)          |
| 40 – 49     | B  (Average)       |
| Below 40    | F  (Fail)          |

---

## Test Scenarios

### Test 1 — Add All 10 Students
Enter each record from the table above using Option 1.
After adding all 10, use Option 2 (Display All) to verify the full table.

### Test 2 — Duplicate ID Check
Try adding a student with ID **S001** again after it already exists.
**Expected:** `[!] A student with ID 'S001' already exists. Duplicate IDs are not allowed.`

### Test 3 — Invalid Marks
Try entering marks = **150** or **-10**.
**Expected:** `[!] Please enter a value between 0.0 and 100.0.`

### Test 4 — Search Found
Search for Student ID **S008**.
**Expected:** Full profile for Lakshmi Devi — Grade: O (Outstanding), Marks: 95

### Test 5 — Search Not Found
Search for Student ID **S999**.
**Expected:** `[!] No student found with ID: S999`

### Test 6 — Update Student
Update Student ID **S007** (Kiran Babu).
Change marks from **35** to **72**.
**Expected:** Grade changes from F (Fail) → A (Very Good)

### Test 7 — Delete Student
Delete Student ID **S010** (Anjali Menon).
Confirm deletion. Then search for S010.
**Expected:** `[!] No student found with ID: S010`

### Test 8 — View Grade
View grade for Student ID **S001** (Ravi Kumar, Marks: 92).
**Expected:** Grade = O — Outstanding

### Test 9 — Total Count
After adding all 10 students and deleting S010:
**Expected Total:** 9 students

### Test 10 — Persistence Test (Java only)
After adding students, close the program (Option 8) and reopen it.
Use Option 2 to display all students.
**Expected:** All previously added students still appear (loaded from `students.dat`).

---

## Expected Statistics (after adding all 10 students)

| Statistic          | Value        |
|--------------------|--------------|
| Total Students     | 10           |
| Average Marks      | 66.3         |
| Students Passed    | 9            |
| Students Failed    | 1 (S007)     |
| Outstanding (O)    | 2 (S001, S008)|

---

## Quick Add Sequence (for Demo)

To quickly demo the system, add just these 3 students first:

| Student ID | Full Name      | Department | Year | Marks |
|------------|----------------|------------|------|-------|
| S001       | Ravi Kumar     | CSE-AIML   | 2    | 92    |
| S002       | Priya Sharma   | CSE-AIML   | 3    | 55    |
| S003       | Arjun Reddy    | CSE-AIML   | 1    | 35    |

This covers all 3 grade categories: Outstanding, B+ Good, and Fail — 
good for demonstrating the grade calculation feature in your viva.

---

*File: docs/data.md | Project: Student Management System | Date: 26 October 2026*
