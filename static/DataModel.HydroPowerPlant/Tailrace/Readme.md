# Tailrace
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Tailrace.png" 
       alt="Tailrace Diagram" 
       style="max-width: 100%; height: auto; width: 500px">
</div>

## Definition

A **Tailrace** is the channel that carries water away from the hydropower plant after it has passed through the turbine and draft tube. It is the final component in the energy extraction process, guiding the used water downstream—often into a river, lake, or reservoir. A properly engineered tailrace minimizes backpressure on the turbine and ensures efficient water discharge into the environment.

**Flow path:**
**Turbine → DraftTube → Tailrace → Water Body**

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.


---

## Attributes Specifications

| Attribute               | Type         | Required | Description                                      | Units / Values |
| ----------------------- | ------------ | -------- | ------------------------------------------------ | -------------- |
| `id`                    | Property     | Yes      | Unique identifier of the tailrace                | URN format     |
| `type`                  | Property     | Yes      | NGSI-LD entity type                              | `"Tailrace"`   |
| `length`                | Property     | No       | Channel length                                   | m              |
| `waterLevel`            | Property     | No       | Current water level at the tailrace              | m              |
| `flowRate`              | Property     | No       | Discharge rate at the tailrace outlet            | m³/s           |
| `connectsToWaterBody`   | Relationship | No       | Points to a downstream river, lake, or reservoir | URI            |
| `receivesFromDraftTube` | Relationship | No       | Indicates which draft tube(s) feed this tailrace | URI            |

