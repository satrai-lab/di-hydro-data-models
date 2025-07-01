## Ultrasonic Generator
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/UltrasonicGenerator.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 500px">
</div>

## Definition
An **Ultrasonic Generator** is an electronic device that produces controlled high-frequency electrical waveforms—typically in the 20–40 kHz range—to drive ultrasonic transducers in antifouling systems. It offers multiple output channels, signal modulation modes, and precise timing controls to synchronize ultrasonic pulses, preventing biofouling on submerged surfaces.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.

### Attribute Specifications

| **Attribute**              | **NGSI-LD Type** | **Description**                          | **Units / Values**                                                |
| -------------------------- | ---------------- | ---------------------------------------- | ----------------------------------------------------------------- |
| **`id`**                   | Identifier       | Unique URI identifier                    | e.g. `urn:ngsi-ld:UltrasonicGenerator:001`                        |
| **`type`**                 | Type             | Fixed entity type                        | `"UltrasonicGenerator"`                                           |
| **`status`**               | Property         | Operational status                       | `"active"` / `"idle"`                                             |
| **`model`**                | Property         | Device model                             | e.g. `"USG-4X2024"`                                               |
| **`manufacturer`**         | Property         | Manufacturer name                        | e.g. `"SonicTech Instruments"`                                    |
| **`numberOfChannels`**     | Property         | Number of independent output channels    | integer (e.g. `4`)                                                |
| **`outputVoltage`**        | Property         | Peak output voltage of each channel      | Object `{ value: number, unitCode: "V" }` (e.g. `{12, "V"}`)      |
| **`signalFrequencyMin`**   | Property         | Minimum generated frequency              | Object `{ value: number, unitCode: "kHz" }` (e.g. `{20, "kHz"}`)  |
| **`signalFrequencyMax`**   | Property         | Maximum generated frequency              | Object `{ value: number, unitCode: "kHz" }` (e.g. `{40, "kHz"}`)  |
| **`pulseControl`**         | Property         | Emission mode                            | `"modulated"` / `"continuous"`                                    |
| **`powerSupplyVoltage`**   | Property         | AC input voltage                         | Object `{ value: number, unitCode: "V" }` (e.g. `{220, "V"}`)     |
| **`powerSupplyFrequency`** | Property         | AC line frequency                        | Object `{ value: number, unitCode: "Hz" }` (e.g. `{50, "Hz"}`)    |
| **`dimensions`**           | Property         | Physical size of the generator enclosure | Object `{ value: [number, number, number], unitCode: "MMT" }`     |
| **`weight`**               | Property         | Mass of the generator                    | Object `{ value: number, unitCode: "KGM" }` (e.g. `{2.5, "KGM"}`) |



