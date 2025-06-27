## E.coli Biosensor

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/EcoliBioSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 300px">
</div>

## Definition 

The **E.coli biosensor** is a portable, single-use electrochemical sensor designed to detect the presence and concentration of *Escherichia coli* bacteria in water samples. It uses a three-electrode system with a gold surface functionalized by aptamers that specifically bind to E.coli, enabling highly selective and sensitive detection. This biosensor is crucial for microbial water quality assessment in hydropower reservoirs, as E.coli is a key indicator of fecal contamination. Its rapid detection capability supports early warning systems, helping prevent public health risks and ensuring compliance with environmental safety standards.


> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attributes Specifications

| Attribute              | NGSI-LD Type | Description                                                    | Units / Values                                    |
| ---------------------- | ------------ | -------------------------------------------------------------- | ------------------------------------------------- |
| **`id`**               | Property     | Unique URI identifier of the entity                            | URN format (e.g. `urn:ngsi-ld:EcoliBioSensor:01`) |
| **`type`**             | Property     | Fixed entity type                                              | `"EcoliBioSensor"`                                |
| **`measureRangeMin`**  | Property     | Lower bound of detection range                                 | `{ "value": 1, "unitCode": "CFU/mL" }`            |
| **`measureRangeMax`**  | Property     | Upper bound of detection range                                 | `{ "value": 5, "unitCode": "CFU/mL" }`            |
| **`measurementTime`**  | Property     | Time required to obtain a reading                              | `"20 min incubation"`                             |
| **`accuracy`**         | Property     | Maximum deviation from true count                              | `"< ±20 %"`                                       |
| **`sizeLength`**       | Property     | Overall sensor length                                          | `{ "value": 20, "unitCode": "MMT" }`              |
| **`sizeWidth`**        | Property     | Overall sensor width                                           | `{ "value": 35, "unitCode": "MMT" }`              |
| **`material`**         | Property     | Wetted-part construction material                              | `"Gold + PVC"`                                    |
| **`limitOfDetection`** | Property     | Smallest reliably detectable concentration                     | `"1 CFU/mL"`                                      |
| **`specificity`**      | Property     | Describes false-positive behavior                              | `"No positive response"`                          |
| **`isComponentOf`**    | Relationship | Reference to the host multi-parameter analyser node (MPG-6099) | `["urn:ngsi-ld:Device:MPG-6099"]`                 |
