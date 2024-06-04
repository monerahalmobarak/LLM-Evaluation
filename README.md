LLM Evaluation Web Application
This project aims to build a web application that evaluates the responses of different Large Language Models (LLMs) in a Question and Answering task. The LLMs being compared are:

1- GPT-3.5-turbo
2- GPT-4
3- Llama-2-70b-chat
4- Falcon-40b-instruct
with me both GPT-4 and Falcon-40b-instruct show great result.

Project Overview
The web application is designed to accept user prompts and provide responses from the four different LLMs. The application scrapes content from a specified website and its subpages, stores the information in a vector database, and uses this data to query the LLMs. The primary objectives include scraping, storing, querying, comparing, and evaluating the outputs of the LLMs.

Features
Web Scraping: Scrapes data from the specified website and all its subpages.
Vector Database Integration: Stores the scraped information in a vector database for efficient retrieval.
LLM Querying: Queries each of the four LLMs with the user's prompt and relevant search results from the vector database.
Real-Time Streaming: Uses Websockets or Server-Sent Events (SSE) for real-time streaming of responses to the frontend.
Evaluation: Compares and evaluates the generated outputs to determine the best-performing LLM for the given user input.
Technologies Used
Python: Backend development.
Flask: Web framework.
FAISS: Vector database.
LangChain: Handling LLM interactions.
OpenAI API: For GPT-3.5-turbo and GPT-4.
Replicate API: For Llama-2-70b-chat and Falcon-40b-instruct.
Setup Instructions
Prerequisites
Python 3.7 or higher
API keys for OpenAI and Replicate
Installation

Clone the repository:
bash
Copy code
git clone https://github.com/monerahalmobarak/LLM-Evaluation.git
cd LLM-Evaluation

Install the required packages:
bash
Copy code
pip install -r requirements.txt

Set up environment variables for API keys:
bash
Copy code
export OPENAI_API_KEY='your_openai_api_key'
export REPLICATE_API_KEY='your_replicate_api_key'
Running the Application
Run the Flask app:
bash
Copy code
python app.py
Access the application at http://127.0.0.1:5000/.

File Structure
app.py: Main Flask application file.
chatbot_Falcon.py: Falcon-40b-instruct chatbot integration.
chatbot_gpt-3.5-turbo.py: GPT-3.5-turbo chatbot integration.
chatbot_gpt-4.py: GPT-4 chatbot integration.
chatbot_llama.py: Llama-2-70b-chat chatbot integration.
Web_Scraping_Code.ipynb: Jupyter notebook for scraping the website.
requirements.txt: List of required Python packages.

Web Application Pages
Landing Page ![image](https://github.com/monerahalmobarak/LLM-Evaluation/assets/136607948/d647970f-4eb4-4a55-b169-ee43ae1a2d48)

Chatbot Page ![image](https://github.com/monerahalmobarak/LLM-Evaluation/assets/136607948/7f619dc7-0590-4923-af36-9a0c52d56660)



Model Evaluation Process
User Prompt: The user enters a prompt on the web application.
Query Vector Database: The application queries the vector database to retrieve relevant search results based on the user's prompt.
LLM Query: Each LLM is queried with the search results and the user's initial query.
Response Streaming: The responses from each LLM are streamed to the frontend in real-time.
Comparison and Evaluation: The generated outputs are compared to find the best-performing LLM for the given user input.

Acknowledgements
OpenAI for providing the API for GPT-3.5-turbo and GPT-4.
Replicate for providing the APIs for Llama-2-70b-chat and Falcon-40b-instruct.
FAISS for the vector database implementation.
LangChain for facilitating LLM interactions.
For any questions or support, please contact Monerah Almobarak.
