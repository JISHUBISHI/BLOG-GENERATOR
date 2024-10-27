# Blog Generation Flask App

This project is a Flask-based web application that generates blog content using a Llama model via a subprocess. Users can input a prompt, and the app generates a blog post based on the given prompt.

## Features
- Simple web interface to input a blog prompt.
- Integration with the `llama3.2` model for generating blog content.
- JSON response with generated blog content.

## Requirements

### Python Packages
- Flask: `pip install Flask`

### Additional Tools
- `ollama` for running the `llama3.2` model (Ensure this is installed and accessible on your system).

## How to Run

1. Clone the repository or download the code.
    ```bash
    git clone "https://github.com/Parthibkarak71/blog-generation.git"
    cd BLOG_GENERATION
    ```

2. Install the required Python packages:
    ```bash
    pip install Flask
    ```

3. Ensure you have `ollama` installed to run the `llama3.2` model.

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5050` to access the application.

## Usage

- Enter a prompt in the input box on the home page and submit.
- The app will generate a blog post based on the prompt and display it on the page.

## File Structure

. ├── app.py 
# Main application file 
  ├── templates │ 
     └── index.html 
# HTML template for the homepage 
  ├── static │   
    └── (css/js files) 
# For any static assets if needed 
    └── README.md


## API Endpoints

- `/generate` (POST): Accepts a `prompt` and returns a generated blog content in JSON format.

### Example Request:
```bash
POST /generate
Content-Type: application/x-www-form-urlencoded

prompt="Write a blog about the importance of AI in healthcare."

Notes
Ensure ollama is set up properly to run llama3.2.
Flask is running in debug mode, which you can disable in production.

###CONTRIBUTORS###
Contributor 1:- Parthib Karak
Github:- "https://github.com/Parthibkarak71"
Role :- BACKEND DEVELOPER,AI MODEL BUIDING
Contributor 2:- Agnik Bishi
Github:- "https://github.com/JISHUBISHI"
Role :- FRONTEND DEVELOPER
Contributor 3:-Soumyadip Changder
Github:- "https://github.com/soumadipchangder"

