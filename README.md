# Python Password Generator

## 📌 Overview
A simple Python project that generates secure, random passwords based on user-defined length. The program ensures passwords contain a mix of uppercase, lowercase, numbers, and special characters.

## ⚙️ Features
- Generates random passwords of a user-specified length (minimum 7 characters).
- Ensures passwords include letters, numbers, and special characters.
- Provides a simple, interactive command-line interface.
- stores generated passwords to a text file with the date they were created 

## 🛠️ Tools Used
- Python (standard library only)
- Random module for character shuffling and selection
- Datetime module for generated passwords

## 🚀 How to Run
1. Clone or download the repository.
2. Run the script in your terminal or command line:

```bash
python password_generator.py
```

3. Follow the on-screen prompts to enter your desired password length.
4. The generated password will be displayed,You may copy it and you can press Enter to exit the terminal
5. The generated password will be available in a text file of the same directory as the python script 

## 📌 Notes
* The program validates input to ensure the password length is at least 7 characters.
* Passwords are randomly generated and cannot be predicted.
* No external libraries are required; fully self-contained using Python standard library.
