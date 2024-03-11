# TechAI

Welcome to TechAI, an Arkansas Tech University-based AI research group.

## Setup Instructions

To contribute to TechAI, you need to set up your development environment.

### Creating a Virtual Environment

First, create a new virtual environment to manage dependencies separately from your global Python installation.

#### For Unix/MacOS:

```sh
python -m venv .venv
source .venv/bin/activate
```

#### For Windows:

```sh
python -m venv .venv
.\.venv\Scripts\activate
```

### Installing Dependencies

With your virtual environment activated, install the project's dependencies to ensure your development environment
matches the project's requirements:

```sh
pip install -r requirements.txt
```

## Contributing Guidelines

### Commit Standards with Commitizen

We use [Commitizen](https://commitizen-tools.github.io/commitizen/) to standardize our commit messages, making our
project history more readable and easier to navigate.

**Preparing Your Commit**: After staging your changes with `git add`, use `cz commit` instead of `git commit`. Follow
the prompts to fill out the required commit fields.

**Commit Message Format**: Commitizen will guide you through creating a commit message that follows our standards. This
ensures consistency across the project's history.

### Managing Dependencies

**Update requirements.txt Regularly**: Whenever you add, update, or remove a dependency, update the
`requirements.txt` file and commit the changes. This ensures that all contributors are working with the same set of
dependencies.

**Testing Major Updates**: Before merging major dependency updates into the main branch, test them in a separate branch.
This minimizes potential disruptions caused by the updates.

To update requirements.txt, use:

```sh
pip freeze > requirements.txt
cz commit
```