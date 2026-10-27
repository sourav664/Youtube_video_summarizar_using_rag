# YouTube Video Summarizer and Q&A (RAG)

A Python application that summarizes YouTube videos and answers questions about their content. It retrieves a video's transcript, splits the transcript into smaller chunks, creates embeddings, searches for relevant chunks with FAISS, and uses a language model to generate a summary or answer.

## Features

- Retrieve available English transcripts from YouTube.
- Generate a concise video summary.
- Ask questions about the video and retrieve relevant transcript chunks.
- Use Retrieval-Augmented Generation (RAG) to ground answers in transcript content.
- Provide a simple browser UI using Gradio.

## Technology Stack

- Python 3.13
- `youtube-transcript-api` — retrieve video transcripts
- `langchain` — prompt and chain orchestration
- `langchain-community` — community integrations, including FAISS
- `langchain-openai` — OpenAI model and embedding integration
- `langchain-text-splitters` — split transcripts into chunks
- `faiss-cpu` — vector similarity search
- `gradio` — web interface
- `uv` — environment and package management

## How It Works

### Summarize a video

1. The user enters a YouTube URL.
2. The application extracts the video ID.
3. It retrieves an available English transcript.
4. Transcript entries are converted into text.
5. A prompt is sent to the configured language model.
6. The generated summary is displayed in the interface.

### Ask a question (RAG)

1. The transcript is retrieved and processed.
2. The transcript is split into chunks, with overlap to preserve nearby context.
3. An embedding model converts chunks into vectors.
4. FAISS indexes the vectors.
5. The question is used to find the most relevant chunks.
6. The retrieved context and question are sent to the language model.
7. The generated answer is displayed to the user.

## Project Structure

```text
youtube_summarizar_using_faiss/
├── __pycache__/
├── .gradio/
├── .venv/     # Local virtual environment; do not commit
├── __init__.py
├── .env       
├── .gitignore
├── .python-version
├── config.py
├── data_preprocessing.py
├── llm_interface.py
├── main.py
├── pyproject.toml
├── query_engine.py
├── README.md
├── requirements.txt
└── uv.lock            
```
## Prerequisites

- Python 3.13, as referenced in the lab's run and compatibility instructions.
- `uv`
- An OpenAI API key if your code uses OpenAI models through `langchain-openai`
- A YouTube video with an accessible English transcript.

## Installation

### 1. Clone or download the project

If the project is in a Git repository:

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

Replace the placeholders with your repository URL and directory name.

### 2. Create and activate a virtual environment

The lab uses `virtualenv`:

```bash
uv venv
```


### 3. Install dependencies

Ensure that `requirements.txt` contains:

```text
youtube-transcript-api
faiss-cpu
langchain
langchain-community
langchain-openai
gradio
langchain-text-splitters
```


Install them into the environment:

**Windows (PowerShell):**

```powershell
uv pip install --python .venv\\Scripts\\python.exe -r requirements.txt
```


These commands explicitly target the project's `.venv` Python interpreter.

## Configure the OpenAI API Key

If your implementation uses OpenAI models, set `OPENAI_API_KEY` before starting the application.

**Windows (PowerShell, current terminal only):**

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

**Linux/macOS:**

```bash
export OPENAI_API_KEY="your-api-key"
```

Replace `your-api-key` with your actual key. Never commit API keys to source control. If you use a `.env` file, ensure it is excluded by `.gitignore` and that your application explicitly loads it.

If your code uses a different model provider, configure that provider's credentials instead.


## Run the Application

From the project directory, with the virtual environment activated:

```bash
uv run main.py
```

The Gradio interface is configured in the lab to listen on:

```text
http://localhost:5000
```

Open that address in your browser if the local environment exposes the port.

## How to Use

1. Start the application.
2. Paste a YouTube video URL into **YouTube Video URL**.
3. Select **Summarize Video** to generate a concise summary.
4. Enter a question in **Ask a Question About the Video**.
5. Select **Ask a Question** to retrieve relevant transcript context and generate an answer.
6. Try different questions or another video that has an accessible English transcript.

### Example video from the lab

```text
https://www.youtube.com/watch?v=T-D1OfcDW1M
```

Example questions to try:

- How does one reduce hallucinations?
- Which problems does RAG solve, according to the video?
- What are the main ideas discussed in the video?

## Troubleshooting

| Problem | Things to check |
|---|---|
| `uv` command not found | Install `uv` and reopen the terminal. |
| Python version mismatch | Run `uv python find 3.13` or verify Python 3.13 is installed. |
| Dependency installation fails | Check that `.venv` was created with Python 3.13 and review the package error. `faiss-cpu` wheel availability can vary by operating system and Python version. |
| No transcript is returned | Check that the URL is valid and the video has accessible English captions. |
| URL is not recognized | The URL parser in your code may support only certain YouTube URL formats. |
| OpenAI authentication error | Check that `OPENAI_API_KEY` is set in the same terminal and that the key is valid. |
| Model or embedding error | Confirm the model classes, model names, and provider settings match your code. |
| Port is already in use | Stop the other process using the port or change the port in the application code. |
| Answers are inaccurate | Check the transcript, retrieved chunks, prompt, and model output. RAG can still produce incorrect answers. |

## Notes

- The application requires an accessible transcript; it does not directly transcribe audio in the described workflow.
- The supported URL formats depend on the URL extraction code in `main.py`.
- The language behavior depends on the transcript-selection logic in your implementation.
- Package names above are intentionally unpinned. For reproducible setups, test the environment and pin known-working versions in `requirements.txt`.
- The README describes the intended stack. Ensure that `main.py` uses `langchain-openai` and the corresponding OpenAI classes if you plan to use OpenAI; dependency changes alone do not rewrite application code.


## 🌟 About Me

Hi there! I'm **Sourav Raj**, a **Data Enthusiast** who loves exploring data, building practical solutions, and making working with data enjoyable and engaging!

