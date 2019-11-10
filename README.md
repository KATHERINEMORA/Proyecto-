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
$ python index.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --video input/race.mp4
```

The script will run the video, and assign a tracker to each runner in the video. Each tracker is running in parallel and using a common Queue to get frames
and another queue to send the processed frames with the bounding boxes around each runner.