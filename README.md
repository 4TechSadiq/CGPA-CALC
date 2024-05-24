# CGPA Calc

## Overview
This project is a CGPA (Cumulative Grade Point Average) calculator designed to help students calculate their CGPA both manually and automatically through image processing. The application is built using Flask and Python, with integrated image processing to extract marks from images.

## Features
- **Manual Calculation**: Manually input subject codes, credits, and marks to calculate CGPA.
- **Automatic Calculation**: Upload images of marksheets for automatic data extraction and CGPA computation.
- **User-Friendly Interface**: Simple and intuitive UI.
- **Persistent Data**: Retains user input across sessions.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/S4DIQ84/CGPA-CALC.git
    ```
2. Navigate to the project directory:
    ```sh
    cd CGPA-CALC
    ```
3. Set up a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```sh
    flask run
    ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure
- `app.py`: Main application file with routes and logic.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory for static files like CSS.
- `cgpa.py`: Module for CGPA calculation logic.
- `image_processing.py`: Module for extracting marks from images.

## Routes
- `/`: Home page.
- `/upload`: Page to upload images for automatic calculation.
- `/auto`: Handles image uploads and displays extracted data.
- `/manual`: Form for manual CGPA calculation.
- `/contact`: Contact page.

## Modules Used
- `flask`: Web framework for Python.
- `PIL` (Pillow): Python Imaging Library for image processing.
- `pandas`: Data analysis and manipulation tool.
- `json`: JSON data handling.

## Contributing
Feel free to open issues or submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
