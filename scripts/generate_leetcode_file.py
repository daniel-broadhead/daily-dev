import os
from datetime import datetime

def slugify(title):
    return title.lower().replace(" ", "_").replace("-", "_")

def generate_leetcode_file(problem_number, title, link, difficulty):
    # Format problem number with leading zeros
    number = str(problem_number).zfill(4)
    filename = f"{number}_{slugify(title)}.py"
    folder = f"scripts/leetcode/{difficulty.lower()}"

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    boilerplate = f'''"""
Problem: {title} (LeetCode #{problem_number})
Link: {link}
Date: {datetime.today().date()}

[Write a brief description or paste the original prompt here.]

Approach:
- [Explain your approach here]

Time complexity: O(?)
Space complexity: O(?)
"""

from typing import List

class Solution:
    def {slugify(title)}(self, ...):  # Update params
        pass

# Example test
if __name__ == "__main__":
    # Add test cases
    pass
'''

    with open(path, "w") as f:
        f.write(boilerplate)

    print(f"✅ File created: {path}")

# Example usage:
if __name__ == "__main__":
    problem_number = input("Problem number: ").strip()
    title = input("Problem title: ").strip()
    link = input("LeetCode link: ").strip()
    difficulty = input("Difficulty (easy/medium/hard): ").strip().lower()

    if difficulty not in {"easy", "medium", "hard"}:
        print("❌ Difficulty must be: easy, medium, or hard.")
    else:
        generate_leetcode_file(problem_number, title, link, difficulty)
