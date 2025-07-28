# Dam
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Dam.png" 
       alt="Dam Diagram" 
       style="max-width: 100%; height: auto; width: 700px">
</div>

## Definition

A **Dam** is a barrier constructed across a river or stream to impound water, creating a reservoir for hydropower production, flood control, irrigation, or water supply. It consists of structural elements such as a crest, spillways, and intakes, and its height, length, and materials determine storage capacity and stability.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.

## Attributes Specifications


| Attribute                   | Type         | Required | Description                                                        | Units / Values                                           |
| --------------------------- | ------------ | -------- | ------------------------------------------------------------------ | -------------------------------------------------------- |
| **`id`**                    | Property     | Yes      | Unique URI identifier for the dam                                  | URN format                                               |
| **`type`**                  | Property     | Yes      | Fixed entity type                                                  | `"Dam"`                                                  |
| **`name`**                  | Property     | Yes      | Official or common name of the dam                                 | String                                                   |
| **`geographicalLocation`**  | GeoProperty  | No       | GeoJSON point of the dam’s location (longitude, latitude)          | `[lon, lat]`                                             |
| **`damHeight`**             | Property     | No       | Vertical height from foundation to crest                           | m                                                        |
| **`damLength`**             | Property     | No       | Horizontal span or width of the dam                                | m                                                        |
| **`constructionMaterials`** | Property     | No       | Primary materials used in dam construction                         | `"Concrete"`, `"Earth-fill"`, `"Rock-fill"`, `"Masonry"` |
| **`damType`**               | Property     | No       | Structural design classification                                   | `"Concrete Gravity"`, `"Arch Dam"`, `"Embankment Dam"`   |
| **`yearOfConstruction`**    | Property     | No       | Calendar year when the dam was completed                           | Integer                                                  |
| **`damCrestElevation`**     | Property     | No       | Elevation of the dam crest above mean sea level                    | m                                                        |
| **`reservoirWaterLevel`**   | Property     | No       | Current water level in the dam’s reservoir                         | m (meters above sea level)                               |
| **`usefulWaterContent`**    | Property     | No       | Volume of usable water stored in the reservoir                     | m³ × 10³                                                 |
| **`energyContent`**         | Property     | No       | Amount of storable energy in the reservoir                         | MWh                                                      |
| **`specificConsumption`**   | Property     | No       | Water needed to generate one unit of electricity                   | m³/kWh                                                   |
| **`lowerProductionLimit`**  | Property     | No       | Minimum technical production limit of turbines                     | m³/s                                                     |
| **`upperProductionLimit`**  | Property     | No       | Maximum technical production limit of turbines                     | m³/s                                                     |
| **`hasSpillway`**           | Relationship | No       | Spillway entities used to safely release excess water              | Array of URIs                                            |
| **`hasintakes`**            | Relationship | No       | Intake entities that feed water into the conveyance system         | Array of URIs                                            |
| **`isPartOfReservoir`**     | Relationship | No       | Reservoir entity or entities created by this dam                   | Array of URIs                                            |
| **`isPartOfHydroPlant`**    | Relationship | No       | HydropowerPlant entity or entities that this dam is a component of | Array of URIs                                            |




