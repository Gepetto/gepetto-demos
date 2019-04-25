#!/usr/bin/env python2

from argparse import ArgumentParser
from pathlib import Path
from subprocess import Popen

SCENARII = [
    'baxter-manipulation-boxes', 'construction-set', 'hrp2-on-the-ground', 'pr2-in-iai-kitchen',
    'pr2-manipulation-kitchen', 'pr2-manipulation-two-hand', 'romeo-placard'
]

parser = ArgumentParser()
parser.add_argument('scenario', nargs='?', default=SCENARII[0], choices=SCENARII)
parser.add_argument('--robotpkg_prefix', default='/opt/openrobots')


def main(robotpkg_prefix, scenario):
    script = Path(robotpkg_prefix) / 'share/hpp_benchmark' / scenario / 'script.py'
    Popen(['python2', str(script), '-N', '1', '--display', '--run'])


if __name__ == '__main__':
    main(**vars(parser.parse_args()))
