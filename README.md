# Learning how to do relative imports

## `firstpackage-env` conda environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `firstpackage-env` conda environment. To do so, please run the following commands:

```bash
# create the conda environment
# note: this make take anywhere from 1-5 minutes
conda env create -f environment.yml

# activate the conda environment
conda activate firstpackage-env
```

### Note

Because this project is dependent on the user pip installing the `src/` directory as a package, it's important to only create the environment from the project directory and not another location.

## Instructions on building a local package

### Step 1: Create `setup.py` file

Example `setup.py` file to put at the root of your repository for making your `src/` directory a package:

```python
from setuptools import find_packages, setup
setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    author="Cristian E. Nuno"
)
```

### Step 2. Create an empty file labeled as `__init__.py` inside of the `src/` directory

### Step 3. Just once, you will need to `pip install` your `src/` as a package:

Run the following from your root project directory in the Terminal/Command Line:

```bash
# note: here we're installing the src/ directory as a package that we called "src"
pip install -e .
```

### Step 4. Manually edit the `environment.yml` file to include instructions on how to `pip` install the `src` package

Unfortunately, the following bash command:

```bash
conda env export > environment.yml
```
does not export both `conda` and `pip` requirements in the `conda` environment.
Instead, you will have to manually add the `pip` installation of the `src` package like so:

```yml
# add this at the end of all conda installs and before the prefix
  - pip:
    - -e .
```

## Overview of directory structure

```
.
├── LICENSE
├── README.md
├── environment.yml
├── notebooks
│   ├── README.md
│   ├── exploratory
│   │   └── README.md
│   └── report
│       ├── README.md
│       └── final.ipynb
├── setup.py
└── src
    ├── README.md
    ├── __init__.py
    └── data
        ├── README.md
        └── utilities.py
```
