"""Installs this package, dependencies and executables."""


import re
from configparser import ConfigParser
from functools import lru_cache
from pathlib import Path
from typing import List, Optional  # noqa: F401

from setuptools import find_packages, setup


PROJECT_NAME = "project"


def get_version() -> str:  # pylint: disable=W9006,W9011,W9012
    """Extracts the version string from the top-level __init__.py file."""
    info_path = Path(__file__).parent / PROJECT_NAME / "__init__.py"
    with open(info_path, "rt") as info_handle:
        info = info_handle.read()
    pattern = r"^__version__ = *[\"'](.+)[\"']"
    version_match = re.search(pattern, info, re.MULTILINE)
    if version_match is not None:
        return version_match.group(1)
    else:
        raise RuntimeError(
            "Failed to parse version string from {path}".format(path=info_path.as_posix())
        )


@lru_cache(1)
def parse_pipfile() -> Optional[ConfigParser]:  # pylint: disable=W9011,W9012
    """Parses Pipfile to get the list of required packages (not dev-packages).

    NOTE: Pipfile is in TOML format, a derivative of INI. This function treats the Pipfile as an
    INI-formatted config file, out of convenience, as INI parsing in available in the Python
    standard library. This may create issues when accessing portions of a Pipfile that use non-INI
    elements of the TOML format.
    """
    pipfile_path = Path(__file__).parent / "Pipfile"
    if not pipfile_path.exists():
        return None
    config = ConfigParser()
    config.read(pipfile_path.as_posix())
    return config


def get_python_version_from_pipfile() -> Optional[str]:  # pylint: disable=W9011,W9012
    """Parses Pipfile to get the list of required packages (not dev-packages)."""
    pipfile_config = parse_pipfile()
    if (
        pipfile_config is not None
        and "requires" in pipfile_config.sections()
        and "python_version" in pipfile_config["requires"].keys()
    ):
        return ">={min_ver}".format(min_ver=pipfile_config["requires"]["python_version"])
    else:
        return None


def get_packages_from_pipfile() -> List[str]:  # pylint: disable=W9011,W9012
    """Parses Pipfile to get the list of required packages (not dev-packages)."""
    pipfile_config = parse_pipfile()
    if pipfile_config is None:
        return []
    else:
        return [
            k.strip("\"'") if v.strip("\"'") == "*" else k.strip("\"'") + v.strip("\"'")
            for k, v in pipfile_config.items("packages")
        ]


setup(
    name=PROJECT_NAME,
    version=get_version(),
    description="Description",
    # Include all python packages and modules in this repo.
    packages=find_packages(exclude=["tests"]),
    py_modules=[],
    python_requires=get_python_version_from_pipfile(),
    install_requires=get_packages_from_pipfile(),
    # Generate entry-points (i.e. executable scripts) in the environment.
    entry_points="""
        [console_scripts]
        name=package.module.cli:main
    """,
)
