# Bengaluru House Price Prediction Model

This repository contains the code and files for a Bengaluru House Price Prediction Model. The project uses machine learning to predict house prices based on location and other features. It includes model training, Flask backend, and a simple frontend.

## Directory Structure

```
/Bengaluru_House_Prediction_Model
│
├── /model                 # Model artifacts and Jupyter notebooks
│   ├── banglore_home_prices_final_(1).ipynb
│   ├── banglore_home_prices_model.pickle
│   ├── columns.json
│
├── /server                # Backend files and logic (Flask)
│   ├── server.py
│   ├── util.py
│   ├── /artifacts
│   │   ├── banglore_home_prices_model.pickle
│   │   └── columns.json
│   ├── /images
│   └── house.webp
│   ├── app.html
│   ├── app.css
│   └── app.js
└── /vscode                # VS Code configurations
    └── launch.json
```

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.12 or higher
- Flask for the backend
- Nginx (for local deployment)
- Required Python libraries: `flask`, `numpy`, `pandas`, `scikit-learn`, `pickle`, etc.
  
Install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

## Steps to Run the Model Locally

### 1. **Run Flask Backend**

Start by running the Flask application:

```bash
python server/server.py
```

The backend server will start on `http://127.0.0.1:5000`. This will serve the prediction logic and APIs.

### 2. **Start Nginx**

If you have Nginx installed, you can use it to handle reverse proxy requests. Make sure Nginx is set up and configured correctly for your environment. You can refer to the Nginx configuration at `nginx.conf`.

Start Nginx to proxy requests to your Flask app.

### 3. **Open the Frontend**

The frontend is located in the `server` folder as HTML, CSS, and JavaScript files. Open `app.html` in a browser to interact with the model.

### 4. **Model Artifacts**

Ensure that the model artifacts (`banglore_home_prices_model.pickle`, `columns.json`) are present in the appropriate directories under `/model` and `/server/artifacts`. These are required for predictions.

## Deployment

**NOTE:**  
I have not deployed this model yet. It is currently set up to run locally.

## How to Contribute

Feel free to fork this repository and contribute. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.
