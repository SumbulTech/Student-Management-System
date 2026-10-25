"""
generate_screenshots.py
Generates mockup PNG screenshots for every section of the
Student Management System UI.
"""

from PIL import Image, ImageDraw, ImageFont
import os, sys

# ── output folder ──────────────────────────────────────────
BASE  = r"c:\Users\DELL\OneDrive\Desktop\Student Management System using java"
OUT   = os.path.join(BASE, "images")
os.makedirs(OUT, exist_ok=True)

# ── colour palette (dark theme) ───────────────────────────
BG       = (13,  17,  23)
SURFACE  = (22,  27,  34)
SURFACE2 = (33,  38,  45)
BORDER   = (48,  54,  61)
TEXT     = (201, 209, 217)
MUTED    = (139, 148, 158)
GREEN    = (63,  185, 80)
BLUE     = (88,  166, 255)
YELLOW   = (227, 179, 65)
RED      = (248, 81,  73)
ORANGE   = (240, 136, 62)
CYAN     = (121, 192, 255)
PURPLE   = (210, 168, 255)
WHITE    = (255, 255, 255)
DARK_GREEN_BG  = (13, 43, 18)
DARK_BLUE_BG   = (13, 31, 60)
DARK_YELLOW_BG = (42, 36, 13)
DARK_RED_BG    = (45, 13, 13)
DARK_ORANGE_BG = (42, 26, 13)

W, H = 1200, 700
SIDEBAR_W = 200

# ── font loader ────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

F10 = font(10); F11 = font(11); F12 = font(12); F13 = font(13)
F14 = font(14); F16 = font(16); F18 = font(18); F20 = font(20)
F24 = font(24, bold=True); F28 = font(28, bold=True)

# ── helpers ────────────────────────────────────────────────
def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    d   = ImageDraw.Draw(img)
    return img, d

def draw_rect(d, x1, y1, x2, y2, fill=None, outline=None, radius=8):
    d.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline)

def draw_header(d, title, subtitle=""):
    # header bar
    d.rectangle([0, 0, W, 56], fill=SURFACE)
    d.rectangle([0, 55, W, 56], fill=BORDER)
    # icon
    draw_rect(d, 14, 8, 46, 48, fill=(31, 111, 235), radius=8)
    d.text((22, 14), "🎓", font=F20, fill=WHITE)
    # title
    d.text((56, 10), "Student Management System", font=F16, fill=TEXT)
    d.text((56, 32), "B V C College of Engineering  ·  CSE – AI & ML  ·  OOP Lab", font=F11, fill=MUTED)
    # right badges
    draw_rect(d, W-180, 16, W-100, 40, fill=SURFACE2, outline=BORDER, radius=12)
    d.text((W-175, 22), "Java Simulation", font=F11, fill=MUTED)
    draw_rect(d, W-90, 16, W-14, 40, fill=(13,31,60), outline=(31,111,235), radius=12)
    d.text((W-85, 22), "10 Students", font=F11, fill=BLUE)

def draw_sidebar(d, active_index):
    d.rectangle([0, 56, SIDEBAR_W, H], fill=SURFACE)
    d.rectangle([SIDEBAR_W-1, 56, SIDEBAR_W, H], fill=BORDER)

    items = [
        ("➕", "Add Student",      "1"),
        ("📋", "Display All",      "2"),
        ("🔍", "Search",           "3"),
        ("✏️",  "Update",           "4"),
        ("🗑️", "Delete",           "5"),
        ("📊", "View Grade",       "6"),
        ("🔢", "Total Count",      "7"),
        ("📚", "Grade Scale",      " "),
    ]

    d.text((14, 70), "OPERATIONS", font=F10, fill=MUTED)

    for i, (icon, label, num) in enumerate(items):
        y = 88 + i * 44
        if i == 5:
            d.line([10, y-6, SIDEBAR_W-10, y-6], fill=BORDER, width=1)
            d.text((14, y-2), "REPORTS", font=F10, fill=MUTED)
            y += 14

        is_active = (i == active_index)
        if is_active:
            draw_rect(d, 6, y, SIDEBAR_W-6, y+34, fill=(13,31,60), radius=6)
            d.rectangle([6, y+4, 9, y+30], fill=BLUE)
            color = BLUE
        else:
            color = TEXT

        d.text((18, y+8), icon, font=F13, fill=color)
        d.text((40, y+9), label, font=F13, fill=color)
        draw_rect(d, SIDEBAR_W-30, y+9, SIDEBAR_W-10, y+26, fill=SURFACE2, outline=BORDER, radius=4)
        d.text((SIDEBAR_W-24, y+11), num, font=F10, fill=MUTED)

def draw_terminal(d, lines):
    tx = W - 310
    d.rectangle([tx, 56, W, H], fill=SURFACE)
    d.rectangle([tx, 56, tx+1, H], fill=BORDER)
    # title bar
    d.rectangle([tx, 56, W, 82], fill=SURFACE2)
    d.rectangle([tx, 81, W, 82], fill=BORDER)
    d.ellipse([tx+10, 64, tx+22, 76], fill=(255,95,87))
    d.ellipse([tx+28, 64, tx+40, 76], fill=(255,189,46))
    d.ellipse([tx+46, 64, tx+58, 76], fill=(40,202,65))
    d.text((tx+68, 64), "StudentManagementSystem.java", font=F11, fill=MUTED)

    y = 92
    for text, color in lines:
        d.text((tx+12, y), text, font=F11, fill=color)
        y += 18
        if y > H - 36: break

    # input row
    d.rectangle([tx, H-36, W, H], fill=SURFACE2)
    d.rectangle([tx, H-37, W, H-36], fill=BORDER)
    d.text((tx+10, H-26), "$ > _", font=F11, fill=GREEN)

def main_area_x():
    return SIDEBAR_W + 20

# ══════════════════════════════════════════════════════════
#  SCREEN 1 — WELCOME / HOME
# ══════════════════════════════════════════════════════════
def make_welcome():
    img, d = new_canvas()
    draw_header(d, "Welcome")
    draw_sidebar(d, -1)

    mx = main_area_x()
    cx = (SIDEBAR_W + W - 310) // 2

    # big welcome box
    draw_rect(d, mx, 80, W-320, H-20, fill=SURFACE, outline=BORDER, radius=12)

    d.text((cx-180, 120), "╔══════════════════════════════════════════╗", font=F13, fill=CYAN)
    d.text((cx-180, 140), "║     STUDENT MANAGEMENT SYSTEM            ║", font=F13, fill=CYAN)
    d.text((cx-180, 158), "║     B V C College of Engineering         ║", font=F13, fill=CYAN)
    d.text((cx-180, 176), "║     CSE – AI & ML Department             ║", font=F13, fill=CYAN)
    d.text((cx-180, 194), "╚══════════════════════════════════════════╝", font=F13, fill=CYAN)

    menu = [
        ("1.", "Add New Student"),
        ("2.", "Display All Students"),
        ("3.", "Search Student"),
        ("4.", "Update Student Details"),
        ("5.", "Delete Student Record"),
        ("6.", "View Student Grade"),
        ("7.", "Total Number of Students"),
        ("8.", "Exit"),
    ]
    d.text((cx-100, 230), "┌─────────────────────────────┐", font=F13, fill=BORDER)
    d.text((cx-100, 248), "│         MAIN MENU           │", font=F13, fill=TEXT)
    d.text((cx-100, 266), "├─────────────────────────────┤", font=F13, fill=BORDER)
    for i, (num, label) in enumerate(menu):
        d.text((cx-100, 284 + i*18), f"│  {num} {label:<26}│", font=F13, fill=TEXT)
    d.text((cx-100, 284 + len(menu)*18), "└─────────────────────────────┘", font=F13, fill=BORDER)

    draw_terminal(d, [
        ("╔══════════════════════════════════╗", CYAN),
        ("║   Student Management System      ║", CYAN),
        ("║   B V C College of Engineering   ║", CYAN),
        ("╚══════════════════════════════════╝", CYAN),
        ("", MUTED),
        ("[✔] Loaded 10 student record(s).", GREEN),
        ("", MUTED),
        ("Type help for commands.", MUTED),
    ])

    img.save(os.path.join(OUT, "01_welcome.png"))
    print("✔ 01_welcome.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 2 — ADD STUDENT
# ══════════════════════════════════════════════════════════
def make_add():
    img, d = new_canvas()
    draw_header(d, "Add Student")
    draw_sidebar(d, 0)

    mx = main_area_x()
    d.text((mx, 70), "Add New Student", font=F20, fill=TEXT)
    d.text((mx, 96), "Fill in the details below. All fields are required.", font=F13, fill=MUTED)

    card_x1, card_y1, card_x2, card_y2 = mx, 118, W-320, H-20
    draw_rect(d, card_x1, card_y1, card_x2, card_y2, fill=SURFACE, outline=BORDER, radius=10)

    fields = [
        ("STUDENT ID",    "S001",            card_x1+20, 138),
        ("FULL NAME",     "Ravi Kumar",       card_x1+20, 208),
        ("DEPARTMENT",    "CSE-AIML",         card_x1+20, 278),
        ("MARKS (0-100)", "92",               card_x1+20, 348),
    ]
    field_w = (card_x2 - card_x1 - 60) // 2

    for label, val, fx, fy in fields:
        d.text((fx, fy), label, font=F10, fill=MUTED)
        draw_rect(d, fx, fy+16, fx+field_w, fy+42, fill=BG, outline=BLUE, radius=6)
        d.text((fx+12, fy+24), val, font=F13, fill=TEXT)

    # Year field beside dept
    d.text((card_x1+20+field_w+20, 278), "ACADEMIC YEAR", font=F10, fill=MUTED)
    draw_rect(d, card_x1+20+field_w+20, 294, card_x1+20+field_w*2+20, 320, fill=BG, outline=BORDER, radius=6)
    d.text((card_x1+32+field_w+20, 302), "2nd Year  ▾", font=F13, fill=TEXT)

    # Add button
    draw_rect(d, card_x1+20, 420, card_x1+160, 450, fill=(35,134,54), outline=(46,160,67), radius=8)
    d.text((card_x1+45, 430), "➕  Add Student", font=F13, fill=WHITE)
    draw_rect(d, card_x1+170, 420, card_x1+250, 450, fill=SURFACE2, outline=BORDER, radius=8)
    d.text((card_x1+192, 430), "Clear", font=F13, fill=MUTED)

    draw_terminal(d, [
        ("", MUTED),
        ("══ ADD STUDENT ══", CYAN),
        ("  Student ID : S001", BLUE),
        ("  Name       : Ravi Kumar", TEXT),
        ("  Department : CSE-AIML", TEXT),
        ("  Year       : 2   Marks: 92", TEXT),
        ("  Grade      : ⭐ O — Outstanding", GREEN),
        ("  [✔] Student added!", GREEN),
    ])

    img.save(os.path.join(OUT, "02_add_student.png"))
    print("✔ 02_add_student.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 3 — DISPLAY ALL
# ══════════════════════════════════════════════════════════
def make_display():
    img, d = new_canvas()
    draw_header(d, "Display All")
    draw_sidebar(d, 1)

    mx = main_area_x()
    d.text((mx, 70), "All Students", font=F20, fill=TEXT)
    d.text((mx, 96), "All registered student records are listed below.", font=F13, fill=MUTED)

    # table
    tx1, ty1, tx2 = mx, 118, W-320
    draw_rect(d, tx1, ty1, tx2, ty1+32, fill=SURFACE2, outline=BORDER, radius=8)

    headers = ["Student ID", "Name", "Department", "Year", "Marks", "Grade"]
    col_x   = [tx1+10, tx1+100, tx1+240, tx1+360, tx1+410, tx1+470]
    for i, h in enumerate(headers):
        d.text((col_x[i], ty1+10), h, font=F11, fill=MUTED)

    rows = [
        ("S001", "Ravi Kumar",       "CSE-AIML", "2", "92.0",  "⭐ O — Outstanding",  DARK_GREEN_BG,  GREEN),
        ("S002", "Priya Sharma",     "CSE-AIML", "3", "78.0",  "🔵 A+ — Excellent",   DARK_BLUE_BG,   BLUE),
        ("S003", "Arjun Reddy",      "CSE-AIML", "1", "65.0",  "✅ A — Very Good",    DARK_GREEN_BG,  GREEN),
        ("S004", "Sneha Patel",      "CSE-AIML", "4", "54.0",  "🟡 B+ — Good",        DARK_YELLOW_BG, YELLOW),
        ("S005", "Mohammed Farhan",  "CSE-AIML", "2", "45.0",  "🟠 B — Average",      DARK_ORANGE_BG, ORANGE),
        ("S006", "Divya Nair",       "CSE-AIML", "3", "88.0",  "🔵 A+ — Excellent",   DARK_BLUE_BG,   BLUE),
        ("S007", "Kiran Babu",       "CSE-AIML", "1", "35.0",  "❌ F — Fail",         DARK_RED_BG,    RED),
        ("S008", "Lakshmi Devi",     "CSE-AIML", "4", "95.0",  "⭐ O — Outstanding",  DARK_GREEN_BG,  GREEN),
        ("S009", "Suresh Varma",     "CSE-AIML", "2", "61.0",  "✅ A — Very Good",    DARK_GREEN_BG,  GREEN),
        ("S010", "Anjali Menon",     "CSE-AIML", "3", "50.0",  "🟡 B+ — Good",        DARK_YELLOW_BG, YELLOW),
    ]
    row_h = 30
    for ri, (sid, name, dept, yr, marks, grade_lbl, gbg, gcol) in enumerate(rows):
        ry = ty1 + 32 + ri * row_h
        row_bg = BG if ri % 2 == 0 else (18, 22, 28)
        d.rectangle([tx1, ry, tx2, ry+row_h], fill=row_bg)
        d.text((col_x[0], ry+8), sid,       font=F11, fill=BLUE)
        d.text((col_x[1], ry+8), name,      font=F11, fill=TEXT)
        d.text((col_x[2], ry+8), dept,      font=F11, fill=MUTED)
        d.text((col_x[3], ry+8), yr,        font=F11, fill=TEXT)
        d.text((col_x[4], ry+8), marks,     font=F11, fill=TEXT)
        # grade pill
        gw = d.textlength(grade_lbl, font=F11) + 16
        draw_rect(d, col_x[5], ry+5, col_x[5]+int(gw), ry+25, fill=gbg, outline=gcol, radius=8)
        d.text((col_x[5]+8, ry+9), grade_lbl, font=F10, fill=gcol)

    # bottom border
    d.rectangle([tx1, ty1, tx2, ty1+32+len(rows)*row_h], outline=BORDER)

    draw_terminal(d, [
        ("[✔] Displaying 10 student(s).", GREEN),
        ("", MUTED),
        ("  S001  Ravi Kumar    92 → ⭐O", GREEN),
        ("  S002  Priya Sharma  78 → 🔵A+", BLUE),
        ("  S003  Arjun Reddy   65 → ✅A", GREEN),
        ("  S004  Sneha Patel   54 → 🟡B+", YELLOW),
        ("  S007  Kiran Babu    35 → ❌F", RED),
        ("  S008  Lakshmi Devi  95 → ⭐O", GREEN),
    ])

    img.save(os.path.join(OUT, "03_display_all.png"))
    print("✔ 03_display_all.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 4 — SEARCH
# ══════════════════════════════════════════════════════════
def make_search():
    img, d = new_canvas()
    draw_header(d, "Search")
    draw_sidebar(d, 2)

    mx = main_area_x()
    d.text((mx, 70), "Search Student", font=F20, fill=TEXT)
    d.text((mx, 96), "Enter a Student ID to view the full profile.", font=F13, fill=MUTED)

    # search bar
    draw_rect(d, mx, 120, mx+300, 148, fill=BG, outline=BLUE, radius=6)
    d.text((mx+12, 128), "S008", font=F13, fill=TEXT)
    draw_rect(d, mx+310, 120, mx+410, 148, fill=(35,134,54), outline=(46,160,67), radius=6)
    d.text((mx+330, 128), "🔍 Search", font=F13, fill=WHITE)

    # profile card
    card_x1, card_y1 = mx, 168
    card_x2, card_y2 = mx+400, H-20
    draw_rect(d, card_x1, card_y1, card_x2, card_y2, fill=SURFACE, outline=BORDER, radius=10)

    # avatar
    d.ellipse([card_x1+20, card_y1+16, card_x1+68, card_y1+64], fill=(31,111,235))
    d.text((card_x1+30, card_y1+24), "LD", font=F20, fill=WHITE)

    d.text((card_x1+80, card_y1+20), "S008", font=F11, fill=BLUE)
    d.text((card_x1+80, card_y1+36), "Lakshmi Devi", font=F16, fill=TEXT)
    d.text((card_x1+80, card_y1+58), "CSE-AIML", font=F11, fill=MUTED)

    d.line([card_x1+20, card_y1+82, card_x2-20, card_y1+82], fill=BORDER, width=1)

    rows = [
        ("Academic Year", "Year 4"),
        ("Marks",         "95.0 / 100"),
        ("Grade",         "⭐  O — Outstanding"),
    ]
    for i, (lbl, val) in enumerate(rows):
        ry = card_y1 + 96 + i*48
        d.text((card_x1+20, ry), lbl, font=F11, fill=MUTED)
        if lbl == "Grade":
            gw = d.textlength(val, font=F13) + 20
            draw_rect(d, card_x1+140, ry-4, card_x1+140+int(gw), ry+22, fill=DARK_GREEN_BG, outline=GREEN, radius=10)
            d.text((card_x1+150, ry), val, font=F13, fill=GREEN)
        elif lbl == "Marks":
            d.text((card_x1+140, ry), val, font=F13, fill=TEXT)
            # progress bar
            d.rectangle([card_x1+140, ry+20, card_x1+340, ry+26], fill=BORDER)
            d.rectangle([card_x1+140, ry+20, card_x1+140+int(200*0.95), ry+26], fill=GREEN)
        else:
            d.text((card_x1+140, ry), val, font=F13, fill=TEXT)
        d.line([card_x1+20, ry+36, card_x2-20, ry+36], fill=SURFACE2, width=1)

    draw_terminal(d, [
        ("══ SEARCH RESULT ══", CYAN),
        ("", MUTED),
        ("[✔] Found: Lakshmi Devi (S008)", GREEN),
        ("    Grade: ⭐ O — Outstanding", GREEN),
        ("", MUTED),
        ("══ SEARCH RESULT ══", CYAN),
        ("[✔] Found: Ravi Kumar (S001)", GREEN),
        ("    Grade: ⭐ O — Outstanding", GREEN),
    ])

    img.save(os.path.join(OUT, "04_search.png"))
    print("✔ 04_search.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 5 — UPDATE
# ══════════════════════════════════════════════════════════
def make_update():
    img, d = new_canvas()
    draw_header(d, "Update")
    draw_sidebar(d, 3)

    mx = main_area_x()
    d.text((mx, 70), "Update Student", font=F20, fill=TEXT)
    d.text((mx, 96), "Find a student by ID, then edit their details.", font=F13, fill=MUTED)

    draw_rect(d, mx, 118, W-320, H-20, fill=SURFACE, outline=BORDER, radius=10)

    # find row
    d.text((mx+18, 134), "STUDENT ID TO UPDATE", font=F10, fill=MUTED)
    draw_rect(d, mx+18, 150, mx+280, 176, fill=BG, outline=BORDER, radius=6)
    d.text((mx+30, 158), "S007", font=F13, fill=TEXT)
    draw_rect(d, mx+290, 150, mx+370, 176, fill=(31,111,235), outline=(88,166,255), radius=6)
    d.text((mx+315, 158), "Find", font=F13, fill=WHITE)

    # divider
    d.line([mx+18, 196, W-338, 196], fill=BORDER, width=1)
    d.text((mx+18, 204), "Student found — enter new details:", font=F12, fill=MUTED)

    fields2 = [
        ("FULL NAME",   "Kiran Babu",  mx+18,  224),
        ("DEPARTMENT",  "CSE-AIML",    mx+18,  294),
        ("MARKS (0-100)","72",          mx+18,  364),
    ]
    fw = 220
    for lbl, val, fx, fy in fields2:
        d.text((fx, fy), lbl, font=F10, fill=MUTED)
        draw_rect(d, fx, fy+16, fx+fw, fy+42, fill=BG, outline=BLUE, radius=6)
        d.text((fx+12, fy+24), val, font=F13, fill=TEXT)

    # year beside dept
    d.text((mx+18+fw+20, 294), "ACADEMIC YEAR", font=F10, fill=MUTED)
    draw_rect(d, mx+18+fw+20, 310, mx+18+fw*2+20, 336, fill=BG, outline=BORDER, radius=6)
    d.text((mx+30+fw+20, 318), "1st Year  ▾", font=F13, fill=TEXT)

    draw_rect(d, mx+18, 430, mx+178, 458, fill=(35,134,54), outline=(46,160,67), radius=8)
    d.text((mx+30, 438), "💾 Save Changes", font=F13, fill=WHITE)
    draw_rect(d, mx+188, 430, mx+278, 458, fill=SURFACE2, outline=BORDER, radius=8)
    d.text((mx+210, 438), "Cancel", font=F13, fill=MUTED)

    draw_terminal(d, [
        ("[i] Found \"Kiran Babu\"", BLUE),
        ("    Edit fields & click Save.", MUTED),
        ("", MUTED),
        ("[✔] Updated: S007 | Kiran Babu", GREEN),
        ("    Marks: 72 | ✅ A — Very Good", GREEN),
        ("", MUTED),
        ("  Grade changed:", MUTED),
        ("  ❌ F — Fail  →  ✅ A", GREEN),
    ])

    img.save(os.path.join(OUT, "05_update.png"))
    print("✔ 05_update.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 6 — DELETE
# ══════════════════════════════════════════════════════════
def make_delete():
    img, d = new_canvas()
    draw_header(d, "Delete")
    draw_sidebar(d, 4)

    mx = main_area_x()
    d.text((mx, 70), "Delete Student", font=F20, fill=TEXT)
    d.text((mx, 96), "Enter a Student ID to permanently remove the record.", font=F13, fill=MUTED)

    draw_rect(d, mx, 118, mx+420, 280, fill=SURFACE, outline=BORDER, radius=10)
    d.text((mx+20, 134), "STUDENT ID", font=F10, fill=MUTED)
    draw_rect(d, mx+20, 150, mx+400, 178, fill=BG, outline=BORDER, radius=6)
    d.text((mx+32, 158), "S010", font=F13, fill=TEXT)

    draw_rect(d, mx+20, 196, mx+190, 224, fill=(218,54,51), outline=(248,81,73), radius=8)
    d.text((mx+35, 204), "🗑️  Delete Student", font=F13, fill=WHITE)
    draw_rect(d, mx+200, 196, mx+290, 224, fill=SURFACE2, outline=BORDER, radius=8)
    d.text((mx+222, 204), "Clear", font=F13, fill=MUTED)

    # confirmation modal overlay
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 160))
    img.paste(Image.new("RGB", (W, H), (0,0,0)), mask=overlay.split()[3])

    # modal box
    mx2, my2 = W//2-200, H//2-110
    draw_rect(d, mx2, my2, mx2+400, my2+220, fill=SURFACE, outline=BORDER, radius=12)
    d.text((mx2+20, my2+20), "⚠️  Confirm Deletion", font=F16, fill=TEXT)
    d.text((mx2+20, my2+52), 'Delete "Anjali Menon" (S010)?', font=F13, fill=MUTED)
    d.text((mx2+20, my2+70), "This cannot be undone.", font=F13, fill=MUTED)

    draw_rect(d, mx2+180, my2+140, mx2+290, my2+170, fill=SURFACE2, outline=BORDER, radius=8)
    d.text((mx2+210, my2+149), "Cancel", font=F13, fill=MUTED)
    draw_rect(d, mx2+300, my2+140, mx2+380, my2+170, fill=(218,54,51), outline=(248,81,73), radius=8)
    d.text((mx2+320, my2+149), "Delete", font=F13, fill=WHITE)

    draw_terminal(d, [
        ("══ DELETE ══", CYAN),
        ("", MUTED),
        ("Found: Anjali Menon (S010)", TEXT),
        ("Awaiting confirmation...", YELLOW),
        ("", MUTED),
        ("[✔] Deleted: Anjali Menon (S010)", RED),
        ("  9 students remaining.", MUTED),
    ])

    img.save(os.path.join(OUT, "06_delete.png"))
    print("✔ 06_delete.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 7 — VIEW GRADE
# ══════════════════════════════════════════════════════════
def make_grade():
    img, d = new_canvas()
    draw_header(d, "Grade")
    draw_sidebar(d, 5)

    mx = main_area_x()
    d.text((mx, 70), "View Student Grade", font=F20, fill=TEXT)
    d.text((mx, 96), "Enter a Student ID to see the calculated grade.", font=F13, fill=MUTED)

    draw_rect(d, mx, 118, mx+400, 172, fill=SURFACE, outline=BORDER, radius=10)
    d.text((mx+20, 132), "STUDENT ID", font=F10, fill=MUTED)
    draw_rect(d, mx+20, 148, mx+240, 172, fill=BG, outline=BORDER, radius=6)
    d.text((mx+32, 155), "S001", font=F13, fill=TEXT)
    draw_rect(d, mx+250, 148, mx+380, 172, fill=(31,111,235), outline=BLUE, radius=6)
    d.text((mx+278, 155), "📊 View Grade", font=F13, fill=WHITE)

    # grade result card
    draw_rect(d, mx, 190, mx+420, H-20, fill=SURFACE, outline=BORDER, radius=10)

    rows = [
        ("Student",  "Ravi Kumar  (S001)"),
        ("Marks",    "92.0 / 100"),
        ("Grade",    "⭐  O — Outstanding"),
    ]
    for i, (lbl, val) in enumerate(rows):
        ry = 210 + i * 70
        d.line([mx+20, ry-5, mx+400, ry-5], fill=SURFACE2 if i>0 else SURFACE, width=1)
        d.text((mx+20, ry+8), lbl, font=F11, fill=MUTED)
        if lbl == "Grade":
            gw = d.textlength(val, font=F18) + 28
            draw_rect(d, mx+140, ry+2, mx+140+int(gw), ry+40, fill=DARK_GREEN_BG, outline=GREEN, radius=12)
            d.text((mx+154, ry+8), val, font=F18, fill=GREEN)
        elif lbl == "Marks":
            d.text((mx+140, ry+8), val, font=F14, fill=TEXT)
            d.rectangle([mx+140, ry+34, mx+360, ry+42], fill=BORDER)
            d.rectangle([mx+140, ry+34, mx+140+int(220*0.92), ry+42], fill=GREEN)
        else:
            d.text((mx+140, ry+8), val, font=F14, fill=TEXT)

    draw_terminal(d, [
        ("══ GRADE LOOKUP ══", CYAN),
        ("", MUTED),
        ("  S001 Ravi Kumar: 92 marks", TEXT),
        ("  ⭐ O — Outstanding", GREEN),
        ("", MUTED),
        ("  S008 Lakshmi Devi: 95 marks", TEXT),
        ("  ⭐ O — Outstanding", GREEN),
        ("  S007 Kiran Babu: 35 marks", TEXT),
        ("  ❌ F — Fail", RED),
    ])

    img.save(os.path.join(OUT, "07_view_grade.png"))
    print("✔ 07_view_grade.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 8 — TOTAL COUNT / STATS
# ══════════════════════════════════════════════════════════
def make_count():
    img, d = new_canvas()
    draw_header(d, "Count")
    draw_sidebar(d, 6)

    mx = main_area_x()
    d.text((mx, 70), "Total Student Count", font=F20, fill=TEXT)
    d.text((mx, 96), "Summary statistics for all registered students.", font=F13, fill=MUTED)

    stats = [
        ("🎓", "10",   "Total Students",      BLUE,   DARK_BLUE_BG,   BLUE),
        ("📈", "66.3", "Average Marks",        GREEN,  DARK_GREEN_BG,  GREEN),
        ("✅", "9",    "Students Passed",      GREEN,  DARK_GREEN_BG,  GREEN),
        ("⭐", "2",    "Outstanding (O Grade)",YELLOW, DARK_YELLOW_BG, YELLOW),
        ("❌", "1",    "Students Failed",      RED,    DARK_RED_BG,    RED),
        ("📅", "26/10","Report Date",          MUTED,  SURFACE2,       MUTED),
    ]

    cols = 3
    card_w = 170; card_h = 110
    gap    = 16
    start_x = mx
    start_y = 118

    for i, (icon, num, label, col, bg, border) in enumerate(stats):
        cx = start_x + (i % cols) * (card_w + gap)
        cy = start_y + (i // cols) * (card_h + gap)
        draw_rect(d, cx, cy, cx+card_w, cy+card_h, fill=SURFACE, outline=BORDER, radius=10)
        d.text((cx+16, cy+14), icon, font=F24, fill=col)
        d.text((cx+16, cy+46), num,  font=F28, fill=TEXT)
        d.text((cx+16, cy+82), label, font=F11, fill=MUTED)

    draw_terminal(d, [
        ("[i] Stats refreshed.", BLUE),
        ("", MUTED),
        ("  Total   : 10", TEXT),
        ("  Average : 66.3 marks", TEXT),
        ("  Passed  : 9", GREEN),
        ("  Failed  : 1", RED),
        ("  Outstanding : 2", YELLOW),
    ])

    img.save(os.path.join(OUT, "08_total_count.png"))
    print("✔ 08_total_count.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 9 — VALIDATION ERROR
# ══════════════════════════════════════════════════════════
def make_validation():
    img, d = new_canvas()
    draw_header(d, "Validation")
    draw_sidebar(d, 0)

    mx = main_area_x()
    d.text((mx, 70), "Input Validation & Error Handling", font=F20, fill=TEXT)
    d.text((mx, 96), "The system prevents invalid input at every step.", font=F13, fill=MUTED)

    draw_rect(d, mx, 118, W-320, H-20, fill=SURFACE, outline=BORDER, radius=10)

    errors = [
        ("STUDENT ID", "S001", True,  "[!] ID 'S001' already exists. Duplicate IDs not allowed."),
        ("MARKS",      "150",  True,  "[!] Please enter a value between 0.0 and 100.0."),
        ("YEAR",       "5",    True,  "[!] Please enter a number between 1 and 4."),
        ("FULL NAME",  "",     True,  "[!] Input cannot be empty. Please try again."),
    ]

    for i, (lbl, val, is_err, errmsg) in enumerate(errors):
        fy = 138 + i * 110
        d.text((mx+20, fy), lbl, font=F10, fill=MUTED)
        outline_col = RED if is_err else BORDER
        draw_rect(d, mx+20, fy+16, mx+360, fy+44, fill=BG, outline=outline_col, radius=6)
        d.text((mx+32, fy+24), val if val else "   (empty)", font=F13, fill=TEXT if val else MUTED)
        if is_err:
            d.text((mx+20, fy+52), errmsg, font=F12, fill=RED)

    draw_terminal(d, [
        ("══ VALIDATION ERRORS ══", CYAN),
        ("", MUTED),
        ("[!] Duplicate ID: S001", RED),
        ("[!] Marks 150 out of range", RED),
        ("[!] Year 5 out of range", RED),
        ("[!] Name cannot be empty", RED),
        ("", MUTED),
        ("  Fix errors & retry.", YELLOW),
    ])

    img.save(os.path.join(OUT, "09_validation.png"))
    print("✔ 09_validation.png")

# ══════════════════════════════════════════════════════════
#  SCREEN 10 — GRADE SCALE
# ══════════════════════════════════════════════════════════
def make_grade_scale():
    img, d = new_canvas()
    draw_header(d, "Grade Scale")
    draw_sidebar(d, 7)

    mx = main_area_x()
    d.text((mx, 70), "Grade Scale Reference", font=F20, fill=TEXT)
    d.text((mx, 96), "Grades are calculated automatically from marks entered.", font=F13, fill=MUTED)

    scale = [
        ("90 – 100", "⭐  O — Outstanding",  GREEN,  DARK_GREEN_BG),
        ("75 – 89",  "🔵  A+ — Excellent",   BLUE,   DARK_BLUE_BG),
        ("60 – 74",  "✅  A — Very Good",    GREEN,  DARK_GREEN_BG),
        ("50 – 59",  "🟡  B+ — Good",        YELLOW, DARK_YELLOW_BG),
        ("40 – 49",  "🟠  B — Average",      ORANGE, DARK_ORANGE_BG),
        ("Below 40", "❌  F — Fail",         RED,    DARK_RED_BG),
    ]

    sw = 420
    draw_rect(d, mx, 118, mx+sw, 118+len(scale)*56, fill=SURFACE, outline=BORDER, radius=10)
    for i, (rng, label, col, bg) in enumerate(scale):
        ry = 118 + i*56
        if i > 0:
            d.line([mx+20, ry, mx+sw-20, ry], fill=SURFACE2, width=1)
        d.text((mx+20, ry+16), rng, font=F13, fill=MUTED)
        gw = d.textlength(label, font=F14) + 22
        draw_rect(d, mx+120, ry+10, mx+120+int(gw), ry+42, fill=bg, outline=col, radius=10)
        d.text((mx+132, ry+16), label, font=F14, fill=col)

    d.text((mx, 118+len(scale)*56+16),
           "Matches calculateGrade() method in Student.java", font=F12, fill=MUTED)

    draw_terminal(d, [
        ("  Grade scale:", CYAN),
        ("  90-100 → O  Outstanding", GREEN),
        ("  75-89  → A+ Excellent",   BLUE),
        ("  60-74  → A  Very Good",   GREEN),
        ("  50-59  → B+ Good",        YELLOW),
        ("  40-49  → B  Average",     ORANGE),
        ("  <40    → F  Fail",        RED),
    ])

    img.save(os.path.join(OUT, "10_grade_scale.png"))
    print("✔ 10_grade_scale.png")

# ── RUN ALL ───────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating screenshots...")
    make_welcome()
    make_add()
    make_display()
    make_search()
    make_update()
    make_delete()
    make_grade()
    make_count()
    make_validation()
    make_grade_scale()
    print(f"\nAll 10 images saved to: {OUT}")
