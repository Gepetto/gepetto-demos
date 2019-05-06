## Crocoddyl

Run examples available on the crocoddyl package.

## Dependencies

- [pinocchio](https://github.com/stack-of-tasks/pinocchio)
- [gepetto-viewer-corba](https://github.com/gepetto/gepetto-viewer-corba)
- [example-robot-data](https://github.com/gepetto/example-robot-data)
- [croccodyl](https://github.com/loco-3d/crocoddyl)

```
py=27
qt=4
sudo apt install -qqy robotpkg-py${py}-qt${qt}-gepetto-viewer-corba robotpkg-py${py}-crocoddyl robotpkg-example-robot-data robotpkg-osg-dae
```

## Available options

Look at `./crocoddyl.py -h` to see the list of available scenarii.

## Run

```
gepetto-gui &
./crocoddyl.py
```
