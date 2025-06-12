# Water Body

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/WaterBody.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **WaterBody** is any significant accumulation of water on Earth’s surface—such as a river, lake, or reservoir—that serves as a source, conduit, or storage for hydropower systems. It is characterized by its physical dimensions, flow dynamics, water quality, and ecological indicators, all of which inform water availability, generation potential, and environmental management.

## Attributes Specifications

| Attribute                      | Type         | Required | Description                                                                    | Units / Values                                        |
| ------------------------------ | ------------ | -------- | ------------------------------------------------------------------------------ | ----------------------------------------------------- |
| **`id`**                       | Property     | Yes      | Unique URI identifier for the water body                                       | URN format                                            |
| **`type`**                     | Property     | Yes      | Fixed entity type                                                              | `"WaterBody"`                                         |
| **`name`**                     | Property     | Yes      | Official or common name of the water body                                      | String                                                |
| **`waterBodyCategory`**        | Property     | No       | Classification of the water body                                               | `"River"`, `"Lake"`, `"Reservoir"`, `"Other"`         |
| **`geographicalLocation`**     | GeoProperty  | No       | Geographic coordinates of the water body                                       | `[lon, lat]`                                          |
| **`dimensions`**               | Property     | No       | Physical size parameters (surface area, length, average depth)                 | km², km, m                                            |
| **`waterFlowCharacteristics`** | Property     | No       | Flow metrics including average, peak, and seasonal variation                   | m³/s                                                  |
| **`waterLevel`**               | Property     | No       | Water level statistics such as average depth                                   | m                                                     |
| **`waterQuality`**             | Property     | No       | Key quality metrics (temperature, pH, dissolved oxygen, sediment load)         | °C, pH units, mg/L                                    |
| **`environmentalIndicators`**  | Property     | No       | Ecological measures including biodiversity index and invasive species presence | Index value, boolean                                  |
| **`operationalData`**          | Property     | No       | Management-related data such as flood risk classification and water rights     | `"Low"/"Medium"/"High"`, `"Public"/"Private"/"Mixed"` |
| **`isFedBy`**                  | Relationship | No       | References to upstream CatchmentArea entities supplying this water body        | Array of URIs                                         |
| **`isPartOfHydroPowerPlant`**  | Relationship | No       | References to HydropowerPlant entities that utilize or include this water body | Array of URIs                                         |
