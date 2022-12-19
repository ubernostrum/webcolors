"""
Automated testing via nox (https://nox.thea.codes/).

Combined with a working installation of nox (``pip install nox``), this file specifies a
matrix of tests, linters, and other quality checks which can be run individually or as a
suite.

To see available tasks, run ``nox --list``. To run all available tasks -- which requires
functioning installs of all supported Python versions -- run ``nox``. To run a single
task, use ``nox -s`` with the name of that task.

"""
import os

import nox

nox.options.default_venv_backend = "venv"
nox.options.keywords = "not release"
nox.options.reuse_existing_virtualenvs = True


# Tasks which run the package's test suites.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"], tags=["tests"])
def tests_with_coverage(session: nox.Session) -> None:
    """
    Run the package's unit tests, with coverage report.

    """
    session.install("pytest", "pytest-cov", ".")
    session.run(
        "python",
        "-Wonce::DeprecationWarning",
        "-Im",
        "pytest",
        "-vv",
        "--ignore=src",
        "--cov=webcolors",
        "--cov-report",
        "term-missing",
    )


@nox.session(python=["3.11"], tags=["tests", "release"])
def tests_definitions(session: nox.Session) -> None:
    """
    Run the full color definitions test suite (requires an internet connection).

    """
    session.install("pytest", "bs4", "html5lib", "requests", ".")
    session.run("python", "-Im", "pytest", "-vv", "tests/definitions.py")


@nox.session(python=["3.11"], tags=["tests", "release"])
def tests_full_colors(session: nox.Session) -> None:
    """
    Run the full color conversion test suite (slow/CPU-intensive).

    """
    session.install("pytest", ".")
    session.run("python", "-Im", "pytest", "-vv", "tests/full_colors.py")


# Tasks which test the package's documentation.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.11"], tags=["docs"])
def docs_build(session: nox.Session) -> None:
    """
    Build the package's documentation as HTML.

    """
    session.install(
        "furo", "sphinx", "sphinx-notfound-page", "sphinxext-opengraph", "."
    )
    session.run(
        "python",
        "-Im",
        "sphinx",
        "-c",
        "docs/",
        "-b",
        "html",
        "-d",
        "docs/_build/doctrees/html",
        "docs/",
        "docs/_build/html",
    )


@nox.session(python=["3.11"], tags=["docs"])
def docs_docstrings(session: nox.Session) -> None:
    """
    Enforce the presence of docstrings on all modules, classes, functions, and
    methods.

    """
    session.install("interrogate")
    session.run("python", "-Im", "interrogate", "--version")
    session.run("python", "-Im", "interrogate", "-v", "src/", "tests/", "noxfile.py")


@nox.session(python=["3.11"], tags=["docs"])
def docs_spellcheck(session: nox.Session) -> None:
    """
    Spell-check the package's documentation.

    """
    session.install(
        "furo",
        "pyenchant",
        "sphinx",
        "sphinxcontrib-spelling",
        "sphinx-notfound-page",
        "sphinxext-opengraph",
        ".",
    )
    session.run(
        "python",
        "-Im",
        "sphinx",
        "-W",  # Promote warnings to errors, so that misspelled words fail the build.
        "-c",
        "docs/",
        "-b",
        "spelling",
        "-d",
        "docs/_build/doctrees/html",
        "docs/",
        "docs/_build/html",
        # On Apple Silicon Macs, this environment variable needs to be set so
        # pyenchant can find the "enchant" C library. See
        # https://github.com/pyenchant/pyenchant/issues/265#issuecomment-1126415843
        env={"PYENCHANT_LIBRARY_PATH": os.getenv("PYENCHANT_LIBRARY_PATH", "")},
    )


@nox.session(python=["3.11"], tags=["docs", "tests"])
def docs_test(session: nox.Session) -> None:
    """
    Run the code samples in the documentation with doctest, to ensure they are
    correct.

    """
    session.install("sphinx", "sphinx-notfound-page", "sphinxext-opengraph", ".")
    session.run(
        "python",
        "-Im",
        "sphinx",
        "-c",
        "docs/",
        "-b",
        "doctest",
        "-d",
        "docs/_build/doctrees/html",
        "docs/",
        "docs/_build/html",
    )


# Code formatting checks.
#
# These checks do *not* reformat code -- that happens in pre-commit hooks -- but will
# fail a CI build if they find any code that needs reformatting.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.11"], tags=["formatters"])
def format_black(session: nox.Session) -> None:
    """
    Check code formatting with Black.

    """
    session.install("black")
    session.run("python", "-Im", "black", "--version")
    session.run(
        "python",
        "-Im",
        "black",
        "--check",
        "--diff",
        "src/",
        "tests/",
        "docs/",
        "noxfile.py",
    )


@nox.session(python=["3.11"], tags=["formatters"])
def format_isort(session: nox.Session) -> None:
    """
    Check code formating with Black.

    """
    session.install("isort")
    session.run("python", "-Im", "isort", "--version")
    session.run(
        "python",
        "-Im",
        "isort",
        "--check-only",
        "--diff",
        "src/",
        "tests/",
        "docs/",
        "noxfile.py",
    )


# Linters.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.11"], tags=["linters", "security"])
def lint_bandit(session: nox.Session) -> None:
    """
    Lint code with the Bandit security analyzer.

    """
    session.install("bandit[toml]")
    session.run("python", "-Im", "bandit", "--version")
    session.run(
        "python", "-Im", "bandit", "-c", "./pyproject.toml", "-r", "src/", "tests/"
    )


@nox.session(python=["3.11"], tags=["linters"])
def lint_flake8(session: nox.Session) -> None:
    """
    Lint code with flake8.

    """
    session.install("flake8", "flake8-bugbear")
    session.run("python", "-Im", "flake8", "--version")
    session.run("python", "-Im", "flake8", "src/", "tests/", "docs/", "noxfile.py")


@nox.session(python=["3.11"], tags=["linters"])
def lint_pylint(session: nox.Session) -> None:
    """
    Lint code with Pyling.

    """
    # Pylint requires that all dependencies be importable during the run. This package
    # does not have any direct dependencies, nor does the normal test suite, but the
    # full conformance suite does require a few extra libraries, so they're installed
    # here.
    session.install("pylint", "bs4", "html5lib", "requests")
    session.run("python", "-Im", "pylint", "--version")
    session.run("python", "-Im", "pylint", "src/", "tests/")


# Packaging checks.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.11"], tags=["packaging"])
def package_build(session: nox.Session) -> None:
    """
    Check that the package builds.

    """
    session.install("build")
    session.run("python", "-Im", "build", "--version")
    session.run("python", "-Im", "build")


@nox.session(python=["3.11"], tags=["packaging"])
def package_description(session: nox.Session) -> None:
    """
    Check that the package description will render on the Python Package Index.

    """
    package_dir = session.create_tmp()
    session.install("build", "twine")
    session.run("python", "-Im", "build", "--version")
    session.run("python", "-Im", "twine", "--version")
    session.run("python", "-Im", "build", "--wheel", "--outdir", f"{package_dir}/build")
    session.run("python", "-Im", "twine", "check", f"{package_dir}/build/*")


@nox.session(python=["3.11"], tags=["packaging"])
def package_manifest(session: nox.Session) -> None:
    """
    Check that the set of files in the package matches the set under version control.

    """
    session.install("check-manifest")
    session.run("python", "-Im", "check_manifest", "--version")
    session.run("python", "-Im", "check_manifest", "--verbose")


@nox.session(python=["3.11"], tags=["packaging"])
def package_pyroma(session: nox.Session) -> None:
    """
    Check package quality with pyroma.

    """
    session.install("pyroma")
    session.run("python", "-Im", "pyroma", ".")


@nox.session(python=["3.11"], tags=["packaging"])
def package_wheel(session: nox.Session) -> None:
    """
    Check the built wheel package for common errors.

    """
    package_dir = session.create_tmp()
    session.install("build", "check-wheel-contents")
    session.run("python", "-Im", "build", "--version")
    session.run("python", "-Im", "check_wheel_contents", "--version")
    session.run("python", "-Im", "build", "--wheel", "--outdir", f"{package_dir}/build")
    session.run("python", "-Im", "check_wheel_contents", f"{package_dir}/build")
