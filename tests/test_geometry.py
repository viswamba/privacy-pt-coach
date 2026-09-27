import pytest

from privacy_pt_coach.geometry import angle_degrees


def test_straight_angle() -> None:
    assert angle_degrees((0, 0), (1, 0), (2, 0)) == pytest.approx(180.0)


def test_right_angle() -> None:
    assert angle_degrees((0, 1), (0, 0), (1, 0)) == pytest.approx(90.0)


def test_zero_length_vector_returns_none() -> None:
    assert angle_degrees((0, 0), (0, 0), (1, 0)) is None
