# Governor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Governor.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 400px">
</div>

## Definition

A **Governor** is a control device in a hydropower plant that regulates the flow of water through the turbine to maintain a desired rotational speed and output power. It dynamically adjusts turbine input based on load changes, using configurable control parameters such as droop, speed set-point, and regulation range.

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                                                 | Units / Values           |
| ----------------------------- | ------------ | -------- | ----------------------------------------------------------------------------------------------------------- | ------------------------ |
| **`id`**                      | Property     | Yes      | Unique URI identifier                                                                                       | URN format               |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                                           | `"Governor"`             |
| **`name`**                    | Property     | Yes      | Official or common name of the governor                                                                     | String                   |
| **`controlParameters`**       | Property     | No       | A set of one or more control settings that determine how the governor reacts (e.g., droop, speed set-point) | See sub-attributes below |
| ├ `droopSetting`              | Property     | Cond’l\* | Percentage by which turbine speed drops per percent load increase                                           | PCT                      |
| ├ `speedSetPoint`             | Property     | Cond’l\* | Target operating speed for the turbine                                                                      | RPM                      |
| └ `regulationRange`           | Property     | Cond’l\* | Maximum range over which the governor can adjust turbine flow                                               | PCT                      |
| **`responseTime`**            | Property     | No       | Time taken by the governor to respond to a change in load or speed                                          | Seconds (S)              |
| **`manufacturer`**            | Property     | No       | Name or details of the governor’s manufacturer                                                              | String                   |
| **`yearOfInstallation`**      | Property     | No       | Calendar year when the governor was installed                                                               | Integer                  |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | Parent hydropower plant entity that this governor belongs to                                                | Array of URIs            |
| **`controlsTurbine`**         | Relationship | No       | Turbine entity or entities whose flow and speed this governor controls                                      | Array of URIs            |
| **`isPartOfPowerHouse`**      | Relationship | No       | PowerHouse entity that houses this governor                                                                 | Array of URIs            |

\* *At least one of `droopSetting`, `speedSetPoint`, or `regulationRange` must be provided within `controlParameters`.*
