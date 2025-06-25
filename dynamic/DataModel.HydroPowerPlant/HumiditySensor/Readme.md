# Capacitive Humidity Sensor (Sense HAT B)

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/HumiditySensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A Capacitive Humidity Sensor on the Sense HAT B provides relative-humidity readings via its on-board ADC.



> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                       | **Units / Values**                                    |
| ----------------------- | ---------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| **`id`**                | Property         | Unique URI identifier of this humidity sensor         | URN format (e.g. `urn:ngsi-ld:HumiditySensor:hs1`)    |
| **`type`**              | Property         | Fixed NGSI-LD entity type                             | `HumiditySensor`                                      |
| **`measuringRangeMin`** | Property         | Lowest relative humidity this sensor can report       | Object with:<br>• `value`: 0<br>• `unitCode`: `%RH`   |
| **`measuringRangeMax`** | Property         | Highest relative humidity this sensor can report      | Object with:<br>• `value`: 100<br>• `unitCode`: `%RH` |
| **`accuracy`**          | Property         | Maximum deviation from true relative humidity         | Object with:<br>• `value`: 2<br>• `unitCode`: `%RH`   |
| **`resolution`**        | Property         | Granularity of the ADC conversion                     | Object with:<br>• `value`: 16<br>• `unitCode`: `bit`  |
| **`isComponentOf`**     | Relationship     | The Sense HAT B board this humidity sensor belongs to | Array of URIs (e.g. `["urn:ngsi-ld:SenseHATB:01"]`)   |

---

