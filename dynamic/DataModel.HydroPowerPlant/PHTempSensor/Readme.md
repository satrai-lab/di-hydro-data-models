# Digital pH–Temperature Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/PHTempSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 450px">
</div>

## Definition

A **Digital pH–Temperature Sensor** is an industrial-grade probe featuring an electrochemical electrode with built-in temperature compensation and onboard ADC. It streams synchronized pH and temperature measurements over a robust serial link (e.g., RS-485), supports remote configuration/calibration, and is engineered for long-term, low-maintenance water-quality monitoring.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.

## Attributes Specifications

| Attribute                   | NGSI-LD Type | Description                                             | Units / Values                                          |
| --------------------------- | ------------ | ------------------------------------------------------- | ------------------------------------------------------- |
| **`id`**                    | Property     | Unique URI identifier of the entity                     | URN format (e.g. `urn:ngsi-ld:DigitalPHTempSensor:001`) |
| **`type`**                  | Property     | Fixed entity type                                       | `"DigitalPHTempSensor"`                                 |
| **`model`**                 | Property     | Manufacturer’s model number                             | e.g. `"IOT-485-PH"`                                     |
| **`pHRangeMin`**            | Property     | Minimum pH measurable                                   | `{ "value": 0.0,  "unitCode": "" }`                     |
| **`pHRangeMax`**            | Property     | Maximum pH measurable                                   | `{ "value": 14.0, "unitCode": "" }`                     |
| **`temperatureRangeMin`**   | Property     | Minimum temperature measurable                          | `{ "value": 0.0,  "unitCode": "CEL" }`                  |
| **`temperatureRangeMax`**   | Property     | Maximum temperature measurable                          | `{ "value": 50.0, "unitCode": "CEL" }`                  |
| **`accuracyPH`**            | Property     | pH measurement accuracy                                 | `±0.1 pH`                                               |
| **`accuracyTemperature`**   | Property     | Temperature measurement accuracy                        | `±0.5 °C`                                               |
| **`resolutionPH`**          | Property     | pH reading granularity                                  | `0.01 pH`                                               |
| **`resolutionTemperature`** | Property     | Temperature reading granularity                         | `0.1 °C`                                                |
| **`powerSupplyMin`**        | Property     | Minimum DC supply voltage                               | `{ "value": 9,  "unitCode": "V" }`                      |
| **`powerSupplyMax`**        | Property     | Maximum DC supply voltage                               | `{ "value": 36, "unitCode": "V" }`                      |
| **`powerDissipation`**      | Property     | Typical power draw                                      | `1 W`                                                   |
| **`communicationMode`**     | Property     | Digital interface protocol                              | `"RS485 (Modbus RTU)"`                                  |
| **`cableLength`**           | Property     | Standard cable length                                   | `{ "value": 10, "unitCode": "MTR" }`                    |
| **`sizeLength`**            | Property     | Probe body length                                       | `{ "value": 230, "unitCode": "MMT" }`                   |
| **`sizeDiameter`**          | Property     | Probe body diameter                                     | `{ "value": 30,  "unitCode": "MMT" }`                   |
| **`housingMaterial`**       | Property     | Wetted-part construction material                       | `"Stainless Steel + ABS"`                               |
| **`protectionGrade`**       | Property     | Ingress protection rating                               | `"IP68"`                                                |
| **`isComponentOf`**         | Relationship | Reference to the host **MPG-6099** multi-parameter node | `["urn:ngsi-ld:Device:MPG-6099"]`                       |


