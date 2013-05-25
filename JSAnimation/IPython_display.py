from .html_writer import HTMLWriter
from matplotlib.animation import Animation
import matplotlib.pyplot as plt
import tempfile

def anim_to_html(anim, embed_frames=True, **kwargs):
    plt.close(anim._fig)
    if hasattr(anim, "_html_representation"):
        return anim._html_representation
    else:
        with tempfile.NamedTemporaryFile(suffix='.html') as f:
            anim.save(f.name, writer=HTMLWriter(embed_frames=embed_frames,
                                                **kwargs))
            html = open(f.name).read()
        anim._html_representation = html
        return html


def display_animation(anim, **kwargs):
    from IPython.display import HTML
    return HTML(anim_to_html(anim, **kwargs))


Animation._repr_html_ = anim_to_html
