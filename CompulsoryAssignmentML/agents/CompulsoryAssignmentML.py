# main.py
from config.config import LLM_CONFIG
from tools.search_papers import search_papers
from autogen import ConversableAgent, register_function


search_tool = register_function(
    search_papers,
    name="search_papers",
    description="Searches for research papers by topic, publication year filter, and citation count filter.",
    caller=1,  # Replace with the appropriate value
    executor=1  # Replace with the appropriate value
)

agent = ConversableAgent(
    name="ResearchAgent",
    llm_config=LLM_CONFIG,
    tools=[search_tool]
)

if __name__ == "__main__":
    prompt = "Find a research paper on reinforcement learning published after 2020 with more than 100 citations."
    response = agent.run(prompt)
    print("\nAgent response:\n", response)


