# Algae Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/AlgaeSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

An **Algae Sensor** is an optical device that measures chlorophyll-a fluorescence to detect and quantify algal biomass in water. By exciting chlorophyll molecules with a light source and capturing the emitted fluorescence, it provides real-time, non-invasive monitoring of algae concentrations—critical for early detection of harmful blooms, prevention of equipment fouling, and maintenance of water quality in hydropower reservoirs.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.

## Attributes Specifications

| Attribute                | NGSI-LD Type | Description                                             | Units / Values                                  |
| ------------------------ | ------------ | ------------------------------------------------------- | ----------------------------------------------- |
| **`id`**                 | Property     | Unique URI identifier of the entity                     | URN format (e.g. `urn:ngsi-ld:AlgaeSensor:001`) |
| **`type`**               | Property     | Fixed entity type                                       | `"AlgaeSensor"`                                 |
| **`model`**              | Property     | Sensor model or sensing principle                       | `"Modified ion selective membrane"`             |
| **`linearRangeMin`**     | Property     | Lower bound of the linear chlorophyll-a range           | `{ "value": 5,   "unitCode": "UG_L" }`          |
| **`linearRangeMax`**     | Property     | Upper bound of the linear chlorophyll-a range           | `{ "value": 300, "unitCode": "UG_L" }`          |
| **`totalRangeMin`**      | Property     | Lower bound of the total chlorophyll-a range            | `{ "value": 2,   "unitCode": "UG_L" }`          |
| **`totalRangeMax`**      | Property     | Upper bound of the total chlorophyll-a range            | `{ "value": 500, "unitCode": "UG_L" }`          |
| **`resolution`**         | Property     | Measurement granularity                                 | `{ "value": 2,   "unitCode": "UG_L" }`          |
| **`reactionTime`**       | Property     | Time to reach 90 % of final reading                     | `"<1 s"`                                        |
| **`accuracy`**           | Property     | Maximum deviation under standard conditions             | `"<±5 % at 20 °C"`                              |
| **`communicationMode`**  | Property     | Digital interface protocol                              | `"RS485 (Modbus RTU)"`                          |
| **`cableLength`**        | Property     | Standard probe cable length                             | `{ "value": 5,   "unitCode": "MTR" }`           |
| **`operationalTempMin`** | Property     | Minimum operating temperature                           | `{ "value": 0,   "unitCode": "CEL" }`           |
| **`operationalTempMax`** | Property     | Maximum operating temperature                           | `{ "value": 25,  "unitCode": "CEL" }`           |
| **`dimensionsLength`**   | Property     | Probe body length                                       | `{ "value": 395, "unitCode": "MMT" }`           |
| **`dimensionsDiameter`** | Property     | Probe body diameter                                     | `{ "value": 25,  "unitCode": "MMT" }`           |
| **`protectionClass`**    | Property     | Ingress protection rating                               | `"IP68"`                                        |
| **`housingMaterial`**    | Property     | Wetted-part construction material                       | `"Stainless Steel + PVC"`                       |
| **`isComponentOf`**      | Relationship | Reference to the host **MPG-6099** multi-parameter node | `["urn:ngsi-ld:Device:MPG-6099"]`               |


