cd ..

export MODEL_NAME="riffusion/riffusion-model-v1"
export DATASET_NAME="/mnt1/zhenhong.szh/Projects/03-diffusion/02-lora/datasets/train"

# dataset_name=$DATASET_NAME  --multi_gpu 
accelerate launch --mixed_precision="fp16"  train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$DATASET_NAME --caption_column="additional_feature" \
  --resolution=512 --random_flip \
  --train_batch_size=1 \
  --num_train_epochs=100 --checkpointing_steps=5000 \
  --learning_rate=1e-04 --lr_scheduler="constant" --lr_warmup_steps=0 \
  --seed=42 \
  --output_dir="piano" \
  --validation_prompt="ghibli medley piano" --report_to="tensorboard"