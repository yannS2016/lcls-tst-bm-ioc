"""
Test that we can move motors.
"""
import pytest
from pcdsdevices.epics_motor import BeckhoffAxis


@pytest.mark.parametrize("suffix", ("M1", "M2"))
def test_basic_motion(suffix: str):
    mot = BeckhoffAxis(f"PLC:TST:IOC:{suffix}", name=suffix.lower())
    mot.wait_for_connection()
    mot.velocity.put(10)
    goal = mot.position + 4
    mot.move(goal, wait=True)
    assert mot.position == pytest.approx(goal)
