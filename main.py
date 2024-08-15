import llm
from prompts import llm_problem_statement, plan, PLAN_TO_PY_INSTRUCTIONS, build_prompt_for_plan_feedback_on_failure, test_error

messages_to_generate_code = [
    {"role": "system", "content": "You are a tool that only produces Python code based on a student's plan to solve a programming problem."},
    {"role": "user", "content": "The next message is a programming problem statement."},
    {"role": "user", "content": f'{llm_problem_statement}'},
    {"role": "user", "content": "The next message is a student's plan to solve the problem."},
    {"role": "user", "content": f'{plan}'},
    {"role": "user", "content": f'{PLAN_TO_PY_INSTRUCTIONS}'},
    {"role": "assistant", "content": f"---START OF PY FILE---\n\n"},
]

code = llm.complete_chat(messages_to_generate_code)


messages_to_generate_feedback = [
    {"role": "system", "content": "You are a tool that only gives feedback based on a student's plan to solve a programming problem."},
    {"role": "user", "content": f'{build_prompt_for_plan_feedback_on_failure(plan, code, test_error)}'}
]

feedback_on_failure = llm.complete_chat(messages_to_generate_feedback)

print(feedback_on_failure)
