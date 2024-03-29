"""
This type stub file was generated by pyright.
"""

def limit(v, low=..., high=...): # -> int:
    ...

class Srgb:
    LUMA_WEIGHTS = ...
    def __init__(self, r, g, b) -> None:
        ...
    
    def __iter__(self): # -> Iterator[float]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def luma(self, wts=...): # -> float:
        ...
    
    def to_srgb(self): # -> Self@Srgb:
        ...
    
    @staticmethod
    def from_hue(h): # -> Srgb:
        ...
    


class Hsl:
    def __init__(self, h, s, l) -> None:
        ...
    
    def __iter__(self): # -> Iterator[float]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def to_srgb(self): # -> Srgb:
        ...
    


class Hsv:
    def __init__(self, h, s, v) -> None:
        ...
    
    def __iter__(self): # -> Iterator[float]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def to_srgb(self): # -> Srgb:
        ...
    


class Sin:
    def __init__(self, h, s, l) -> None:
        ...
    
    def __iter__(self): # -> Iterator[float]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def to_srgb(self): # -> Srgb:
        ...
    


class Hcy:
    HCY_WEIGHTS = ...
    def __init__(self, h, c, y) -> None:
        ...
    
    def __iter__(self): # -> Iterator[float]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def to_srgb(self): # -> Srgb:
        ...
    
    @classmethod
    def from_srgb(cls, srgb): # -> Hcy:
        ...
    


class Cielab:
    REF_WHITE = ...
    def __init__(self, l, a, b) -> None:
        ...
    
    def __iter__(self): # -> Iterator[float]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def to_srgb(self): # -> Srgb:
        ...
    
    @classmethod
    def from_srgb(cls, srgb, ref_white=...): # -> Cielab:
        ...
    


