環境構築
uv venv openr1 --python 3.11 && source openr1/bin/activate && uv pip install --upgrade pip
uv pip install vllm==0.8.3
uv pip install setuptools && uv pip install flash-attn --no-build-isolation

cd open-r1
GIT_LFS_SKIP_SMUDGE=1 uv pip install -e ".[dev]"
huggingface-cli login
wandb login
git-lfs --version
sudo apt-get install git-lfs

gcc --version
sudo apt update
sudo apt install build-essential


環境起動
source openr1/bin/activate
cd Document/puwaer_code_trans/open-r1/

deactivate

export=LD_LIBRARY_PATH=/openr1/lib/python3.11/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH



学習 実行コマンド
accelerate launch --config_file recipes/accelerate_configs/zero3.yaml src/open_r1/sft.py \
    --config recipes/Qwen2.5-1.5B-Instruct/sft/config_demo.yaml

accelerate launch --config_file recipes/accelerate_configs/zero2.yaml src/open_r1/sft.py \
    --config recipes/Qwen2.5-1.5B-Instruct/sft/config_demo.yaml

CUDA_VISIBLE_DEVICES=0 accelerate launch --config_file recipes/accelerate_configs/zero2.yaml src/open_r1/sft.py \
    --config recipes/Qwen2.5-1.5B-Instruct/sft/config_demo.yaml