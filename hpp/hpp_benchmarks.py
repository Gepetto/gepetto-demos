#!/usr/bin/env python2

from pathlib import Path
from subprocess import Popen

from integration_utils import wrap_with_processes

DEPS = ['hpp-tutorial']

PATCHES = {
    'baxter_manipulation_boxes': [
        ('N = 20', 'N = 1'),
        ('#v = vf.createViewer ()', 'v = vf.createViewer()'),
        ('#pp = PathPlayer (v)', 'pp = PathPlayer(v)'),
    ]
}


def baxter_manipulation_boxes(rbprm_path, **kwargs):
    script = Path(rbprm_path) / 'hpp_benchmark/future' / 'baxter-manipulation-boxes' / 'script.py'
    temp = '/tmp/gepetto-integrations-hpp-benchmarks.py'
    with open(temp, 'w') as f_out:
        with script.open() as f_in:
            for line in f_in:
                for before, after in PATCHES['baxter_manipulation_boxes']:
                    line = line.replace(before, after)
                f_out.write(line)
        f_out.write('pp(0)')
    Popen(['python2', temp])


if __name__ == '__main__':
    wrap_with_processes(['gepetto-gui', 'hppcorbaserver'], baxter_manipulation_boxes, DEPS)
