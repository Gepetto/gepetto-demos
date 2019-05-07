#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path

import pinocchio as pin
from pinocchio.robot_wrapper import RobotWrapper

ROBOTS = {
    'talos': 'talos_data/robots/talos_reduced.urdf',
    'hyq': 'hyq_description/robots/hyq_no_sensors.urdf',
}

parser = ArgumentParser()
parser.add_argument('robot', nargs='?', default=list(ROBOTS.keys())[0], choices=ROBOTS.keys())
parser.add_argument('--robotpkg_prefix', default='/opt/openrobots')


def main(robotpkg_prefix, robot):
    pkg = Path(robotpkg_prefix) / 'share/example-robot-data'
    urdf = ROBOTS[robot]
    robot = RobotWrapper.BuildFromURDF(str(pkg / urdf), [str(pkg)], pin.JointModelFreeFlyer())
    robot.initDisplay()
    robot.loadDisplayModel("pinocchio")
    robot.display(robot.q0)


if __name__ == '__main__':
    main(**vars(parser.parse_args()))
