"""
This type stub file was generated by pyright.
"""

import dataclasses
from typing import Optional, Sequence, Union
from .native_animation import SyncedAnimationConfig

@dataclasses.dataclass(frozen=True)
class Context:
    '''Additional drawing configuration that can modify element's SVG output.'''
    invert_y: bool = ...
    animation_config: Optional[SyncedAnimationConfig] = ...
    def extra_prepost_drawing_elements(self, d): # -> tuple[list[Unknown], list[Unknown]]:
        ...
    
    def extra_css(self, d): # -> list[Unknown]:
        ...
    
    def extra_javascript(self, d): # -> list[str] | list[Unknown]:
        ...
    
    def extra_onload_js(self, d): # -> list[str] | list[Unknown]:
        ...
    
    def override_view_box(self, view_box): # -> str | tuple[Unknown, Unknown, Unknown, Unknown]:
        ...
    
    def is_attr_inverted(self, name): # -> bool:
        ...
    
    def override_args(self, args):
        ...
    
    def write_svg_document_args(self, d, args, output_file): # -> None:
        '''Called by Drawing during SVG output of the <svg> tag.'''
        ...
    


@dataclasses.dataclass(frozen=True)
class LocalContext:
    context: Context
    element: DrawingElement
    parent: Union[DrawingElement, Drawing]
    siblings: Sequence[DrawingElement] = ...
    def write_tag_args(self, args, output_file, id_map=...): # -> None:
        '''Called by an element during SVG output of its tag.'''
        ...
    


class DrawingElement:
    '''Base class for drawing elements.

    Subclasses must implement write_svg_element.
    '''
    def write_svg_element(self, id_map, is_duplicate, output_file, lcontext, dry_run, force_dup=...):
        ...
    
    def get_svg_defs(self): # -> tuple[()]:
        ...
    
    def get_linked_elems(self): # -> tuple[()]:
        ...
    
    def write_svg_defs(self, id_map, is_duplicate, output_file, lcontext, dry_run): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class DrawingBasicElement(DrawingElement):
    '''Base class for SVG drawing elements that are a single node with no child
    nodes.
    '''
    TAG_NAME = ...
    has_content = ...
    def __init__(self, **args) -> None:
        ...
    
    def check_children_allowed(self): # -> None:
        ...
    
    def extra_children_with_context(self, lcontext=...): # -> list[Unknown]:
        ...
    
    def all_children(self, lcontext=...): # -> list[Unknown]:
        '''Return self.children and self.ordered_children as a single list.'''
        ...
    
    @property
    def id(self): # -> None:
        ...
    
    def write_svg_element(self, id_map, is_duplicate, output_file, lcontext, dry_run, force_dup=...): # -> None:
        ...
    
    def write_content(self, id_map, is_duplicate, output_file, lcontext, dry_run):
        '''Override in a subclass to add data between the start and end tags.

        This will not be called if has_content is False.
        '''
        ...
    
    def write_children_content(self, id_map, is_duplicate, output_file, lcontext, dry_run): # -> None:
        '''Override in a subclass to add data between the start and end tags.

        This will not be called if has_content is False.
        '''
        ...
    
    def get_svg_defs(self): # -> list[DrawingElement]:
        ...
    
    def write_svg_defs(self, id_map, is_duplicate, output_file, lcontext, dry_run): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def append_anim(self, animate_element): # -> None:
        ...
    
    def extend_anim(self, animate_iterable): # -> None:
        ...
    
    def append_title(self, text, **kwargs): # -> None:
        ...
    
    def add_key_frame(self, time, animation_args=..., **attr_values): # -> None:
        ...
    
    def add_attribute_key_sequence(self, attr, times, values, *, animation_args=...): # -> None:
        ...
    


class DrawingParentElement(DrawingBasicElement):
    '''Base class for SVG elements that can have child nodes.'''
    has_content = ...
    def __init__(self, children=..., ordered_children=..., **args) -> None:
        ...
    
    def draw(self, obj, *, z=..., **kwargs): # -> None:
        ...
    
    def append(self, element, *, z=...): # -> None:
        ...
    
    def extend(self, iterable, *, z=...): # -> None:
        ...
    
    def write_content(self, id_map, is_duplicate, output_file, lcontext, dry_run): # -> None:
        ...
    


def normalize_attribute_name(name):
    ...

