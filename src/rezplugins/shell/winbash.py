import os
import subprocess

from rez.shells import Shell

from .bash import Bash

class WinBash(Bash):

    @classmethod
    def name(cls):
        return 'bash'

    @classmethod
    def get_executable(cls):
        if cls._executable is None:
            cls._executable = Shell.find_executable('bash').replace("\\", "/")
        return cls._executable

    @property
    def executable(self):
        return self.get_executable()

    @property
    def env_var_separators(self):
        return {"PATH":":"}

    @classmethod
    def get_syspaths(cls):
        if not cls.syspaths:
            cmd = "%s %s %s 'echo __PATHS_ $PATH'" \
                  % (cls.name(), cls.norc_arg, cls.command_arg)
            p = subprocess.Popen([cls.get_executable(), "-c", cmd], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=False)
            out_, err_ = p.communicate()

            if p.returncode:
                paths = []
            else:
                lines = out_.split('\n')
                line = [x for x in lines if x.startswith("__PATHS_")][0]
                paths = line.strip().split(":")
                paths[0] = paths[0].strip("___PATHS_ ")

            for path in os.defpath.split(os.path.pathsep):
                if path not in paths:
                    paths.append(path)
            cls.syspaths = [x for x in paths if x]

        return cls.syspaths

    def _bind_interactive_rez(self):
        pass

def register_plugin():
    return WinBash
