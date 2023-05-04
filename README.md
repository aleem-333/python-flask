## Watermelon

This is a Flask application that allows users to fill out a form and stores the data in a CSV file. The application has two routes: `/` and `/results`.

To run the application, please follow the below steps:

1. Install Conda by following the instructions on the official website: <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>

2. Create a new Conda environment with Python 3.8:

        conda create --name formdata python=3.8

3. Activate the environment:

        conda activate formdata

4. Install the required packages using the `requirements.txt` file provided:

        pip install -r requirements.txt

5. Start the application by running the `run.py` file:

6. Open a web browser and navigate to `http://localhost:5001/` to access the form.

7. Fill out the form and submit it. The data will be stored in a CSV file.

Note: Currently, the server is keeping the data in memory. To handle concurrent users, it's recommended to use something like gunicorn, supervisor, Flask, and nginx.
