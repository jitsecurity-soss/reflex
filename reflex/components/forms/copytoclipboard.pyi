"""Stub file for copytoclipboard.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Set, Union, overload, Optional
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class CopyToClipboard(Component):
    @overload
    @classmethod
    def create(cls, *children, text: Optional[Union[Var[str], str]] = None, **props) -> "CopyToClipboard": ...  # type: ignore