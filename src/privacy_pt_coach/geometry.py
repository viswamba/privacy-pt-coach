"""Small geometry helpers used by the local movement-analysis pipeline."""

from __future__ import annotations

import math
from collections.abc import Sequence


def angle_degrees(
    a: Sequence[float],
    b: Sequence[float],
    c: Sequence[float],
) -> float | None:
    """Return the 2D angle ABC in degrees.

    The function uses the first two coordinates of each point. It returns None
    if either vector has zero length.
    """

    bax = float(a[0]) - float(b[0])
    bay = float(a[1]) - float(b[1])
    bcx = float(c[0]) - float(b[0])
    bcy = float(c[1]) - float(b[1])

    norm_ba = math.hypot(bax, bay)
    norm_bc = math.hypot(bcx, bcy)
    if norm_ba == 0.0 or norm_bc == 0.0:
        return None

    cosine = (bax * bcx + bay * bcy) / (norm_ba * norm_bc)
    cosine = max(-1.0, min(1.0, cosine))
    return math.degrees(math.acos(cosine))
