import torch
from datasets import load_dataset
from transformers import (AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer, pipeline)
import warnings
from .utils import format_text

warnings.filterwarnings('ignore')

def llama_chat(query, base_model, llama_tokenizer):

    text_gen = pipeline(task="text-generation", model=base_model, tokenizer=llama_tokenizer, max_length=1000)
    output = text_gen(f"<s>[INST] {query} [/INST]")
    return format_text(output[0]['generated_text'])
