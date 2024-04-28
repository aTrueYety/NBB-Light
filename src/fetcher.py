"""
This module provides a function to record system audio and save it to a WAV file.

Usage:
    record_system_audio(output_filename, record_seconds)

Parameters:
    output_filename (str): The name of the output WAV file.
    record_seconds (int): The duration of the audio recording in seconds.

Example:
    record_system_audio("output.wav", 10)
"""

import wave
import pyaudio

# Parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10  # Adjust as needed
OUTPUT_FILENAME = "output.wav"

def record_system_audio(output_filename, record_seconds):
    """
    Record system audio and save it to a WAV file.

    Parameters:
        output_filename (str): The name of the output WAV file.
        record_seconds (int): The duration of the audio recording in seconds.
    """
    audio = pyaudio.PyAudio()

    # Check available input devices
    print("Available input devices:")
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"Index: {i}, Name: {info['name']}")
    print()

    _input_device_index = int(input("Enter the input device index: "))

    # Open the audio stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=_input_device_index)

    print("Recording...")

    frames = []

    # Record audio frames
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded audio to a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved to {output_filename}")

if __name__ == "__main__":
    # Example usage
    record_system_audio(OUTPUT_FILENAME, RECORD_SECONDS)
