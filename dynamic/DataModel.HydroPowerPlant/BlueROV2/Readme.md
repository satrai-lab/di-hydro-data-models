# BlueROV2

## Definition

The **BlueROV2** is a remotely operated underwater vehicle (ROV) used in the Di-Hydro project to perform remote inspections of hydropower infrastructure. It provides a mobile platform for visual assessment of submerged components, detection of damage and biofouling, and identification of foreign objects. The ROV can be equipped with various cameras and sensors and supports advanced analytics (e.g., machine-learning-based damage detection).
**Inherits** all core properties and relationships from the **Device** entity.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.

### Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                  | **Units / Values**                                                          |
| ----------------------- | ---------------- | ------------------------------------------------ | --------------------------------------------------------------------------- |
| **`id`**            | Property         | Unique URI identifier of this ADC conversion chip | URN format (e.g. `urn:ngsi-ld:ADCChip:adc1`)         |
| **`type`**          | Property         | Fixed NGSI-LD entity type                         | `BlueROV2`                                            |
| `thrustersNumbers`      | Property         | Number of thruster units installed               | Integer (e.g. `8`)                                                          |
| `thrustersModel`        | Property         | Model identifier of each thruster                | String (e.g. `"T200"`)                                                      |
| `directions`            | Property         | Degrees-of-freedom (motion axes)                 | Array of strings: `["surge","sway","heave","roll","pitch","yaw"]`           |
| `maxForwardThrust`      | Property         | Maximum continuous forward thrust                | `{ value: number, unitCode: "N" }` (e.g. `{40, "N"}`)                       |
| `topSpeed`              | Property         | Maximum forward speed                            | `{ value: number, unitCode: "m/s" }` (e.g. `{2.0, "m/s"}`)                  |
| `weightInAir`           | Property         | Vehicle weight (including battery)               | `{ value: number, unitCode: "KGM" }` or `{ value: number, unitCode: "LB" }` |
| `batteryVoltage`        | Property         | Nominal pack voltage                             | `{ value: number, unitCode: "V" }` (e.g. `{14.8, "V"}`)                     |
| `batteryCapacity`       | Property         | Pack capacity                                    | `{ value: number, unitCode: "AH" }` (e.g. `{18, "AH"}`)                     |
| `batteryConfiguration`  | Property         | Cell arrangement                                 | String (e.g. `"4S×6P"`)                                                     |
| `runtimeMin`            | Property         | Minimum expected mission duration                | `{ value: number, unitCode: "h" }` (e.g. `{1.0, "h"}`)                      |
| `runtimeMax`            | Property         | Maximum expected mission duration                | `{ value: number, unitCode: "h" }` (e.g. `{4.0, "h"}`)                      |
| `numberOfLEDs`          | Property         | Number of onboard adjustable-brightness LED bars | Integer (e.g. `2`; up to `4` optional)                                      |
| `LEDType`               | Property         | LED light bar output                             | String (e.g. `"1500-lumen"`)                                                |
| `cameraResolution`      | Property         | Main camera imaging resolution                   | String (e.g. `"1080p"`)                                                     |
| `cameraFrameRate`       | Property         | Main camera maximum frame rate                   | `{ value: number, unitCode: "fps" }` (e.g. `{30, "fps"}`)                   |
| `cameraLowLightCapable` | Property         | Whether main camera supports low-light operation | Boolean-string (e.g. `"yes"` / `"no"`)                                      |
| `cameraMount`           | Property         | Mount type/mechanism for the main camera         | String (e.g. `"servo tilt"`)                                                |
| `cameraEncoding`        | Property         | Live-stream encoding format                      | String (e.g. `"H.264"`)                                                     |
| `depthPressureSensor`   | Property         | Depth/pressure sensor model                      | String (e.g. `"Bar30"`)                                                     |
| `imuComponents`         | Property         | Built-in IMU components                          | Array of strings: `["gyro","accel","mag"]`                                  |
| `optionalGPS`           | Property         | Whether GPS/compass is present                   | Boolean-string (e.g. `"optional"`)                                          |
| `commLinkType`          | Property         | Data/video tether physical medium                | String (e.g. `"Ethernet"`)                                                  |
| `commBandwidth`         | Property         | Data/video tether bandwidth                      | `{ value: number, unitCode: "Mb/s" }` (e.g. `{100, "Mb/s"}`)                |
| `commRange`             | Property         | Maximum tether length                            | `{ value: number, unitCode: "m" }` (e.g. `{300, "m"}`)                      |
| `payloadCapacity`       | Property         | Spare buoyancy payload capacity                  | `{ value: number, unitCode: "KGM" }` (e.g. `{1.5, "KGM"}`)                  |

