import os
from huggingface_hub import HfApi
api = HfApi(endpoint="https://hf-mirror.com")
print(api.whoami())



api.create_repo(
    repo_id="xn6o/lora-vit-large-patch16-224-in21k-r32-imagenet1k",
    repo_type="model",
    exist_ok=True
)


api.upload_folder(
    folder_path="./vit_lora_imagenet_r32",
    repo_id="xn6o/lora-vit-large-patch16-224-in21k-r32-imagenet1k",
    repo_type="model"
)