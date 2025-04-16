import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model_name = "Qwen/Qwen2.5-1.5B-Instruct"
logger.info("Loading tokenizer")
tokenizer = AutoTokenizer.from_pretrained(model_name)

logger.info("Loading model")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map=None,
)
model = model.to('cuda')
logger.info(f"Model device: {model.device}")

logger.info("Testing forward pass")
inputs = tokenizer("Hello, world!", return_tensors="pt").to('cuda')
outputs = model(**inputs)
logger.info("Forward pass completed")