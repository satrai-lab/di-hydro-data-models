# Pressure Tunnel
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/PressureTunnel.png" 
       alt="PressureTunnel Diagram" 
       style="max-width: 100%; height: auto; width: 450px">
</div>

## Definition

A **PressureTunnel** is a conduit that conveys water under pressure from a reservoir to a penstock in a hydropower system. It is designed to maintain hydraulic gradient and minimize head losses over long distances, ensuring stable delivery of water to the turbine inlet.

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                                 | Units / Values     |
| ----------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------- | ------------------ |
| **`id`**                      | Property     | Yes      | Unique URI identifier for the pressure tunnel                                               | URN format         |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                           | `"PressureTunnel"` |
| **`length`**                  | Property     | No       | Length of the pressure tunnel between reservoir and penstock                                | m                  |
| **`fromReservoir`**           | Relationship | No       | Reference(s) to the upstream Reservoir entity or entities feeding this tunnel               | Array of URIs      |
| **`toPenstock`**              | Relationship | No       | Reference(s) to the downstream Penstock entity or entities receiving flow from this tunnel  | Array of URIs      |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | Reference(s) to the HydropowerPlant entity or entities that this pressure tunnel is part of | Array of URIs      |

