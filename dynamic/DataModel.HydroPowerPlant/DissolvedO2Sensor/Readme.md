## Dissolved Oxygen Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/DissolvedO2Sensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

The **digital dissolved oxygen sensor** used in the Di-Hydro project is an electrochemical sensor designed to measure the concentration of oxygen dissolved in water accurately and in real time. It plays a vital role in assessing water quality in hydropower reservoirs, as dissolved oxygen is essential for the survival of aquatic organisms and reflects the ecological health of the ecosystem. The sensor operates using RS485 communication, is resistant to interference, and provides stable, low-maintenance performance, making it suitable for continuous environmental monitoring and early detection of conditions that could lead to oxygen depletion or ecosystem stress.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attributes

| Attribute                | NGSI-LD Type | Description                                             | Units / Values                                        |
| ------------------------ | ------------ | ------------------------------------------------------- | ----------------------------------------------------- |
| **`id`**                 | Property     | Unique URI identifier of the entity                     | URN format (e.g. `urn:ngsi-ld:DissolvedO2Sensor:001`) |
| **`type`**               | Property     | Fixed entity type                                       | `"DissolvedO2Sensor"`                                 |
| **`rangeO2Min`**         | Property     | Minimum dissolved-O₂ concentration                      | `{ "value": 0, "unitCode": "MG_L" }`                  |
| **`rangeO2Max`**         | Property     | Maximum dissolved-O₂ concentration                      | `{ "value": 20.0, "unitCode": "MG_L" }`               |
| **`rangeTempMin`**       | Property     | Minimum temperature                                     | `{ "value": 0, "unitCode": "CEL" }`                   |
| **`rangeTempMax`**       | Property     | Maximum temperature                                     | `{ "value": 50, "unitCode": "CEL" }`                  |
| **`basicError`**         | Property     | Maximum measurement error                               | `{ "value": 0.30, "unitCode": "MG_L" }`               |
| **`reactionTime`**       | Property     | Time to reach 90% of final reading                      | `"<60 s"`                                             |
| **`resolutionO2`**       | Property     | Smallest detectable change in dissolved-O₂              | `{ "value": 0.01, "unitCode": "MG_L" }`               |
| **`resolutionTemp`**     | Property     | Smallest detectable change in temperature               | `{ "value": 0.1, "unitCode": "CEL" }`                 |
| **`powerSupply`**        | Property     | Nominal DC supply voltage                               | `{ "value": 24, "unitCode": "V" }`                    |
| **`powerDissipation`**   | Property     | Maximum power consumption                               | `{ "value": 1, "unitCode": "W" }`                     |
| **`communicationMode`**  | Property     | Digital interface protocol                              | `"RS485 (Modbus RTU)"`                                |
| **`cableLength`**        | Property     | Standard probe cable length                             | `{ "value": 5, "unitCode": "MTR" }`                   |
| **`dimensionsLength`**   | Property     | Probe body length                                       | `{ "value": 230, "unitCode": "MMT" }`                 |
| **`dimensionsDiameter`** | Property     | Probe body diameter                                     | `{ "value": 30, "unitCode": "MMT" }`                  |
| **`housingMaterial`**    | Property     | Wetted-part construction material                       | `"Stainless Steel + PVC"`                             |
| **`isComponentOf`**      | Relationship | Reference to the host multi-parameter node (`MPG-6099`) | `["urn:ngsi-ld:Device:MPG-6099"]`                     |


