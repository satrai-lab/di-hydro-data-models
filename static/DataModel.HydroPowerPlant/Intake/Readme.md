# Intake
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Intake.png" 
       alt="Intake Diagram" 
       style="max-width: 100%; height: auto; width: 450px">
</div>

## Definition

An **Intake** is the structure at the head of a hydropower conveyance system that diverts water from its source—river, reservoir, or lake—into the penstocks or canals. It typically includes gates, screens, or trash racks to control flow and prevent debris entry, ensuring safe and efficient delivery to downstream turbines.

## Attributes Specifications

| Attribute                       | Type         | Required | Description                                                                            | Units / Values |
| ------------------------------- | ------------ | -------- | -------------------------------------------------------------------------------------- | -------------- |
| **`id`**                        | Property     | Yes      | Unique URI identifier for the intake                                                   | URN format     |
| **`type`**                      | Property     | Yes      | Fixed entity type                                                                      | `"Intake"`     |
| **`name`**                      | Property     | Yes      | Official or common name of the intake                                                  | String         |
| **`geographicalLocation`**      | GeoProperty  | No       | GeoJSON point representing the intake’s location (longitude, latitude)                 | `[lon, lat]`   |
| **`intakeStructureType`**       | Property     | No       | Design or configuration of the intake (e.g., open channel, gated, screened, submerged) | String         |
| **`waterFlowRate`**             | Property     | No       | Volumetric flow rate drawn into the intake                                             | m³/s           |
| **`filtrationOrDebrisControl`** | Property     | No       | Mechanisms (screens, gratings, trash racks) used to prevent debris from entering       | String         |
| **`isPartOfDam`**               | Relationship | No       | Reference to the Dam entity of which this intake is a component                        | Array of URIs  |
| **`isPartOfHydroPowerPlant`**   | Relationship | No       | Reference to the HydropowerPlant entity that this intake serves                        | Array of URIs  |
| **`leadsToPenstocks`**          | Relationship | No       | References to Penstock entities that receive water from this intake                    | Array of URIs  |

