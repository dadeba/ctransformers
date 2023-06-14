# -*- coding: utf-8 -*-
import ctransformers
from ctransformers import AutoModelForCausalLM

print(ctransformers.__path__)

llm = AutoModelForCausalLM.from_pretrained('nnakasato/open-calm-large-lora-all', model_type='gpt_neox', model_file='ggml-model-q4.bin')

q = "日本で一番標高の高い山は？"
i = ""

ptext = f"### Instruction:\n{q}\n\n### Input:\n{i}\n\n### Response:\n"

res = llm(ptext)

print(ptext)
print(res)
