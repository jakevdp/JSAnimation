JSAnimation
===========

*Copyright (c) 2013, Jake Vanderplas*

*License: [BSD](http://opensource.org/licenses/BSD-2-Clause)*

This package implements an HTML/Javascript writer for Matplotlib animations.
The result can be embedded in a web page, or an IPython notebook.

Example
-------
See a [rendered example](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/JSAnimation/master/animation_example.ipynb): please note the browser
requirements listedbelow.

Testing it Out
--------------
There are several scripts which demonstrate this.  ``make_animation.py``
creates a basic animation, with the frame data embedded within the HTML
document.  Run this using

    python make_animation.py

and then open the resulting file, ``animation.html`` using your web browser.
This file is created using the option ``embed = True``, which means that the
image data is embedded directly in the html file in base64-representation.
This means that the animation is entirely self-contained in the file.

A more sophisticated animation can be created using

    python make_lorenz_animation.py

(adapted from [this blog post](http://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/)
The resulting file, ``lorenz_animation.html``,
can be opened in your web browser.
This animation is created using the option ``embed = False``, which means that
the frames are individually stored in the directory ``lorenz_animation_frames``.
This prevents the html file from being too large.

If you have IPython notebook installed, you can open ``animation_example.ipynb``
to see the automatic animation representation within the notebook.  Simply
import the ``IPython_display`` submodule, create the animation, and the
javascript widget will appear embedded in your notebook window.

Browser Compatibility
---------------------
Because the animation widget uses an HTML5 slider element, it does not work
in some browsers.  For a comprehensive list of supported browsers, see
[this list](http://caniuse.com/input-range).