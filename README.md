# 🌍 City Assistant Agent

City Assistant Agent is an AI-powered chatbot that helps users retrieve **real-time weather information** and **the latest city-related news** through a conversational interface. The application combines the reasoning capabilities of **Mistral AI** with **LangChain Agents**, allowing the AI to automatically decide when to use external tools based on the user's request.

The project features a clean and interactive interface built with **Streamlit**, making it easy to chat with the assistant directly from the browser.

---

# ✨ Features

* 🌦️ Get real-time weather information for any city.
* 📰 Retrieve the latest news related to a city.
* 🤖 AI-powered responses using Mistral AI.
* 🛠️ Automatic tool selection with LangChain Agents.
* 💬 Interactive chat interface using Streamlit.
* ⚡ Fast and lightweight application.
* 🔍 Live information powered by external APIs.

---

# 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Mistral AI**
* **Streamlit**
* **OpenWeather API**
* **Tavily Search API**
* **Requests**
* **Python Dotenv**

---

# 📂 Project Structure

```text
City-Assistant-Agent/
│
├── app.py               # Streamlit application
├── agent.py             # LLM, tools and agent configuration
├── requirements.txt
├── .env                  #make it yourself for storing api keys 
└── README.md
```

---

# ⚙️ How It Works

1. The user enters a question in the Streamlit interface.
2. The LangChain Agent analyzes the request.
3. If weather information is required, the agent calls the OpenWeather API.
4. If news is requested, the agent uses the Tavily Search API.
5. The tool output is sent back to the LLM.
6. The LLM generates a natural language response for the user.

---

# 🚀 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd City-Assistant-Agent
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory and add the following API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Once the server starts, open the local URL displayed in the terminal (usually `http://localhost:8501`) in your browser.

---

# 💬 Example Queries

* What is the weather in Delhi?
* Show me the latest news about Mumbai.
* What's happening in Bengaluru today?
* Tell me the current weather in Jaipur.
* Give me recent news from Chennai.
* Is it raining in Hyderabad?
* What's the weather like in Kolkata?

---

# 📦 Dependencies

The project uses the following major libraries:

* langchain
* langchain-mistralai
* streamlit
* requests
* python-dotenv
* tavily-python

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📄 License

This project is developed for educational and learning purposes. Feel free to use and modify it for your own projects while following the respective API providers' terms of service.

---

# Demo 

<img width="1007" height="860" alt="Screenshot 2026-07-30 235021" src="https://github.com/user-attachments/assets/cb27001f-6b44-4b57-bbc2-8a910f551c0d" />
