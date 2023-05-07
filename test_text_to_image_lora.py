# coding=utf-8
# Copyright 2023 Zhenhong Sun modified. All rights reserved.
# Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import torch
import argparse

from diffusers import StableDiffusionPipeline


class PianoDiffusion:
    def __init__(self, args):
        self.pretrain_model = args.pretrain_model
        self.model_path = args.model_path
        self.prompt = args.prompt
        self.output_path = args.output_path
        self.no_lora = args.no_lora
        self.args = args

    def run(self):
        pipe = StableDiffusionPipeline.from_pretrained(self.pretrain_model, torch_dtype=torch.float16)
        if not self.no_lora: pipe.unet.load_attn_procs(self.model_path)
        pipe.to("cuda")
        
        if self.no_lora:
            image = pipe(prompt=self.prompt).images[0]
        else:
            image = pipe(self.prompt, num_inference_steps=30, guidance_scale=7.5, cross_attention_kwargs={"scale": 0.5}).images[0]
        os.makedirs(self.output_path, exist_ok=True)
        image.save(os.path.join(self.output_path, self.args.audio_name))


def parse_args():
    parser = argparse.ArgumentParser(description="Piano diffusion image generation")
    parser.add_argument("--pretrain_model", type=str, default="riffusion/riffusion-model-v1", help="Path to the model weights")
    parser.add_argument("--model_path", type=str, default=None, help="Path to the model weights")
    parser.add_argument("--prompt", type=str, default="Ghibli Medley Piano", help="Image generation prompt")
    parser.add_argument("--seed", type=int, default=42, help="Image generation prompt")
    parser.add_argument("--output_path", type=str, default="output", help="Path to save the generated image")
    parser.add_argument("--audio_name", type=str, default="test.png", help="Path to save the generated image")
    parser.add_argument("--no_lora", type=int, default=0, help="Path to save the generated image")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args)
    piano_diffusion = PianoDiffusion(args)
    piano_diffusion.run()
