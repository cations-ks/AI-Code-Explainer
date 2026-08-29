\# 🤖 AI Code Explainer



An AI-powered web application that helps beginners understand, improve, and optimize programming code.



\## ✨ Features



\* Explain code in beginner-friendly language

\* Step-by-step explanation of code

\* Time complexity analysis

\* Space complexity analysis

\* Identify important functions and variables

\* Improve code readability

\* Optimize code efficiency

\* Supports Python, C, C++, Java, and JavaScript



\## 🛠️ Technologies Used



\* Python

\* Streamlit

\* Google Gemini API

\* python-dotenv



\## 🚀 How to Run



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_LINK

```



\### 2. Open the project folder



```bash

cd AI-Code-Explainer

```



\### 3. Install the required packages



```bash

pip install -r requirements.txt

```



\### 4. Create the environment file



Create a file named `.env` in the project folder and add:



```text

GEMINI\_API\_KEY=YOUR\_GEMINI\_API\_KEY

```



Replace `YOUR\_GEMINI\_API\_KEY` with your own Gemini API key.



\### 5. Run the application



```bash

python -m streamlit run app.py

```



The application will open in your browser.



\## 📁 Project Structure



```text

AI-Code-Explainer/

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

└── .env

```



\## 🔐 Security



The API key is stored in a `.env` file and is excluded from GitHub using `.gitignore`.



Never upload the `.env` file or your API key to a public repository.



\## 🎯 Purpose



This project was created as a Generative AI application to demonstrate how a Large Language Model can be used to assist beginners in understanding programming concepts and improving their code.



