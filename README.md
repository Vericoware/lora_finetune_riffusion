## Introduction


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
* Python 3.9+
* PyTorch 2.0+
* CUDA 11.7+
* Pyaudio
* Diffusser 0.9.0+


### Prepare environment
1. Create a conda virtual environment and activate it.

    ```shell
    conda create -n light-nas python=3.6 -y
    conda activate light-nas
    ```

2. Install torch and torchvision with the following command or [offcial instruction](https://pytorch.org/get-started/locally/).
    ```shell
    pip install torch==2.0.0+cu117 trochaudio==2.0.1+cu117 torchvision==0.15.1+cu117 -f https://download.pytorch.org/whl/torch_stable.html
    ```

3. Install other packages with the following command.

    ```shell
    pip install -r requirements.txt
    ```

4. Install Diffuser following the [official instruction](https://huggingface.co/docs/diffusers/installation#install-from-source), instead of directly installing by pip.

    ```shell
    pip install git+https://github.com/huggingface/diffusers
    ```
***
## Easy to use

* **Prepare raw audio files by downloading or use the `pre_process.py`, which could be saved in `datasets/raw_data`**
    ```shell
    python record_speaker.py
    ```
    Note: Any use of the musical work without proper permission may result in legal action, please follow the copyright instruction.
* **Automatively prepare training datasets for finetuning by `riffusion` tools**
    
    ```shell
    cd scripts && sh predata.sh
    # convert audio clips into spectrogram images
    ```
* **Finetune model with official lora training script**
    
    ```shell
    cd scripts && sh finetune.sh
    # finally, save the lora weights
    ```
* **Generate the audio files with official lora examples**
    
    ```shell
    cd scripts && sh generate.sh
    # choose with or without lora
    ```
***
## Main Results

* **Original audo clips**

<audio controls>
  <source src="results/chunk_1_1_start_16998_ms_dur_5120_ms.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

* **Generated audo clip without lora, steps=50, seed=30, gudiance=7.5**

<audio controls>
  <source src="results/piano_lora0_s30_st50.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

* **Generated audo clip with lora, steps=50, seed=30, gudiance=7.5**

<audio controls>
  <source src="results/piano_lora1_s30_st50.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

* **Generated audo clip with lora, steps=50, seed=10, gudiance=7.5**

<audio controls>
  <source src="results/piano_lora1_s10_st50.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

* **Generated audo clip without lora, steps=50, seed=100, gudiance=7.5**

<audio controls>
  <source src="results/piano_lora1_s100_st50.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

***
## Main Contributors

[Zhenhong Sun](https://sites.google.com/view/sunzhenhong)
