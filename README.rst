.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |check_| raw:: html

    <input checked=""  disabled="" type="checkbox">

.. |uncheck| raw:: html

    <input type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">

umm: yoUr Mirror Manager
=========================

A toolkit to manager the fastest mirror of various tools, such as pip, npm, composer and etc.

Features
--------

|check_| pip

|check_| npm

|uncheck_| composer

|uncheck_| homebrew

|uncheck_| ubuntu

|uncheck_| centos


Installation
------------

.. code-block:: shell

    pip install umm

Usage
-----

Show `umm` help
~~~~~~~~~~~~~~~

.. code-block:: shell

    umm

or

.. code-block:: shell

    umm --help

Output ::

    Usage: umm [OPTIONS] COMMAND [ARGS]...

    A toolkit to manager the fastest mirror of various tools, such as pip,
    npm, composer and etc.

    Options:
    --help  Show this message and exit.

    Commands:
    pip  Manage pip mirrors.

Manage `pip`
~~~~~~~~~~~~

List all available mirrors
**************************

.. code-block:: shell

    umm pip ls

Output ::

    pypi            https://pypi.python.org/simple/
    tuna            https://pypi.tuna.tsinghua.edu.cn/simple
    douban          http://pypi.douban.com/simple/
    aliyun          https://mirrors.aliyun.com/pypi/simple/
    ustc            https://mirrors.ustc.edu.cn/pypi/web/simple





How to test in local
--------------------

Once your developed a while and want to test the umm, your have two ways to test:

1. install this package in your local via:

.. code-block:: shell

    pip install --editable .

2. directly run the python file via:

.. code-block:: shell

    python src/cli.py


This is a paragraph.  It's quite
short.

    This paragraph will result in an indented block of 
    text, typically used for quoting other text.

This is another one.