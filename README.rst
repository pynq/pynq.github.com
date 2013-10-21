pynq.github.com
===============

Blog for the Python NQ Users Group

Installation and hacking
========================

Do the following to install::

    python boostrap.py
    ./bin/buildout
    source ./bin/activate
    make html

Check out the output HTML files in the ``./output`` directory inside where you've just
installed the blog configuration.

Re-building
-----------

To do a manual rebuild::

    make html
    
    
Building and uploading to GitHub
--------------------------------

If you need to update the GitHub pages branch of the repository for this blog, finish
updating your pages, commit your changes, and then run::

    make github
    
This will push the resulting output files into the dedicated ``master`` branch for the
site.
