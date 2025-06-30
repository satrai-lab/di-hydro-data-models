# Camera
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/camera.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 200px">
</div>

## **Definition**
The **Camera** is a high-resolution industrial imaging device used to capture detailed visual data. It integrates with the DHM system, converting optical signals into digital images for analysis.

---

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attribute Specifications

| **Attribute**             | **NGSI-LD Type** | **Required** | **Description**                               | **Units / Values**                                                                 |
| ------------------------- | ---------------- | ------------ | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| **`id`**                  | Property         | Yes          | Unique URI identifier for the camera          | URN format, e.g. `urn:ngsi-ld:Camera:001`                                          |
| **`type`**                | Property         | Yes          | Fixed entity type                             | `"Camera"`                                                                         |
| **`model`**               | Property         | No           | Camera model                                  | e.g. `"IDS U3-3990CP-M-GL_Rev_2_2"`                                                |
| **`sensorResolution`**    | Property         | No           | Maximum image resolution                      | Array of two integers, e.g. `[4512, 4512]` (pixels)                                |
| **`pixelSize`**           | Property         | No           | Size of each photosite                        | Object `{ value: number, unitCode: "UM" }`, e.g. `{ value: 2.74, unitCode: "UM" }` |
| **`acquisitionSoftware`** | Property         | No           | Software used for image capture               | e.g. `"IDS Peak"`                                                                  |
| **`status`**              | Property         | No           | Operational status of the camera              | e.g. `"operational"`                                                               |
| **`isComponentOf`**       | Relationship     | No           | Reference to the DHM entity this camera feeds | Array of URIs, e.g. `["urn:ngsi-ld:DHM:001"]`                                      |
