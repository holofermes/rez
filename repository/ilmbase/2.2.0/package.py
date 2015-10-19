name = "ilmbase"

version = "2.2.0"

authors = [
    "ILM"
]

description = \
    """
    Utility libraries from ILM used by OpenEXR.
    """

import os
build_requires = [ "%s" % "msvc-12.0" if os.name == "nt" else "gcc-4.8.2" ]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-12.04"],
    ["platform-windows", "arch-AMD64", "os-windows-6.2.9200"]
]

uuid = "repository.ilmbase"

def commands():
    if building:
        env.ILMBASE_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")
