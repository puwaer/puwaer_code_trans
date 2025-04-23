set -x

#MODEL_PATH=Qwen/Qwen2.5-VL-3B-Instruct  # replace it with your local file path
MODEL_PATH=Qwen/Qwen2.5-3B-Instruct

python3 -m verl.trainer.main \
    config=examples/config_3b.yaml \
    data.train_files=hiyouga/geometry3k@train \
    data.val_files=hiyouga/geometry3k@test \
    worker.actor.model.model_path=${MODEL_PATH} \
    worker.rollout.tensor_parallel_size=1 \
    worker.actor.fsdp.torch_dtype=bf16 \
    worker.actor.optim.strategy=adamw_bf16 \
    trainer.experiment_name=qwen2_5_vl_3b_geo_grpo \
    trainer.n_gpus_per_node=1
