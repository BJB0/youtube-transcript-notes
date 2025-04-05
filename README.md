# 📽️ YouTube Transcript to Notes Converter

Transform YouTube videos into **clean, structured notes** using AI.

This is an **LLM-powered application** that leverages **Google’s Gemini AI (gemini-1.5-pro)** to extract and summarize YouTube video transcripts into concise, bullet-point notes. Ideal for summarizing educational content, podcasts, lectures, or interviews into quick reference material.

---

## ✨ Features

- 🎯 Converts YouTube videos into concise bullet-point summaries  
- 🧠 Powered by Google Gemini AI (`gemini-1.5-pro`) — a Large Language Model (LLM)  
- 📝 Outputs human-readable, structured notes within 250 words  
- 💾 Download notes as a `.txt` file  
- 📷 Automatically fetches and displays video thumbnail  
- ⚡ Fast and lightweight Streamlit web interface  

---
## 🚀 Getting Started

### 1. Clone the repository
## 🚀 Getting Started

### 1. Clone the repository
```bash  
git clone https://github.com/your-username/youtube-transcript-to-notes.git
cd youtube-transcript-to-notes
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your API Key
```ini
Create a .env file in the root directory and add your Google Generative AI API Key:
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

### 🧪 Example Use Case
Paste a link like:
```arduino
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Output:
```diff
- Discusses the power of commitment and follow-through  
- Highlights how passion drives creativity and momentum  
- Recommends daily habit tracking and time-blocking
...
```

### 🧰 Built With

- 🔗 **[Streamlit](https://streamlit.io/)**
- 🔗 **[Google Generative AI (Gemini)](https://ai.google.dev/docs)**
- 🔗 **[YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)**
- 🔗 **[python-dotenv](https://pypi.org/project/python-dotenv/)**

 

### ⭐ Support
If you found this project useful, please consider giving it a ⭐ on GitHub.
It helps others discover it and motivates future development!


---





