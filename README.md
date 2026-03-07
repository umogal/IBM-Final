# Emotion Detection API

## Project Overview

This project provides a Flask-based web application that offers emotion detection from text. The application utilizes a backend API to analyze text input for emotional content, identifying emotions such as anger, disgust, fear, joy, and sadness, and determining the predominant emotion. This API is ideal for integrating into applications requiring sentiment analysis or emotion detection functionalities.

## Features

- **Emotion Analysis**: Analyze text to detect various emotions.
- **Dominant Emotion Detection**: Identify the most predominant emotion in the text.
- **Error Handling**: Manage blank entries effectively and ensure robust error feedback.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine along with Flask. If not, you can install them using:

```bash
pip install python
pip install flask
```

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/ehernandezvilla/IBM-finalia
cd IBM-finalia
```

### Running the Application

Navigate to the project directory and run the application using:

```bash
python server.py
```

The server will start running on `http://localhost:5000/`. Navigate to this URL in your web browser to interact with the application.

## Usage

The main page presents a user interface where you can input the text to be analyzed. Upon submission, the text is sent to the backend where the emotion is analyzed, and the results are displayed on the same page.

### API Endpoints

- **GET `/`**: Renders the main index page.
- **GET `/emotionDetector`**: Endpoint that receives text as input and returns the emotion analysis results.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, or open issues to suggest features or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

