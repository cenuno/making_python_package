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

# Step 2. Create an empty file labeled as `__init__.py` inside of the `src/` directory


