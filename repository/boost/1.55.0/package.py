name = "boost"

version = "1.55.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """
import os
build_requires = [ "%s" % "msvc-12.0" if os.name == "nt" else "gcc-4.8.2" ]


variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-12.04", "python-2.7"],
    ["platform-windows", "arch-AMD64", "os-windows-6.2.9200", "python-2.7"]
]

uuid = "repository.boost"

def commands():
    if building:
        env.BOOST_INCLUDE_DIR = "{root}/include"

        # static libs
        env.LD_LIBRARY_PATH.append("{root}/lib")
