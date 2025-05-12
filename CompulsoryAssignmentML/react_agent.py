# from autogen.agentchat import ConversableAgent
import autogen
from autogen import ConversableAgent
from prompts import SYSTEM_MESSAGE_V2

LLM_CONFIG = {
    "config_list": [{
        "model": "open-mistral-nemo",
        "api_key": "b2UzjIW2V4Cyr2UnsC8jQj5XVpUiZAi7",
        "api_type": "mistral",
        "api_rate_limit": 0.25,
        "repeat_penalty": 1.1,
        "temperature": 0.0,
        "seed": 42,
        "stream": False,
        "native_tool_calls": False,
        "cache_seed": None,
    }]
}

assistant_v2 = ConversableAgent(
    name="AssistantV2",
    llm_config=LLM_CONFIG,
    system_message=SYSTEM_MESSAGE_V2
)
