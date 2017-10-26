Project Summary

# Request for help

The instructions below are meant for Linux and MacOS systems. If you are using a Windows system
with this repository, *please help me* update the instructions.

# Prerequisites

Run `bin/prereq-check` and install or upgrade the missing prerequisites.

You will need:

* Python 3.6+
* Pipenv 8+

If you would like to use the non-Python bioinformatics utilities, you need:

* Docker 17+

Use a package manager of your choice to satisfy these prerequisites. For instance:

    apt-get install python3.6
    brew install python3  # Check or specify the version.

Follow the Install or Develop section below to satisfy the remaining requirements.

# Installation

## Use as a python package/library

To use this package in your python project, add to your `Pipfile`:

    [requires]
    python_version = "3.6"

    [packages]
    python_project = { git = "git@github.com:<user>/python_project", ref = "<commit-id>", editable = "true" }

## Use as a python program

Follow instructions below under 'Contribute improvements'.

# Contributing Improvements

To contribute to this package, use:

    git clone git@github.com:<user>/python_project
    cd python_project
    bin/repo-setup

## Guidelines

* Follow the coding style used in this repo. Use the settings in the `.editorconfig` file to
  configure your editor, by installing the (http://editorconfig.org)[editorconfig] plugin if needed.

* `git commit` will fail if the files you have changes do not satisfy the linting requirements for
  this repo. You can run `bin/repo-lint` to check your files before committing. In addition, you can
  or configure your editor/IDE to run the linting tools `flake8` and `mypy` *from the virtual
  environment* while you edit. Note that the linter checks the working tree not the index, and
  requires that the two be identical from git's perspective. In other words, the working tree must
  not be "dirty" when you run `git commit`, which you can verify by checking that `git diff` reports
  no changes. If you only want to commit a subset of your changes, you can stash the rest to "clean"
  the working tree.

  The above is a hack. Ideally, the linter would "check out" the staged changes into a clean working
  directory and run the linters. This would also remove the need to "clean" the working tree before
  committing changes.

* To modify the python virtual environment, update `Pipfile` and run `bin/pyvenv-update`. *Do not
  use `pip` directly*. `bin/pyvenv-update` uses `pipenv`, which - unlike `pip` - tracks packages
  installed in the virtualenv and enables a reproducible runtime and development environment.

* Keep the repo light - minimal test examples, no binary or large files.
