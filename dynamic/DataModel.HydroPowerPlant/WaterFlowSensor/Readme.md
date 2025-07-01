## Water Flow Sensor (μVTX-2.1)

### Definition

A **Water Flow Sensor** is a compact, autonomous hydrological monitoring station designed for non-invasive measurement of river surface height, flow velocity, and water temperature. Installed above the watercourse (e.g., under a bridge), it combines LiDAR, infrared, and thermal imaging to capture real-time hydrological and visual data, transmitting it over mobile networks for downstream analysis and model validation.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.

### Attribute Specifications

| **Attribute**                  | **NGSI-LD Type** | **Description**                            | **Units / Values**                                               |
| ------------------------------ | ---------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| **`id`**                       | Identifier       | Unique URI identifier of this sensor       | URN format (e.g. `urn:ngsi-ld:WaterFlowSensor:uvtx21`)           |
| **`type`**                     | Type             | Fixed NGSI-LD entity type                  | `"WaterFlowSensor"`                                              |
| **`measurementType`**          | Property         | Sensing modality                           | `"remote"` (non-invasive, above-water)                           |
| **`waterHeightAccuracy`**      | Property         | Accuracy of surface-height measurement     | `{ value: number, unitCode: "CM" }` (e.g. `{±1,"CM"}`)           |
| **`imagingComponents`**        | Property         | On-board imaging sensors                   | Array of strings: `["LiDAR","infrared","thermal","nightVision"]` |
| **`communication`**            | Property         | Data transmission interface                | `"3G/4G mobile"`                                                 |
| **`powerSource`**              | Property         | Energy supply                              | Array of strings: `["battery","solarPanel"]`                     |
| **`realTimeAlerts`**           | Property         | Threshold-triggered acquisition capability | `"yes"` / `"no"`                                                 |
| **`fieldOfView`**              | Property         | Camera field of view                       | `{ value: number, unitCode: "DEG" }` (e.g. `{130,"DEG"}`)        |
| **`dataOutputs`**              | Property         | Types of data produced                     | Array of strings: `["hydrology","images","videos"]`              |
| **`installationRequirements`** | Property         | Mounting instructions                      | `"above water under bridge"`                                     |

