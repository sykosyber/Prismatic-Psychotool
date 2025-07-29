
# SYBER PRISMATIC PSYCHOTOOL

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

A web-based instrument for multi-dimensional analysis of human behavior and psychology. This tool uses OpenAI's GPT-4o to process text through a variety of selectable academic and theoretical lenses, providing deep, structured insights.

![Psychotool Screenshot]([img]https://i.imgur.com/oWhYlsz.png[/img])

## Features

- **Multi-Lens Analysis**: Analyze any text through multiple frameworks simultaneously.
- **Rich Theoretical Frameworks**: Includes over 20 lenses from fields like Psychoanalysis (Freudian, Jungian, Lacanian), Sociology, Economics, Systems Theory, and more.
- **Integrative Synthesis**: An optional feature that combines insights from all selected lenses into a single, high-level meta-analysis.
- **Scenario Decomposition Tool**: A helper utility (`frontend/scenario-decomposition.html`) to structure complex scenarios before analysis.
- **Mock Mode**: A development mode to test the frontend and backend connection without making real API calls, saving costs.

## Tech Stack

- **Backend**: Python with Flask
- **AI Integration**: OpenAI API (`openai-python` library)
- **Frontend**: HTML, CSS, Vanilla JavaScript

## Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.9 or newer
- An active OpenAI API Key with access to the GPT-4o model.

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd Psychotool/
    ```

2.  **Set Up the Backend**
    Navigate into the `backend` directory. This is where the Python environment will live.
    ```bash
    cd backend
    ```

3.  **Create and Activate a Virtual Environment**
    
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate it (macOS/Linux)
    source .venv/bin/activate

    # Activate it (Windows)
    .venv\Scripts\activate
    ```
    Your terminal prompt should now be prefixed with `(.venv)`.

4.  **Install Dependencies**
    Install the required Python packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables**
    Create a file named `.env` inside the `backend` folder. Add your OpenAI API key to this file.
    ```
    OPENAI_API_KEY="sk-YourSecretKeyGoesHere"
    MOCK_MODE=False
    ```

## Usage

1.  **Start the Backend Server**
    Make sure you are in the `backend` directory with your virtual environment activated.
    ```bash
    flask run
    # Or: python -m flask run
    ```
    The backend server will start and be available at `http://127.0.0.1:5000`.

2.  **Launch the Frontend**
    Navigate to the `frontend` directory and open the `mdh-analysis-instrument.html` file directly in your web browser (e.g., by double-clicking it).

3.  **Run an Analysis**
    - Paste the text you want to analyze into the input box.
    - Select one or more analytical lenses.
    - Click the "Analyze" button.

## Project Structure

```
Psychotool/
├── .gitignore          # Specifies files for Git to ignore
├── README.md           # This file
├── frontend/
│   ├── mdh-analysis-instrument.html      # Main user interface for the analysis tool
│   └── scenario-decomposition.html # Helper tool for structuring input
└── backend/
    ├── .venv/          # Your isolated Python virtual environment (ignored by Git)
    ├── .env            # Your secret API keys (ignored by Git)
    ├── app.py          # The Flask web server and API endpoint logic
    ├── prompts.py      # Contains all the detailed prompts for the AI
    └── requirements.txt  # List of Python package dependencies
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

````
