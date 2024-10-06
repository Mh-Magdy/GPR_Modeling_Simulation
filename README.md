# Wakeb_GPR_Autonomous

## Description

Modeling and simulation of ground penetration radar (GPR) sensor in python3.
The simulation is based on [gprMax](https://github.com/gprMax/gprMax) simulator.

### License

Apache License, Version 2.0

**Maintainer: Mohamed Magdy<br />**

## Table of contents

* [Installation](#Installation)
* [Usage](#Usage)
* [Demo](#Demo)


## Installation

**1- conda**:

```
conda update conda
conda install git
git clone https://github.com/gprMax/gprMax.git
cd gprMax
conda env create -f conda_env.yml
```

**2- pip**:

inside the gprMax directory.
```
pip3 install -r requirements.txt
python3 setup.py build
python3 setup.py install
```

## Usage

```
python3 -m gprMax model1.in -n 60 -gpu
```
## Demo

![output1](./imgs/output1.gif)

![output2](./imgs/output2.gif)

![output3](./imgs/output3.gif)

![output4](./imgs/BscanEy.png)

![output5](./imgs/BscanHy.png)
