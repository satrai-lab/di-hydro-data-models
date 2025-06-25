# Microcontroller

## Definition

A **Microcontroller** is a programmable computing unit that interfaces with sensors and actuators within a hydropower‐plant monitoring system. It hosts Analog-to-Digital Converters (ADCs), communication buses, and power interfaces, and can be a component of larger platforms or portable data‐acquisition modules.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `controlledObservation`, `observations`, `controlledActuation`, `actuations`, `deviceType`, `relativePosition`, etc.). It then adds the following microcontroller-specific attributes.


## Attribute Specifications

| **Attribute**                 | **NGSI-LD Type** | **Description**                                                                                                      | **Units / Values**                                                        |
| ----------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **`microcontrollerType`**     | Property         | Role or family of this controller (e.g., board/CPU type)                                                             | String (e.g. `"RaspberryPi"`, `"EmbeddedControlPC"`)                      |
| **`processor`**               | Property         | Name/model of the CPU or System-on-Chip                                                                              | String (e.g. `"Broadcom BCM2837"`, `"Intel Atom x7"`)                     |
| **`memory`**                  | Property         | Installed RAM capacity                                                                                               | Object with:<br>• `value`: number<br>• `unitCode`: `"GBA"` (gigabytes)    |
| **`storage`**                 | Property         | Local non-volatile storage size                                                                                      | Object with:<br>• `value`: number<br>• `unitCode`: `"GBA"` (gigabytes)    |
| **`adcResolution`**           | Property         | Resolution of the on-board ADC used for analog sensor inputs                                                         | Object with:<br>• `value`: integer<br>• `unitCode`: `"bit"`               |
| **`adcChannels`**             | Property         | Number of independent ADC input channels available                                                                   | Object with:<br>• `value`: integer<br>• `unitCode`: `""`                  |
| **`interfaces`**              | Property         | List of I/O and communication buses exposed by this controller                                                       | Array of strings (e.g. `["GPIO","I2C","SPI","USB3.0","Ethernet","WiFi"]`) |
| **`powerInternal`**           | Property         | Capacity of the internal battery pack                                                                                | Object with:<br>• `value`: number<br>• `unitCode`: `"Wh"` (watt-hours)    |
| **`powerExternalVoltage`**    | Property         | Nominal voltage of the external DC power input                                                                       | Object with:<br>• `value`: number<br>• `unitCode`: `"V"`                  |
| **`operatingTemperatureMin`** | Property         | Minimum ambient temperature at which the controller is rated to operate                                              | Object with:<br>• `value`: number<br>• `unitCode`: `"CEL"` (°C)           |
| **`operatingTemperatureMax`** | Property         | Maximum ambient temperature at which the controller is rated to operate                                              | Object with:<br>• `value`: number<br>• `unitCode`: `"CEL"` (°C)           |
| **`hasDevices`**              | Relationship     | References to all **Device** entities (sensors, actuators, etc.) directly connected to this microcontroller          | Array of URIs (e.g. `["urn:ngsi-ld:AEPZTSensor:001", …]`)                 |
| **`hasComponents`**           | Relationship     | References to component modules or sub-devices that this microcontroller hosts (e.g., Sense HAT, AE-DAQ interface)   | Array of URIs (e.g. `["urn:ngsi-ld:SensorModule:shb1", …]`)               |
| **`isComponentOf`**           | Relationship     | References to higher-level systems or platforms that this microcontroller is part of (e.g., a portable DAQ platform) | Array of URIs (e.g. `["urn:ngsi-ld:Platform:PortableDAQ-01"]`)            |


*For more on Device inheritance, see the [Device schema](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device`).*
