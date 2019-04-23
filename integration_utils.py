from argparse import ArgumentParser
from subprocess import CalledProcessError, Popen, check_call
from time import sleep

parser = ArgumentParser()
parser.add_argument('--robotpkg_prefix', default='/opt/openrobots')
parser.add_argument('--python', default=27)
parser.add_argument('--qt', default=4)
parser.add_argument(
    '--rbprm_path', default='/local/gsaurel/humanoid-path-planner', help='TODO this scripts should be installed')


def wrap_with_processes(processes, f, deps):
    kwargs = vars(parser.parse_args())
    check_installed(deps, **kwargs)
    try:
        plist = [Popen(process) for process in processes]
        sleep(2)
        f(**kwargs)
        print('Done. Press Enter to exit')
        raw_input()
    finally:
        for process in plist:
            process.terminate()


def check_installed(pkgs, python, qt, **kwargs):
    for pkg_name in pkgs:
        pkg = 'robotpkg-' + pkg_name
        pkg = pkg.replace('py-', 'py%i-' % python)
        pkg = pkg.replace('qt-', 'qt%i-' % qt)
        try:
            check_call(['dpkg', '-s', pkg])
        except CalledProcessError:
            print('please run: sudo apt install -qqy %s' % pkg)
