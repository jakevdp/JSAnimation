from distutils.core import setup

DESCRIPTION = "Javascript Animation exporter for matplotlib and IPython"
LONG_DESCRIPTION = DESCRIPTION
NAME = "JSAnimation"
AUTHOR = "Jake VanderPlas"
AUTHOR_EMAIL = "jakevdp@cs.washington.edu"
MAINTAINER = "Jake VanderPlas"
MAINTAINER_EMAIL = "jakevdp@cs.washington.edu"
DOWNLOAD_URL = 'http://github.com/jakevdp/JSAnimation'
LICENSE = 'BSD'

VERSION = '0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=DOWNLOAD_URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['JSAnimation'],
      package_data={'JSAnimation': ['icons/*.png']}
     )
