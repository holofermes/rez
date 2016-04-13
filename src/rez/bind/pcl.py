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

def enumerate_program(is_win64):
    result = {}
    version = "1.7.2"
    path = r'C:\Program Files (x86)\PCL 1.7.2'
    if os.path.isdir(path):
        result[version] = r'C:\Program Files (x86)\PCL 1.7.2'
    return result

def commands():
    env.PATH.append('{this.root}/bin')
    if building:
        env.CMAKE_MODULE_PATH.append('{this.root}/cmake')
        # env.PKG_CONFIG_PATH.append
    
def setup_parser(parser):
    parser.add_argument("--version", type=str, metavar="VERSION",
                        help="manually specify the pcl version to install.")
    parser.add_argument("--root", type=str, metavar="ROOT",
                        help="the root of pcl.")

def bind(path, version_range=None, opts=None, parser=None):
    programs = enumerate_program()
    if not programs:
        version = getattr(opts, "version", None)
        if not version:
            _program_root = getattr(opts, "root", None) 
            if not _program_root:
                print "can't find pcl root, use --root and pass a path."
                exit(1)
            else:
                if not os.path.isdir(_program_root):
                    print "can't find:", _program_root
                    exit(1)
                programs[version] = _program_root

    for variant in [ 'target-AMD86' ]:
        variants = system.variant+[variant]
        for version, program_root in programs.iteritems():
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


            with make_package("pcl", path, make_root=make_root) as pkg:
                pkg.version = version
                pkg.commands = commands
                pkg.variants = [variants]

    return "pcl", programs.keys()
