# Water Body

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/WaterBody.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **WaterBody** is any significant accumulation of water on Earth’s surface—such as a river, lake, or reservoir—that serves as a source, conduit, or storage for hydropower systems. It is characterized by its physical dimensions, flow dynamics, water quality, and ecological indicators, all of which inform water availability, generation potential, and environmental management.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.


## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                            | Units / Values                                        |
| ----------------------------- | ------------ | -------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier for the water body                                               | URN format                                            |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                      | `"WaterBody"`                                         |
| **`name`**                    | Property     | Yes      | Official or common name of the water body                                              | String                                                |
| **`waterBodyCategory`**       | Property     | No       | Classification indicating whether the water body is a river, lake, reservoir, or other | `"River"`, `"Lake"`, `"Reservoir"`, `"Other"`         |
| **`geographicalLocation`**    | GeoProperty  | No       | GeoJSON point specifying the water body’s location (longitude, latitude)               | `[lon, lat]`                                          |
| **`surfaceArea`**             | Property     | No       | Surface area of the water body                                                         | km² (`KM2`)                                           |
| **`length`**                  | Property     | No       | Length of the water body (applicable for rivers or elongated lakes)                    | km (`KM`)                                             |
| **`averageDepth`**            | Property     | No       | Average depth of the water body                                                        | m (`M`)                                               |
| **`averageFlowRate`**         | Property     | No       | Average water flow rate                                                                | m³/s (`M3S`)                                          |
| **`peakFlow`**                | Property     | No       | Maximum observed or design flow rate                                                   | m³/s (`M3S`)                                          |
| **`seasonalVariation`**       | Property     | No       | Flow rate variation by season (winter, spring, summer, autumn)                         | numeric (m³/s)                                        |
| **`averageWaterLevel`**       | Property     | No       | Mean water‐surface elevation                                                           | m (`M`)                                               |
| **`operationalData`**         | Property     | No       | Management data including flood risk classification and water rights                   | `"Low"/"Medium"/"High"`, `"Public"/"Private"/"Mixed"` |
| **`isFedBy`**                 | Relationship | No       | References to upstream CatchmentArea entities that supply this water body              | Array of URIs                                         |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | References to HydropowerPlant entities that utilize or include this water body         | Array of URIs                                         |
                                      |
