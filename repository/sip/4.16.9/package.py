name = "sip"

version = "4.16.9"

authors = [
    "Riverbank Computing Limited"
]
description = \
    """
    SIP is a tool that makes it very easy to create Python bindings for C and C++ libraries.
    """

build_requires = ["target-AMD64"]
variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-12.04"],
    ["platform-windows", "arch-AMD64", "os-windows-6.2.9200", "msvc-10", "python-2.7"],
    ["platform-windows", "arch-AMD64", "os-windows-6.2.9200", "msvc-12", "python-2.7"]
]

uuid = "repository.sip"

def commands():
    env.PATH.append("{root}")
    env.PYTHONPATH.append("{root}/Lib/site-packages")
    if building:
        env.SIP_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")
