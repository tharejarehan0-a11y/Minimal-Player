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

The table below lists all components used in the Minimal Player, matching the exact footprints and values from the KiCad PCB design layout. 

| Designator | Value | Footprint | Qty | India Sourcing / Purchase Links |
| :--- | :--- | :--- | :--- | :--- |
| **A1** | RaspberryPi_Pico | RaspberryPi_Pico_Common_THT | 1 | [Robu.in - Raspberry Pi Pico](https://robu.in/product/raspberry-pi-pico/) / [ElectronicsComp](https://www.electronicscomp.com/raspberry-pi-pico-board) |
| **BT1** | Battery Connector | JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical | 1 | [Robu.in - JST PH 2.0mm Male Header](https://robu.in/product/jst-ph-2-0-2-pin-male-connector-straight/) |
| **C1, C10, C11, C14, C15, C3** | $10\,\mu\text{F}$ | 0805 SMD Capacitor | 6 | [ElectronicsComp - 10uF 0805 Ceramic](https://www.electronicscomp.com/10uf-25v-0805-smd-capacitor) |
| **C12** | $2.2\text{ nF}$ | 0805 SMD Capacitor | 1 | [ElectronicsComp - 2.2nF 0805 Ceramic](https://www.electronicscomp.com/2.2nf-50v-0805-smd-capacitor) |
| **C13, R13** | 470 *(See Notes)* | 0805 SMD | 2 | [Resistor (470 $\Omega$)](https://www.electronicscomp.com/470-ohm-0805-smd-resistor) / [Capacitor (470 pF)](https://www.electronicscomp.com/470pf-50v-0805-smd-capacitor) |
| **C2, C5, C6, C8, C9** | $0.1\,\mu\text{F}$ | 0805 SMD Capacitor | 5 | [ElectronicsComp - 0.1uF 0805 Ceramic](https://www.electronicscomp.com/0.1uf-50v-0805-smd-capacitor) |
| **C4, C7** | $2.2\,\mu\text{F}$ | 0805 SMD Capacitor | 2 | [ElectronicsComp - 2.2uF 0805 Ceramic](https://www.electronicscomp.com/2.2uf-50v-0805-smd-capacitor) |
| **D1, D2** | LED_Small | 0805 SMD LED | 2 | [Robu.in - 0805 SMD LED Kit](https://robu.in/product/0805-smd-led-diode-assortment-kit-5-colors/) |
| **J1** | USB_C_Receptacle_14P | USB_C_Receptacle_HRO_TYPE-C-31-M-12 | 1 | [Robu.in - TYPE-C-31-M-12 Compatible 16P SMT](https://robu.in/product/usb-c-type-c-female-connector-16-pin-surface-mount/) |
| **J2** | Micro_SD_Card Slot | microSD_HC_Molex_104031-0811 | 1 | [ElectronicsComp - Push-Push MicroSD Slot](https://www.electronicscomp.com/micro-sd-card-slot-socket-smd-push-push-type) / [DigiKey India - Molex Exact](https://www.digikey.in/en/products/detail/molex/1040310811/3044122) |
| **J3** | AudioJack3 | Jack_3.5mm_CUI_SJ1-3523N_Horizontal | 1 | [DigiKey India - CUI SJ1-3523N Exact](https://www.digikey.in/en/products/detail/cui-devices/SJ1-3523N/738686) |
| **R1, R11, R2** | $5.1\text{ k}\Omega$ | 0805 SMD Resistor | 3 | [ElectronicsComp - 5.1k 0805 Resistor](https://www.electronicscomp.com/5.1k-ohm-0805-smd-resistor) |
| **R10** | $1.2\text{ k}\Omega$ | 0805 SMD Resistor | 1 | [ElectronicsComp - 1.2k 0805 Resistor](https://www.electronicscomp.com/1.2k-ohm-0805-smd-resistor) |
| **R12, R14, R5, R6, R7, R8, TH1** | $10\text{ k}\Omega$ *(See Notes)* | 0805 SMD | 7 | [Resistor (10k $\Omega$)](https://www.electronicscomp.com/10k-ohm-0805-smd-resistor) / [NTC Thermistor](https://www.electronicscomp.com/10k-ntc-thermistor-smd-0805) |
| **R3, R4** | $1\text{ k}\Omega$ | 0805 SMD Resistor | 2 | [ElectronicsComp - 1k 0805 Resistor](https://www.electronicscomp.com/1k-ohm-0805-smd-resistor) |
| **R9** | 0.4 / 400 $\Omega$ | 0805 SMD Resistor | 1 | [ElectronicsComp - 0805 SMD Resistor Assortment](https://www.electronicscomp.com/0805-smd-resistor-kit-36-values) |
| **SW1, SW2, SW3, SW4** | SW_SPST | SW_PUSH_6mm_H4.3mm | 4 | [Robu.in - 6x6x4.3mm Tactile Switch](https://robu.in/product/6x6x4-3mm-tactile-micro-push-button-switch-2-pin/) |
| **SW5** | RotaryEncoder | RotaryEncoder_Bourns_Vertical_PEC12R | 1 | [ElectronicsComp - EC11/12 with Switch](https://www.electronicscomp.com/ec11-rotary-encoder-with-switch-20mm-half-shaft) / [DigiKey India - Bourns Exact](https://www.digikey.in/en/products/detail/bourns-inc/PEC12R-4220F-S0024/3780188) |
| **U1** | TP4056-42-ESOP8 | SOIC-8-1EP (Exposed Thermal Pad) | 1 | [ElectronicsComp - TP4056 IC](https://www.electronicscomp.com/tp4056-linear-li-ion-battery-charger-ic) |
| **U2** | PCM5102A | TSSOP-20_4.4x6.5mm_P0.65mm | 1 | [ElectronicsComp - PCM5102A IC](https://www.electronicscomp.com/pcm5102a-audio-dac-ic-tssop-20) / [DigiKey India - TI Original](https://www.digikey.in/en/products/detail/texas-instruments/PCM5102APWR/3055979) |

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
