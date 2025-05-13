from react_agent import assistant_v2
from critic import critic_agent, evaluate_response
from prompts import test_prompts

if __name__ == "__main__":
    for prompt in test_prompts:
        print(f"\n🔎 Prompt: {prompt}\n")

        initial_response = assistant_v2.generate_reply(
            messages=[{"role": "user", "content": prompt}]
        )
        print("🤖 Initial response:\n", initial_response)

        evaluation = evaluate_response(critic_agent, prompt, initial_response)
        print("🧠 Evaluation:\n", evaluation)
        refined_response = assistant_v2.generate_reply(
            messages=[{"role": "user", "content": "Based on the self-evaluation, refine the recommendation."}]
        )
        print("✅ Refined response:\n", refined_response)
