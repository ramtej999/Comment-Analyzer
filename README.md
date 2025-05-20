# LLM-Based Multilingual Comment Analyzer

This project extracts comments (especially in Chinese or Japanese) from sources like YouTube or Instagram Reels, translates them into English, and summarizes the main discussion points using a Large Language Model (LLM). It's designed for use cases like social media monitoring, international sentiment analysis, and content moderation.

## 🔍 Features

- **Comment Extraction**: Parses comments from video links or social sources.
- **Translation**: Automatically translates Chinese or Japanese comments into English using Google Translate.
- **Summarization**: Uses a powerful LLM to summarize and identify key points from translated comments.
- **Modular Design**: Each core function—extraction, translation, summarization—is separated into reusable modules.

## 🧱 Project Structure

LLM-Project/
│
├── main.py                   # Entry point: integrates extraction, translation, and summarization
├── extract_comments.py       # Extracts multilingual comments
├── translate_comments.py     # Translates comments to English
├── summarize_comments.py     # Summarizes translated comments using Google Generative AI
└── myenv/                    # Python virtual environment (do not include in GitHub)

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/ramtej999/LLM-Project.git
cd LLM-Project

### 2. Create and Activate Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

> 📌 Note: You may need access to the **Google Generative AI API**. Make sure to set your API key as an environment variable:

export GOOGLE_API_KEY="your-api-key-here"

### 4. Run the Project

python main.py

You'll be prompted to enter a comment source (like a YouTube video ID or other supported input), and the script will return a summarized interpretation in English.

## 📦 Dependencies

* `google-generativeai`
* `googletrans==4.0.0-rc1`
* `requests`

> Generate a `requirements.txt` by running:

pip freeze > requirements.txt

## 📌 Example

Enter source ID: abc123xyz
Extracting comments...
Translating...
Summarizing...

📝 Summary:
- Many users praised the visual effects.
- A few comments discussed political context.
- Overall positive sentiment.

## 📜 License

This project is for educational and research purposes. Modify it freely for personal use. For commercial use, please consult the author.

## ✨ Author

Developed by [Ramtej](https://github.com/ramtej999)
Feel free to contribute or raise issues!

```

---

Let me know if you'd like me to generate the actual `requirements.txt` or add badges/documentation links!
```
