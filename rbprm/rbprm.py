#!/usr/bin/env python2

from argparse import ArgumentParser
from pathlib import Path
from subprocess import Popen

parser = ArgumentParser()
parser.add_argument(
    '--rbprm_path', default='/local/gsaurel/humanoid-path-planner', help='TODO this scripts should be installed')


def main(rbprm_path):
    path = Path(rbprm_path) / 'hpp-rbprm-corba/script/scenarios/demos'
    Popen(['python2', 'darpa_hyq.py'], cwd=str(path))


if __name__ == '__main__':
    main(**vars(parser.parse_args()))
