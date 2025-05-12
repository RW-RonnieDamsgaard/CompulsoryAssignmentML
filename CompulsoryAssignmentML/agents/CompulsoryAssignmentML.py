# from config.config import LLM_CONFIG
# from tools.search_papers import find_paper
# from autogen_agentchat.agents import AssistantAgent
# from autogen_core.tools import FunctionTool

# # Wrap the search function
# search_tool = FunctionTool(
#     find_paper,
#     "Searches for research papers based on keywords and filters."
# )
# # Define the agent
# agent = AssistantAgent(
#     name="ResearchAssistant",
#     llm_config=LLM_CONFIG,
#     tools=[search_tool]
# )

# # Example prompt
# prompt = "Find a research paper on reinforcement learning published after 2020 with more than 100 citations."
# response = agent.run(prompt)
# print(response)