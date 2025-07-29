# Generator
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Generator.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 600px">
</div>

## Definition
A **Generator** is the core electrical component in hydropower plants that converts mechanical energy from turbines into electrical energy. It consists of rotating electromagnets (rotor) and stationary coils (stator) that produce alternating current through electromagnetic induction.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.

## Attributes Specifications


| Attribute                       | Type         | Required | Description                                                                                 | Units/Values                           |
| ------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------- | -------------------------------------- |
| **`id`**                        | Property     | Yes      | Unique URI identifier                                                                       | URN format                             |
| **`type`**                      | Property     | Yes      | Fixed entity type                                                                           | `"Generator"`                          |
| **`name`**                      | Property     | Yes      | Official/Common name                                                                        | String                                 |
| **`generatorModel`**            | Property     | No       | Specific model identifier of the generator                                                  | String                                 |
| **`ratedCapacity`**             | Property     | No       | Maximum power output the generator is designed to produce under normal operating conditions | MW                                     |
| **`efficiency`**                | Property     | No       | Conversion efficiency of the generator                                                      | PCT                                    |
| **`manufacturer`**              | Property     | No       | Name or details of the generator’s manufacturer                                             | String                                 |
| **`yearOfInstallation`**        | Property     | No       | Year the generator was installed                                                            | Integer                                |
| **`generatorType`**             | Property     | No       | Model or design identifier of the generator                                                 | String                                 |
| **`axis`**                      | Property     | No       | Orientation of the rotating shaft                                                           | `Horizontal` / `Vertical`              |
| **`voltageLevel`**              | Property     | No       | Voltage at which the generator produces electricity                                         | kV                                     |
| **`connectionToGrid`**          | Property     | No       | Voltage level at which the generator is connected to the electrical grid                    | kV                                     |
| **`ratedOutputMVA`**            | Property     | No       | Apparent power capacity under standard conditions                                           | MVA                                    |
| **`transformersQuantity`**      | Property     | No       | Number of transformers associated with this generator                                       | Integer                                |
| **`transformersApparentPower`** | Property     | No       | Total apparent power capacity of connected transformers                                     | MVA                                    |
| **`industrialControlSystem`**   | Property     | No       | Type of supervisory control or SCADA system used for this generator                         | String (e.g., "Siemens SCADA S7-1500") |
| **`speed`**                     | Property     | No       | Rotational speed of the generator shaft                                                     | RPM                                    |
| **`ratedPowerFactor`**          | Property     | No       | Ratio of real power to apparent power                                                       | Unitless                               |
| **`voltageRegulationRange`**    | Property     | No       | Allowable percentage variation above or below nominal voltage                               | PCT                                    |
| **`windingInsulationClass`**    | Property     | No       | Insulation temperature rating class of the generator windings                               | String (e.g., "F")                     |
| **`isPartOfHydroPowerPlant`**   | Relationship | No       | Parent hydropower plant                                                                     | Array of URIs                          |
| **`isDrivenByTurbines`**        | Relationship | No       | Array of references to the Turbine entities that drive this Generator                       | Array of URIs                          |
| **`hasTransformers`**           | Relationship | No       | Linked transformer(s)                                                                       | Array of URIs                          |
| **`isPartOfPowerHouse`**        | Relationship | No       | PowerHouse entity that houses this Generator                                                | Array of URIs                          |




