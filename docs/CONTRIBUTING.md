# Contributing to this project


## Reporting Bugs

Please report bugs on github as issues. If there's an open issue matching the bug, please add your
comments to it. Fill out the issue template thoroughly, to allow others to reproduce and fix the
issue.


## Contributing Code and Documentation

Follow the [code](#code-guidelines) and [repository](#repository-guidelines) guidelines below to
create your contribution, commit it, have it reviewed and merge it. Please read it all carefully.


## Code Guidelines

### Documentation

**Document the requirements, design and implementation** in the Python source files. Use
[reStructured Text][rest] and the [Google docstring format][sphinx_google]. **Provide internal
links** to relevant classes, methods, attributes, functions, types and constants using markup
directives such as `:class:`, `:meth:` and `:func:`. You can even **provide schematic diagrams** in
as literal/code blocks (i.e. preceeded by a line ending with `::`).

[rest]: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
[sphinx_google]: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

  * Regular (function or method) docstrings should include the following:

      * A summary line -- in the style "Calculates X using method Y and data Z" or "Requests a Foo
        from service Bar using protocol Quux" -- followed by a blank line.

      * A brief description of what the associated code does. Any assumptions, pre-conditions
        (e.g. constraints on values of arguments, existence of a file or directory, use of a global
        variable) and post-conditions should be summarized.

      * Arguments, return values and their types.

      * Exceptions and why they are raised. These should be listed for all functions and methods
        that raise them, and by public methods or functions that do not handle them.

  * Class docstrings should include the documentation for the constructor (`__new__` or `__init__`),
    as well as for class and instance attributes.

  * Package (`__init__.py`) and module-level (`*.py`) docstrings should include the following
    sections, as appropriate:

      * `Todo`: A list of gaps and open items.

      * `REQUIREMENTS`: The high-level goals to be met.

      * `DESIGN`: The engineering choices made to meet the requirements, including algorithms, data
        structures, file formats, logic of each component and the interaction between components.

      * `IMPLEMENTATION`: The public interface (classes and functions that users and other modules
        are allowed to use) and internal logic (summary description of methods and functions and how
        they relate to each other).

See the [Notes](#notes) section for a discussion of documentation styles and tools.

To view the documentation, use `bin/build-docs` which runs Sphinx to build the documentation and
opens it in your default web browser. As noted in the repo README, you may need `latex` and `dvipng`
if the documentation includes math.

#### Call For Help

Help setting up online documentation would be welcome. Options include:

  * [ReadTheDocs][rtd], which builds and serves documentation from any branch, tag or commit.
  * [Github Pages][ghp], which requires that the built documentation be committed to the repo.

Alternatively, if you are willing to set up a simple webserver to host static pages and some
quick-n-dirty automation (such as a cron job that periodically runs `git pull` followed by
`bin/build-docs`), please volunteer.

[rtd]: https://readthedocs.com
[ghp]: https://pages.github.com

### Coding Practices

  * **Type Annotation**: All functions and methods should be annotated with types, for use with a
    type checker such as `mypy`.

    For a small number of arguments, include multiple arguments on each line. For a large number of
    arguments, use a multi-line signature with each argument and its type annotation on a separate
    line.

        def foo(x: int, y: float) -> bool:
            """Returns True if x <= y."
            return x <= y

        def bar(
            x: int,
            y: float,
        ) -> bool:
            """Returns True if x > y."
            return not foo(x, y)

    To further abbreviate type annotations, `mypy` is configured such that `Optional[...]` can be
    omitted for arguments with a default value of `None`. For instance, the following are
    equivalent:

        def foo(x, y=None):
            # type: (int, Optional[float]) -> bool
            """Returns True if x <= y or x <= 0 if y is not specified."""
            ...

        def foo(x, y=None):
            # type: (int, float) -> bool
            """Returns True if x <= y or x <= 0 if y is not specified."""
            ...

  * **Keyword-only Arguments**: Functions and methods with two or more arguments should designate
    all as keyword-only, with the possible exception of the first. Implicit arguments such as `self`
    and `cls` are ignored for the purpose of this guideline. The resulting function/method calls are
    explicit and easier to read. In addition, the risk of swapping arguments of the same type is
    also reduced.

        def send_foo(foo, *, bar, quux):
            # type: (Foo, Bar, Quux) -> None
            """Sends ``foo`` to ``bar`` using ``quux``."""
            ...

        foo = Foo(...)
        send_foo(foo, bar=..., quux=...)

### Code and Documentation Linting

Python source in this repo is checked for:

  * Type errors, using [`mypy`][mypy].
  * Usage issues, using [`flake8`][flake8].
  * Usage and documentation issues, using [`pylint`][pylint].

**Errors detected by these checkers have to fixed manually.** Activate the project virtualenv
(`PIPENV_VENV_IN_PROJECT=1 pipenv shell` or `source .venv/bin/activate`) to use the correct version
of these programs. Settings for these programs are also tracked in the repo. The source can be
linted in one of the following ways:

  * Automatically by your code editor or IDE. For instance, you can configure flycheck on emacs or
    neomake on vim/neovim to run these programs while you edit or whenever the files are
    saved. Ensure that your editor or IDE uses the project virtualenv and settings files.
  * Automatically by `git commit` through the pre-commit hook calling `bin/lint-repo`.
  * Automatically by Travis CI running `bin/lint-repo`.
  * Manually by running `bin/lint-repo`.

[mypy]: http://mypy-lang.org/
[flake8]: http://flake8.pycqa.org/en/latest/
[pylint]: https://www.pylint.org/

### Coding Style

Python source in this repo should be formatted according to our style guide. This style is
operationally defined as that generated using:

  * [editorconfig][editorconfig] for whitespace and line length, as configured in `.editorconfig`.
  * [`black`][black], a python source formatter, which allows no configuration other than line
    length. As in "Any color you like, as long as it's black".
  * [`isort`][isort], an import statement formatter, with settings in `.isort.cfg`.

**The coding style can be applied automatically**. Use an editorconfig plugin for your editor/IDE.
For the remaining formatters, the project virtualenv provides the correct versions.  These can be
run in the following ways:

  * Automatically by your editor/IDE by configuring it appropriately or using plugins. For instance,
    there are emacs packages available to run `black` and `isort` on a buffer when it is saved. For
    details see the [Notes](#notes) section below.
  * Automatically by `git add` using a "clean filter" specified in `.gitattributes` and implemented
    in `bin/format-python`. This can be problematic, as the working tree can differ from the repo,
    which can be confusing.
  * Manually, using `bin/format-repo`.

[editorconfig]: http://editorconfig.org
[black]: https://github.com/ambv/black
[isort]: https://github.com/timothycrosley/isort

### Tracking dependencies

Use `pipenv` and the `Pipfile` to track Python dependencies. The scripts in `bin/` automatically
update the virtual environment whenever the `Pipfile` is changed. To manually update, use
`bin/update-venv`. **Do not use `pip` directly**. `pipenv`, which -- unlike `pip` -- tracks packages
installed in the virtualenv and enables a reproducible runtime and development environment.


## Repository guidelines

### Branch standards

  * `master` is production-ready code that is documented, tested and reviewed by at least two team
    members. The bar for code in `master` is high. Each release is tagged. This is the branch that
    other projects should use.

  * `develop` is where new features are _aggregated_. The bar for code in `develop` is
    intermediate. The code should not only work, but be at least somewhat documented and at least
    minimally tested. At least one team member should have reviewed code prior to merging to
    `develop`. This is the default branch on Github and the one for which documentation is hosted by
    Github.

  * `hotfix/*` branches are intended to fix a bug in `master`. So they branch off from `master` and
    are merged into both `master` and `develop`.

  * `feature/*` branches are intended to add new features to `develop`. The bar for these branches
    is low, to allow fast iteration. Code may be in any state, although early sharing, documentation
    and testing are highly encouraged. These branch off from `develop` and are merged back into
    `develop`, after review.  You don't have to wait till your documentation and testing are
    complete to merge. For large features, consider breaking them up into smaller features to allow
    you to integrate the early pieces into `develop` sooner.

    To ensure that you can merge cleanly, you may want to merge the latest from `develop` into your
    feature branch prior to merging it into `develop`.

  * `release/*` branches are the way to release new features from `develop` to `master`. Use these
    branches to bring the documentation, testing and review up to the standard of `master`.

### Git commit messages

To allow others to follow your contribution, please use the following template for all your commit
messages. In addition, for large changes, please try to divide the work into a series of small
incremental commits.

    Fix #1234: Summary sentence with capitalized first letter.

    Summary should ideally be around 50 characters or less, certainly no more
    than 72. The summary should be prefixed by "Fix #1234: " if the commit
    fixes github issue #1234. Additional details, if needed, can be included
    in paragraphs separated by a blank line and wrapped at 72 characters.

    - Bulleted lists can be included. List elements use a hanging indent as
      seen here.

### File restrictions

Keep the repo light - minimal test data, no binary or large files. No GIT LFS, unless there is a
clear need and other solutions have been explored and found inadequate.

### Rebasing branches

Please do not rebase branches once you've pushed them. It can be confusing for teammates to keep up
with rebases if they have already started building on your pre-rebase branch.

### Deleting branches

Delete hotfix, feature and release branches after merging, both locally and on Github.

### Pull Requests

Pull requests on Github are used to review branches prior to merging. Make sure to use the correct
"base" or "target" branch when created the PR. Fill out all the sections of the PR template. The
number of required reviews depends on the target branch (see [Branch standards](#branch-standards)).
Upon completion of the review, merge and delete the branch.

### Backwards compatibility

Changes that break backwards compatibility of the code should be discussed and planned. Prior to
merging, all users of the library need to be informed about the changes.


## Notes

### Docstring styles

  * For a discussion on different docstring styles, you can start at
    https://stackoverflow.com/a/24385103.

  * Your favorite code editor or IDE may use or even auto-fill a docstring template for you. For
    instance, if you use PyCharm, see https://stackoverflow.com/a/33497841.

### Coding style

  * For a discussion on the choice of a code formatter, see
    https://news.ycombinator.com/item?id=17151813 and, in particular
    https://news.ycombinator.com/item?id=17155205 for ways `black` may improve upon `yapf`.

  * To integrate `black` with your editor/IDE, consult the [`black` README][black-readme]. Shiv can
    help with emacs configuration.

  * To integrate `isort` with your editor/IDE, consult the [`isort` wiki][isort-wiki]. You can also
    ask Shiv for emacs configuration.

[black-readme]: https://github.com/ambv/black#editor-integration
[isort-wiki]: https://github.com/timothycrosley/isort/wiki/isort-Plugins
