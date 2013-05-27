from .html_writer import HTMLWriter
from matplotlib.animation import Animation
import matplotlib.pyplot as plt
import tempfile

def anim_to_html(anim, fps=None, embed_frames=True, default_mode='loop'):
    if fps is None and hasattr(anim, '_interval'):
        # Convert interval in ms to frames per second
        fps = 1000. / anim._interval

    plt.close(anim._fig)
    if hasattr(anim, "_html_representation"):
        return anim._html_representation
    else:
        with tempfile.NamedTemporaryFile(suffix='.html') as f:
            anim.save(f.name, writer=HTMLWriter(fps=fps,
                                                embed_frames=embed_frames,
                                                default_mode=default_mode))
            html = open(f.name).read()
        anim._html_representation = html
        return html


def display_animation(anim, **kwargs):
    from IPython.display import HTML
    return HTML(anim_to_html(anim, **kwargs))


Animation._repr_html_ = anim_to_html
