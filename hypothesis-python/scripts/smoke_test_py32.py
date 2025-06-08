# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Copyright the Hypothesis Authors.
# Individual contributors are listed in AUTHORS.rst and the git log.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.

"""Simple smoke test for Python 3.2.5 environment."""

from hypothesis import given, strategies as st


@given(st.integers())
def test_identity(x):
    assert x == x


if __name__ == "__main__":
    test_identity()
    print("Hypothesis imported and ran basic test")
