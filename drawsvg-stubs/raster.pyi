"""
This type stub file was generated by pyright.
"""

def delay_import_cairo(): # -> Module("cairosvg"):
    ...

def delay_import_imageio(): # -> Module("imageio"):
    ...

class Raster:
    def __init__(self, png_data=..., png_file=...) -> None:
        ...
    
    def save_png(self, fname): # -> None:
        ...
    
    @staticmethod
    def from_svg(svg_data): # -> Raster:
        ...
    
    @staticmethod
    def from_svg_to_file(svg_data, out_file): # -> Raster:
        ...
    
    @staticmethod
    def from_arr(arr, out_file=...): # -> Raster:
        ...
    
    def as_data_uri(self): # -> str:
        ...
    


