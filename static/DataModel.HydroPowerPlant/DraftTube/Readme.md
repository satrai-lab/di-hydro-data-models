# DraftTube

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/DraftTube.png" 
       alt="Draft Tube Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **Draft Tube** is a critical hydraulic component in a reaction turbine system. It is a passage connected to the turbine's outlet that allows water to decelerate and expand, recovering part of the pressure energy lost as it exits the runner. This improves the overall efficiency of the hydropower system by minimizing energy losses. Draft tubes are often shaped conically or in an elbow form, depending on the site configuration and flow characteristics.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.


## Attributes Specifications

| Attribute              | Type         | Required | Description                                                           | Units / Values                |
| ---------------------- | ------------ | -------- | --------------------------------------------------------------------- | ----------------------------- |
| `id`                   | Property     | Yes      | Unique identifier of the Draft Tube                                   | URN format                    |
| `type`                 | Property     | Yes      | NGSI-LD entity type                                                   | `"DraftTube"`                 |
| `shape`                | Property     | No       | Shape of the draft tube                                               | `"conical"`, `"elbow"`, etc.  |
| `length`               | Property     | No       | Length of the draft tube                                              | m                             |
| `diameterAtEntry`      | Property     | No       | Internal diameter of the tube at the turbine outlet                   | m                             |
| `diameterAtExit`       | Property     | No       | Internal diameter of the tube at the tailrace end                     | m                             |
| `material`             | Property     | No       | Construction material                                                 | `"Concrete"`, `"Steel"`, etc. |
| `connectsTurbine`      | Relationship | No       | Points to the Turbine entity that the draft tube is connected to      | URI                           |
| `dischargesToTailrace` | Relationship | No       | Points to the Tailrace entity that receives water from the draft tube | URI                           |


