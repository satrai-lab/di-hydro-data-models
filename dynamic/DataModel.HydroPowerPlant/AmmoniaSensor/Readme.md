## Ammonia Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/AmmoniaSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition
The **ammonia sensor** developed in the Di-Hydro project is an electrochemical device designed to measure the concentration of ammonia ions in water in real time. It uses a custom-made ion-selective membrane based on carbon nanotubes, which ensures high sensitivity and selectivity. This sensor is crucial for monitoring water quality in hydropower reservoirs, as elevated ammonia levels can indicate pollution from agricultural runoff or wastewater discharge and pose a threat to aquatic life. Its integration into the environmental monitoring system helps enable early detection of contamination and supports sustainable operation of hydropower plants.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attributes Specifications

| Attribute                | NGSI-LD Type | Description                                             | Units / Values                                    |
| ------------------------ | ------------ | ------------------------------------------------------- | ------------------------------------------------- |
| **`id`**                 | Property     | Unique URI identifier of the entity                     | URN format (e.g. `urn:ngsi-ld:AmmoniaSensor:001`) |
| **`type`**               | Property     | Fixed entity type                                       | `"AmmoniaSensor"`                                 |
| **`model`**              | Property     | Sensor model or sensing principle                       | `"Modified ion selective membrane"`               |
| **`ionsType`**           | Property     | Target ion species                                      | `"NH4"`                                           |
| **`rangeMin`**           | Property     | Lower bound of the measurement range                    | `{ "value": 15,  "unitCode": "PPB" }`             |
| **`rangeMax`**           | Property     | Upper bound of the measurement range                    | `{ "value": 150, "unitCode": "PPM" }`             |
| **`resolution`**         | Property     | Smallest detectable concentration increment             | `{ "value": 1,   "unitCode": "PPB" }`             |
| **`reactionTime`**       | Property     | Time to reach 90 % of final reading                     | `"<1 min"`                                        |
| **`accuracy`**           | Property     | Maximum deviation under standard conditions             | `"<±3 %"` at 20 °C                                |
| **`powerSupply`**        | Property     | Nominal DC supply voltage                               | `{ "value": 24,  "unitCode": "V" }`               |
| **`powerDissipation`**   | Property     | Maximum power consumption                               | `{ "value": 1,   "unitCode": "W" }`               |
| **`communicationMode`**  | Property     | Digital interface protocol                              | `"RS485 (Modbus RTU)"`                            |
| **`cableLength`**        | Property     | Standard probe cable length                             | `{ "value": 5,   "unitCode": "MTR" }`             |
| **`dimensionsLength`**   | Property     | Probe body length                                       | `{ "value": 250, "unitCode": "MMT" }`             |
| **`dimensionsDiameter`** | Property     | Probe body diameter                                     | `{ "value": 30,  "unitCode": "MMT" }`             |
| **`housingMaterial`**    | Property     | Wetted-part construction material                       | `"Stainless Steel + PVC"`                         |
| **`isComponentOf`**      | Relationship | Reference to the host multi-parameter node (`MPG-6099`) | `["urn:ngsi-ld:Device:MPG-6099"]`                 |


