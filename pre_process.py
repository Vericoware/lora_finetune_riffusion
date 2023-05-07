# coding=utf-8
# Copyright 2023 Zhenhong Sun modified. All rights reserved.
# Copyright 2023 Riffusion team. All rights reserved.

# The format of fine-tuning dataset reference is available at
# https://huggingface.co/docs/datasets/v2.4.0/en/image_load#imagefolder-with-metadata.
# The dataset dir consists of training images and a "metadata.jsonl" file, containing
# {"file_name": "0001.png", "additional_feature": "This is a first value of a text feature you added to your images"}

import os
import json
import argparse
from tqdm import tqdm

class MetadataGenerator:
    def __init__(self, dataset_dir, metadata_file_name, additional_feature):
        self.dataset_dir = dataset_dir
        self.metadata_file = os.path.join(dataset_dir, metadata_file_name)
        self.additional_feature = additional_feature

    def get_training_images(self):
        # TODO: may be have different levels of the directory.
        return [f for f in os.listdir(self.dataset_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    def generate_metadata_entries(self, training_images):
        metadata_entries = []
        for file_name in tqdm(training_images):
            additional_feature = self.additional_feature
            metadata_entry = {"file_name": file_name, "additional_feature": additional_feature}
            metadata_entries.append(metadata_entry)
        return metadata_entries

    def write_metadata_to_file(self, metadata_entries):
        with open(self.metadata_file, "w") as f:
            for entry in metadata_entries:
                f.write(json.dumps(entry) + "\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Generate metadata for a dataset")
    parser.add_argument("-d", "--dataset_dir", type=str, default="datasets/train", help="Path to the dataset directory containing training images")
    parser.add_argument("-m", "--metadata_file_name", type=str, default="metadata.jsonl", help="Name of the metadata JSON file")
    parser.add_argument("-a", "--additional_feature", type=str, default="Ghibli Medley Piano", help="additional_feature")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args)
    print("Start processing the dataset_dir...")
    dataset_dir = args.dataset_dir
    metadata_file_name = args.metadata_file_name
    additional_feature = args.additional_feature

    metadata_generator = MetadataGenerator(dataset_dir, metadata_file_name, additional_feature)
    
    training_images = metadata_generator.get_training_images()
    metadata_entries = metadata_generator.generate_metadata_entries(training_images)
    metadata_generator.write_metadata_to_file(metadata_entries)
    print("Finish processing the dataset_dir...")
