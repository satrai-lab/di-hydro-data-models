# Penstock
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Penstock.png" 
       alt="Penstock Diagram" 
       style="max-width: 100%; height: auto; width: 750px">
</div>

## Definition

A **Penstock** is a large conduit or pipe that delivers water under pressure from an intake or reservoir to the turbine in a hydropower plant. It is engineered to withstand high hydraulic pressures and minimize energy losses, connecting upstream water sources through components such as surge tanks, valves, and the turbine inlet.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.


## Attributes Specifications


| Attribute                       | Type         | Required | Description                                                                                | Units / Values                                     |
| ------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| **`id`**                        | Property     | Yes      | Unique URI identifier for the penstock                                                     | URN format                                         |
| **`type`**                      | Property     | Yes      | Fixed entity type                                                                          | `"Penstock"`                                       |
| **`name`**                      | Property     | Yes      | Official or common name of the penstock                                                    | String                                             |
| **`geographicalLocation`**      | GeoProperty  | No       | GeoJSON point marking the penstock’s upstream or downstream location (longitude, latitude) | `[lon, lat]`                                       |
| **`length`**                    | Property     | No       | Total physical length of the penstock                                                      | m                                                  |
| **`diameter`**                  | Property     | No       | Internal diameter of the penstock                                                          | m                                                  |
| **`material`**                  | Property     | No       | Construction material (e.g., steel, reinforced concrete, composite)                        | `"Steel"`, `"Reinforced Concrete"`, `"Composite"`  |
| **`designPressure`**            | Property     | No       | Maximum hydraulic pressure the penstock is engineered to withstand                         | bar                                                |
| **`flowCapacity`**              | Property     | No       | Maximum volumetric flow rate the penstock can deliver to the turbine                       | m³/s                                               |
| **`valveMaxFlow`**              | Property     | No       | Maximum flow the penstock’s valve can handle                                               | m³/s                                               |
| **`valveMaxStaticPressure`**    | Property     | No       | Maximum static pressure the penstock valve can withstand                                   | bar                                                |
| **`inletPipeDimensions`**       | Property     | No       | Dimensions of inlet pipe: length, inner diameter, outer diameter                           | Object: `{ length, innerDiameter, outerDiameter }` |
| **`outletPipeDimensions`**      | Property     | No       | Dimensions of outlet pipe: length, inner diameter, outer diameter                          | Object: `{ length, innerDiameter, outerDiameter }` |
| **`diversionTunnelDimensions`** | Property     | No       | Dimensions of diversion tunnel: length, inner diameter, outer diameter                     | Object: `{ length, innerDiameter, outerDiameter }` |
| **`drainingPipeDimensions`**    | Property     | No       | Dimensions of draining pipe: length, inner diameter, outer diameter                        | Object: `{ length, innerDiameter, outerDiameter }` |
| **`isPartOfHydroPowerPlant`**   | Relationship | No       | Reference to the parent HydropowerPlant entity                                             | Array of URIs                                      |
| **`isConnectedToIntake`**       | Relationship | No       | Intake entity or entities feeding this penstock                                            | Array of URIs                                      |
| **`isConnectedToSurgeTank`**    | Relationship | No       | SurgeTank entity or entities mitigating pressure transients along this penstock            | Array of URIs                                      |
| **`isConnectedToValve`**        | Relationship | No       | Valve entity or entities installed on this penstock for flow control                       | Array of URIs                                      |
| **`isConnectedToValveHouse`**   | Relationship | No       | ValveHouse entity or entities housing flow-control valves associated with this penstock    | Array of URIs                                      |

---



