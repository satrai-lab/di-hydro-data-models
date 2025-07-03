# Reservoir

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Reservoir.png" 
       alt="Reservoir Diagram" 
       style="max-width: 100%; height: auto; width: 800px">
</div>

## Definition

A **Reservoir** is a managed **WaterBody**—typically impounded by a dam—that stores and regulates water for hydropower generation, irrigation, flood control, or water supply. It inherits all WaterBody characteristics (identity, classification, location, dimensions, flow dynamics, level and operational data, and relationships) and adds storage-specific parameters (capacity, inflow/outflow rates, historical levels, operating limits, and links to dams, tunnels, and pumping stations).
> **Inheritance:**
> This entity **inherits** all core properties from the [WaterBody ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/WaterBody/DataModel/type.json).

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                                                       | Units / Values                                |
| ----------------------------- | ------------ | -------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier                                                                                             | URN format                                    |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                                                 | `"WaterBody"`                                 |
| **`name`**                    | Property     | Yes      | Official or common name of the water body                                                                         | String                                        |
| **`waterBodyCategory`**       | Property     | No       | Classification: River, Lake, Reservoir, or Other                                                                  | `"River"`, `"Lake"`, `"Reservoir"`, `"Other"` |
| **`geographicalLocation`**    | GeoProperty  | No       | GeoJSON Point giving longitude and latitude                                                                       | `[lon, lat]`                                  |
| **`surfaceArea`**             | Property     | No       | Surface area                                                                                                      | km² (`KM2`)                                   |
| **`length`**                  | Property     | No       | Length of the water body (for rivers or elongated lakes)                                                          | km (`KM`)                                     |
| **`averageDepth`**            | Property     | No       | Mean depth                                                                                                        | m (`M`)                                       |
| **`averageFlowRate`**         | Property     | No       | Mean volumetric flow                                                                                              | m³/s (`M3S`)                                  |
| **`peakFlow`**                | Property     | No       | Maximum observed or design flow                                                                                   | m³/s (`M3S`)                                  |
| **`seasonalVariation`**       | Property     | No       | Seasonal flow rates:<br>• **winter**, **spring**, **summer**, **autumn**                                          | numeric (m³/s)                                |
| **`averageWaterLevel`**       | Property     | No       | Mean water-surface elevation                                                                                      | m (`M`)                                       |
| **`operationalData`**         | Property     | No       | Operational metrics:<br>• **floodRisk** (`Low`/`Medium`/`High`)<br>• **waterRights** (`Public`/`Private`/`Mixed`) | —                                             |
| **`isFedBy`**                 | Relationship | No       | Upstream CatchmentArea entities supplying this water body                                                         | Array of URIs                                 |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | HydropowerPlant entities utilizing this water body                                                                | Array of URIs                                 |
| **`storageCapacity`**         | Property     | No       | Total volume that can be stored                                                                                   | m³ (`M3`)                                     |
| **`averageInflowRate`**       | Property     | No       | Average inflow rate                                                                                               | m³/s (`M3S`)                                  |
| **`averageOutflowRate`**      | Property     | No       | Average outflow rate                                                                                              | m³/s (`M3S`)                                  |
| **`historicalMaxLevel`**      | Property     | No       | Historical maximum water level                                                                                    | m (`M`)                                       |
| **`historicalMinLevel`**      | Property     | No       | Historical minimum water level                                                                                    | m (`M`)                                       |
| **`maxReservoirLevel`**       | Property     | No       | Highest allowed water surface elevation                                                                           | m (`M`)                                       |
| **`normalReservoirLevel`**    | Property     | No       | Typical operating water surface elevation                                                                         | m (`M`)                                       |
| **`reservoirLength`**         | Property     | No       | Upstream extent from dam at normal level                                                                          | km (`KM`)                                     |
| **`maximumEnergeticVolume`**  | Property     | No       | Potential energy contained when full                                                                              | GWh (`GWH`)                                   |
| **`reservoirType`**           | Property     | No       | Operation classification                                                                                          | `"seasonal"`, `"weekly"`, `"daily"`           |
| **`grossVolume`**             | Property     | No       | Total storage capacity at normal level for a given year                                                           | m³ (`M3`)                                     |
| **`usefulVolume`**            | Property     | No       | Usable storage for power generation at normal level                                                               | m³ (`M3`)                                     |
| **`hasDams`**                 | Relationship | No       | Dams that create or control this reservoir                                                                        | Array of URIs                                 |
| **`feedsIntakes`**            | Relationship | No       | Intake entities drawing water from this reservoir                                                                 | Array of URIs                                 |
| **`hasPressureTunnel`**       | Relationship | No       | PressureTunnel entities conveying water between reservoir and penstock                                            | Array of URIs                                 |
| **`fedByPumpingStation`**     | Relationship | No       | PumpingStation entities supplying water into this reservoir                                                       | Array of URIs                                 |


