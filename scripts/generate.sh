cd ..

seed="${1:-"42"}"
prompt="${2:-"Ghibli Medley Piano"}"
audio_name="${3:-"piano"}"
no_lora="${4:-"0"}"
output_dir="${5:-"piano"}"

export MODEL_NAME="riffusion/riffusion-model-v1"
export DATASET_NAME="/mnt1/zhenhong.szh/Projects/03-diffusion/02-lora/datasets/train"
export LORA_PATH="/mnt1/zhenhong.szh/Projects/03-diffusion/02-lora/piano/pytorch_lora_weights.bin"

python test_text_to_image_lora.py --pretrain_model=$MODEL_NAME --model_path=$LORA_PATH \
      --prompt="$prompt" --seed=$seed --no_lora=$no_lora \
      --output_path=$output_dir --audio_name="$audio_name.png"

python -m riffusion.cli image-to-audio -i $output_dir/$audio_name.png -a $output_dir/$audio_name.wav
