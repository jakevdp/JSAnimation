JSAnimation
===========

Experimenting with frame-based Javascript animations.
Eventually, I'd like this to become a plugin for the IPython notebook, so
that animations can be embedded automatically.  For a couple examples of
initial ideas along these lines, see
[this notebook](http://nbviewer.ipython.org/5573741) and
[this blog post](http://jakevdp.github.io/blog/2013/05/12/embedding-matplotlib-animations/).


Trying it Out
-------------
To test this with a basic animation using non-embedded frames, run

    python make_animation.py

and then use your web browser to open the file ``animation.html``.
This script creates the ``animation_frames`` directory, which contains the
individual png image representing each frame.

To test a more sophisticated animation with embedded frames, run

    python make_lorenz_animation.py

and then use your web browser to open the file ``lorenz_animation.html``.
This does not create a frame directory, but rather embeds the frames directly
in the html document in base64 encoding.