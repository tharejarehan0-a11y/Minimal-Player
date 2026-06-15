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

# Schematics 

<img width="1470" height="956" alt="Screenshot 2026-06-15 at 12 40 12 PM" src="https://github.com/user-attachments/assets/5edddf49-b923-4830-a87f-6e93ed8b63fe" />


The schematics were not that difficult because both the newer components had the datasheets to be followed the TP4056A and the PAM DAC they were easy to setup but the newer things that i explored onto this project were the electrolytic capcitors and how they have more capacitors and i also learned about this like analog and digital signals are different but sometimes when you have a project where you are going whith a pcb design for only 2 layers you can have same ground for both of them so i had the same ground for both of them and the TP4056 helped a lot with having a stable current towards the pico so that it can run easily and at last the PAM is a machine when it comes to audio only via headphones and works with the 3 pin audio jack that i setted up. I also added rotatory encoder , the buttons and a micro sd card a usb c and a lithium battery which can be recharged 

<br>

# PCB
<img width="1470" height="956" alt="Screenshot 2026-06-15 at 12 54 30 PM" src="https://github.com/user-attachments/assets/94ecb52f-38c6-4091-82ae-dcbe73b6e062" />

Then I started with the PCB it was really the hard part to deal with. I started by placing all the components but there were like so many capacitors and resistors that were to be placed which made it so confusing to set it up . So I took the schematics as the reference and placed all the capacitors as it was in that and then I started with routing it and got to know that the traces with the power are to be kept thick and the digital can be thin so i did it all wrong at the first try but got it on the second try. Then was the time to fix the errors . I had like so many errors I had to deal with so i started with the short errors all the way to body malformed errors and stuff and did that at last by filling the zone with AGND as the net 

<br>

# CAD
<img width="1470" height="956" alt="Screenshot 2026-06-15 at 12 53 39 PM" src="https://github.com/user-attachments/assets/eed1ba7f-6fb6-49c0-9304-37c50ef74d38" />
Onshape is the best . I started by drawing two rectangles and then i extruded the part that was common to only one bigger rectangle in which with the same center was the other rectange and then i extruded it then i made the sketched for those tiny rectangular holes onto the sides of it and with the help of linear pattern i redrew them all easily and then i removed them from the sides to a certain extent to give a retro vibe then i imported the step file for the pcb and then what I did was i made the lower case and the upper case derived some parts and sketches drew the rotatory encoder the buttons . Imported the step files for the springs and the battery and then made the assembly that was it in all 
