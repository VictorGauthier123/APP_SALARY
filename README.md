# Developer Salary Prediction

This project is a Flask web application that predicts a developer's salary based on different characteristics (country, programming language, experience, etc.).  
The model used is a pre-trained XGBoost model saved as a `.pkl` file. This model has been trained with some data I found online.

<img width="1883" height="867" alt="image" src="https://github.com/user-attachments/assets/6460c5b5-8d14-4423-80fb-b7c9cbb57b8e" />

<img width="1858" height="839" alt="image" src="https://github.com/user-attachments/assets/cc66c01f-557d-4700-a081-829e74164429" />



## Project Structure

```
project/
│── app.py                  # Main Flask application
│── best_xgb_model.pkl      # Pre-trained XGBoost model
│── templates/
│   └── index.html          # HTML page with the form and prediction result
```

## Installation

1. Clone this repository or download the files.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser at:
   ```
   http://127.0.0.1:5000/
   ```
3. Fill in the form to get a salary prediction.

## Notes

- The model is already trained, the original dataset is not required.
- The HTML form (`index.html`) must contain the fields expected by the application (`Country`, `EdLevel`, `OrgSize`, `Industry`, `RemoteWork`, `DevType`, `Employment`, `LanguageHaveWorkedWith`, `PlatformHaveWorkedWith`, `YearsCodePro`).



