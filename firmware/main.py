import os
from machine import Pin, SPI, I2S
import sdcard
import time

# --- 1. PIN CONFIGURATION ---
# Rotary Encoder Pins
ENCODER_A = Pin(2, Pin.IN, Pin.PULL_UP)
ENCODER_B = Pin(3, Pin.IN, Pin.PULL_UP)
BUTTON_PIN = Pin(4, Pin.IN, Pin.PULL_UP)

# MicroSD Card SPI Pins
SD_CS = Pin(5, Pin.OUT)
spi = SPI(0, sck=Pin(6), mosi=Pin(7), miso=Pin(4)) # Adjust to your exact SPI pins

# PCM5102A I2S Pins
I2S_BCK = Pin(16)  # Bit Clock
I2S_LRCK = Pin(17) # Left/Right Clock (Word Select)
I2S_DIN = Pin(18)  # Data In

# --- 2. HARDWARE INITIALIZATION ---
# Mount the SD Card
try:
    sd = sdcard.SDCard(spi, SD_CS)
    os.mount(sd, "/sd")
    print("SD Card mounted successfully!")
except Exception as e:
    print("SD Card setup failed:", e)

# Initialize I2S Audio Audio Output
audio_out = I2S(
    0, 
    sck=I2S_BCK, 
    ws=I2S_LRCK, 
    sd=I2S_DIN, 
    mode=I2S.TX, 
    bits=16, 
    format=I2S.STEREO, 
    rate=44100, 
    ibuf=4096
)

# --- 3. ENCODER & PLAYER VARIABLES ---
volume = 50  # Start at 50% volume
last_state_A = ENCODER_A.value()
playing = True

# --- 4. CORE FUNCTIONS ---
def handle_encoder():
    global last_state_A, volume
    current_state_A = ENCODER_A.value()
    
    # Check if knob turned
    if current_state_A != last_state_A and current_state_A == 0:
        if ENCODER_B.value() != current_state_A:
            volume = min(100, volume + 5) # Turn Right: Vol Up
            print(f"Volume: {volume}%")
        else:
            volume = max(0, volume - 5)  # Turn Left: Vol Down
            print(f"Volume: {volume}%")
            
    last_state_A = current_state_A

def play_wav(filename):
    global playing
    try:
        with open(filename, "rb") as wav:
            # Skip the 44-byte WAV header to get straight to raw audio data
            wav.seek(44) 
            
            # Create a memory buffer for fast reading
            buffer = bytearray(1024)
            
            while True:
                # Check controls while playing
                handle_encoder()
                if BUTTON_PIN.value() == 0:  # Button pressed
                    playing = not playing
                    print("Play/Pause Toggled")
                    time.sleep(0.3)  # Software debounce delay
                
                if playing:
                    num_bytes = wav.readinto(buffer)
                    if num_bytes == 0:
                        break # End of file reached
                    
                    # Write audio chunk to the I2S DAC
                    audio_out.write(buffer[:num_bytes])
                    
    except Exception as e:
        print("Playback error:", e)

# --- 5. MAIN LOOP ---
print("Scanning SD Card for music...")
songs = [f"/sd/{file}" for file in os.listdir("/sd") if file.endswith(".wav")]

if songs:
    print(f"Found tracks: {songs}")
    while True:
        for song in songs:
            print(f"Playing: {song}")
            play_wav(song)
else:
    print("No .wav files found on the SD card root directory.")