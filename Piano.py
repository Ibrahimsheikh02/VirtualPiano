import pygame
from pynput.keyboard import Key, Listener

pygame.mixer.init()
pygame.mixer.set_num_channels(32)
notes = { 
    'a': pygame.mixer.Sound('C.mp3'),
    's': pygame.mixer.Sound('C#.mp3'),
    'd': pygame.mixer.Sound('D.mp3'),
    'f': pygame.mixer.Sound('D#.mp3'),
    'g': pygame.mixer.Sound('E.mp3'),
    'h': pygame.mixer.Sound('F.mp3'),
    'j': pygame.mixer.Sound('F#.mp3'),
    'k': pygame.mixer.Sound('G.mp3'),
    'l': pygame.mixer.Sound('G#.mp3'),
    ';': pygame.mixer.Sound('A.mp3'),
    '\'': pygame.mixer.Sound('A#.mp3'),
    '\"': pygame.mixer.Sound('B.mp3'),
    ' ': pygame.mixer.Sound('F.mp3')  # added a separate case for the spacebar
}

def play_sound(key):
    if key == Key.space:  # if the key is the spacebar
        note = notes.get(' ')
    elif hasattr(key, 'char'):  # if the key has a char attribute
        note = notes.get(key.char)  # get the sound object from the dictionary
    else:
        note = None

    if note:  # if the key exists in the dictionary
        note.play()  # play the sound

with Listener(on_press=play_sound) as listener:
    listener.join()


'''
Recording the sound (Record and Replay)

Play some professional notes by a professional pianist and record it. 

'''