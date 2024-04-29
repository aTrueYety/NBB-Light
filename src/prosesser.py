"""
  This module provides a function to process audio data.
"""

import wave

def prcess_audio(_input_filename) -> tuple[list[int], list[int], list[int]]:
    """
    Process audio data, providing tempo, intensity and volum information over time.
  
    Args:
      _input_filename (str): The name of the input WAV file without the file extension.

    Returns:
      tuple[list[int], list[int], list[int], list[int]]: A tuple containing the tempo, 
      intensity and volum information over time, respectively.  
    """
    # Open the audio file
    audio = wave.open(f"{_input_filename}.wav", "rb")

    # Process the audio data
    tempo = []
    intensity = []
    volume = []

    # Close the audio file
    audio.close()

    return tempo, intensity, volume
