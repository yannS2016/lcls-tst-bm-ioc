"""
Test that we get updating values back from the PLC.
"""
import time

import pytest

from .devices import PytmcVars


def test_basic_gets(vars_incr: PytmcVars):
    before = vars_incr.get()
    time.sleep(3)
    after = vars_incr.get()
    for key, value in before.items():
        assert after[key] != pytest.approx(value)
