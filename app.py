from langflow.load import run_flow_from_json

# Path to your exported JSON file
FLOW_JSON_PATH = "ClimaCrop(final).json"

# Your user input/question
input_value = "What is the climate risk described in the document?"

# Run the flow
result = run_flow_from_json(
    flow=FLOW_JSON_PATH,
    input_value=input_value,
    fallback_to_env_vars=True # This allows you to use GitHub Secrets for API Keys
)

# Print the final response from the last component
print(result[0].outputs[0].results)