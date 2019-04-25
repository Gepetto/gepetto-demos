## HPP

Run examples available on the hpp-benchmark package.

## Dependencies

- [hpp-benchmark](https://github.com/humanoid-path-planner/hpp_benchmark)
- [hpp-tutorial](https://github.com/humanoid-path-planner/hpp-tutorial)
- [ros-baxter-common](https://github.com/RethinkRobotics/baxter_common)
- :warning: [iai-maps](https://github.com/TeamSPoon/iai_maps) :warning: This is not yet packaged on robotpkg :warning:

```
py=27
qt=4
sudo apt install -qqy robotpkg-py${py}-qt${qt}-hpp-benchmark robotpkg-ros-baxter-common robotpkg-hpp-tutorial
```

## Available options

Look at `./hpp.py -h` to see the list of available scenarii.

## Run

```
hppcorbaserver &
gepetto-gui &
./hpp.py
```
