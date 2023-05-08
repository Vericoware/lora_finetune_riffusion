cd ..

seed="${1:-"42"}"
prompt="${2:-"Ghibli Medley Piano"}"
audio_name="${3:-"piano"}"
with_lora="${4:-"1"}"
steps="${5:-"30"}"
output_dir="${6:-"piano"}"

export MODEL_NAME="riffusion/riffusion-model-v1"
export DATASET_NAME="/mnt1/zhenhong.szh/Projects/03-diffusion/02-lora/datasets/train"
export LORA_PATH="/mnt1/zhenhong.szh/Projects/03-diffusion/02-lora/piano/pytorch_lora_weights.bin"

python test_text_to_image_lora.py --pretrain_model=$MODEL_NAME --model_path=$LORA_PATH \
      --prompt="$prompt" --seed=$seed --with_lora=$with_lora --steps=$steps \
      --output_path=$output_dir --audio_name="${audio_name}_lora${with_lora}_s${seed}_st${steps}.png"

python -m riffusion.cli image-to-audio -i $output_dir/${audio_name}_lora${with_lora}_s${seed}_st${steps}.png \
      -a $output_dir/${audio_name}_lora${with_lora}_s${seed}_st${steps}.wav
