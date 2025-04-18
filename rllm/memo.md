conda create -n rllm python=3.10 -y
conda activate rllm

cd /Document/puwaer_code_trans/rllm
pip install -e ./verl
pip install -e .
