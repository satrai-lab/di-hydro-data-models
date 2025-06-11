# Generator
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Generator.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 600px">
</div>

## Definition
A **Generator** is the core electrical component in hydropower plants that converts mechanical energy from turbines into electrical energy. It consists of rotating electromagnets (rotor) and stationary coils (stator) that produce alternating current through electromagnetic induction.

## Attributes Specifications

| Attribute | Type | Required | Description | Units/Values |
|-----------|------|----------|-------------|--------------|
| **`id`** | Property | Yes | Unique URI identifier | URN format |
| **`type`** | Property | Yes | Fixed entity type | `"Generator"` |
| **`name`** | Property | Yes | Official/Common name | String |
| **`ratedCapacity`** | Property | No | It indicates the maximum power output the generator is designed to produce under normal operating conditions. | MW |
| **`efficiency`** | Property | No | The conversion efficiency of the generator | PCT |
| **`manufacturer`** | Property | No | The name or details of the manufacturer of the generator | String |
| **`yearOfInstallation`** | Property | No | The year when the generator was installed | Integer |
| **`generatorType`** | Property | No | Model or design identifier of the generator | String |
| **`axis`** | Property | No | Orientation of the rotating shaft | `Horizontal`/`Vertical` |
| **`voltageLevel`** | Property | No | Voltage at which the generator produces electricity | kV |
| **`ratedOutputMVA`** | Property | No | Apparent power capacity under standard conditions | MVA |
| **`speed`** | Property | No | Rotational speed of the generator shaft | RPM |
| **`ratedPowerFactor`** | Property | No | Ratio of real power to apparent power | unitless |
| **`voltageRegulationRange`** | Property | No | Allowable percentage variation above or below nominal voltage | PCT |
| **`windingInsulationClass`** | Property | No | Insulation temperature rating class of the generator windings | String (e.g., "F") |
| **`isPartOfHydroPowerPlant`** | Relationship | No | Parent hydropower plant | Array of URIs |
| **`isDrivenByTurbines`** | Relationship | No | Array of references to the Turbine entities that drive this Generator| Array of URIs |
| **`hasTransformers`** | Relationship | No | Linked transformer(s) | Array of URIs |
| **`isPartOfPowerHouse`** | Relationship | No | the PowerHouse entity that houses this Generator | Array of URIs |

