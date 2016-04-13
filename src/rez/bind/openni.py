"""
Binds a MSVC executable as a rez package.
"""
from __future__ import absolute_import
from rez.package_maker__ import make_package
from rez.bind._utils import check_version, find_exe, extract_version, make_dirs
from rez.utils.platform_ import platform_
from rez.system import system
from rez.utils.lint_helper import env
import os.path

def enumerate_program_and_variants():
    result = {}
    version = "2"
    path = r'C:\Program Files\OpenNI2'
    variants = []
    if os.path.isdir(path):
        result[version] = "C:\\Program Files{0}\\OpenNI2"
        variants.append('target-AMD64')
    if os.path.isdir(path):
        result[version] = "C:\\Program Files{0}\\OpenNI2"
        variants.append('target-AMD86')
    return result, variants

def commands():
    import subprocess
    import os

    env.PATH.append('{this.root}/bin')
    env.PATH.append('{this.root}/OpenNI2/Drivers')
    

def setup_parser(parser):
    parser.add_argument("--version", type=str, metavar="VERSION",
                        help="manually specify the openni version to install.")
    parser.add_argument("--root", type=str, metavar="ROOT",
                        help="the root of openni.")
    # parser.add_argument("--arch", type=str, metavar="ARCH",
                        # help="the target architecture. (AMD64|AMD86)")

def bind(path, version_range=None, opts=None, parser=None):
    is_win64 = False
    if os.environ.get('PROCESSOR_ARCHITECTURE','x86') != 'x86':
        is_win64 = True
    if os.environ.get('PROCESSOR_ARCHITEW6432'):
        is_win64 = True
    if os.environ.get('ProgramW6432'):
        is_win64 = True

    programs, variants = enumerate_program_and_variants()
    if not programs:
        version = getattr(opts, "version", None)
        if not version:
            _program_root = getattr(opts, "root", None)
            # arch = getattr(opts, "arch", None)
            if not _program_root:
                print "can't find openni root, use --root and pass a path."
                exit(1)
            else:
                if not os.path.isdir(_program_root):
                    print "can't find:", _program_root
                    exit(1)
                programs[version] = _program_root
    if not variants:
        print "--arch option not implemented"
        exit(1)

    for variant in variants:
        _variants = system.variant+[variant]
        for version, program_root in programs.iteritems():
            program_root = program_root.format(" (x86)" if variant.endswith('86') else "")
            check_version(version, version_range)

            def make_root(variant, root):
                subdirectories = os.listdir(program_root)
                for d in subdirectories:
                    link_from = os.path.join(program_root, d)
                    link_to = os.path.join(root, d)
                    try:
                        platform_.symlink(link_from, link_to)
                    except WindowsError, e:
                        if e.winerror == 183: #[Error 183] Cannot create a file when that file already exists.
                            os.remove(link_to)
                            platform_.symlink(link_from, link_to)


            with make_package("openni", path, make_root=make_root) as pkg:
                pkg.version = version
                pkg.commands = commands
                pkg.variants = [_variants]

    return "openni", programs.keys()
