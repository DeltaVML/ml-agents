import logging
import os

import argparse

import yaml
import json

import shutil

from pathlib import Path

from huggingface_hub import HfApi, HfFolder, Repository


def _generate_config(repo_local_path, configfile_name):
    """
    Generate a config.json file from configuration.yaml
    To do that we convert yaml to json
    :param repo_local_path: path of the local repository
    :param configfile_name: name of the yaml config file (by default configuration.yaml)
    """
    # Read the YAML file and generate a config.json
    with open(os.path.join(repo_local_path, configfile_name), "r") as yaml_in, open(
        os.path.join(repo_local_path, "config.json"), "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out)


def select_tags(env_id):
    """
    Define the tags for the model card
    :param env_id: name of the environment
    """

    model_card = f"""
---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - ML-Agents-{env_id}
      library_name: ml-agents
---
    """
    return model_card


def _generate_model_card(repo_local_path, configfile_name, repo_id):
    """
    Generate the model card for the Hub
    :param model_name: name of the model
    :env_id: name of the environment
    :mean_reward: mean reward of the agent
    :std_reward: standard deviation of the mean reward of the agent
    """
    # Step 1: Read the config.json
    with open(os.path.join(repo_local_path, "config.json"), 'r') as f:
        data = json.load(f)
        # Get env_id
        env_id = list(data["behaviors"].keys())[0]
        # Get trainer_type
        model_name = data["behaviors"][env_id]["trainer_type"]

    # Step 2: Select the tags
    model_card = select_tags(env_id)

    # Step 3: Generate the model card
    model_card += f"""
  # **{model_name}** Agent playing **{env_id}**
  This is a trained model of a **{model_name}** agent playing **{env_id}** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  """

    model_card += """
  ## Usage (with ML-Agents)
  The Documentation: https://github.com/huggingface/ml-agents#get-started
  We wrote a complete tutorial to learn to train your first agent using ML-Agents and publish it to the Hub:


  ### Resume the training
  ```
  mlagents-learn <your_configuration_file_path.yaml> --run-id=<run_id> --resume
  ```
  ### Watch your Agent play
  You can watch your agent **playing directly in your browser:**.
  """

    model_card += f"""
  1. Go to https://huggingface.co/spaces/unity/Unity-ML-Agents-{env_id}
  2. Step 1: Write your model_id: {repo_id}
  3. Step 2: Select your *.nn /*.onnx file
  4. Click on Watch the agent play 👀
  """

    return model_card


def _create_model_card(repo_dir: Path, generated_model_card):
    """Creates a model card for the repository.
    :param repo_dir: repository directory
    :param generated_model_card: model card generated by _generate_model_card() method
    """
    readme_path = repo_dir / "README.md"
    readme = ""
    if readme_path.exists():
        with readme_path.open("r", encoding="utf8") as f:
            readme = f.read()
    else:
        readme = generated_model_card
    with readme_path.open("w", encoding="utf-8") as f:
        f.write(readme)


def package_to_hub(run_id,
                   path_of_run_id,
                   repo_id: str,
                   commit_message: str,
                   configfile_name,
                   use_auth_token=True,
                   local_repo_path="hub",
                   ):
    """
    This method generates the model card and upload the run_id folder
    with all his files into the Hub
    :param run_id : name of the run
    :param path_of_run_id: path of the run_id folder that contains the onnx model.
    :param commit_message: commit message
    :param configfile_name: name of the yaml config file (by default configuration.yaml)
    :param use_auth_token
    :param local_repo_path: local repository path
    """
    print(
        f"This function will create a model card and upload your {run_id} "
        f"into HuggingFace Hub. This is a work in progress: If you encounter a bug, "
        f"please send a message to thomas.simonini@huggingface.co and use mlagents-push-to-hf instead")
    huggingface_token = HfFolder.get_token()

    temp = repo_id.split('/')
    organization = temp[0]
    repo_name = temp[1]
    print("REPO NAME: ", repo_name)
    print("ORGANIZATION: ", organization)

    # Step 1: Clone or create the repo
    # Create the repo (or clone its content if it's nonempty)
    api = HfApi()
    repo_url = api.create_repo(
        name=repo_name,
        token=huggingface_token,
        organization=organization,
        private=False,
        exist_ok=True, )

    # Git pull
    repo_local_path = Path(local_repo_path) / repo_name
    repo = Repository(repo_local_path, clone_from=repo_url, use_auth_token=use_auth_token)
    repo.git_pull(rebase=True)

    repo.lfs_track(["*.onnx"])

    # Copy and paste the files to the repo
    repo_local_path = Path(local_repo_path) / repo_name

    # Store the source and destination directory path into two variables
    src_path = Path(path_of_run_id)
    dst_path = repo_local_path

    for filename in src_path.iterdir():
        _copy_file(Path(filename), repo_local_path)

    # Step 1: Create a config file
    _generate_config(repo_local_path, configfile_name)

    # Step 2: Generate the model card
    generated_model_card = _generate_model_card(repo_local_path, configfile_name, repo_id)

    _create_model_card(repo_local_path, generated_model_card)

    logging.info(f"Pushing repo {run_id} to the Hugging Face Hub")
    repo.push_to_hub(commit_message=commit_message)

    logging.info(f"Your model is pushed to the hub. You can view your model here: {repo_url}")
    print(f"Your model is pushed to the hub. You can view your model here: {repo_url}")
    return repo_url


def _copy_file(filepath: Path, dst_directory: Path):
    """
    Copy the file to the correct directory
    :param filepath: path of the file
    :param dst_directory: destination directory
    """
    dst = dst_directory / filepath.name

    if dst.is_dir():
        shutil.rmtree(str(dst))
    elif dst.is_file():
        dst.unlink()
    if filepath.is_dir():
        shutil.copytree(filepath, dst)
    elif filepath.is_file():
        shutil.copy(str(filepath), str(dst))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", help="Name of the run-id folder", type=str)
    parser.add_argument("--local-dir", help="Path of the run_id folder that contains the trained model", type=str, default="./")
    parser.add_argument("--repo-id", help="Repo id of the model repository from the Hugging Face Hub", type=str)
    parser.add_argument("--commit-message", help="Commit message", type=str)
    parser.add_argument("--configfile-name", help="Name of the configuration yaml file", type=str,
                        default="configuration.yaml")
    parser.add_argument("--use_auth_token", type=bool, default=True)
    parser.add_argument("--local-repo-path", help="local repository path", type=str, default="hub")
    args = parser.parse_args()

    print(args.run_id)
    print(args.repo_id)

    # Push model to hub
    package_to_hub(args.run_id,
                   args.local_dir,
                   args.repo_id,
                   args.commit_message,
                   args.configfile_name,
                   args.use_auth_token,
                   args.local_repo_path)

# For python debugger to directly run this script
if __name__ == "__main__":
    main()
