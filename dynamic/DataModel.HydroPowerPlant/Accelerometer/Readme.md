# Accelerometer Sensor (Sense HAT B)

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Accelerometer.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **3-Axis MEMS Accelerometer** on the Sense HAT B measures linear acceleration along three orthogonal axes and streams digital acceleration values over I²C.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                    | **Units / Values**                                                |
| ----------------------- | ---------------- | -------------------------------------------------- | ----------------------------------------------------------------- |
| **`id`**                | Property         | Unique URI identifier of this accelerometer entity | URN format (e.g. `urn:ngsi-ld:Accelerometer:acc1`)                |
| **`type`**              | Property         | Fixed NGSI-LD entity type                          | `Accelerometer`                                                   |
| **`axes`**              | Property         | Number of measurement axes                         | Object with:<br>• `value`: 3<br>• `unitCode`: `""`                |
| **`measurementRanges`** | Property         | Supported acceleration ranges                      | Object with:<br>• `value`: `[2, 4, 8, 16]`<br>• `unitCode`: `"G"` |
| **`resolution`**        | Property         | ADC conversion granularity                         | Object with:<br>• `value`: 16<br>• `unitCode`: `"bit"`            |
| **`isComponentOf`**     | Relationship     | The Sense HAT B board this sensor belongs to       | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)               |

---

