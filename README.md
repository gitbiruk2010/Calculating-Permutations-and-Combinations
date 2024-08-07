# Permutations and Combinations Calculator

This is a web application that calculates permutations and combinations based on user input. The application allows users to enter values for `n` (total items) and `r` (items to be chosen or arranged), and then displays the results. The app is built using Python and Flask for the backend, and HTML, CSS, and JavaScript for the frontend.

## Screenshots
![Premutation and combination screenshot](https://github.com/user-attachments/assets/a19cb44a-4d21-4c3a-8587-b8919fb40865)

## Features

- **Calculate Permutations**: The application calculates permutations using the formula `P(n, r) = n! / (n - r)!`.
- **Calculate Combinations**: The application calculates combinations using the formula `C(n, r) = n! / (r! * (n - r)!)`.
- **Error Handling**: Provides error messages for invalid inputs, such as when `r` is greater than `n`.
- **Test Cases**: Integrated test cases to ensure the accuracy and reliability of the calculations.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
   git clone https://github.com/gitbiruk2010/Calculating-Permutations-and-Combinations
2. Navigate to the project directory: cd permutations-combinations-calculator
3. Install the required python packages: pip install flask

## Running the Application
Start the Flask application: python app.py
Directory structure:
/permutations-combinations-calculator
│
├── app.py                  # The main Flask application
├── /static                 # Static files (CSS, JavaScript, etc.)
│   ├── /css
│   │   └── styles.css      # Stylesheet for the application
│
└── /templates              # HTML templates
    └── index.html          # Main HTML file

## Usage:
    Enter the total number of items (n) and the number of items to choose or arrange (r).
    Click on the "Calculate" button.
    The results for permutations and combinations will be displayed below the form.
