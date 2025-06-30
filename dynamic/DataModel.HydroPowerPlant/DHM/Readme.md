# Digital Holographic Microscope (DHM)
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/DHM.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 700px">
</div>

## Definition
The **Digital Holographic Microscope (DHM)** is an inline imaging module that captures high-resolution interference patterns of samples by splitting a coherent laser beam and recombining it after interaction with the specimen. The resulting hologram encodes both amplitude and phase information, enabling rapid, label-free quantitative analysis of microscopic features without physical sectioning or staining. This non-contact technique supports real-time monitoring in harsh or fluid environments.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attribute Specifications

| Attribute                               | NGSI-LD Type | Description                                                 | Units / Values                                             |
| --------------------------------------- | ------------ | ----------------------------------------------------------- | ---------------------------------------------------------- |
| **`id`**                                | Property     | Unique URI identifier of the DHM entity                     | URN format (e.g. `urn:ngsi-ld:DHM:001`)                    |
| **`type`**                              | Property     | Fixed NGSI-LD entity type                                   | `"DHM"`                                                    |
| **`laserSource.value`**                 | Property     | Laser source model                                          | e.g. `"Cobolt Samba™"`                                     |
| **`laserSource.waveLength`**            | Property     | Emitted laser wavelength                                    | number; unitCode: `"NM"`                                   |
| **`beamExpander`**                      | Property     | Magnification factor of the beam expander                   | number; unitCode: `"C62"`                                  |
| **`microscopeObjective.value`**         | Property     | Objective model                                             | e.g. `"Olympus PLN10XCY"`                                  |
| **`microscopeObjective.magnification`** | Property     | Objective magnification                                     | number; unitCode: `"C62"`                                  |
| **`resolutionAchieved`**                | Property     | Lateral resolution achieved in imaging                      | number; unitCode: `"MM"`                                   |
| **`interferencePattern`**               | Property     | Typical fringe spacing in interference patterns             | number; unitCode: `"UM"`                                   |
| **`status`**                            | Property     | Operational status of the DHM                               | e.g. `"operational"`                                       |
| **`hasCamera`**                         | Relationship | References to the associated camera module                  | Array of URIs (e.g. `["urn:ngsi-ld:Camera:cam1"]`)         |
| **`hasMicrocontroller`**                | Relationship | References to the host microcontroller driving this DHM     | Array of URIs (e.g. `["urn:ngsi-ld:Microcontroller:pi1"]`) |
| **`isComponentOf`**                     | Relationship | References to the **Suitcase** platform this DHM belongs to | Array of URIs (e.g. `["urn:ngsi-ld:Suitcase:01"]`)         |
