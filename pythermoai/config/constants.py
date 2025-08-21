# import libs

# local

# SECTION: available llm providers
llm_providers = ["openai", "google", "anthropic", "grok"]

# SECTION: token metadata
# set default values for input and output tokens
default_token_metadata = {
    "input_tokens": -1,
    "output_tokens": -1
}

# set default temperature and max tokens
default_model_settings = {
    "temperature": 0.0,
    "max_tokens": 2048
}
