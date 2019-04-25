## RBPRM

Run examples available on the hpp-rbprm-corba package.

## Dependencies

- [pinocchio](https://github.com/stack-of-tasks/pinocchio)
- [hpp-gepetto-viewer](https://github.com/humanoid-path-planner/hpp-gepetto-viewer)
- [hpp-rbprm-corba](https://github.com/humanoid-path-planner/hpp-rbprm-corba)
- [osg-dae](https://github.com/gepetto/osg-dae)

```
py=27
qt=4
sudo apt install -qqy robotpkg-py${py}-pinocchio robotpkg-py${py}-qt${qt}-hpp-gepetto-viewer robotpkg-osg-dae robotpkg-hpp-rbprm-corba
```

## Run

```
hpp-rbprm-server &
gepetto-gui &
./rbprm.py
```
