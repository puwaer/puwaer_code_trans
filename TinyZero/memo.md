conda環境構築
conda create -n tiny_zero python=3.9
conda activate tiny_zero

pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cu121
pip3 install vllm==0.6.3 
pip3 install ray

cd Document/puwaer_code_trans/TinyZero
pip install -e .

pip3 install flash-attn --no-build-isolation
pip install wandb IPython matplotlib


実行コマンド
conda activate tiny_zero


python ./examples/data_preprocess/countdown.py --local_dir ./dataset


学習コマンド
conda activate tiny_zero
cd TinyZero

export N_GPUS=1
export BASE_MODEL=base_model/Qwen2.5-1.5B-Instruct
export DATA_DIR=dataset
export ROLLOUT_TP_SIZE=1
export EXPERIMENT_NAME=countdown-qwen2.5-1.5b_test_2
export VLLM_ATTENTION_BACKEND=XFORMERS

chmod +777 ./scripts/train_tiny_zero_qwen_1.5b.sh
bash ./scripts/train_tiny_zero_qwen_1.5b.sh

