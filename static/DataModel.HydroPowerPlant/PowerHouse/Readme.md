# Power House
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/PowerHouse.png" 
       alt="PowerHouse Diagram" 
       style="max-width: 100%; height: auto; width: 650px">
</div>

## Definition

A **PowerHouse** is the structural and mechanical enclosure within a hydropower plant that houses the prime movers (turbines), electrical generators, governors, and auxiliary systems. It serves as the interface between the water conveyance system (penstocks) and the energy conversion machinery, providing support, protection, and access for operation and maintenance.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.


## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                           | Units / Values     |
| ----------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------- | ------------------ |
| **`id`**                      | Property     | Yes      | Unique URI identifier                                                                 | URN format         |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                     | `"PowerHouse"`     |
| **`name`**                    | Property     | Yes      | Official or common name                                                               | String             |
| **`geographicalLocation`**    | GeoProperty  | No       | Geographic location as a GeoJSON Point—first element is longitude, second is latitude | `[lon, lat]`       |
| **`address`**                 | Property     | No       | Physical street address of the PowerHouse                                             | String             |
| **`buildingArea`**            | Property     | No       | Total floor area of the PowerHouse                                                    | square meters (M2) |
| **`numberOfFloors`**          | Property     | No       | Number of stories or levels within the PowerHouse                                     | Integer            |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | Reference to the parent HydropowerPlant entity                                        | Array of URIs      |
| **`containsGenerators`**      | Relationship | No       | Generators installed and operated inside this PowerHouse                              | Array of URIs      |
| **`containsTurbines`**        | Relationship | No       | Turbines installed and operated inside this PowerHouse                                | Array of URIs      |
| **`isConnectedToPenstock`**   | Relationship | No       | Penstock(s) delivering water to this PowerHouse                                       | Array of URIs      |
| **`hasGovernors`**            | Relationship | No       | Governor devices that regulate turbine speed and flow within this PowerHouse          | Array of URIs      |
