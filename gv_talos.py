#!/usr/bin/env python2

from pathlib import Path

import pinocchio as pin
from pinocchio.robot_wrapper import RobotWrapper

from integration_utils import wrap_with_processes

DEPS = ['py-pinocchio', 'py-qt-gepetto-viewer-corba', 'example-robot-data']


def main(robotpkg_prefix, **kwargs):
    pkg = Path(robotpkg_prefix) / 'share/example-robot-data'
    urdf = 'talos_data/robots/talos_reduced.urdf'
    robot = RobotWrapper.BuildFromURDF(str(pkg / urdf), [str(pkg)], pin.JointModelFreeFlyer())
    robot.initDisplay()
    robot.loadDisplayModel("pinocchio")
    robot.display(robot.q0)


if __name__ == '__main__':
    wrap_with_processes(['gepetto-gui'], main, DEPS)
