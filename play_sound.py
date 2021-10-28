from pygame import mixer
import sys

def playAudio(fileName, volumeLevel):
    print(f'trying to play sound: {fileName}')
    sys.stdout.flush()
    mixer.init()
    mixer.music.set_volume(volumeLevel)
    mixer.music.load(fileName)
    mixer.music.play()
    print(f'{fileName} playing')
    sys.stdout.flush()
    while mixer.music.get_busy() == True:
        continue
    print(f'finished playing {fileName}')
    sys.stdout.flush()
    return True

def getUrl():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return './helgwerge.wav' #default

playAudio(getUrl(), 10)
