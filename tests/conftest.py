from __future__ import annotations

import pytest

from .devices import AllPVs


@pytest.mark.fixture(scope="session")
def all_pvs():
    return AllPVs()


@pytest.mark.fixture(scope="session")
def vars_incr(all_pvs: AllPVs):
    return all_pvs.incr


@pytest.mark.fixture(scope="session")
def vars_set(all_pvs: AllPVs):
    return all_pvs.setp
