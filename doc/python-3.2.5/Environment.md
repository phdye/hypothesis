# Python 3.2.5 Environment Setup

This document describes how to build a working Python **3.2.5** environment for experimenting with Hypothesis.

The easiest approach is to build Python from source inside a Docker container.  A sample `Dockerfile` is provided in `docker/python-3.2.5/Dockerfile`.

## Building the Docker Image

```bash
cd docker/python-3.2.5
docker build -t python325 .
```

The build downloads and compiles Python 3.2.5 along with the libraries required to run Hypothesis.  After the image is built you can start a shell with:

```bash
docker run -it --rm python325 bash
```

Inside the container the `python3.2` executable will be on the `PATH`.

## Manual Installation with `pyenv`

If you prefer not to use Docker, install [`pyenv`](https://github.com/pyenv/pyenv) and run:

```bash
pyenv install 3.2.5
pyenv local 3.2.5
```

Depending on your operating system you may need to install a number of build dependencies.  See the [pyenv wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) for details.

## Verifying the Interpreter

Once installed, run the smoke test from the repository root:

```bash
python3.2 hypothesis-python/scripts/smoke_test_py32.py
```

You should see `Hypothesis imported and ran basic test` if everything is working.
