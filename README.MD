# Paris Trip Guide – OpenAI + Docker

A simple Python-based project that uses the OpenAI API to answer Paris tourist questions using **few-shot prompting**.  
The project is containerized using Docker for easy setup and portability.

---

## 📌 Features
- Uses **OpenAI's GPT-4o-mini** model for fast, cost-effective responses.
- Implements **few-shot prompting** to guide the AI's behavior (as a Paris tourist guide).
- Maintains a **conversation history** so responses remain context-aware.
- Containerized with **Docker** so you don’t need to manually install dependencies.
- Reads the API key securely from environment variables.

---

## 🛠 Prerequisites
Before you run the project, make sure you have:
- [Docker](https://docs.docker.com/get-docker/) installed on your system.
- An **OpenAI API key** (see below for how to generate one).

---

## 🔑 Getting an OpenAI API Key
1. Sign up or log in at [OpenAI](https://platform.openai.com/).
2. Go to your [API Keys page](https://platform.openai.com/account/api-keys).
3. Click **Create new secret key**.
4. Copy the generated key — it will look like:
5. Store it securely — you will need it for the `.env` file.

---

## 📂 Project Structure
.
├── Dockerfile # Docker build instructions
├── main.py # Python script using OpenAI API
├── requirements.txt # Python dependencies
├── .env # Environment variables (contains your API key)
└── README.md # Project documentation

Create a `.env` file in the project root:
OPEN_API_SECRET=your_openai_api_key_here


### 1. Build the Docker Image
Run the following command in the project folder:
```
docker build -t my-openai-app .
```
### 2. Run the Container
Pass the .env file so the container can access your API key:
```
docker run --env-file .env my-openai-app
```



💡 How It Works
1. Few-Shot Prompting
We start the conversation with a system message:
```
{"role": "system", "content": "You are a helpful tourist guide, who will answer Parisian tourist questions."}
```
This guides the AI to act like a Paris tour guide.
We then append each user question and AI response to the conversation list so the model remembers context.

2. OpenAI Chat API
The script uses:
```
client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation,
    max_tokens=100,
    temperature=0.0
)
```
model: Specifies GPT-4o-mini.
temperature=0.0: Makes responses more factual and consistent.
max_tokens=100: Limits response length.



