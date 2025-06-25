# Magnetometer 

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Magnetometer.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **3-Axis MEMS Magnetometer** on the Sense HAT B measures the local magnetic field along three orthogonal axes via an on-board ADC.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.

---

## Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                   | **Units / Values**                                       |
| ----------------------- | ---------------- | ------------------------------------------------- | -------------------------------------------------------- |
| **`id`**                | Property         | Unique URI identifier of this magnetometer entity | URN format (e.g. `urn:ngsi-ld:Magnetometer:m1`)          |
| **`type`**              | Property         | Fixed NGSI-LD entity type                         | `Magnetometer`                                           |
| **`axes`**              | Property         | Number of measurement axes                        | Object with:<br>• `value`: 3<br>• `unitCode`: `""`       |
| **`measuringRangeMin`** | Property         | Minimum magnetic flux density measurable          | Object with:<br>• `value`: -49.12<br>• `unitCode`: `GAU` |
| **`measuringRangeMax`** | Property         | Maximum magnetic flux density measurable          | Object with:<br>• `value`: 49.12<br>• `unitCode`: `GAU`  |
| **`resolution`**        | Property         | ADC conversion resolution                         | Object with:<br>• `value`: 16<br>• `unitCode`: `bit`     |
| **`isComponentOf`**     | Relationship     | The Sense HAT B board this sensor belongs to      | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)      |


