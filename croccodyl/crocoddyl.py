#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
from subprocess import Popen

SCENARII = ['bipedal_walking_from_foot_traj', 'jump', 'quadrupedal_walking_balancing', 'salto', 'talos_arm', 'walk']

parser = ArgumentParser()
parser.add_argument('scenario', nargs='?', default=SCENARII[0], choices=SCENARII)
parser.add_argument(
    '--crocoddyl', default='/local/users/gsaurel/loco-3d/crocoddyl', help='TODO: these files should be installed')


def main(crocoddyl, scenario):
    script = Path(crocoddyl) / 'examples' / (scenario + '.py')
    Popen(['python2', str(script), 'disp'], cwd=crocoddyl)


if __name__ == '__main__':
    main(**vars(parser.parse_args()))
