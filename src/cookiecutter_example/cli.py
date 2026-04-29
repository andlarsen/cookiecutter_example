"""Console script for cookiecutter_example."""

import typer
from rich.console import Console

from cookiecutter_example import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for cookiecutter_example."""
    console.print("Replace this message by putting your code into cookiecutter_example.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
