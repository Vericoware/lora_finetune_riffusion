## Introduction

English | [简体中文](README_zh-CN.md)

This projects aims to fine-tune the Riffusion model using LORA on 5~20 audio clips, generated from some ‘Ghibli Medley Piano’ style music. The master branch works with **Diffusers** and **Riffusion**.

***
## License

This project is developed by Zhenhong Sun and licensed under the [Apache 2.0 license](LICENSE).

***
## Changelog
**0.1** was released in 05/05/2023:

* Fine-tune the Riffusion model.

***
## Installation

### Prerequisites
* Linux
* GCC 7+
* Python 3.9+
* PyTorch 2.0+
* CUDA 11.7+

### Prepare environment
1. Compile the OpenMPI 4.0+ [Downloads](https://www.open-mpi.org/software/ompi/v4.0/). 
    ```shell
    cd path
    tar -xzvf openmpi-4.0.1.tar.gz
    cd openmpi-4.0.1
    ./configure --prefix=/your_path/openmpi
    make && make install
    ```
    add the commands into your `~/.bashrc`
    ```shell
    export PATH=/your_path/openmpi/bin:$PATH
    export LD_LIBRARYPATH=/your_path/openmpi/lib:$LD_LIBRARY_PATH
    ```
    For Ubuntu-OS
    ```
    sudo apt install openmpi-bin # while needed
    conda install -c conda-forge mpi4py openmpi
    ```

2. Create a conda virtual environment and activate it.

    ```shell
    conda create -n light-nas python=3.6 -y
    conda activate light-nas
    ```

3. Install torch and torchvision with the following command or [offcial instruction](https://pytorch.org/get-started/locally/).
    ```shell
    pip install torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f https://download.pytorch.org/whl/torch_stable.html
    # or
    pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 -f https://download.pytorch.org/whl/torch_stable.html
    ```
    if meet `"Not be found for jpeg"`, please install the libjpeg for the system.
    ```shell
    sudo yum install libjpeg # for centos
    sudo apt install libjpeg-dev # for ubuntu
    ```

4. Install other packages with the following command.

    ```shell
    pip install -r requirements.txt
    ```

***
## Easy to use

* **Search with examples**
    
    ```shell
    cd scripts/classification
    sh example_xxxx.sh
    ```



***
## Main Contributors

[Zhenhong Sun](https://sites.google.com/view/sunzhenhong)
