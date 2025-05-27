# Password Generator

## Overview
This Python script generates random passwords based on user-selected complexity levels and desired length. The program offers three password types with varying complexity and ensures the password length does not exceed 15 characters.

## Code Explanation

### Main Components

1. **Main Function (`main()`)**
   - Prompts the user to select a password type (1-3)
   - Asks for the desired password length (up to 15 characters)
   - Handles invalid inputs with try-except blocks
   - Calls the `system()` function with user inputs and displays the generated password

2. **Password Generation System (`system()`)**
   - Takes two parameters: `selection` (password type) and `entry` (password length)
   - Validates that the selection is between 1-3 and length ≤ 15
   - Generates passwords based on the selected type:
     - **Type 1**: Letters only (uppercase and lowercase)
     - **Type 2**: Letters and numbers
     - **Type 3**: Letters, numbers, and special characters (!@#$%)

3. **Generator Functions**
   - `letter_generator()`: Returns a random uppercase or lowercase letter
   - `number_generator()`: Returns a random digit (0-9)
   - `special_character_generator()`: Returns a random special character from !@#$%

### How It Works

1. The program starts by asking the user to choose a password complexity level:
   - 1 for Letters only
   - 2 for Letters and Numbers
   - 3 for Letters, Numbers, and Special Characters

2. The user then specifies the desired password length (up to 15 characters).

3. Based on the selections:
   - For Type 1: Only letters are used
   - For Type 2: Randomly alternates between letters and numbers
   - For Type 3: Randomly selects between letters, numbers, and special characters

4. The program builds the password character by character until it reaches the requested length.

5. Input validation ensures:
   - Only numbers are accepted for both selections
   - Password length doesn't exceed 15 characters
   - Only options 1-3 are accepted for password type

## Example Usage

```
What should your password be?
Please enter the desired number
1-Letters
2-Letters & Numbers
3-Letters & Numbers & Special Characters
2
How many characters should be in your password? 10
X7j9K2lP5q
```

## Limitations
- Maximum password length is fixed at 15 characters
- Limited set of special characters (!@#$%)
- No option to exclude uppercase/lowercase letters
- No password strength indicator

## Requirements
- Python 3.x
- Standard library modules: `random`

# Flask Web Application

## Overview
This is a basic Flask web application that serves a single webpage. Flask is a lightweight Python web framework that allows you to quickly create web applications with minimal setup.

## Code Explanation

### 1. Import Statements
```python
from flask import Flask, render_template
```
- **Flask**: The main Flask class used to create the web application instance
- **render_template**: A function that processes Jinja2 templates (HTML files with dynamic content)

### 2. Application Initialization
```python
app = Flask(__name__)
```
- Creates a Flask application instance
- `__name__` tells Flask where to look for templates and static files
- The `app` variable will be our WSGI application

### 3. Route Definition
```python
@app.route('/')
def home():
    return render_template('main_page.html')
```
- `@app.route('/')`: A decorator that registers the following function to handle requests to the root URL ('/')
- When users visit the root URL, Flask will call the `home()` function
- `render_template('main_page.html')`: Looks for a file called `main_page.html` in the `templates/` folder and returns its content

### 4. Application Execution
```python
if __name__ == '__main__':
    app.run(debug=True)
```
- Standard Python idiom to ensure the code only runs when executed directly (not when imported)
- `app.run(debug=True)`: Starts the Flask development server
  - `debug=True` enables:
    - Automatic reloader (server restarts when code changes)
    - Detailed error messages in the browser
    - Debugger for troubleshooting

## File Structure Requirements
For this to work properly, you need:
```
your_project/
├── app.py                # This Flask application file
└── templates/
    └── main_page.html    # Your HTML template file
```

## How to Run
1. Save this code in a file (typically `app.py`)
2. Create a `templates` folder in the same directory
3. Add your `main_page.html` file in the templates folder
4. Run the application with `python app.py`
5. Visit `http://localhost:5000` in your web browser

## Key Features
- Minimal setup for a web application
- Automatic template rendering
- Built-in development server
- Debug mode for easier development

## Notes
- This is a development server - not suitable for production
- By default, the server is only accessible from your local machine
- The default port is 5000 (can be changed with `app.run(port=5001)`)

Here's a detailed explanation of the HTML code for the SecurePass Generator:

# SecurePass Generator - HTML/CSS/JavaScript Breakdown

## 1. Basic Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Metadata and resources -->
</head>
<body>
    <!-- Page content -->
</body>
</html>
```
- Standard HTML5 document structure with English language setting
- Contains `head` (for metadata) and `body` (for visible content)

## 2. Head Section
```html
<head>
    <meta charset="UTF-8"> <!-- Character encoding -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Responsive design -->
    <title>SecurePass Generator</title> <!-- Browser tab title -->
    
    <!-- External resources -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    
    <!-- Embedded CSS -->
    <style>
        /* All CSS styles */
    </style>
</head>
```
- Sets up responsive viewport
- Loads Google Fonts (Poppins) and Font Awesome icons
- Contains all CSS directly in the document

## 3. CSS Styles (Key Features)
```css
:root {
    /* CSS variables for consistent theming */
}

body {
    /* Gradient background and centering */
}

.container {
    /* White card with shadow and animation */
}

.header {
    /* Gradient header with lock icon */
}

.form-group {
    /* Styled form inputs with custom dropdown arrow */
}

.btn {
    /* Gradient button with hover effects */
}

.result {
    /* Password display area with copy button */
}

.strength-meter {
    /* Visual password strength indicator */
}

.error {
    /* Animated error messages */
}

@media (max-width: 576px) {
    /* Responsive adjustments */
}
```
- Uses CSS variables for easy theming
- Includes animations (fadeIn, hover effects)
- Mobile-responsive design
- Visual feedback for interactions

## 4. Body Content
```html
<body>
    <div class="container">
        <div class="header">
            <i class="fas fa-lock"></i>
            <h1>SecurePass Generator</h1>
            <p>Create strong, secure passwords instantly</p>
        </div>
        
        <div class="content">
            <!-- Password type dropdown -->
            <div class="form-group">
                <select id="passwordType">
                    <option value="1">Letters only</option>
                    <option value="2">Letters & Numbers</option>
                    <option value="3">Letters, Numbers & Special Characters</option>
                </select>
            </div>
            
            <!-- Password length input -->
            <div class="form-group">
                <input type="number" id="passwordLength" min="1" max="15" value="12">
            </div>
            
            <!-- Generate button -->
            <button class="btn" onclick="generatePassword()">
                <i class="fas fa-key"></i> Generate Password
            </button>
            
            <!-- Error display -->
            <div id="error" class="error"></div>
            
            <!-- Result section -->
            <div class="result-container">
                <div class="result" id="result">Click "Generate" to create a password</div>
                <button class="copy-btn" onclick="copyToClipboard()">
                    <i class="far fa-copy"></i>
                </button>
                <div class="strength-meter">
                    <div class="strength-bar" id="strengthBar"></div>
                </div>
                <div class="strength-labels">
                    <span>Weak</span>
                    <span>Medium</span>
                    <span>Strong</span>
                </div>
            </div>
            
            <!-- Features tags -->
            <div class="features">
                <div class="feature">
                    <i class="fas fa-check-circle"></i> Secure
                </div>
                <!-- ... more features ... -->
            </div>
        </div>
    </div>
```
- Clean, card-based layout
- Three main interactive elements:
  1. Password type selector
  2. Length input (1-15 characters)
  3. Generate button
- Visual password strength meter
- Copy-to-clipboard functionality
- Error handling display

## 5. JavaScript Functionality
```javascript
// Main password generation function
function generatePassword() {
    // Gets user inputs and validates them
    // Calls password generation system
    // Displays result and updates strength meter
}

// Password generation logic
function generatePasswordSystem(selection, entry) {
    // Creates password based on type and length
    // Uses different character sets for each type
}

// Character generators
function letterGenerator() { /* ... */ }
function numberGenerator() { /* ... */ }
function specialCharacterGenerator() { /* ... */ }

// UI functions
function displayPassword(password) { /* ... */ }
function showError(message) { /* ... */ }
function updateStrengthMeter(selection, length) { /* ... */ }
function copyToClipboard() { /* ... */ }
```
Key features:
- Input validation
- Three password complexity levels
- Visual feedback (animations, strength meter)
- Clipboard copy functionality
- Error handling

## 6. Key Features Summary
1. **User-Friendly Interface**
   - Clean, modern design with animations
   - Responsive layout works on all devices
   - Visual feedback for all actions

2. **Password Generation Options**
   - Three complexity levels
   - Customizable length (1-15 characters)
   - Visual strength indicator

3. **Technical Features**
   - Pure client-side operation (no server needed)
   - Secure random number generation
   - Copy-to-clipboard functionality
   - Comprehensive error handling

4. **Visual Design**
   - Consistent color scheme using CSS variables
   - Smooth transitions and animations
   - Professional typography and icons

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.