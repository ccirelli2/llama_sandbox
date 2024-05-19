"""
https://huggingface.co/blog/not-lain/rag-chatbot-using-llama3
"""
import os
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from decouple import config as d_config

# Config
MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
HF_TOKEN = d_config('HF_TOKEN')

# Quantization Config
BNB_CONFIG = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# TOKENIZER
TOKENIZER = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path=MODEL_ID,
    use_fast=False,
    token=HF_TOKEN
)

# MODEL
MODEL = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    quantization_config=BNB_CONFIG,
    token=HF_TOKEN
)

terminators = [
    TOKENIZER.eos_token_id,
    TOKENIZER.convert_tokens_to_ids("<|eot_id|>")
]
