"""
Purpose:
- Use meta llama3 model locally.

References
- model page: https://huggingface.co/meta-llama/Meta-Llama-3-8B
- hf-pipelines:
    - overview: https://huggingface.co/transformers/
    - source: https://github.com/huggingface/transformers/blob/v4.41.0/src/transformers/pipelines/__init__.py#L562
    - description: provides a simple API for NLP tasks like using models for inference.
- pytorch-accerlerate library
    - https://github.com/huggingface/accelerate
"""
import os
import torch
import transformers
from decouple import config as d_config

# Configurations
MODEL_ID = "meta-llama/Meta-Llama-3-8B"
HF_TOKEN = d_config('HF_TOKEN')

# Load Model
pipeline = transformers.pipeline(
    task="text-generation",
    model=MODEL_ID,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    token=HF_TOKEN
)




