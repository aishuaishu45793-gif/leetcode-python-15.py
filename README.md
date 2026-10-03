# LeetCode Python Practice 18 🐍

## 📌 About the Project

This repository contains my **LeetCode and Python problem-solving practice**.
The goal is to improve my Python programming skills, logical thinking, and understanding of Data Structures and Algorithms (DSA).

## 🎯 Objectives

* Practice Python programming regularly
* Improve problem-solving and logical thinking
* Learn important DSA concepts
* Solve LeetCode-style coding problems
* Improve coding speed and accuracy
* Build a consistent coding practice habit

## 🛠️ Technologies Used

* **Python 3**
* **VS Code**
* **Git**
* **GitHub**
* **LeetCode**

## 📚 Topics Covered

This practice repository includes problems related to:

* Python Basics
* Variables and Data Types
* Conditions
* Loops
* Functions
* Strings
* Lists
* Dictionaries
* Sets
* Searching
* Sorting
* Arrays
* Problem Solving
* Basic DSA

## 💡 Example Problem

### Two Sum

Given an array of integers and a target value, find two numbers whose sum equals the target.

Example:

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

Python solution:

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()

nums = [2, 7, 11, 15]
target = 9

print(solution.twoSum(nums, target))
```

Output:

```text
[0, 1]
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/aishuaishu45793-gif/leetcode-python18.py.git
```

### Step 3: Open the Project

Open the folder in **VS Code**.

### Step 4: Run a Python File

```bash
python filename.py
```

## 📂 Project Structure

```text
leetcode-python18.py/
│
├── problem1.py
├── problem2.py
├── problem3.py
├── problem4.py
├── problem5.py
│
└── README.md
```

## 🧠 Problem-Solving Approach

For each problem, I follow these steps:

1. Understand the problem
2. Identify the inputs and outputs
3. Think about a simple solution
4. Write the Python code
5. Test the code with examples
6. Check edge cases
7. Improve the solution when possible
8. Upload the solution to GitHub

## 📈 Learning Progress

Through this practice, I am improving my understanding of:

* Python syntax
* Problem-solving techniques
* Arrays and strings
* Loops and conditions
* Functions
* Searching and sorting
* Basic DSA concepts
* Writing clean and readable code
* Using Git and GitHub

## 🔄 GitHub Workflow

I use the following commands to save my practice:

```bash
git add .
git commit -m "Add LeetCode Python practice"
git push
```

## 🚀 Future Goals

* Solve more LeetCode problems
* Learn advanced DSA
* Improve time and space complexity
* Practice Dynamic Programming
* Learn Trees and Graphs
* Solve medium and hard problems
* Build more Python projects

## 🎓 Learning Outcomes

This repository helps me develop:

* Stronger Python programming skills
* Better logical thinking
* Problem-solving ability
* DSA knowledge
* Git and GitHub experience
* Consistent coding practice

## 👩‍💻 Author

**Aishwarya**

GitHub:
[aishuaishu45793-gif](https://github.com/aishuaishu45793-gif?utm_source=chatgpt.com)

---

⭐ This repository represents my continuous journey of learning **Python, LeetCode, and Data Structures & Algorithms**.
