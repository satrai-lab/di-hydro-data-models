# Conductivity-Temperature Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/ConductivityTempSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **Digital Conductivity–Temperature Sensor** is a four-wire, DC-powered probe that simultaneously measures water electrical conductivity and temperature. It integrates temperature compensation and onboard analog-to-digital conversion, and communicates readings over a digital interface (e.g. Modbus RTU) for reliable, real-time water-quality monitoring.
> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attributes

| Attribute                    | NGSI-LD Type | Description                                             | Units / Values                         |
| ---------------------------- | ------------ | ------------------------------------------------------- | -------------------------------------- |
| **`model`**                  | Property     | Manufacturer’s model number                             | `"BH-485-DD"`                          |
| **`conductivityRangeMin`**   | Property     | Minimum conductivity                                    | `{ "value": 0,    "unitCode": "USC" }` |
| **`conductivityRangeMax`**   | Property     | Maximum conductivity                                    | `{ "value": 2000, "unitCode": "USC" }` |
| **`temperatureRangeMin`**    | Property     | Minimum temperature                                     | `{ "value": 0,    "unitCode": "CEL" }` |
| **`temperatureRangeMax`**    | Property     | Maximum temperature                                     | `{ "value": 50,   "unitCode": "CEL" }` |
| **`accuracyConductivity`**   | Property     | Conductivity measurement error                          | `±20 USC`                              |
| **`accuracyTemperature`**    | Property     | Temperature measurement error                           | `±0.5 CEL`                             |
| **`reactionTime`**           | Property     | Time to 90 % of final reading                           | `< 60 s`                               |
| **`resolutionConductivity`** | Property     | Conductivity granularity                                | `1 USC`                                |
| **`resolutionTemperature`**  | Property     | Temperature granularity                                 | `0.1 CEL`                              |
| **`powerSupplyMin`**         | Property     | Minimum DC supply voltage                               | `{ "value": 9,    "unitCode": "V" }`   |
| **`powerSupplyMax`**         | Property     | Maximum DC supply voltage                               | `{ "value": 36,   "unitCode": "V" }`   |
| **`powerDissipation`**       | Property     | Typical power draw                                      | `1 W`                                  |
| **`communicationMode`**      | Property     | Field-bus interface                                     | `"RS485 (Modbus RTU)"`                 |
| **`cableLength`**            | Property     | Standard cable length                                   | `{ "value": 5,    "unitCode": "MTR" }` |
| **`sizeLength`**             | Property     | Body length                                             | `{ "value": 230,  "unitCode": "MMT" }` |
| **`sizeDiameter`**           | Property     | Body diameter                                           | `{ "value": 30,   "unitCode": "MMT" }` |
| **`housingMaterial`**        | Property     | Wetted-part construction                                | `"Stainless Steel + PVC"`              |
| **`isComponentOf`**          | Relationship | Reference to the host **MPG-6099** multi-parameter node | `["urn:ngsi-ld:Device:MPG-6099"]`      |


