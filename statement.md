# Project Statement

## Problem Statement
Managing student accommodation records manually can be cumbersome and prone to errors, especially in a hostel with many residents. Hostel administrators need an efficient way to keep track of student details, room assignments, and fee payment statuses to streamline operations and reduce administrative overhead.

## Scope of the Project
This project provides a basic command-line application that manages student information for a hostel. It supports adding, viewing, and removing student records along with tracking fee payments. The data is stored persistently in a CSV file, enabling simple data management without requiring a complex database system. The project is intended to handle the core administrative tasks related to student accommodation management but does not cover advanced features like billing systems, multi-user access, or graphical interfaces.

## Target Users
- Hostel administrators and wardens who need to maintain student occupancy and fee status records.
- Small to medium-sized hostels where simple record keeping is sufficient.
- Educational institutions looking for a lightweight solution for managing hostel student data without heavy infrastructure.

## High-level Features
- Add new student entries with registration number, name, branch, room number, and fee status.
- View a list of all registered students with their room and fee details.
- Remove students from the system by registration number.
- Display statistics on total students, fee payments received, and pending fees.
- Automatic creation and maintenance of a CSV file to persist student data.
