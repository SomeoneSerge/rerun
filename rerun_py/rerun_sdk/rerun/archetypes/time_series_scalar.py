# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/archetypes/time_series_scalar.fbs".

# You can extend this class by creating a "TimeSeriesScalarExt" class in "time_series_scalar_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import (
    Archetype,
)

__all__ = ["TimeSeriesScalar"]


@define(str=False, repr=False)
class TimeSeriesScalar(Archetype):
    """
    Log a double-precision scalar that will be visualized as a timeseries plot.

    The current simulation time will be used for the time/X-axis, hence scalars
    cannot be timeless!

    Examples
    --------
    ```python
    import math

    import rerun as rr
    import rerun.experimental as rr2

    rr.init("rerun_example_scalar", spawn=True)

    for step in range(0, 64):
        rr.set_time_sequence("step", step)
        rr2.log("scalar", rr2.TimeSeriesScalar(math.sin(step / 10.0)))
    ```

    ```python

    from math import cos, sin, tau

    import numpy as np
    import rerun as rr
    import rerun.experimental as rr2

    rr.init("rerun_example_scalar_multiple_plots", spawn=True)
    lcg_state = np.int64(0)

    for t in range(0, int(tau * 2 * 100.0)):
        rr.set_time_sequence("step", t)

        # Log two time series under a shared root so that they show in the same plot by default.
        rr2.log("trig/sin", rr2.TimeSeriesScalar(sin(float(t) / 100.0), label="sin(0.01t)", color=[255, 0, 0]))
        rr2.log("trig/cos", rr2.TimeSeriesScalar(cos(float(t) / 100.0), label="cos(0.01t)", color=[0, 255, 0]))

        # Log scattered points under a different root so that they shows in a different plot by default.
        lcg_state = (1140671485 * lcg_state + 128201163) % 16777216  # simple linear congruency generator
        rr2.log("scatter/lcg", rr2.TimeSeriesScalar(lcg_state, scattered=True))
    ```
    """

    # You can define your own __init__ function as a member of TimeSeriesScalarExt in time_series_scalar_ext.py

    scalar: components.ScalarArray = field(
        metadata={"component": "required"},
        converter=components.ScalarArray.from_similar,  # type: ignore[misc]
    )
    """
    The scalar value to log.
    """

    radius: components.RadiusArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.RadiusArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    An optional radius for the point.

    Points within a single line do not have to share the same radius, the line
    will have differently sized segments as appropriate.

    If all points within a single entity path (i.e. a line) share the same
    radius, then this radius will be used as the line width too. Otherwise, the
    line will use the default width of `1.0`.
    """

    color: components.ColorArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ColorArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Optional color for the scalar entry.

    If left unspecified, a pseudo-random color will be used instead. That
    same color will apply to all points residing in the same entity path
    that don't have a color specified.

    Points within a single line do not have to share the same color, the line
    will have differently colored segments as appropriate.
    If all points within a single entity path (i.e. a line) share the same
    color, then this color will be used as the line color in the plot legend.
    Otherwise, the line will appear gray in the legend.
    """

    label: components.TextArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TextArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    An optional label for the point.

    TODO(#1289): This won't show up on points at the moment, as our plots don't yet
    support displaying labels for individual points.
    If all points within a single entity path (i.e. a line) share the same label, then
    this label will be used as the label for the line itself. Otherwise, the
    line will be named after the entity path. The plot itself is named after
    the space it's in.
    """

    scattered: components.ScalarScatteringArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ScalarScatteringArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Specifies whether a point in a scatter plot should form a continuous line.

    If set to true, this scalar will be drawn as a point, akin to a scatterplot.
    Otherwise, it will form a continuous line with its neighbors.
    Points within a single line do not have to all share the same scatteredness:
    the line will switch between a scattered and a continuous representation as
    required.
    """

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
