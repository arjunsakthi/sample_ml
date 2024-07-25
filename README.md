# Stress Meter Project

## Overview

The Stress Meter project is a web application designed to measure and display a user's stress level. It allows users to input their stress level, which is then processed by a machine learning model to predict and display the result in a visually engaging manner. The application is built using HTML, CSS, JavaScript, Flask, and a pre-trained machine learning model.

It's just a Fun project to learn how to integerate flask and ml model and also how to interact with frontend

## Features

- **User Input:** Allows users to input their stress level via a number input and range slider.
- **Real-time Processing:** Sends the user input to a Flask backend for processing by a machine learning model.
- **Dynamic Display:** Updates the display with the processed stress level.
- **Responsive Design:** The application is responsive and works on different screen sizes.

## Technologies Used

- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn
- **Data Handling:** JSON
- **Cross-Origin Requests:** Flask-CORS

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-CORS
- Scikit-learn
- A pre-trained machine learning model saved as `my_model.pkl`

### Installation

1. **Clone the repository:**

```sh
git clone https://github.com/your-username/stress-meter.git
cd stress-meter
```

2. **Install the required Python packages:**

```sh
pip install flask flask-cors scikit-learn
```

3. **Prepare your machine learning model:**

Make sure you have a trained model saved as `my_model.pkl` in the project directory.

### Running the Application

1. **Start the Flask server:**

```sh
python app.py
```

2. **Open `index.html` in your web browser:**

Navigate to the project directory and open `index.html` in a web browser to view the application.

## Usage

1. **Enter Stress Level:**
   - Use the number input or the range slider to enter a stress level between 1 and 1000.

2. **Submit the Form:**
   - Click the "Submit" button to send the input to the Flask backend.

3. **View Results:**
   - The application will display the processed stress level and update the meter accordingly.

## Code Structure

- **app.py:** Flask backend to handle POST requests and process stress levels using a machine learning model.
- **index.html:** Main HTML file containing the structure of the web application.
- **style.css:** CSS file for styling the web application.
- **script.js:** JavaScript file for handling form submissions and updating the UI.
- **my_model.pkl:** Pre-trained machine learning model (Decision Tree in this case).

## Example Output

When the user submits their stress level, the application processes the input and displays the result in a styled box with capitalized text.

```html
<div class="box">
    <h1>Athul's Mind</h1>
    <p>Your stress level is: <span id="stress-level">50</span></p>
</div>
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome contributions that improve the functionality and usability of the application.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
