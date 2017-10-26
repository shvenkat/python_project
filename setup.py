from configparser import ConfigParser
from pathlib import Path
from setuptools import setup, find_packages
from typing import List


def get_required_packages_from_pipfile() -> List[str]:
    """Parses Pipfile to get the list of required packages (not dev-packages)."""
    pipfile_path = Path(__file__).parent / "Pipfile"
    if not pipfile_path.exists():
        return []
    config = ConfigParser()
    config.read(pipfile_path.as_posix())
    return [k if v.strip("\"'") == "*" else k + v.strip("\"'")
            for k, v in config.items("packages")]


setup(
    name = "python_project",
    version = "1.0.0",
    description = "Project description",

    # Include all python packages and modules in this repo.
    packages = find_packages("python", exclude = ["tests"]),
    package_dir = {"": "python"},
    py_modules = [
    ],

    # Generate entry-points (i.e. executable scripts) in the environment.
    # entry_points = """
    #     [console_scripts]
    #     command=package.module:function
    # """,

    # Install dependencies.
    install_requires = get_required_packages_from_pipfile(),
)
