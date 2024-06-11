# RAG Evaluator Application

This application is built using Streamlit to evaluate different techniques for RAG (Retrieval-Augmented Generation). Follow the instructions below to set up and run the application.

## Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Navigate to the application directory:**
    ```sh
    cd <repository_directory>
    ```

2. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

3. **Open your web browser and go to:**
    ```
    http://localhost:8501
    ```

## Usage

1. **Enter your input text** in the provided text area.
2. The application will automatically process the input using three different techniques:
    - SQL Query Chain
    - RAPTOR
    - GraphRAG
3. **View the responses** and the time taken for each technique in the respective columns.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

If you wish to contribute, please fork the repository and submit a pull request.

## Contact

For any questions or feedback, please contact raoofnaushad.7@gmail.com.

Enjoy using the RAG Evaluator Application!

