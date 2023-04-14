Linux Test Tool
===============
## Introduction
Linux Test Tool is a generic open source automation tool based on pytest for linux device test.<br>
It's based on device_pool to run testcases quickly.
## Installation
Build a docker image to use it, or install python package(found in Dockerfile) manually.
```
docker build -t test:test .
```
## Example
### one testcase
Write case down in testcases/ or it's sub dir.<br>
eg: testcases/mm/mm_info_test.py
```
def get_mm_info_test(dev):
    status, data = dev.con.ask("free; echo result:$?", "result:0", 2)
    assert status == True
```
Code means:<br>
A linux device **exec** cmd `"free; echo result:$?"` through `connection` method(such as ssh) which defined in *config.yaml*, and **expecting** `"result:0"` **in** 2 seconds. `data` collects log, and `status` gives that cmd's result is `True` or `False`.