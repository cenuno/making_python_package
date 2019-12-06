# Learning how to do relative imports

## Step 1: Create `setup.py` file
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

## Step 2. Create an empty file labeled as `__init__.py` inside of the `src/` directory

## Step 3. Just once, you will need to `pip install` your `src/` as a package:

Run the following from your root project directory in the Terminal/Command Line:

```bash
# note: here we're installing the src/ directory as a package that we called "src"
pip install -e .
```

## Overview of directory structure

```
.
├── README.md
├── notebooks
│   ├── README.md
│   ├── exploratory
│   │   └── README.md
│   └── report
│       └── README.md
├── setup.py
└── src
    ├── README.md
    ├── __init__.py
    └── data
        ├── README.md
        └── utilities.py
```