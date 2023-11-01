import pyaudio

audio = pyaudio.PyAudio()

# for i in range(audio.get_device_count()):
#         devInfo = audio.get_device_info_by_index(i)
        
#         if devInfo['hostApi'] == 0:
#             print(devInfo['name'])


print("\n\n\n")
print(audio.get_default_input_device_info())
print(audio.get_default_output_device_info())