Install the dev env
> `mamba env create -p ./.venv --file conda.dev.env.yaml`

This will create a `.venv` folder in the root of the project. Activate it with `conda activate ./.venv`. You'll also be wanting to add this file into a `.gitignore`

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

Then commit eveything to the repo.
