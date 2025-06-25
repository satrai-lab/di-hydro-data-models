# Barometric Pressure Sensor (Sense HAT B)

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Barometer.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **barometric pressure sensor** on the Sense HAT B uses a MEMS diaphragm and on-board ADC to provide high-precision atmospheric pressure readings.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.
---

## Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                              | **Units / Values**                                        |
| ----------------------- | ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| **`measuringRangeMin`** | Property         | Lowest pressure this sensor can measure      | Object with:<br>• `value`: 260<br>• `unitCode`: `"hPa"`   |
| **`measuringRangeMax`** | Property         | Highest pressure this sensor can measure     | Object with:<br>• `value`: 1260<br>• `unitCode`: `"hPa"`  |
| **`accuracy`**          | Property         | Maximum pressure error                       | Object with:<br>• `value`: 0.025<br>• `unitCode`: `"hPa"` |
| **`resolution`**        | Property         | ADC conversion resolution                    | Object with:<br>• `value`: 24<br>• `unitCode`: `"bit"`    |
| **`isComponentOf`**     | Relationship     | The Sense HAT B board this module belongs to | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)       |


