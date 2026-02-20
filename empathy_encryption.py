"""
The Empathy Encryption – Hackathon Submission (GUI Version)
------------------------------------------------------------

Author: [Your Name]
Event: UnsaidTalks Hackathon

INTERPRETATION OF PRODUCT GUIDANCE
-----------------------------------

The product team did not define rigid complexity rules.
Instead, they described behavioral expectations.

Therefore, this solution:

• Encourages structured, readable passwords
• Discourages brute-force friendly patterns
• Avoids visually confusing character combinations
• Detects keyboard smashing behavior
• Balances repetition and variation
• Promotes thoughtful human-created patterns

Rather than enforcing extreme complexity,
this validator focuses on intelligent pattern recognition.

Core Function Required by Problem:
    is_valid_password(password: str) -> bool
"""

import re
import tkinter as tk


# ==========================================================
# CORE VALIDATION FUNCTION (Required by Problem Statement)
# ==========================================================

def is_valid_password(password: str) -> bool:
    """
    Determines if password aligns with product expectations.
    Returns True (Accepted) or False (Rejected).

    This function prioritizes:
    - Human intentionality
    - Readability
    - Structural balance
    - Moderate security
    """

    # 1️⃣ Length Constraint (reasonable security)
    if len(password) < 8 or len(password) > 16:
        return False

    # 2️⃣ Character Diversity (structured variation)
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False

    # 3️⃣ Excessive repetition check
    if re.search(r"(.)\1\1\1", password):
        return False

    # 4️⃣ Avoid overly predictable sequences
    predictable = ["1234", "abcd", "qwerty", "0000", "1111", "password"]
    for seq in predictable:
        if seq.lower() in password.lower():
            return False

    # 5️⃣ Avoid visually confusing combinations
    confusing = ["O0", "0O", "l1", "1l", "I1"]
    for pattern in confusing:
        if pattern in password:
            return False

    # 6️⃣ Detect keyboard smashing (no vowels = low intentionality)
    if not re.search(r"[aeiouAEIOU]", password):
        return False

    # 7️⃣ Special character balance
    special_chars = re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)
    if len(special_chars) > 3:
        return False

    return True


# ==========================================================
# OPTIONAL FEEDBACK FUNCTION (Enhances GUI Experience)
# ==========================================================

def evaluate_password(password: str):
    """
    Returns detailed feedback for GUI display.
    This does NOT replace is_valid_password.
    It enhances usability.
    """

    feedback = []
    score = 0

    if 8 <= len(password) <= 16:
        score += 1
    else:
        feedback.append("Use 8–16 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if not re.search(r"(.)\1\1\1", password):
        score += 1
    else:
        feedback.append("Avoid repeating characters.")

    if not any(seq in password.lower() for seq in ["1234", "abcd", "qwerty"]):
        score += 1
    else:
        feedback.append("Avoid predictable sequences.")

    if not any(pattern in password for pattern in ["O0", "l1", "I1"]):
        score += 1
    else:
        feedback.append("Avoid visually confusing characters.")

    if re.search(r"[aeiouAEIOU]", password):
        score += 1
    else:
        feedback.append("Include a vowel for readability.")

    return score, feedback


# ==========================================================
# GUI IMPLEMENTATION (Product Demonstration Layer)
# ==========================================================

def check_password():
    password = entry.get()

    score, feedback = evaluate_password(password)

    if is_valid_password(password):
        result_label.config(text=f"✅ Accepted (Score: {score}/8)", fg="green")
        feedback_label.config(text="Thoughtful and well-structured password.")
    else:
        result_label.config(text=f"❌ Rejected (Score: {score}/8)", fg="red")
        feedback_label.config(text="\n".join(feedback))


# Create GUI window
root = tk.Tk()
root.title("Empathy Encryption")
root.geometry("500x400")
root.configure(bg="#ffe6f2")

title = tk.Label(
    root,
    text="🔐 Empathy Encryption",
    font=("Arial", 18, "bold"),
    bg="#ffe6f2"
)
title.pack(pady=15)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(
    root,
    text="Validate Password",
    command=check_password,
    bg="#ff99cc",
    font=("Arial", 11)
)
button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#ffe6f2"
)
result_label.pack(pady=10)

feedback_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#ffe6f2",
    wraplength=450
)
feedback_label.pack(pady=10)

root.mainloop()


"""
---------------------------------------------------
List of 10 Accepted Passwords According to My Logic
---------------------------------------------------

1. SunRise2024
2. BlueMoon89
3. CalmRiver7
4. WinterSky21
5. FreshStart9
6. GoldenLeaf5
7. OceanWave12
8. DreamBuild3
9. BrightPath8
10. SilentHill4


---------------------------------------------------
List of 10 Rejected Passwords According to My Logic
---------------------------------------------------

1. 12345678
2. abcd1234
3. qwerty123
4. AAAAA1111
5. asdkjh123!!
6. O0PassWord
7. l1Secure
8. !!!@@@###
9. Zxcvbnm1
10. password123

"""