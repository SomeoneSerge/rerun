# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/testing/components/fuzzy.fbs".

# You can extend this class by creating a "AffixFuzzer21Ext" class in "affix_fuzzer21_ext.py".

from __future__ import annotations

from rerun._baseclasses import (
    BaseDelegatingExtensionArray,
    BaseDelegatingExtensionType,
)

from .. import datatypes

__all__ = ["AffixFuzzer21", "AffixFuzzer21Array", "AffixFuzzer21Type"]


class AffixFuzzer21(datatypes.AffixFuzzer21):
    # You can define your own __init__ function as a member of AffixFuzzer21Ext in affix_fuzzer21_ext.py

    # Note: there are no fields here because AffixFuzzer21 delegates to datatypes.AffixFuzzer21
    pass


class AffixFuzzer21Type(BaseDelegatingExtensionType):
    _TYPE_NAME = "rerun.testing.components.AffixFuzzer21"
    _DELEGATED_EXTENSION_TYPE = datatypes.AffixFuzzer21Type


class AffixFuzzer21Array(BaseDelegatingExtensionArray[datatypes.AffixFuzzer21ArrayLike]):
    _EXTENSION_NAME = "rerun.testing.components.AffixFuzzer21"
    _EXTENSION_TYPE = AffixFuzzer21Type
    _DELEGATED_ARRAY_TYPE = datatypes.AffixFuzzer21Array


AffixFuzzer21Type._ARRAY_TYPE = AffixFuzzer21Array

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(AffixFuzzer21Type())
