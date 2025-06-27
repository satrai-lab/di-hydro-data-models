## Tryptophan-Like Fluorescence (TLF) Pathogen Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/TLFSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 700px">
</div>

## Definition

The **Tryptophan-Like Fluorescence (TLF) Pathogen Sensor** is a sensitive optical device designed to detect microbial contamination in water by measuring the natural fluorescence of tryptophan, an amino acid commonly found in bacterial cells. When exposed to ultraviolet (UV) light, tryptophan emits a specific fluorescent signal, which the sensor captures to estimate the presence and concentration of bacteria like *E. coli*. This non-invasive, rapid method allows for real-time monitoring of water quality, making it especially useful for environmental and public health applications.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attribute Specifications

| Attribute                | NGSI-LD Type | Description                                                        | Units / Values                                             |
| ------------------------ | ------------ | ------------------------------------------------------------------ | ---------------------------------------------------------- |
| **`id`**                 | Property     | Unique URI identifier of the TLF sensor                            | URN format (e.g. `urn:ngsi-ld:TlfSensor:01`)               |
| **`type`**               | Property     | Fixed entity type                                                  | `"TlfSensor"`                                              |
| **`hasMicrocontroller`** | Relationship | Reference to the host microcontroller driving this sensor          | Array of URIs (e.g. `["urn:ngsi-ld:Microcontroller:pi1"]`) |
| **`isComponentOf`**      | Relationship | Reference to the **Suitcase** platform that this sensor belongs to | Array of URIs (e.g. `["urn:ngsi-ld:Suitcase:01"]`)         |
