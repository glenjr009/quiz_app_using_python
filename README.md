# Python GUI Quiz Application

A simple graphical quiz application built with Python and the Tkinter library. This tool reads questions from a SQLite database and records user scores in a CSV file, providing a user-friendly interface for an interactive quiz experience.

### Features ✨
-   **Graphical User Interface (GUI):** A clean and simple interface built with Python's standard Tkinter library.
-   **Database Integration:** Questions and answers are stored and fetched from a `quiz.db` SQLite database.
-   **Score Tracking:** User scores are saved to `quiz_scores.csv` for later review.
-   **Modular Design:** The core logic is separated into a main script and a test script.

### How to Run the Application 🚀

#### Prerequisites
-   Python 3.x installed on your system.
-   No external libraries are needed beyond Python's built-in `tkinter`, `sqlite3`, and `csv` modules.

#### Steps
1.  Clone this repository:
    ```bash
    git clone  https://github.com/glenjr009/quiz_app_using_python.git
    cd glenjr009/quiz_app_using_python
    ```
2.  Run the main script:
    ```bash
    python python.py
    ```
    The GUI window will appear, allowing you to start the quiz.

### File Structure 🗂️
-   `python.py`: The main script that runs the GUI and the quiz logic.
-   `quiz.db`: The SQLite database containing quiz questions.
-   `quiz_scores.csv`: The CSV file where user scores are saved.
-   `test.py`: A separate script for testing the application's functionality.

### License 📜
This project is licensed under the MIT License. See the `LICENSE` file for more details.
