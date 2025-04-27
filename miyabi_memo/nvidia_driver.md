

[j26001@miyabi-g3 ~]$ nvidia-smi
-bash: nvidia-smi: command not found

[j26001@miyabi-g3 ~]$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Fri_Jun_14_16:44:37_PDT_2024
Cuda compilation tools, release 12.6, V12.6.20
Build cuda_12.6.r12.6/compiler.34431801_0



nvidia-smi
(command not found)となる場合、NVIDIAドライバがインストールされていない

nvcc --version
Cuda compiler driver, cuda 12.6


nvidaiドライバー
https://www.nvidia.com/en-us/drivers/details/231054/
nvidia-driver-local-repo-rhel9-560.35.03-1.0-1.aarch64.rpm


os
Rocky Linux 9 (ログインノードはRed Hat Enterprise Linux 9)

gpu 
gh200 

os
linux aarch64-bit RHEL 9


sudoコマンドが使えない
[j26001@miyabi-g3 ~]$ sudo apt update
[sudo] password for j26001:
j26001 is not in the sudoers file.  This incident will be reported.


[j26001@miyabi-g3 ~]$ lspci | grep -i nvidia
0000:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0001:00:00.0 PCI bridge: NVIDIA Corporation Device 22b8
0002:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0004:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0006:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0008:00:00.0 PCI bridge: NVIDIA Corporation Device 22b9
0010:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0011:00:00.0 PCI bridge: NVIDIA Corporation Device 22b8
0012:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0014:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0015:00:00.0 PCI bridge: NVIDIA Corporation Device 22b8
0016:00:00.0 PCI bridge: NVIDIA Corporation Device 22b2
0018:00:00.0 PCI bridge: NVIDIA Corporation Device 22b9


現在、MiyabiでLLMの学習環境を構築中ですが、以下のような問題に直面しており、困っています。
どうすればいいのでしょうか？ また、根本的なアプローチに誤りがあり、別の解決策がある場合は教えていただきたいです。

nvidia-smiコマンドを実行すると「command not found」と表示され、NVIDIAドライバがインストールされていないためGPUが認識されていません。
一方、nvcc --versionコマンドではCUDA 12.6のコンパイラがインストールされていることが確認できました。
このようなことから、NVIDIAドライバがインストールされていなくgpuを認識していないのに、cuda 12.6のみある状態になっています。

このようなことから、以下のnvidiaのドライバーをインストールするために、sudoコマンドを使用したいのですが、私のアカウントには権限がありませんでした。

システム情報
OS: Rocky Linux 9（ログインノードは Red Hat Enterprise Linux 9）
GPU: GH200
cpu: arm系(aarch64)
CUDA バージョン: 12.6
対応するNVIDIAドライバ: nvidia-driver-local-repo-rhel9-560.35.03-1.0-1.aarch64.rpm
                    　 https://www.nvidia.com/en-us/drivers/details/231054/

コマンドの出力
[j26001@miyabi-g3 ~]$ nvidia-smi
-bash: nvidia-smi: command not found

[j26001@miyabi-g3 ~]$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Fri_Jun_14_16:44:37_PDT_2024
Cuda compilation tools, release 12.6, V12.6.20
Build cuda_12.6.r12.6/compiler.34431801_0

[j26001@miyabi-g3 ~]$ sudo apt update
[sudo] password for j26001:
j26001 is not in the sudoers file.  This incident will be reported.






# 依存パッケージインストール（カーネル開発環境）
sudo dnf install -y kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc make dkms

# ローカルリポジトリ登録
sudo rpm -i nvidia-driver-local-repo-rhel9-560.35.03-1.0-1.aarch64.rpm

# リポジトリキャッシュ更新
sudo dnf clean all
sudo dnf makecache

# ドライバインストール
sudo dnf install -y nvidia-driver

# (必要なら) Fabric Managerインストール
sudo dnf install -y nvidia-fabricmanager

# Fabric Managerを有効化・起動
sudo systemctl enable nvidia-fabricmanager
sudo systemctl start nvidia-fabricmanager

# 確認 (ドライババージョン表示)
nvidia-smi
