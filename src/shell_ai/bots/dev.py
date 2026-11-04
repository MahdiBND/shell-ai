"""Shell Script Agent for agentkit: write scripts"""

from __future__ import annotations

from agentkit import InMemorySessionStore, new_agent

from ..prompts.shell_agent import SYSTEM_PROMPT
from ..tools.shell_agent import write_new_file
from langchain_core.prompts import PromptTemplate


def init(
    instructions=SYSTEM_PROMPT,
    tools=[write_new_file],
    session_store=InMemorySessionStore(),
    **kwargs,
):
    prompt = PromptTemplate.from_template(instructions)
    prompt = prompt.format(**kwargs)

    return new_agent(prompt, tools=tools, session_store=session_store)
