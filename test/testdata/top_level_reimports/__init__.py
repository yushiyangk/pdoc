"""
Test that objects re-exposed from an internal module are properly interlinked if they appear on the same page.

 - top_level_reimports._internal.baz
 - top_level_reimports._internal.baz()
 - `top_level_reimports._internal.baz`
 - `top_level_reimports._internal.baz()`
"""
from ._internal import Bar
from ._internal import baz
from ._internal import Foo

__all__ = ["Foo", "Bar", "baz"]
