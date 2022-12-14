# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['set_env_variables', 'find_runs', 'find_runs_in_source_but_not_dest', 'cli']

# %% ../00_core.ipynb 4
# standard libs
import os
import re

# add into settings.ini, package name is python-dotenv
from dotenv import dotenv_values # Used for loading configs

# %% ../00_core.ipynb 5
from dotenv import load_dotenv # for loading config from .env files

def set_env_variables(config_path) -> bool:
    # Order of precedence: environment variables > .env file > default values

    # Set the env vars first, this is needed for the card.yaml to replace ENV variables
    if config_path is not None:
        load_dotenv(config_path)
    load_dotenv("./config/config.default.env")

    return True

# %% ../00_core.ipynb 6
import os
set_env_variables(os.environ.get("FRD_CONFIG_PATH"))

# %% ../00_core.ipynb 8
def find_runs(dir, regex):
    # make keys from capture groups of regex
    runs = {}
    for root, dirs, files in os.walk(dir):
        for dir in dirs:
            if regex.match(dir):
                key = ""
                for group in range(1, regex.match(dir).lastindex + 1):
                    key += regex.match(dir).group(group)
                runs[key] = os.path.join(root, dir)
    return runs

# %% ../00_core.ipynb 9
def find_runs_in_source_but_not_dest(source_dir, source_regex, destination_dir, destination_regex, output_file):
    source_runs = find_runs(source_dir, source_regex)
    destination_runs = find_runs(destination_dir, destination_regex)

    target_runs = set(source_runs.keys()) - set(destination_runs.keys())
    target_runs = sorted(target_runs)

    with open(output_file, 'w') as f:
        f.write(f'#paths\n')
        for run in target_runs:
            f.write(f"{source_runs[run]}\n")

# %% ../00_core.ipynb 10
from fastcore.script import call_parse
import os

@call_parse
def cli(
    source_dir:str=os.environ.get("FRD_SOURCE_DIR"), # Path to source directory
    dest_dir:str=os.environ.get("FRD_DEST_DIR"), # Path to destination directory
    source_regex:str=os.environ.get("FRD_SOURCE_REGEX"), # Regex to match source directory
    dest_regex:str=os.environ.get("FRD_DEST_REGEX"), # Regex to match destination directory
    output_file:str=os.environ.get("FRD_OUTPUT_FILE"), # Path to output file
    ):
    "Move all files in source_dir to dest_dir"
    find_runs_in_source_but_not_dest(source_dir, source_regex, dest_dir, dest_regex, output_file)
    print("Hello World!")
