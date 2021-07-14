[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-robots.svg)](https://forthebadge.com)

# VSSSProtoComm

Python library to communicate with TraveSim/FIRASim using protobuf.

The library supports the following communications:

- Receiving vision data in polling and multithread mode
- Sending speed commands in polling and multithread mode
- Receiving game data from the VSSReferee in polling mode
- Sending replacement packages to the VSSReplacer in polling mode

To install the dependencies, do as follows:

```bash
pip3 install -r requirements.txt
```

Than to run a test, run:

```bash
python3 test_name.py
```