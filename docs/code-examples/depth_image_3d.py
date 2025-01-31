"""Create and log a depth image and pinhole camera."""

import numpy as np
import rerun as rr
import rerun.experimental as rr2

# Create a dummy depth image
image = 65535 * np.ones((8, 12), dtype=np.uint16)
image[0:4, 0:6] = 20000
image[4:8, 6:12] = 45000


rr.init("rerun_example_depth_image", spawn=True)

# If we log a pinhole camera model, the depth gets automatically back-projected to 3D
rr2.log(
    "world/camera",
    rr2.Pinhole(
        width=image.shape[1],
        height=image.shape[0],
        focal_length=20,
    ),
)

# Log the tensor.
rr2.log("world/camera/depth", rr2.DepthImage(image, meter=10_000.0))
