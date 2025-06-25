# 3-Axis MEMS Gyroscope
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Geroscope.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **3-Axis MEMS Gyroscope** on the Sense HAT B measures angular rate (rotation speed) about three orthogonal axes (roll, pitch, yaw) and streams digital I²C outputs synchronized with other board sensors.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                        | **Units / Values**                                                                         |
| ----------------------- | ---------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **`id`**                | Property         | Unique URI identifier of this gyroscope entity         | URN format (e.g. `"urn:ngsi-ld:GyroscopeSensor:g1"`)                                       |
| **`type`**              | Property         | Fixed NGSI-LD entity type                              | `"Geroscope"`                                                                              |
| **`axes`**              | Property         | Number of rotation axes                                | Object with:<br>• `value`: 3<br>• `unitCode`: `""`                                         |
| **`measurementRanges`** | Property         | Supported angular-rate measurement ranges              | Object with:<br>• `value`: `[16, 32, 64, 128, 512, 1024, 2048]`<br>• `unitCode`: `"DEG/S"` |
| **`resolution`**        | Property         | ADC conversion granularity                             | Object with:<br>• `value`: 16<br>• `unitCode`: `"bit"`                                     |
| **`isComponentOf`**     | Relationship     | The Sense HAT B board this gyroscope module belongs to | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)                                        |


