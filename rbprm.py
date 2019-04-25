#!/usr/bin/env python2

from pathlib import Path
from subprocess import Popen

from integration_utils import wrap_with_processes

DEPS = ['py-qt-hpp-gepetto-viewer', 'hpp-rbprm-corba', 'osg-dae', 'py-pinocchio']


def main(rbprm_path, **kwargs):
    path = Path(rbprm_path) / 'hpp-rbprm-corba/script/scenarios/demos'
    Popen(['python2', 'darpa_hyq.py'], cwd=str(path))


if __name__ == '__main__':
    wrap_with_processes(['gepetto-gui', 'hpp-rbprm-server'], main, DEPS)
