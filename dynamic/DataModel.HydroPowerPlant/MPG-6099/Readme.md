# MPG-6099 Multi-Parameter Analyser Node
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/MPG-6099.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 700px">
</div>

## Definition

The **MPG-6099** is an IP65-rated, panel-mounted multiparameter controller and data-logger with a built-in 7″ capacitive touch LCD. It accepts 24 V DC or 220 V AC power, gathers sensor data over RS-485 Modbus RTU, and digitizes and timestamps all inputs for synchronized recording. Onboard memory stores measurements locally—downloadable via USB or an optional wireless modem—while the touchscreen interface provides real-time visualization and configuration. Its rugged enclosure and versatile I/O make it the central hub for aggregating, displaying, logging, and transmitting data from a diverse array of environmental and structural sensors.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attribute Specifications

| **Attribute**                   | **NGSI-LD Type** | **Description**                                         | **Units / Values**                                                 |
| ------------------------------- | ---------------- | ------------------------------------------------------- | ------------------------------------------------------------------ |
| **`id`**                        | Property         | Unique URI identifier                                   | URN format (e.g. `urn:ngsi-ld:MPG6099:01`)                         |
| **`type`**                      | Property         | Fixed NGSI-LD entity type                               | `MPG6099`                                                          |
| **`display`**                   | Property         | Local display type                                      | `"LCD 7 inch touch screen"`                                        |
| **`power`**                     | Property         | Supported power supplies                                | `"24 V DC or 220 V AC"`                                            |
| **`protection`**                | Property         | Enclosure protection rating                             | `"IP65"`                                                           |
| **`inputs`**                    | Property         | Input communication interface                           | `"RS-485 (Modbus RTU)"`                                            |
| **`output`**                    | Property         | Output communication interface                          | `"RS-485 (Modbus RTU)"`                                            |
| **`dataLogger`**                | Property         | Local data-logging capability                           | `true`                                                             |
| **`downloadInterface`**         | Property         | Interface for data export and firmware updates          | `"USB"`                                                            |
| **`wirelessOption`**            | Property         | Optional wireless modem availability                    | `true`                                                             |
| **`dimensions`**                | Property         | Physical dimensions                                     | Object with:<br>• `value`: \[320,270,121]<br>• `unitCode`: `"MMT"` |
| **`hasConductivityTempSensor`** | Relationship     | Reference to the conductivity/temperature sensor module | Array of URIs                                                      |
| **`hasPhTempSensor`**           | Relationship     | Reference to the pH/temperature sensor module           | Array of URIs                                                      |
| **`hasAmmoniaSensor`**          | Relationship     | Reference to the ammonia sensor module                  | Array of URIs                                                      |
| **`hasTurbiditySensor`**        | Relationship     | Reference to the turbidity sensor module                | Array of URIs                                                      |
| **`hasAlgaeSensor`**            | Relationship     | Reference to the algae sensor module                    | Array of URIs                                                      |
| **`hasDissolvedO2Sensor`**      | Relationship     | Reference to the dissolved oxygen sensor module         | Array of URIs                                                      |
