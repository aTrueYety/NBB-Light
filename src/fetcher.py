"""
This module provides a function to record system audio and save it to a WAV file.

Usage:
    record_audio(output_filename, record_seconds)

Parameters:
    output_filename (str): The name of the output WAV file.
    record_seconds (int): The duration of the audio recording in seconds.
    input_device_index (int): The index of the input device to record from.

Example:
    record_audio("output", 10, 2)
    
Note:
    This software has some legal implications. It is the responsibility of the user to ensure that they are compliant with all relevant laws and regulations.
    This software shoul UNDER NO CIRCUMSTANCES be used be used with virtual cable software, like VB-Audio Virtual Cable, to record audio from streaming services, like Spotify.
"""

import wave
import pyaudio

# Parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

def record_audio(_output_filename, _record_seconds, _input_device_index=1) -> None:
    """
    Record system audio and save it to a WAV file.

    Parameters:
        _output_filename (str): The name of the output WAV file.
        _record_seconds (int): The duration of the audio recording in seconds.
    """
    audio = pyaudio.PyAudio()

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
    for i in range(0, int(RATE / CHUNK * _record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded audio to a WAV file
    with wave.open(_output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved to {_output_filename}")

if __name__ == "__main__":
    audio = pyaudio.PyAudio()

    # Check available input devices
    print("Available input devices:")
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"Index: {i}, Name: {info['name']}")
    print()

    input_device_index = int(input('Skriv inn input device index: '))

    print('Velg lengde på opptak i sekunder:')
    record_seconds = int(input('Skriv inn antall sekunder: '))

    print('Velg navn på output fil:')
    output_filename = input('Skriv inn filnavn: ')

    # Example usage
    record_audio('./songs/' + output_filename + '.wav', record_seconds, input_device_index)
