# Porting Hypothesis to Python 3.2.5

This document outlines a multi‑phase implementation plan to port all Python code
under `hypothesis/hypothesis-python` to Python **3.2.5**.  Each phase is designed
so that it can reasonably be completed within a single Codex session.

> **Warning**
> Python 3.2.5 is extremely old and lacks many features relied on by modern
> Hypothesis.  This plan therefore assumes extensive backporting of
> functionality or major code rewrites.  Proceed with caution and expect major
> incompatibilities.

## Phase 1 – Set Up a Python 3.2.5 Environment

- Create a Dockerfile or virtual environment capable of running Python 3.2.5.
- Document the environment setup steps in `doc/python-3.2.5/Environment.md`.
- Update any CI configuration to include the new environment (optional if CI
  cannot easily run such an old version).
- Verify that the interpreter launches and can run a simple script from
  `hypothesis-python`.

## Phase 2 – Static Analysis and Dependency Review

- Use tools such as `pipdeptree` to list all dependencies of
  `hypothesis-python`.
- Check which dependencies are compatible with Python 3.2.5 and note any that
  require replacement or vendorising.
- Run `pyflakes` or `pyright` targeting Python 3.2 to surface obvious
  incompatibilities (e.g. syntax errors or use of features from newer versions).
- Record all issues in a tracking document within this folder.

## Phase 3 – Codebase Syntax Downgrade

- Replace or refactor features unsupported in Python 3.2, such as:
  - f‑strings ⇒ `str.format` calls.
  - `yield from` syntax ⇒ explicit iterator loops.
  - `async` / `await` ⇒ synchronous implementations or backports.
- Ensure all files use only syntax valid in Python 3.2.
- Run the existing test suite under Python 3.2.5 (expect many failures).

## Phase 4 – Standard Library and Dependency Backports

- Replace `asyncio` usage with compatible alternatives or custom
  implementations.
- Vendor or backport any modules missing in Python 3.2 (e.g. `typing`).
- Modify import statements and feature checks accordingly.
- Continue running the test suite to track progress.

## Phase 5 – Feature Parity and Behaviour Verification

- Iterate through failing tests, implementing missing functionality or altering
  tests where behaviour differences cannot reasonably be resolved.
- Focus on core features of Hypothesis first (strategies, engine, shrinking).
- Defer advanced integrations (e.g. Django, NumPy) until the basics work.

## Phase 6 – Documentation and Cleanup

- Document any limitations or incompatibilities that remain.
- Update README and documentation to mention Python 3.2.5 support (or partial
  support).
- Remove temporary compatibility shims once stable.
- Perform a final pass with linters targeting Python 3.2.

## Phase 7 – Release Process

- Tag a pre‑release version specifically for Python 3.2.5 users.
- Publish installation instructions and caveats.
- Merge changes into the main branch once the port is stable and tested.

---

Porting to Python 3.2.5 will be a substantial effort and may require significant
maintenance overhead.  Consider carefully whether long‑term support for such an
old version is worthwhile.
