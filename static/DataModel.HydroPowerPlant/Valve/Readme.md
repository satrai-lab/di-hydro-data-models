# Valve
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Valve.png" 
       alt="Valve Diagram" 
       style="max-width: 100%; height: auto; width: 450px">
</div>

## Definition

A **Valve** is a mechanical device in a hydropower system that regulates or isolates water flow within conduits such as penstocks or valve houses. It can throttle, start, or stop flow to control pressure, protect equipment, and facilitate maintenance.

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                   | Units / Values                                                       |
| ----------------------------- | ------------ | -------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier for the valve                                           | URN format                                                           |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                             | `"Valve"`                                                            |
| **`name`**                    | Property     | Yes      | Official or common name of the valve                                          | String                                                               |
| **`geographicalLocation`**    | GeoProperty  | No       | GeoJSON point indicating the valve’s physical location (longitude, latitude)  | `[lon, lat]`                                                         |
| **`valveType`**               | Property     | No       | Design or classification of the valve                                         | `"Gate Valve"`, `"Butterfly Valve"`, `"Ball Valve"`, `"Sluice Gate"` |
| **`material`**                | Property     | No       | Construction material of the valve                                            | `"Stainless Steel"`, `"Cast Iron"`, `"Composite"`                    |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | Reference(s) to HydropowerPlant entity or entities that this valve belongs to | Array of URIs                                                        |
| **`isPartOfValveHouse`**      | Relationship | No       | Reference(s) to ValveHouse entity or entities that house this valve           | Array of URIs                                                        |
| **`isConnectedToPenstock`**   | Relationship | No       | Reference(s) to Penstock entity or entities to which this valve is connected  | Array of URIs                                                        |
