# Crack Growth Sensor

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/CrackGrowthSensor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>


## Definition

A **Crack-Growth (Strain) Sensor** is a precision resistive gauge housed in a flexible rubber casing that converts tiny structural deformations—such as those caused by a propagating crack—into changes in electrical resistance. It uses a four-wire (Kelvin) connection and a 16-bit ADC for high-resolution, low-noise readings, and integrates seamlessly with the platform’s other sensors for synchronized health monitoring.



> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.



## Attribute Specifications

| Attribute                | NGSI-LD Type | Required | Description                                                       | Units / Values                                                                                      |
| ------------------------ | ------------ | -------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **`monitoringType`**     | Property     | Yes      | Category of monitoring application for this sensor                | `"StructuralHealthAndConditionMonitoring"`, `"EnvironmentalMonitoring"`, `"BiodiversityMonitoring"` |
| **`adcResolution`**      | Property     | Yes      | Resolution of the ADC used for strain readings                    | Object with:<br>• `value`: integer (e.g. `16`)<br>• `unitCode`: `"bit"`                             |
| **`leadConfiguration`**  | Property     | Yes      | Lead-wiring method to minimize measurement errors                 | Object with:<br>• `value`: string (e.g. `"Four-wire (Kelvin)"`)<br>• `unitCode`: `""`               |
| **`hasMicrocontroller`** | Relationship | No       | Reference to the microcontroller that this sensor is connected to | Array of URIs (e.g. `["urn:ngsi-ld:Microcontroller:MCU-01"]`)                                       |


*For full list of inherited properties, see the [Device schema](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device).*
