# Robots

Load a robot in a viewer, and put it in a standard posture.

## Dependencies

- [pinocchio](../../../stack-of-tasks/pinocchio)
- [gepetto-viewer-corba](../../../gepetto/gepetto-viewer-corba)
- [example-robot-data](../../../gepetto/example-robot-data)

```
py=27
qt=4
sudo apt install -qqy robotpkg-py${py}-pinocchio robotpkg-py${py}-qt${qt}-gepetto-viewer-corba robotpkg-example-robot-data
```

## Available options

Look at `./robots.py -h` to see the list of available robots.

## Run

```
gepetto-gui &
./robots.py
```
