# cookiecutter_example

![PyPI version](https://img.shields.io/pypi/v/cookiecutter_example.svg)

Python Boilerplate contains all the boilerplate you need to create a Python package.

* [GitHub](https://github.com/andlarsen/cookiecutter_example/) | [PyPI](https://pypi.org/project/cookiecutter_example/) | [Documentation](https://andlarsen.github.io/cookiecutter_example/)
* Created by [Andreas Larsen](https://audrey.feldroy.com/) | GitHub [@andlarsen](https://github.com/andlarsen) | PyPI [@andlarsen](https://pypi.org/user/andlarsen/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://andlarsen.github.io/cookiecutter_example/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/cookiecutter_example.git
cd cookiecutter_example

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `cookiecutter_example`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

cookiecutter_example was created in 2026 by Andreas Larsen.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
