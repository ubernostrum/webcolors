"""
Automated testing via nox (https://nox.thea.codes/).

Combined with a working installation of nox (see ``nox`` documentation), this file
specifies a matrix of tests, linters, and other quality checks which can be run
individually or as a suite.

To see available tasks, run ``python -m nox --list``. To run all available tasks --
which requires functioning installs of all supported Python versions -- run ``python -m
nox``. To run a single task, use ``python -m nox --session`` with the name of that task.

"""

import os
import pathlib
import shutil
import typing

import nox

nox.options.default_venv_backend = "venv"
nox.options.reuse_existing_virtualenvs = True

PACKAGE_NAME = "webcolors"

IS_CI = bool(os.getenv("CI", False))

NOXFILE_PATH = pathlib.Path(__file__).parents[0]
ARTIFACT_PATHS = (
    NOXFILE_PATH / "src" / f"{PACKAGE_NAME}.egg-info",
    NOXFILE_PATH / "build",
    NOXFILE_PATH / "dist",
    NOXFILE_PATH / "__pycache__",
    NOXFILE_PATH / "src" / "__pycache__",
    NOXFILE_PATH / "src" / PACKAGE_NAME / "__pycache__",
    NOXFILE_PATH / "tests" / "__pycache__",
)


def clean(paths: typing.Iterable[pathlib.Path] = ARTIFACT_PATHS) -> None:
    """
    Clean up after a test run.

    """
    # This cleanup is only useful for the working directory of a local checkout; in CI
    # we don't need it because CI environments are ephemeral anyway.
    if IS_CI:
        return
    [
        shutil.rmtree(path) if path.is_dir() else path.unlink()
        for path in paths
        if path.exists()
    ]


# Tasks which run the package's test suites.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.10", "3.11", "3.12", "3.13", "3.14"], tags=["tests"])
def tests_with_coverage(session: nox.Session) -> None:
    """
    Run the package's unit tests, with coverage instrumentation.

    """
    session.install(".", "pytest", "coverage[toml]")
    session.run(
        f"python{session.python}",
        "-Wonce::DeprecationWarning",
        "-Im",
        "coverage",
        "run",
        "-m",
        "pytest",
        "-vv",
    )
    clean()


@nox.session(python=["3.13"], tags=["tests"])
def coverage_report(session: nox.Session) -> None:
    """
    Combine coverage from the various test runs and output the report.

    """
    # In CI this job does not run because we substitute one that integrates with the CI
    # system.
    if IS_CI:
        session.skip(
            "Running in CI -- skipping nox coverage job in favor of CI coverage job"
        )
    session.install("coverage[toml]")
    session.run(f"python{session.python}", "-Im", "coverage", "combine")
    session.run(
        f"python{session.python}", "-Im", "coverage", "report", "--show-missing"
    )
    session.run(f"python{session.python}", "-Im", "coverage", "erase")


@nox.session(python=["3.13"], tags=["release"])
def tests_definitions(session: nox.Session) -> None:
    """
    Run the full color definitions test suite (requires an internet connection).

    """
    if IS_CI:
        session.skip("Release tests do not run in CI.")
    session.install("pytest", "bs4", "html5lib", "requests", ".[tests]")
    session.run(f"python{session.python}", "-I", "tests/definitions.py")
    clean()


@nox.session(python=["3.13"], tags=["release"])
def tests_full_colors(session: nox.Session) -> None:
    """
    Run the full color conversion test suite (slow/CPU-intensive).

    """
    if IS_CI:
        session.skip("Release tests do not run in CI.")
    session.install(".[tests]")
    session.run(f"python{session.python}", "-I", "tests/full_colors.py")
    clean()


# Tasks which test the package's documentation.
# -----------------------------------------------------------------------------------


# The documentation jobs ordinarily would want to use the latest Python version, but
# currently that's 3.13 and Read The Docs doesn't yet support it. So to ensure the
# documentation jobs are as closely matched to what would happen on RTD, these jobs stay
# on 3.12 for now.
@nox.session(python=["3.12"], tags=["docs"])
def docs_build(session: nox.Session) -> None:
    """
    Build the package's documentation as HTML.

    """
    session.install(".", "-r", "docs/requirements.txt")
    build_dir = session.create_tmp()
    session.run(
        f"{session.bin}/python{session.python}",
        "-Im",
        "sphinx",
        "--builder",
        "html",
        "--write-all",
        "-c",
        "docs/",
        "--doctree-dir",
        f"{build_dir}/doctrees",
        "docs/",
        f"{build_dir}/html",
    )
    clean()


@nox.session(python=["3.12"], tags=["docs"])
def docs_docstrings(session: nox.Session) -> None:
    """
    Enforce the presence of docstrings on all modules, classes, functions, and
    methods.

    """
    session.install("interrogate")
    session.run(f"python{session.python}", "-Im", "interrogate", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "interrogate",
        "-v",
        "src/",
        "tests/",
        "noxfile.py",
    )
    clean()


@nox.session(python=["3.12"], tags=["docs"])
def docs_spellcheck(session: nox.Session) -> None:
    """
    Spell-check the package's documentation.

    """
    session.install(".", "-r", "docs/requirements.txt")
    session.install("pyenchant", "sphinxcontrib-spelling")
    build_dir = session.create_tmp()
    session.run(
        f"{session.bin}/python{session.python}",
        "-Im",
        "sphinx",
        "-W",  # Promote warnings to errors, so that misspelled words fail the build.
        "--builder",
        "spelling",
        "-c",
        "docs/",
        "--doctree-dir",
        f"{build_dir}/doctrees",
        "docs/",
        f"{build_dir}/html",
        # On Apple Silicon Macs, this environment variable needs to be set so
        # pyenchant can find the "enchant" C library. See
        # https://github.com/pyenchant/pyenchant/issues/265#issuecomment-1126415843
        env={"PYENCHANT_LIBRARY_PATH": os.getenv("PYENCHANT_LIBRARY_PATH", "")},
    )
    clean()


# Code formatting checks.
#
# These checks do *not* reformat code -- that happens in pre-commit hooks -- but will
# fail a CI build if they find any code that needs reformatting.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.13"], tags=["formatters"])
def format_black(session: nox.Session) -> None:
    """
    Check code formatting with Black.

    """
    session.install("black>=25.0,<26.0")
    session.run(f"python{session.python}", "-Im", "black", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "black",
        "--check",
        "--diff",
        "src/",
        "tests/",
        "docs/",
        "noxfile.py",
    )
    clean()


@nox.session(python=["3.13"], tags=["formatters"])
def format_isort(session: nox.Session) -> None:
    """
    Check import order with isort.

    """
    session.install("isort")
    session.run(f"python{session.python}", "-Im", "isort", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "isort",
        "--check-only",
        "--diff",
        "src/",
        "tests/",
        "docs/",
        "noxfile.py",
    )
    clean()


# Linters.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.13"], tags=["linters", "security"])
def lint_bandit(session: nox.Session) -> None:
    """
    Lint code with the Bandit security analyzer.

    """
    session.install("bandit[toml]")
    session.run(f"python{session.python}", "-Im", "bandit", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "bandit",
        "-c",
        "./pyproject.toml",
        "-r",
        "src/",
        "tests/",
    )
    clean()


@nox.session(python=["3.13"], tags=["linters"])
def lint_flake8(session: nox.Session) -> None:
    """
    Lint code with flake8.

    """
    session.install("flake8", "flake8-bugbear", "flake8-pytest-style")
    session.run(f"python{session.python}", "-Im", "flake8", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "flake8",
        "src/",
        "tests/",
        "docs/",
        "noxfile.py",
    )
    clean()


@nox.session(python=["3.13"], tags=["linters"])
def lint_pylint(session: nox.Session) -> None:
    """
    Lint code with Pylint.

    """
    # Pylint requires that all dependencies be importable during the run.
    session.install("pylint", "bs4", "html5lib", "requests", "pytest")
    session.run(f"python{session.python}", "-Im", "pylint", "--version")
    session.run(f"python{session.python}", "-Im", "pylint", "src/", "tests/")
    clean()


# Packaging checks.
# -----------------------------------------------------------------------------------


@nox.session(python=["3.13"], tags=["packaging"])
def package_build(session: nox.Session) -> None:
    """
    Check that the package builds.

    """
    session.install("build")
    session.run(f"python{session.python}", "-Im", "build", "--version")
    session.run(f"python{session.python}", "-Im", "build")
    clean()


@nox.session(python=["3.13"], tags=["packaging"])
def package_description(session: nox.Session) -> None:
    """
    Check that the package description will render on the Python Package Index.

    """
    package_dir = session.create_tmp()
    session.install("build", "twine")
    session.run(f"python{session.python}", "-Im", "build", "--version")
    session.run(f"python{session.python}", "-Im", "twine", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "build",
        "--wheel",
        "--outdir",
        f"{package_dir}/build",
    )
    session.run(
        f"python{session.python}", "-Im", "twine", "check", f"{package_dir}/build/*"
    )
    clean()


@nox.session(python=["3.13"], tags=["packaging"])
def package_manifest(session: nox.Session) -> None:
    """
    Check that the set of files in the package matches the set under version control.

    """
    if IS_CI:
        session.skip("check-manifest already run by earlier CI steps.")
    session.install("check-manifest")
    session.run(f"python{session.python}", "-Im", "check_manifest", "--version")
    session.run(f"python{session.python}", "-Im", "check_manifest", "--verbose")
    clean()


@nox.session(python=["3.13"], tags=["packaging"])
def package_pyroma(session: nox.Session) -> None:
    """
    Check package quality with pyroma.

    """
    session.install("pyroma")
    session.run(f"python{session.python}", "-Im", "pyroma", ".")
    clean()


@nox.session(python=["3.13"], tags=["packaging"])
def package_wheel(session: nox.Session) -> None:
    """
    Check the built wheel package for common errors.

    """
    package_dir = session.create_tmp()
    session.install("build", "check-wheel-contents")
    session.run(f"python{session.python}", "-Im", "build", "--version")
    session.run(f"python{session.python}", "-Im", "check_wheel_contents", "--version")
    session.run(
        f"python{session.python}",
        "-Im",
        "build",
        "--wheel",
        "--outdir",
        f"{package_dir}/build",
    )
    session.run(
        f"python{session.python}", "-Im", "check_wheel_contents", f"{package_dir}/build"
    )
    clean()
