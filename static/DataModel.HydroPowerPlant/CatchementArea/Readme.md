# Catchement Area
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/CatchementArea.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>


## Definition

A **CatchmentArea** is the geographic region draining into a common water body, such as a river, lake, or reservoir. It collects surface water and precipitation, channeling flow through streams and tributaries into the hydropower system. Understanding its characteristics—area, soil, vegetation, and flow patterns—is critical for predicting water availability and managing reservoir inflows.

## Attributes Specifications

| Attribute                            | Type         | Required | Description                                                                                       | Units / Values                     |
| ------------------------------------ | ------------ | -------- | ------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **`id`**                             | Property     | Yes      | Unique URI identifier for the catchment area                                                      | URN format                         |
| **`type`**                           | Property     | Yes      | Fixed entity type                                                                                 | `"CatchmentArea"`                  |
| **`area`**                           | Property     | No       | Total surface area of the catchment                                                               | km² (square kilometers)            |
| **`annualPrecipitationVolume`**      | Property     | No       | Total volume of rainfall collected annually within the catchment                                  | m³ (cubic meters)                  |
| **`seasonalRainfallDistribution`**   | Property     | No       | Breakdown of annual precipitation by season (e.g., spring, summer, autumn, winter)                | JSON object with seasonal values   |
| **`soilType`**                       | Property     | No       | Dominant soil classification in the catchment (e.g., clay, sand, loam)                            | String                             |
| **`vegetationCover`**                | Property     | No       | Description of vegetation types and coverage in the area (e.g., forest, grassland, agriculture)   | String                             |
| **`flowVariationProfile`**           | Property     | No       | Time-series data or summary statistics describing how streamflow varies throughout the year       | JSON object or time-series dataset |
| **`averageWaterFlow`**               | Property     | No       | Mean historical flow rate from the catchment into the river system                                | m³/s (cubic meters per second)     |
| **`suppliesWaterToWaterBody`**       | Relationship | No       | References to downstream WaterBody entities (lakes, rivers) that receive flow from this catchment | Array of URIs                      |
| **`suppliesWaterToHydroPowerPlant`** | Relationship | No       | References to HydropowerPlant entities that depend on runoff from this catchment                  | Array of URIs                      |
