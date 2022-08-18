# Developing a python script

This repo is meant to be a guide for developing a python library using nbdev as a framework. This is made with focus on development at SSI and is a way to encourage us to make more reusable code that can be made available to the community via pypi and conda as well. A strong focus is put into documentation which led to the choice of nbdev as a framework. If you want additional information I recommend the reference material at https://nbdev.fast.ai/tutorial.html

## Things you'll need to get started
- A github account
- `conda` installed (preferably with `mamba`)
- A github user [token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with repo access (this is for GitHub releases via nbdev_release_gh)
    - This function makes use of the `gh` cli tool and helps create a automatic CHANGELOG.md file from your github issues and PRs. It also creates a release on github with the version number from your `settings.ini` file. This is a great way to keep track of changes and to make your code more accessible to the community. It's also a great way to get yourself more familiar with github issues using it to track requests and bugs.
- A [anaconda](https://anaconda.org/) account (optional)
    - This is optional but if you want to make your code available via conda you'll need an account. Conda is a common standard for deploying bioinformatics packages to the greater community.
- A [pypi](https://pypi.org/) account (optional)
    - This is optional but if you want to make your code available via pypi you'll need an account. Pypi is a common standard for deploying python packages to the greater community.

## First steps
Lets create a new repo on github and clone it to your local machine. I'll be using the name `nbdev_startup` for this example. You can use any name you want but I recommend using something that is descriptive of the code you're writing. I also recommend using the `nbdev` template when creating the repo. This will create a basic structure for you to start working with. If you don't use the template you'll have to create the structure yourself. This is not hard but it's a bit more work. I'll be using the template so I'll be able to skip some steps.

Install the dev env
> `mamba env create -p ./.venv --file conda.dev.env.yaml`

This will create a `.venv` folder in the root of the project. Activate it with `conda activate ./.venv`. You'll also be wanting to add this file into a `.gitignore`, This will include all the packages you need to develop the project

In this example:
```dotnetcli
USER=kimleeng
PROJECT_NAME=find_run_diff
```

Create a repo on github
> e.g. https://github.com/kimleeng/find_run_diff

Do:
`git init`
`git remote add origin git@github.com:kimleeng/find_run_diff.git`

This will set some git parameters up so that when the `nbdev_new` command is run must values will be automatically inferred.

Run command
> `nbdev_new`

It should return something like:
```dotnetcli
# settings.ini
lib_name = find_run_diff # Automatically inferred from git
user = kimleeng # Automatically inferred from git
branch = master # Automatically inferred from git
author = Kim Ng # Automatically inferred from git
author_email = kimleeng@gmail.com # Automatically inferred from git
keywords = nbdev # Automatically inferred from git
# Please enter a value for description
description =
```

For description describe what the software will do:
> e.g. `description = Checks two directories for subdirectories with minor name variations, the find the subdirectories which appear to be missing in the targer directory.`

And then it'll finish with:
```dotnetcli
# settings.ini
lib_name = find_run_diff # Automatically inferred from git
user = kimleeng # Automatically inferred from git
branch = master # Automatically inferred from git
author = Kim Ng # Automatically inferred from git
author_email = kimleeng@gmail.com # Automatically inferred from git
keywords = nbdev # Automatically inferred from git
# Please enter a value for description
description = Checks two directories for subdirectories with minor name variations, the find the subdirectories which appear to be missing in the targer directory.
repo = find_run_diff # Automatically inferred from git
```

From this it'll create the following. The majority of these should not be interacted with at all.
```dotnetcli
- .github
    - workflows
        - deploy.yaml
        - test.yaml
- find_run_diff
    - __init__.py
    - _modidx.py
    - core.py
- _quarto.yml
- .gitignore # will have to add some additional values to this.
- 00_core.ipynb # Main working file, note it generates core.py. If you create another .ipynb e.g. 01_test.ipynb it will generate test.py
- index.ipynb # Generates the README.md from it's contents
- LICENSE
- MANIFEST.in
- README.md
- settings.ini # Requires some modifaction for entry points and libraries.
- setup.py
- styles.css
```

Now we add the following to the `.gitignore` file:
> `.venv`

Then commit eveything to the repo. Once this is done check your `Actions` on github. NBDev will automatically run its actions related to testing and deploying. One of the deployments is for the documentation. If your repo is a public one adjust the GitHub pages source setting to use `Deploy from a branch` and select the `gh-pages` branch. Once you save you should then have a page available. e.g. https://kimleeng.github.io/find_run_diff/.

From here you'll be able to start making your code.

## For PyPi package deployment.

Ensure you have a `~/.pypirc` file with a user based token for [PyPi](https://pypi.org/manage/account/). Once set you can use `nbdev_pypi` to automatically deploy there. Be sure to run `nbdev_bump_version` before running again.

## For Conda package deployment

Run `nbdev_conda`

# Flow on saving a notebook change.

`nbdev_prepare`

on deploy

> `nbdev_bump_version`
>
> `nbdev_prepare`
>
> `nbdev_pypi`
Requirements here are assumed to be handled in pip.

>
> `nbdev_conda`
>
Using settings.ini it'll use requirements for checking. You will need to add alternative channels `conda config --add channels conda-forge` for it to build while looking at those locations as well

> `nbdev_release_git`

# Using 

https://nbdev.fast.ai/release.html

`nbdev_changelog` makes a chaneglog from the git repo's issues. You'll need a token in order to use this accordingly.

# Recommended default dirs
```dotnetcli
./input/ # Used as a placeholder for running
./output/ # Used as a placeholder for output
- ./config/
    - config.default.env
    - config.env # in .gitignore
./services/ # For use with systemd, this is intended for running and monitoring the task on a routine and automated basic.
```