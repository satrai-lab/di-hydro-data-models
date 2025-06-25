# Sense HAT B

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/SenseHatB.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 650px">
</div>

## Definition

The **Multi-Sensor Unit**—commonly referred to as **Sense HAT B**—is an integrated environmental sensor board designed for Raspberry Pi–based platforms. It provides synchronized measurements of temperature, humidity, pressure, acceleration, gyroscope, and magnetic field via a high-resolution analogue-to-digital converter, and streams them alongside other monitoring subsystems.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `controlledObservation`, `observations`, `controlledActuation`, `actuations`, `deviceType`, `relativePosition`, etc.), and adds the following board-specific attributes and relationships.


## Attribute Specifications

| **Attribute**                 | **NGSI-LD Type** | **Description**                                       | **Units / Values**                                                                   |
| ----------------------------- | ---------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **`operatingVoltage`**        | Property         | Supply voltage required by the board                  | Object with:<br>• `value`: 3.3<br>• `unitCode`: `"V"`                                |
| **`communicationInterface`**  | Property         | Bus used to communicate with the host microcontroller | String (e.g. `"I2C"`)                                                                |
| **`length`**                  | Property         | Physical length of the board                          | Object with:<br>• `value`: 65<br>• `unitCode`: `"MMT"` (mm)                          |
| **`width`**                   | Property         | Physical width of the board                           | Object with:<br>• `value`: 36.5<br>• `unitCode`: `"MMT"` (mm)                        |
| **`adcConversionResolution`** | Property         | Resolution of the analogue-to-digital conversion chip | Object with:<br>• `value`: 16<br>• `unitCode`: `"bit"`                               |
| **`isComponentOf`**           | Relationship     | Host microcontroller that this board plugs into       | Array of URIs (e.g. `["urn:ngsi-ld:Microcontroller:pi1"]`)                           |
| **`hasHumiditySensor`**       | Relationship     | Onboard humidity sensor module                        | URI of the humidity-sensor entity (e.g. `"urn:ngsi-ld:HumiditySensor:hs1"`)          |
| **`hasGyroscope`**            | Relationship     | Onboard 3-axis gyroscope module                       | URI of the gyroscope-sensor entity (e.g. `"urn:ngsi-ld:GyroscopeSensor:g1"`)         |
| **`hasMagnetometer`**         | Relationship     | Onboard 3-axis magnetometer module                    | URI of the magnetometer-sensor entity (e.g. `"urn:ngsi-ld:MagnetometerSensor:m1"`)   |
| **`hasTemperatureSensor`**    | Relationship     | Onboard temperature sensor module                     | URI of the temperature-sensor entity (e.g. `"urn:ngsi-ld:TemperatureSensor:t1"`)     |
| **`hasConversion`**           | Relationship     | Analogue-to-digital conversion chip                   | URI of the ADC-conversion-chip entity (e.g. `"urn:ngsi-ld:ADCChip:adc1"`)            |
| **`hasBarometer`**            | Relationship     | Onboard barometric pressure sensor module             | URI of the barometer-sensor entity (e.g. `"urn:ngsi-ld:BarometerSensor:b1"`)         |
| **`hasAccelerometer`**        | Relationship     | Onboard 3-axis accelerometer module                   | URI of the accelerometer-sensor entity (e.g. `"urn:ngsi-ld:AccelerometerSensor:a1"`) |

---

*For the full list of inherited properties, see the [Device schema](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device).*
