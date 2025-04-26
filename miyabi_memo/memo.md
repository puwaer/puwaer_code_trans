anaconda install

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
bash Miniconda3-latest-Linux-aarch64.sh


conda create -n rllm python=3.10 -y
conda activate rllm

cd ./puwaer_code_trans/rllm

python setup.py install
pip install -e ./verl
pip install -e .

pip install numpy
pip install 

