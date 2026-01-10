from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKENN"))
api.upload_folder(
    folder_path="week_2_mls/deployment",     # the local folder containing your files
    repo_id="kjdeka/Machine-Failure-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
