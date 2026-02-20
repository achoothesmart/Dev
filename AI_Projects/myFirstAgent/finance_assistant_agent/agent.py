from google.adk.agents import LlmAgent

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="An AI agent that provides financial advice and assistance.",
    instruction="Assist users with their financial queries and provide relevant information."
)

root_agent = finance_assistance_agent 