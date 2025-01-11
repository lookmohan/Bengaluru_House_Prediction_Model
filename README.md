# Bengaluru House Price Prediction Model

This repository contains the code and files for a Bengaluru House Price Prediction Model. The project uses machine learning to predict house prices based on location and other features. It includes model training, a Flask backend, and a simple frontend.

### Model Prediction Results

Here is an example of the output from the Bengaluru House Price Prediction model:

![UI](https://github.com/user-attachments/assets/7d81e333-60d8-4e3d-b177-963662b22ed7)

---

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

---

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

---

## Steps to Run the Model Locally

### 1. **Run Flask Backend**

Start by running the Flask application:

```bash
python server/server.py
```

The backend server will start on `http://127.0.0.1:5000`. This will serve the prediction logic and APIs.

### 2. **Configure and Start Nginx**

If you have Nginx installed, you can use it to handle reverse proxy requests. Here are the steps:

1. **Edit Nginx Configuration**:
   - Open your `nginx.conf` file.
   - Add a new configuration block to proxy requests to your Flask app:

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           proxy_pass http://127.0.0.1:5000;  # Flask app running on port 5000
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

2. **Start Nginx**:
   - Make sure the `nginx.conf` file is set up correctly in your Nginx directory.
   - Start Nginx using the following command:

   ```bash
   nginx -c /path/to/nginx.conf
   ```

   Replace `/path/to/nginx.conf` with the actual path to your `nginx.conf` file.

### 3. **Open the Frontend**

The frontend files (`app.html`, `app.css`, `app.js`) are located in the `server` folder. Open `app.html` in a browser to interact with the model.

---

## Model Artifacts

Ensure that the model artifacts (`banglore_home_prices_model.pickle`, `columns.json`) are present in the appropriate directories under `/model` and `/server/artifacts`. These are required for predictions.

---

## Deployment

**NOTE:**  
I have not deployed this model yet. It is currently set up to run locally.

---

## How to Contribute

Feel free to fork this repository and contribute. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

---

### Notes:

- This README file now includes detailed steps for configuring and using Nginx to proxy requests to your Flask app.
- Make sure the `nginx.conf` file reflects the correct paths and server configurations.
