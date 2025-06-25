# ADC Conversion Chip 
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/ADCChip.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

An **Analog–Digital Conversion Chip** on the Sense HAT B digitizes all onboard analog sensor outputs at 16-bit resolution and streams synchronized data over I²C.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attribute Specifications

| **Attribute**       | **NGSI-LD Type** | **Description**                                   | **Units / Values**                                   |
| ------------------- | ---------------- | ------------------------------------------------- | ---------------------------------------------------- |
| **`id`**            | Property         | Unique URI identifier of this ADC conversion chip | URN format (e.g. `urn:ngsi-ld:ADCChip:adc1`)         |
| **`type`**          | Property         | Fixed NGSI-LD entity type                         | `ADCChip`                                            |
| **`resolution`**    | Property         | Bit-depth of the analog-to-digital conversion     | Object with:<br>• `value`: 16<br>• `unitCode`: `bit` |
| **`isComponentOf`** | Relationship     | The Sense HAT B board this ADC chip belongs to    | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)  |

