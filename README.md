
# 🌍 GenAI Travel Planner

This is a Gradio-based AI Travel Planner built using:
- OpenAI (for language generation)
- LangChain (for tool-powered agent reasoning)
- SerpAPI + Wikipedia (for up-to-date travel facts)
- Gradio (to create the UI)

## 🚀 How it works
Just type a travel query like:
```
Plan me a 5-day solo trip to Manali in October
```
And the app will use LLM + tools to return an AI-generated plan.

## 🧠 Technologies Used
- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI](https://openai.com)
- [Gradio](https://www.gradio.app/)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [SerpAPI](https://serpapi.com/) (optional for live search)

## 🔐 Secrets to Add in HF Space Settings
Go to **Settings > Secrets** and add:
- `OPENAI_API_KEY`: your OpenAI API key (e.g. `sk-...`)
- `SERPAPI_API_KEY`: (optional) your SerpAPI key

## 📁 File Structure
```
├── app.py              # Main app code using Gradio
├── requirements.txt    # Python dependencies
├── README.md           # Project overview (this file)
```

## ✨ Live Demo
[👉 Visit on Hugging Face Spaces](https://huggingface.co/spaces/madhavangoel/AI-Travel-Planner)

---

Made with ❤️ by Madhavan Goel
