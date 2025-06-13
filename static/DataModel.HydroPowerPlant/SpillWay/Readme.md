# Spillway
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Spillway.png" 
       alt="Spillway Diagram" 
       style="max-width: 100%; height: auto; width: 300px">
</div>

## Definition

A **Spillway** is a structure engineered to safely pass excess water from a reservoir or dam to downstream channels, preventing overtopping and potential dam failure.
It is designed with specific discharge capacities, crest elevations, and flow control features to handle varying flood conditions.

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                            | Units / Values                                                        |
| ----------------------------- | ------------ | -------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier for the spillway                                                 | URN format                                                            |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                      | `"Spillway"`                                                          |
| **`name`**                    | Property     | Yes      | Official or common name of the spillway                                                | String                                                                |
| **`geographicalLocation`**    | GeoProperty  | No       | GeoJSON point indicating the spillway’s location (longitude, latitude)                 | `[lon, lat]`                                                          |
| **`dischargeCapacity`**       | Property     | No       | Maximum water discharge capacity of the spillway                                       | m³/s                                                                  |
| **`designFlowRate`**          | Property     | No       | Flow rate the spillway is engineered to handle under normal operating conditions       | m³/s                                                                  |
| **`spillwayType`**            | Property     | No       | Structural classification or design type of the spillway                               | `"Chute Spillway"`, `"Side-Channel Spillway"`, `"Fuse Plug Spillway"` |
| **`crestElevation`**          | Property     | No       | Elevation of the spillway’s crest above mean sea level, determining activation level   | m                                                                     |
| **`spillwayClassification`**  | Property     | No       | Indicates whether it is a principal (regular operation) or emergency (safety) spillway | `"Principal"`, `"Emergency"`                                          |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | Reference to the HydropowerPlant entity that this spillway belongs to       | Array of URIs                                                         |
