メモだよ

docker run -it --rm --gpus all \
  hiyouga/verl:ngc-th2.6.0-cu126-vllm0.8.3-flashinfer0.2.2-cxx11abi0

docker run --gpus all -it --rm -p 8000:8000 hiyouga/verl:ngc-th2.6.0-cu126-vllm0.8.3-flashinfer0.2.2-cxx11abi0


実行コマンド
docker container run -it --gpus all  --name verl-container -v $(pwd):/workspace hiyouga/verl:ngc-th2.6.0-cu126-vllm0.8.3-flashinfer0.2.2-cxx11abi0

docker start -ai verl-container




dockerビルド
docker image build -t easy-r1 .
docker container run -it --gpus all --shm-size=8g --name easy-r1 -v $(pwd):/app easy-r1

pip install -e .
ping google.com
ping cdn-lfs-us-1.hf.co
cat /etc/resolv.conf

wandb login



docker起動
docker start -i easy-r1



実行コマンド
bash examples/qwen2_5_vl_3b_geo3k_grpo_test.sh


