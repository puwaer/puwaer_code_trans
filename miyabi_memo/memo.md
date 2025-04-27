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


wget https://jp.download.nvidia.com/tesla/560.35.03/NVIDIA-Linux-aarch64-560.35.03.run
bash NVIDIA-Linux-aarch64-560.35.03.run



pytorchについて
pip3 install torch torchvision torchaudio
Successfully installed MarkupSafe-3.0.2 filelock-3.18.0 fsspec-2025.3.2 jinja2-3.1.6 mpmath-1.3.0 networkx-3.2.1 numpy-2.0.2 pillow-11.2.1 sympy-1.13.3 torch-2.7.0 torchaudio-2.7.0 torchvision-0.22.0 typing-extensions-4.13.2


conda install -c nvidia/label/cuda-12.1.0 cuda-toolkit -y
conda install -c conda-forge cudnn=8.9.7 nccl=2.18.3 mpi4py=3.1.6 -y
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
Looking in indexes: https://download.pytorch.org/whl/cu121