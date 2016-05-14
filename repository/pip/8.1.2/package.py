name = 'pip'

version = '8.1.2'

tools = [
    'pip',
]

import os
build_requires = [ "%s" % "msvc-14.0" if os.name == "nt" else "gcc-4.8.2" ]


variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-12.04", "python-2.7"],
    ["python-2.7"]
]


def commands():
    import os
    bin_name = "Scripts" if os.name == "nt" else "bin"
    env.PATH.append("{root}/%s" % bin_name)
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.setuptools'
