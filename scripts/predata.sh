cd ..

python -m riffusion.cli sample-clips-batch -a datasets/raw_data -o datasets/raw_clips --num-clips-per-file 2 --num-threads 10
python -m riffusion.cli audio-to-images-batch -a datasets/raw_clips -o datasets/train/
python pre_process.py -d datasets/train -m metadata.jsonl -a "Ghibli Medley Piano"