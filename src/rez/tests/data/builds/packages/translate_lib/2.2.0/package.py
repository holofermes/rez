# -*- coding: utf-8 -*-

name = 'translate_lib'

version = '2.2.0'

description = \
    """
    A simple C++ library with minimal dependencies.
    """

import os
build_requires = [ "%s" % "msvc" if os.name == "nt" else "gcc" ]

authors = ['axl.rose']

def commands():
    # comment('OLD COMMAND: export CMAKE_MODULE_PATH=$CMAKE_MODULE_PATH:!ROOT!/cmake')
    appendenv('CMAKE_MODULE_PATH', '{root}/cmake')
    # comment('OLD COMMAND: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:!ROOT!/lib')
    appendenv('LD_LIBRARY_PATH', '{root}/lib')

uuid = '38eda6e8-f162-11e0-9de0-0023ae79d988'
