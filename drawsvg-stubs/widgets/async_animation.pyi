"""
This type stub file was generated by pyright.
"""

from .drawing_widget import DrawingWidget

class AsyncAnimation(DrawingWidget):
    '''A Jupyter notebook widget for asynchronously displaying an animation.

    Example:
        # Jupyter cell 1:
        widget = AsyncAnimation(fps=10)
        widget
        # [Animation is displayed here]

        # Jupyter cell 2:
        global_variable = 'a'
        @widget.set_draw_frame  # Animation above is automatically updated
        def draw_frame(secs=0):
            # Draw something...
            d = draw.Drawing(300, 40)
            d.append(draw.Text(global_variable, 20, 0, 10))
            d.append(draw.Text(str(secs), 20, 30, 10))
            return d

        # Jupyter cell 3:
        global_variable = 'b'  # Animation above now displays 'b'

    Attributes:
        fps: The animation frame rate (frames per second).
        draw_frame: A function that takes a single argument (animation time) and
            returns a Drawing.
        paused: While True, the animation will not run.  Only the current frame
            will be shown.
        disable: While True, the widget will not be interactive and the
            animation will not update.
        click_pause: If True, clicking the drawing will pause or resume the
            animation.
        mousemove_pause: If True, moving the mouse up across the drawing will
            pause the animation and moving the mouse down will resume it.
        mousemove_y_threshold: Controls the sensitivity of mousemove_pause in
            web browser pixels.
    '''
    def __init__(self, fps=..., draw_frame=..., *, paused=..., disable=..., click_pause=..., mousemove_pause=..., mousemove_y_threshold=...) -> None:
        ...
    
    @property
    def fps(self): # -> int:
        ...
    
    @fps.setter
    def fps(self, new_fps): # -> None:
        ...
    
    @property
    def paused(self): # -> bool:
        ...
    
    @paused.setter
    def paused(self, new_paused): # -> None:
        ...
    
    @property
    def draw_frame(self): # -> (secs: Unknown) -> Drawing:
        ...
    
    @draw_frame.setter
    def draw_frame(self, new_draw_frame): # -> None:
        ...
    
    def set_draw_frame(self, new_draw_frame):
        ...
    


