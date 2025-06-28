import gradio as gr
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper, WikipediaAPIWrapper
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

search = SerpAPIWrapper()
wiki = WikipediaAPIWrapper()

tools = [
    Tool(name="Search", func=search.run, description="Useful for current events or factual questions"),
    Tool(name="Wikipedia", func=wiki.run, description="Useful for general knowledge")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def plan_trip(query):
    response = agent.run(query)
    return response

iface = gr.Interface(
    fn=plan_trip,
    inputs=gr.Textbox(label="What do you want to plan?", placeholder="e.g. 5-day solo trip to Goa in January"),
    outputs=gr.Textbox(label="AI Travel Plan"),
    title="🌍 GenAI Travel Planner",
    description="LangChain + OpenAI-powered AI Trip Planning Assistant"
)

if __name__ == "__main__":
    iface.launch()