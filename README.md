# Command-Line Contact Management System (Python)

A robust, interactive command-line application developed in Python to manage a personal contact book. This application was built from the ground up, evolving from a simple procedural script to a feature-rich, object-oriented program with data persistence.

![Demo Screenshot](link_to_your_screenshot.png) 
*(Optional: You can take a screenshot of your app running and add it here for a great visual effect!)*

---

### Core Features

-   **Data Persistence:** Contact information is saved to a `contacts.csv` file, ensuring data is not lost between sessions. The application automatically loads from this file on startup.
-   **Object-Oriented Design:** Uses a `Contact` class to model data, encapsulating contact attributes and methods for a cleaner, more scalable architecture.
-   **Full CRUD Functionality:**
    -   **Create:** Add new contacts with duplicate name prevention.
    -   **Read:** View a complete, formatted list of all contacts or search for specific contacts.
    -   **Update:** Modify the phone number and email for any existing contact.
    -   **Delete:** Remove contacts from the book.
-   **Smart Search:** Features a case-insensitive, partial-match search to easily find contacts without knowing their full name.
-   **Enhanced User Interface:** A colorful and intuitive UI using the `colorama` library provides clear feedback for success and error states.

---

### Technologies & Concepts Demonstrated

-   **Language:** Python 3
-   **Key Libraries:** `csv` (for data persistence), `os` (for file path handling), `colorama` (for UI).
-   **Core Concepts:**
    -   **Object-Oriented Programming (OOP):** Class and object creation, instance methods, and class methods.
    -   **Data Structures:** Expert use of lists and dictionaries, specifically the "list of objects" pattern.
    -   **File I/O:** Reading from and writing to CSV files.
    -   **Modular Programming:** Decomposing the application into single-responsibility functions.
    -   **Error Handling & Validation:** Duplicate entry prevention and graceful handling of missing files.
    -   **Version Control:** Project managed with Git, featuring incremental, feature-based commits.
    -   **Environment Adaptation:** The final version includes logic for running within a Google Colab environment and persisting data to Google Drive.

---

### How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<Your-Username>/<Your-Repository-Name>.git
    cd <Your-Repository-Name>
    ```
2.  **Install dependencies:**
    ```bash
    pip install colorama
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```
