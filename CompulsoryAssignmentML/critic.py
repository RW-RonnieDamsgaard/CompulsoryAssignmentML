from autogen import ConversableAgent
from react_agent import LLM_CONFIG
import json

critic_agent = ConversableAgent(
    name="Critic",
    llm_config=LLM_CONFIG
)

def evaluate_response(agent, prompt, response):
    critic_prompt = f"""
You are evaluating an AI agent's answer based on the following criteria:

- Completeness (1-5)
- Quality (1-5)
- Robustness (1-5)
- Consistency (1-5)
- Specificity (1-5)

Answer with a JSON object including the above scores and a brief 'feedback' field explaining strengths and weaknesses.

User Prompt:
{prompt}

Agent Response:
{response}
"""
    reply = agent.generate_reply([{"role": "user", "content": critic_prompt}])
    if isinstance(reply, dict):
        return reply
    try:
        return json.loads(reply)
    except json.JSONDecodeError:
        return {"error": "Could not parse JSON from LLM", "raw": reply}
