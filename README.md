# YouTube Video Analysis Chatbot

![image](https://github.com/ComputingVictor/LLM_Projects/assets/115224707/583ddb13-48d7-49c9-818e-1babbc2b21f4)


This project is a chatbot developed using LLM (Large Language Models) capable of answering questions about YouTube videos based on their transcriptions. The chatbot utilizes natural language processing techniques to analyze user queries and retrieve relevant information from the video transcriptions.

## Features

- **Video Analysis**: The chatbot can respond to questions about YouTube videos using the information present in their transcriptions.
- **Spanish Interaction**: The chatbot is designed to respond in Spanish, facilitating communication for Spanish-speaking users.
- **Utilization of LLM Models**: The langchain_community.llms library is used to leverage LLM models in generating responses.

## Installation

To run the project, follow these steps:

1. Clone this repository to your local machine.
2. Install dependencies using pip:
    
```bash
pip install -r requirements.txt
```
To initiate the Streamlit web application, run the following command in your terminal:
    
    streamlit run app.py
    
This will open the Streamlit application in your default web browser.

## Usage

Once the Streamlit application is running, you'll be presented with a web interface where you can:

- Enter the URL of the YouTube video you're interested in.
- Select the transcription language (e.g., Spanish or English).
- Type your question into the provided text box.
- Click on "Obtener respuesta" to submit your question and receive a response.
- The chatbot will process your question and return a response based on the video's transcription.

## Contribution

If you wish to contribute to this project, feel free to submit pull requests with improvements, bug fixes, or new features. You can also open issues to report bugs or suggest new ideas.

## Credits

This project was developed by Víctor Viloria.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE.md](LICENSE.md) file.
