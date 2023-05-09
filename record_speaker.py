import os
import time
import wave
import pyaudio
import numpy as np
import argparse


class AudioRecorder:
    def __init__(self, settings):
        self.audio = pyaudio.PyAudio()
        self.settings = settings
        self.device_index = None
        self.stream = None
        self.chunk_count = 0
    
    def list_audio_devices(self):
        for i in range(0, self.audio.get_device_count()):
            print(i, self.audio.get_device_info_by_index(i)['name'])
    
    def set_audio_device(self, index):
        self.device_index = index
    
    def start_recording(self):
        if self.device_index is None:
            print("Please select an audio device first.")
            return
        self.stream = self.audio.open(format=self.settings.format,
                                        channels=self.settings.channels,
                                        rate=self.settings.rate,
                                        input=True,
                                        frames_per_buffer=self.settings.chunk_size,
                                        input_device_index=self.device_index,)
        
        # Monitoring and saving audio chunks
        print("Monitoring audio...")
        while True:
            try:
                audio_data = []
                for _ in range(0, int(self.settings.rate / self.settings.chunk_size * self.settings.record_seconds)):
                    data = self.stream.read(self.settings.chunk_size, exception_on_overflow=False)
                    audio_data.append(data)
                self.chunk_count += 1
                self.save_audio_chunk(audio_data)
                msg = input("Please input 1 to continue:")
                print("chunk_count: %d"%self.chunk_count)
            except KeyboardInterrupt:
                print("Stopped monitoring audio")
                break
    

    def save_audio_chunk(self, audio_data):
        os.makedirs(self.settings.output_folder, exist_ok=True)
        output_file = os.path.join(self.settings.output_folder, f"chunk_{self.chunk_count}.wav")
        with wave.open(output_file, 'wb') as wf:
            wf.setnchannels(self.settings.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.settings.format))
            wf.setframerate(self.settings.rate)
            wf.writeframes(b''.join(audio_data))
        print(f"Saved: {output_file}") 


    def stop_recording(self):
        if self.stream is None:
            return
        
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        

class SettingsSet:
    def __init__(self, args):

        self.chunk_size = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = args.rate
        self.record_seconds = args.record_seconds
        self.output_folder = args.output_folder


def parse_args():
    parser = argparse.ArgumentParser(description="Generate metadata for a dataset")
    parser.add_argument("-r", "--rate", type=int, default=44100, help="sampling rate")
    parser.add_argument("-d", "--record-seconds", type=int, default=60, help="recording duration in seconds")
    parser.add_argument("-o", "--output-folder", default="datasets/raw_data", help="folder to save recorded audio chunks")
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    
    settings = SettingsSet(args)
    recorder = AudioRecorder(settings)
    recorder.list_audio_devices()
    device_index = int(input('Device index: '))
    recorder.set_audio_device(device_index)
    recorder.start_recording()
    recorder.stop_recording()
    # git