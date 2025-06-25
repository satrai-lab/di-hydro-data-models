# Temperature Sensor (Sense HAT B)

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/TemperatureSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **Band-Gap Diode Temperature Sensor** on the Sense HAT B provides calibrated °C readings via differential diode voltage measured by the on-board ADC.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.
---

## Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                  | **Units / Values**                                    |
| ----------------------- | ---------------- | ------------------------------------------------ | ----------------------------------------------------- |
| **`id`**                | Property         | Unique URI identifier of this temperature sensor | URN format (e.g. `urn:ngsi-ld:TemperatureSensor:t1`)  |
| **`type`**              | Property         | Fixed NGSI-LD entity type                        | `TemperatureSensor`                                   |
| **`measuringRangeMin`** | Property         | Minimum temperature this sensor can report       | Object with:<br>• `value`: -40<br>• `unitCode`: `CEL` |
| **`measuringRangeMax`** | Property         | Maximum temperature this sensor can report       | Object with:<br>• `value`: 85<br>• `unitCode`: `CEL`  |
| **`accuracy`**          | Property         | Maximum deviation from true temperature          | Object with:<br>• `value`: 0.5<br>• `unitCode`: `CEL` |
| **`resolution`**        | Property         | ADC conversion granularity                       | Object with:<br>• `value`: 16<br>• `unitCode`: `bit`  |
| **`isComponentOf`**     | Relationship     | The Sense HAT B board this sensor belongs to     | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)   |


