# Valve
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/ValveHouse.png" 
       alt="Valve Diagram" 
       style="max-width: 100%; height: auto; width: 550px">
</div>

## Definition

A **ValveHouse** is a structure that encloses and protects one or more valves, associated actuators, and control equipment in a hydropower system. It provides a controlled environment for operation, maintenance access, and safeguarding of flow-control components against weather and debris.

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                | Units / Values |
| ----------------------------- | ------------ | -------- | -------------------------------------------------------------------------- | -------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier for the ValveHouse                                   | URN format     |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                          | `"ValveHouse"` |
| **`name`**                    | Property     | Yes      | Official or common name of the ValveHouse                                  | String         |
| **`geographicalLocation`**    | GeoProperty  | No       | GeoJSON Point indicating the ValveHouse’s location (longitude, latitude)   | `[lon, lat]`   |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | References to the HydropowerPlant entities that this ValveHouse belongs to | Array of URIs  |
| **`containsValves`**          | Relationship | No       | References to Valve entities contained within this ValveHouse              | Array of URIs  |
| **`isConnectedToPenstock`**   | Relationship | No       | References to Penstock entities that this ValveHouse is connected to       | Array of URIs  |
