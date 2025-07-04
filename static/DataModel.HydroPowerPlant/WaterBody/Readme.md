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

| Attribute                     | NGSI Type    | Required | Description                                                              | Units / Values                                   |
| ----------------------------- | ------------ | -------- | ------------------------------------------------------------------------ | ------------------------------------------------ |
| **`id`**                      | Property     | Yes      | Unique NGSI-LD URI identifier for the water body                         | URN (e.g., `urn:ngsi-ld:WaterBody:river1`)       |
| **`type`**                    | Property     | Yes      | Entity type, must be `"WaterBody"`                                       | `"WaterBody"`                                    |
| **`name`**                    | Property     | Yes      | Official or common name of the water body                                | String                                           |
| **`waterBodyCategory`**       | Property     | No       | Classification of the water body                                         | `"River"`, `"Lake"`, `"Reservoir"`, `"Other"`    |
| **`geographicalLocation`**    | GeoProperty  | No       | GeoJSON point indicating geographic coordinates (longitude, latitude)    | `[lon, lat]`                                     |
| **`surfaceArea`**             | Property     | No       | Total surface area of the water body                                     | km² (`KM2`)                                      |
| **`length`**                  | Property     | No       | Linear length of the water body (mainly for rivers or long lakes)        | km (`KM`)                                        |
| **`averageDepth`**            | Property     | No       | Average vertical depth of the water body                                 | meters (`M`)                                     |
| **`averageFlowRate`**         | Property     | No       | Long-term average volumetric flow rate                                   | cubic meters per second (`M3S`)                  |
| **`peakFlow`**                | Property     | No       | Maximum recorded or designed flow rate                                   | cubic meters per second (`M3S`)                  |
| **`seasonalVariation`**       | Property     | No       | Seasonal flow variation as array `[winter, spring, summer, autumn]`      | numeric array (m³/s), unit via nested `unitCode` |
| **`averageWaterLevel`**       | Property     | No       | Average elevation of the water surface                                   | meters (`M`)                                     |
| **`floodRisk`**               | Property     | No       | Flood risk classification                                                | `"Low"`, `"Medium"`, `"High"`                    |
| **`waterRights`**             | Property     | No       | Legal ownership or usage rights of water                                 | `"Public"`, `"Private"`, `"Mixed"`               |
| **`isFedBy`**                 | Relationship | No       | References to upstream `CatchmentArea` entities feeding this water body  | Array of URNs                                    |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | References to `HydropowerPlant` entities that this water body is part of | Array of URNs                                    |

