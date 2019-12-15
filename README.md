# Multi Object Tracking with dlib

## Python environment

**Python version:** `Python 3.6.8`

For this project, we used `virtualenv` as environment.
You can create an environment with virtualenv, then you just can **activate** it with:

```bash
$ workon 'environment name'
```

and **disable** it with:

```bash
$ deactivate
```

## Python dependencies

You can install all the dependencies with:

```bash
$ pip3 install -r requirements.txt
```

## How to use it

You have to run this command:

```bash
$ mpirun -n 3 python mpi_index.py
```

The script will run three processes, each of them on every core of the processor

- first process fetch the frames from camera
- second process will detect every face in frames
- third process will show every frame with every face detected with a square around the faces detected.
