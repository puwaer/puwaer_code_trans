conda create -n rllm python=3.10 -y
conda activate rllm

cd Document/puwaer_code_trans/rllm
pip install -e ./verl
pip install -e .


起動
conda activate rllm
cd rllm


export MODEL_PATH="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
chmod +777 ./scripts/deepscaler/train/deepscaler_1.5b_8k.sh
./scripts/deepscaler/train/deepscaler_1.5b_8k.sh --model $MODEL_PATH


