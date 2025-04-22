メモだよ

docker run -it --rm --gpus all \
  hiyouga/verl:ngc-th2.6.0-cu126-vllm0.8.3-flashinfer0.2.2-cxx11abi0


dockerビルド
docker image build -t easy-r1 .
docker container run -it --gpus all --name easy-r1 -v $(pwd):/app easy-r1

pip install -e .

docker起動
docker start -i easy-r1
ping google.com
ping cdn-lfs-us-1.hf.co
cat /etc/resolv.conf



実行コマンド
bash examples/qwen2_5_vl_3b_geo3k_grpo_test.sh


