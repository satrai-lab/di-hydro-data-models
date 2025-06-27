## Portable Multiparametric Platform (“Suitcase”)
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Suitcase.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 650px">
</div>

## Definition

A **Portable Multiparametric Platform**, also referred to as the **Suitcase**, is a field-ready monitoring system developed in the Di-Hydro project for on-site biodiversity and water-quality assessment. Housed in a rugged, waterproof suitcase, it integrates a digital holographic microscope (DHM), a fluorescence-based pathogen sensor, and a turbidity sensor, allowing detailed analysis of microbial and algal content in water samples. Designed for portability and ease of use, the platform enables real-time, high-resolution monitoring of key biological indicators like algae and *E.coli* directly at hydropower sites, supporting early detection of ecological changes and enhancing environmental management.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attribute Specifications

| Attribute                | NGSI-LD Type | Description                                                          | Units / Values                                      |
| ------------------------ | ------------ | -------------------------------------------------------------------- | --------------------------------------------------- |
| **`id`**                 | Property     | Unique URI identifier of the Portable Suitcase Node                  | URN format (e.g. `urn:ngsi-ld:Suitcase:01`)         |
| **`type`**               | Property     | Fixed entity type                                                    | `"Suitcase"`                                        |
| **`dimensions`**         | Property     | External case dimensions \[length, width, height]                    | `{ "value": [500, 400, 200], "unitCode": "MMT" }`   |
| **`weight`**             | Property     | Total system mass                                                    | `{ "value": 7, "unitCode": "KGM" }` (approximate)   |
| **`powerSupply`**        | Property     | On-board battery capacity                                            | `{ "value": 20, "unitCode": "AHT" }` (12 V @ 20 Ah) |
| **`operatingTime`**      | Property     | Maximum autonomous runtime                                           | `"10 hours"`                                        |
| **`connectivity`**       | Property     | Data communication interfaces                                        | `["Wi-Fi","Bluetooth","USB","RS485"]`               |
| **`display`**            | Property     | Integrated human–machine interface                                   | `"Touchscreen"`                                     |
| **`protection`**         | Property     | Environmental rating of the enclosure                                | `"IP67"`                                            |
| **`dataStorage`**        | Property     | On-board data logging capacity                                       | `"1 month continuous"`                              |
| **`hasTurbiditySensor`** | Relationship | References to connected Turbidity Sensor modules                     | `["urn:ngsi-ld:TurbiditySensor:01"]`                |
| **`hasDhm`**             | Relationship | Reference to the onboard Digital Holographic Microscope (DHM) module | `["urn:ngsi-ld:DHMModule:01"]`                      |
| **`hasMicrocontroller`** | Relationship | References to host microcontroller(s)                                | `["urn:ngsi-ld:Microcontroller:pi1"]`               |
| **`hasTlfSensor`**       | Relationship | References to connected Turbulence Flow Sensor(s)                    | `["urn:ngsi-ld:TlfSensor:01"]`                      |
