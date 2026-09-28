# Hostel Management System

## Overview
This is a simple command-line based Hostel Management System written in Python. It allows hostel administrators to manage student records including registration details, room allocation, and fee status. The system stores data in a CSV file and provides basic functionalities to add, view, remove students, and view overall statistics about the students' fee status.

## Features
- Add new student records with registration number, name, branch, room number, and fee status.
- View all students currently registered in the system.
- Remove student records by registration number.
- View statistics such as total number of students, number of students who have paid fees, and those with pending fees.
- Persistent storage of student data in a CSV file (`data/students.csv`).

## Technologies/Tools Used
- Python 3.x
- CSV module for file handling
- OS module for directory and file operations

## Steps to Install & Run the Project
1. **Prerequisites:**  
   Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Project:**  
   Download the project files or clone the repository to your local machine.

3. **Run the Program:**  
   Open a terminal or command prompt in the project directory and run:
   ```bash
   python <main>.py

4. **Data Storage:**
The program will create a folder named data and a CSV file students.csv inside it automatically if they do not exist.

5. **Screenshots**

![alt text](<Screenshot (15).png>) ![alt text](<Screenshot (16).png>) ![alt text](<Screenshot (17).png>) ![alt text](<Screenshot (18).png>) ![alt text](<Screenshot (19).png>) ![alt text](<Screenshot (20).png>) ![alt text](<Screenshot (21).png>) ![alt text](<Screenshot (22).png>) ![alt text](<Screenshot (23).png>) ![alt text](<Screenshot (24).png>)

6. **Instructions for Testing**

Launch the program by running the Python script.

Use the menu options to:

Add students by entering required details.

View all student records.

Remove a student by entering their registration number.

View statistics about student fees.

Test for duplicate registration numbers by trying to add a student with an existing registration number.

Try removing a non-existent registration number to check error handling.

Exit the program by selecting the quit option.