# Metrics Project

Python script which can get system's CPU or MEM stats.
May be dockerized by using attached Dockerfile.

## [Getting Started](https://github.com/aolinor/metrics#getting-started)

These instructions will get you a copy of the project up and running on your local machine.

## [Prerequisites](https://github.com/aolinor/metrics#prerequisites)

Linux OS. Tested with Ubuntu 18.04

## [Installing](https://github.com/aolinor/metrics#installing)

### Usage as Python script

We will require:
- Python3
- pip3 (python package manager)
- psutil  (cross-platform library for retrieving information on **running processes** and **system utilization** (CPU, memory, disks, network, sensors) in Python)

Install instructions:
- [How to install Python 3.7 on Ubuntu 18.04](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
- [How to install pip on Ubuntu 18.04](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
- [How to install psutil](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst)

### Usage as Docker container

We will require:
- Docker CE (open source containerization technology for building and containerizing your applications)

Instructions:
- [How to install Docker CE on Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## [Using](https://github.com/aolinor/metrics#using)

### Copy project files to your machine

```
mkdir metrics
cd metrics
# download project files to current folder manually

# OR (if git is installed)
git clone https://github.com/aolinor/metrics.git
cd metrics
```

### Usage as Python script

```
# run command to show cpu stats
python3 metrics.py cpu

# OR 

# run command to show mem stats
python3 metrics.py mem

```

### Usage as Docker container

```
# build docker image
sudo docker build -t metrics:latest .
```

```
# run docker container to show cpu stats
sudo docker run -it --rm --pid=host metrics cpu

# OR 

# run docker container to show mem stats
sudo docker run -it --rm --pid=host metrics mem
```

## [Authors](https://github.com/aolinor/metrics#authors)

-   **Serhii Tyshchenko**  -  _Initial work_  -  [aolinor](https://github.com/aolinor)

## [License](https://github.com/aolinor/metrics#license)

This project is licensed as open source software. You can freely distribute, modify and use it in your projects without any limitations. Use it AS-IS at your own risk.   
The author is not responsible for any problems appeared due to using this project.

## [Acknowledgments](https://github.com/aolinor/metrics#acknowledgments)

- [Thanks for a nice MD template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
