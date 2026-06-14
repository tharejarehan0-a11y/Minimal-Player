# Minimal Player
<p align="center">
<img width="420" height="595" alt="A5 - 2" src="https://github.com/user-attachments/assets/85ffbbcf-acc7-4567-b866-2f3be926f563" />
</p>
Minimal Player is a compact, robust, and highly optimized pocket MP3 player built around the **Raspberry Pi Pico**. Designed to bridge the gap between high-speed digital processing and clean analog audio output, it packs incredible audio fidelity into a pocket-sized form factor without any unnecessary bulk.

---

## Why I Created This

Most modern music devices are distracting. They come with touchscreens, internet connectivity, and endless notifications that pull you away from the music. I wanted to build something that strips away the noise—both literally and figuratively. 

The goal was to create a dedicated, distraction-free audio player that focuses entirely on local playback with tactile hardware controls. Building it from scratch also provided the perfect opportunity to master the complexities of mixed-signal hardware design, hardware filtering (debouncing), and PCB power routing.

---

## My Inspiration

The inspiration came from a blend of nostalgia and engineering curiosity:
* **The Early 2000s iPod Shuffle / Sansa Clip:** Devices that did one thing perfectly—play music at the click of a physical button.
* **The Maker Movement:** Seeing the incredible power of the $4 Raspberry Pi Pico made me wonder how far its dual-core processor could be pushed in handling real-time audio decoding alongside file systems.
* **Pure Audiophile Simplicity:** The desire to implement a dedicated high-quality DAC circuit directly tied to physical controls, bypassing complex operating systems altogether.

---

## Bill of Materials (BOM)

Here are the core components used to build the Minimal Player:

| Component Reference | Description | Qty | Package / Style | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **A1** | Raspberry Pi Pico | 1 | Through-Hole Module | Main microcontroller; handles file parsing and I2S audio streaming. |
| **U1** | TP4056 | 1 | SOP-8 / Thermal Pad | Lithium battery charger management IC with status LEDs. |
| **U2** | PCM5102A | 1 | TSSOP-20 | Dedicated 32-bit I2S Audio DAC for crisp sound generation. |
| **J1** | MicroSD Card Slot | 1 | Surface Mount (SMD) | SPI-based storage for holding your MP3/WAV library. |
| **J3** | CUI Devices SJ1-3523N | 1 | 3-Pin Horizontal THT | Robust 3.5mm headphone jack for standard earphones. |
| **EC11** | Bourns PEC11R | 1 | 5-Pin Vertical THT | Rotary encoder with built-in push switch for volume and track control. |
| **C_Elec** | 10µF to 47µF Electrolytic | 4 | Radial THT (Polarized) | Bulk power stabilization reservoirs for the SD card, DAC, and Charger. |
| **C_Cer** | 0.1µF / 10nF / 2.2nF | Var | 0805 / THT Ceramic | Decoupling capacitors and hardware low-pass RC filters. |
| **R_Sig** | 470Ω / 10kΩ | Var | 0805 / THT | Current-limiting protection for the audio lines and encoder debouncing. |

---

## Hardware Features & Design Choices

* **2-Layer PCB Architecture:** The top layer is dedicated to wide power traces and signal routing, while the bottom layer acts as an unbroken **AGND/GND ground plane** to shield the headphones from digital processor hiss.
* **Hardware Debouncing:** The rotary encoder features integrated RC low-pass filters (10 kΩ + 10 nF) on the rotation pins to guarantee smooth, skip-free volume steps.
* **Power Isolation:** Thick power rivers (24 mils) are utilized from the USB-C bus through the TP4056 and into the Pico's voltage regulators to safely manage battery charging surges.
