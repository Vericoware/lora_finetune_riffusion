import os
import time
import wave
import pyaudio
import numpy as np

# Settings
chunk_size = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100
record_seconds = 10*6
output_folder = "saved"

# Initialize PyAudio
audio = pyaudio.PyAudio()

for i in range(0, audio.get_device_count()):
    print(i, audio.get_device_info_by_index(i)['name'])

device_index = int(input('Device index: '))

# Define audio stream settings
stream = audio.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size,
                    input_device_index=device_index, 
                    )

# Function to save recorded chunks
def save_audio_chunk(audio_data, chunk_count):

    output_file = f"{output_folder}/chunk_{chunk_count}.wav"
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(audio_data))
    print(f"Saved: {output_file}")

# Monitoring and saving audio chunks
print("Monitoring audio...")
chunk_count = 0
while True:
    try:
        audio_data = []
        for _ in range(0, int(rate / chunk_size * record_seconds)):
            data = stream.read(chunk_size, exception_on_overflow=False)
            audio_data.append(data)
        chunk_count += 1
        save_audio_chunk(audio_data, chunk_count)
        msg = input("Please input 1 to continue:")
        print("chunk_count: %d"%chunk_count)
    except KeyboardInterrupt:
        print("Stopped monitoring audio")
        break

# Clean up
stream.stop_stream()
stream.close()
audio.terminate()