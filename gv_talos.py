#!/usr/bin/env python2

from argparse import ArgumentParser
from pathlib import Path
from subprocess import Popen

import pinocchio as pin
from pinocchio.robot_wrapper import RobotWrapper

parser = ArgumentParser()
parser.add_argument('robotpkg_prefix', nargs='?', default='/opt/openrobots')


def main(robotpkg_prefix):
    pkg = Path(robotpkg_prefix) / 'share/example-robot-data'
    urdf = 'talos_data/robots/talos_reduced.urdf'
    robot = RobotWrapper.BuildFromURDF(str(pkg / urdf), [str(pkg)], pin.JointModelFreeFlyer())
    robot.initDisplay()
    robot.loadDisplayModel("pinocchio")
    robot.display(robot.q0)


if __name__ == '__main__':
    gepetto_gui = Popen('gepetto-gui')
    try:
        main(**vars(parser.parse_args()))
    finally:
        gepetto_gui.terminate()
    print('Done. Press Enter to exit')
    raw_input()
