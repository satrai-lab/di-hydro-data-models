# Reservoir

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Reservoir.png" 
       alt="Reservoir Diagram" 
       style="max-width: 100%; height: auto; width: 800px">
</div>

Here’s the updated **Reservoir** specification—note that its NGSI-LD `type` remains **WaterBody**, and I’ve added the two missing relationships at the end.

## Definition

A **Reservoir** is a managed **WaterBody**—typically impounded by a dam—that stores water for hydropower generation, irrigation, flood control, or supply. It extends the generic WaterBody model with storage‐specific parameters such as capacity, inflow/outflow controls, operational levels, and historical volume records.

## Attributes Specifications

| Attribute                      | Type         | Required | Description                                                                              | Units / Values                                        |
| ------------------------------ | ------------ | -------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **`id`**                       | Property     | Yes      | Unique URI identifier for the water body                                                 | URN format                                            |
| **`type`**                     | Property     | Yes      | Fixed entity type                                                                        | `"WaterBody"`                                         |
| **`name`**                     | Property     | Yes      | Official or common name of the water body                                                | String                                                |
| **`waterBodyCategory`**        | Property     | No       | Category—for a reservoir this will be `"Reservoir"`                                      | `"River"`, `"Lake"`, `"Reservoir"`, `"Other"`         |
| **`geographicalLocation`**     | GeoProperty  | No       | Coordinates of the water body centre (longitude, latitude)                               | `[lon, lat]`                                          |
| **`dimensions`**               | Property     | No       | Surface area, length, and average depth                                                  | km², km, m                                            |
| **`waterFlowCharacteristics`** | Property     | No       | Average, peak, and seasonal flow variation                                               | m³/s                                                  |
| **`waterLevel`**               | Property     | No       | Average water level                                                                      | m                                                     |
| **`waterQuality`**             | Property     | No       | Temperature, pH, dissolved oxygen, sediment load                                         | °C, pH units, mg/L                                    |
| **`environmentalIndicators`**  | Property     | No       | Biodiversity index, invasive species presence                                            | Index value, boolean                                  |
| **`operationalData`**          | Property     | No       | Flood risk, water rights                                                                 | `"Low"/"Medium"/"High"`, `"Public"/"Private"/"Mixed"` |
| **`isFedBy`**                  | Relationship | No       | Upstream CatchmentArea entities supplying this reservoir                                 | Array of URIs                                         |
| **`isPartOfHydroPowerPlant`**  | Relationship | No       | HydropowerPlant entities utilizing this reservoir                                        | Array of URIs                                         |
| **`storageCapacity`**          | Property     | No       | Total volume that can be stored                                                          | m³                                                    |
| **`inflowCharacteristics`**    | Property     | No       | Inflow regulation details:<br>• averageInflowRate (m³/s)<br>• retentionTime (h)          | m³/s, h                                               |
| **`outflowControl`**           | Property     | No       | Outflow management:<br>• gateStatus (open/closed/percent)<br>• averageOutflowRate (m³/s) | String, m³/s                                          |
| **`historicalLevels`**         | Property     | No       | Historical levels:<br>• historicalMaxLevel (m)<br>• historicalMinLevel (m)               | m                                                     |
| **`hasDams`**                  | Relationship | No       | Dams that create or control this reservoir                                               | Array of URIs                                         |
| **`feedsIntakes`**             | Relationship | No       | Intake entities that draw water from this reservoir                                      | Array of URIs                                         |
| **`hasPressureTunnel`**        | Relationship | No       | PressureTunnel entities conveying water into or out of this reservoir                    | Array of URIs                                         |
| **`fedByPumpingStation`**      | Relationship | No       | PumpingStation entities that supply water into this reservoir                            | Array of URIs                                         |
| **`maxReservoirLevel`**        | Property     | No       | Highest permitted water surface elevation                                                | m                                                     |
| **`normalReservoirLevel`**     | Property     | No       | Typical operating water surface elevation                                                | m                                                     |
| **`reservoirLength`**          | Property     | No       | Upstream extent length at normal level                                                   | km                                                    |
| **`maximumEnergeticVolume`**   | Property     | No       | Potential energy content when full                                                       | GWh                                                   |
| **`reservoirType`**            | Property     | No       | Operation classification                                                                 | `"seasonal"`, `"weekly"`, `"daily"`                   |
| **`reservoirVolumes`**         | Property     | No       | Annual historical capacity records (gross/useful volumes per year)                       | Array of `{year, grossVolume, usefulVolume}`          |


