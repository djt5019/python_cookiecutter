{{cookiecutter.project_name}}
{{ '=' * (cookiecutter.project_name|length) }}

|Version| |Downloads| |Status| |Coverage| |License|

{{cookiecutter.short_description}}.


Installation
------------

::

    pip install {{cookiecutter.project_name}}


.. include:: contributing.rst


Development
-----------

1. Create a new virtual environment
2. Install development requirements from *dev-requirements.txt*
3. Run tests  ``nosetests``
4. `detox`_ is installed and will run the test suite across all supported python platforms
5. `python setup.py build_sphinx` will generate documentation into *build/sphinx/html*

TL;DR
+++++

::

    $ virtualenv env
    $ ./env/bin/pip install -qr dev-requirements.txt
    $ source env/bin/activate
    (env) $ nosetests
    (env) $ python setup.py build_sphinx
    (env) $ detox


.. include:: ../HISTORY.rst


License
-------

.. include:: ../LICENSE


.. _detox: https://testrun.org/tox/

.. |Version| image:: https://badge.fury.io/py/{{cookiecutter.project_name}}.svg?
   :target: http://badge.fury.io/py/{{cookiecutter.project_name}}

.. |Status| image:: https://travis-ci.org/djt5019/{{cookiecutter.project_name}}.svg?branch=master
   :target: https://travis-ci.org/djt5019/{{cookiecutter.project_name}}

.. |Coverage| image:: https://img.shields.io/coveralls/djt5019/{{cookiecutter.project_name}}.svg?
   :target: https://coveralls.io/r/djt5019/{{cookiecutter.project_name}}

.. |Downloads| image:: https://pypip.in/d/{{cookiecutter.project_name}}/badge.svg?
   :target: https://pypi.python.org/pypi/{{cookiecutter.project_name}}

.. |License| image:: https://pypip.in/license/{{cookiecutter.project_name}}/badge.svg?
   :target: https://{{cookiecutter.project_name}}.readthedocs.org
