# Robots

Load a robot in a viewer, and put it in a standard posture.

## Dependencies

- [pinocchio](https://github.com/stack-of-tasks/pinocchio)
- [gepetto-viewer-corba](https://github.com/gepetto/gepetto-viewer-corba)
- [example-robot-data](https://github.com/gepetto/example-robot-data)

```
py=27
qt=4
sudo apt install -qqy robotpkg-py${py}-qt${qt}-gepetto-viewer-corba robotpkg-py${py}-example-robot-data robotpkg-osg-dae
```

## Available options

Look at `python -m example_robot_data -h` to see the list of available robots.

## Run

```
gepetto-gui &
python -m example_robot_data [robot]
```
