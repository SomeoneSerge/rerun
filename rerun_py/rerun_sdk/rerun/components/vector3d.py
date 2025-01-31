# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/components/vector3d.fbs".

# You can extend this class by creating a "Vector3DExt" class in "vector3d_ext.py".

from __future__ import annotations

from .. import datatypes
from .._baseclasses import (
    BaseDelegatingExtensionArray,
    BaseDelegatingExtensionType,
)

__all__ = ["Vector3D", "Vector3DArray", "Vector3DType"]


class Vector3D(datatypes.Vec3D):
    """A vector in 3D space."""

    # You can define your own __init__ function as a member of Vector3DExt in vector3d_ext.py

    # Note: there are no fields here because Vector3D delegates to datatypes.Vec3D
    pass


class Vector3DType(BaseDelegatingExtensionType):
    _TYPE_NAME = "rerun.components.Vector3D"
    _DELEGATED_EXTENSION_TYPE = datatypes.Vec3DType


class Vector3DArray(BaseDelegatingExtensionArray[datatypes.Vec3DArrayLike]):
    _EXTENSION_NAME = "rerun.components.Vector3D"
    _EXTENSION_TYPE = Vector3DType
    _DELEGATED_ARRAY_TYPE = datatypes.Vec3DArray


Vector3DType._ARRAY_TYPE = Vector3DArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(Vector3DType())
