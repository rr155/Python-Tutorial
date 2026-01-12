import os
import sys
import langgraph

"""
starting_llm.py

Basic LLM agent using langgraph (template + safe fallback).
Place your API key in the environment (e.g. OPENAI_API_KEY).
"""


# langgraph is required for this script
HAS_LANGGRAPH = True
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("LLM_MODEL", "gpt-4o")  # change default model as needed

def create_langgraph_agent(api_key: str | None, model: str = MODEL):
    """
    Create a basic agent using langgraph.
    This is a small template that tries common patterns across langgraph versions.
    Adjust to your installed langgraph API if needed.
    """
    if not HAS_LANGGRAPH:
        raise RuntimeError("langgraph is not installed. pip install langgraph")

    # Common patterns — adapt to your langgraph version:
    # 1) langgraph.Client(...) and client.create_agent(...)
    # 2) langgraph.Agent(...) direct constructor
    client = None
    agent = None

    # Pattern A: langgraph.Client
    Client = getattr(langgraph, "Client", None)
    if Client is not None:
        client = Client(api_key=api_key) if api_key is not None else Client()
        create_agent = getattr(client, "create_agent", None) or getattr(client, "agent", None)
        if callable(create_agent):
            # try a simple create_agent signature
            try:
                agent = create_agent(name="basic-agent", model=model, temperature=0.2)
            except TypeError:
                # try with a simpler signature
                agent = create_agent(model=model)
    # Pattern B: direct Agent class
    if agent is None:
        Agent = getattr(langgraph, "Agent", None)
        if Agent is not None:
            try:
                agent = Agent(model=model, temperature=0.2)
            except TypeError:
                agent = Agent(model=model)

    if agent is None:
        raise RuntimeError("Couldn't create a langgraph agent with detected API. Update this template for your langgraph version.")

    return agent


def ask_with_langgraph(agent, prompt: str, timeout: float = 30.0) -> str:
    """
    Send a prompt to the langgraph agent. Tries common invoke/run APIs.
    """
    # Try common call patterns
    for method_name in ("run", "invoke", "call", "__call__"):
        method = getattr(agent, method_name, None)
        if callable(method):
            try:
                # many agent run methods accept just the prompt
                return method(prompt)
            except TypeError:
                # some accept dict or named args
                try:
                    return method({"input": prompt})
                except Exception:
                    continue
    # Last resort: try .complete or .generate
    for method_name in ("complete", "generate"):
        method = getattr(agent, method_name, None)
        if callable(method):
            return method(prompt)

    raise RuntimeError("No supported invocation method found on langgraph agent.")


# No OpenAI fallback: this script requires langgraph. If you need an OpenAI fallback,
# reintroduce the openai dependency and corresponding code.


def main():
    prompt = "Write a short one-paragraph summary explaining recursion to a beginner."

    # Use langgraph only
    try:
        agent = create_langgraph_agent(api_key=OPENAI_API_KEY, model=MODEL)
    except Exception as e:
        print(f"Failed to create langgraph agent: {e}", file=sys.stderr)
        print("Please install and configure langgraph and ensure your backend/API key is set.", file=sys.stderr)
        sys.exit(1)

    try:
        answer = ask_with_langgraph(agent, prompt)
        print("Response from langgraph agent:\n")
        print(answer)
    except Exception as e:
        print(f"langgraph invocation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()