# Governor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Governor.png" 
       alt="Governor Diagram" 
       style="max-width: 100%; height: auto; width: 500px">
</div>

## Definition

A **Governor** is a control device in a hydropower system that regulates turbine speed and power output. By sensing deviations from a set speed, it adjusts water flow into the turbine—via wicket gates or guide vanes—to maintain stable frequency and load response.

> **Inheritance:**
> This entity **inherits** all core properties from the [GenericStaticComponent ](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/static/DataModel.HydroPowerPlant/GenericStaticComponent/DataModel/type.json) base type (e.g. `id`, `type`, `name`, `geographicalLocation`, `isPartOfHydroPowerPlant`, `hasDevices`, `observations`, `actuations`), and adds the following specific attributes.


## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                     | Units / Values |
| ----------------------------- | ------------ | -------- | ------------------------------------------------------------------------------- | -------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier for the governor                                          | URN format     |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                               | `"Governor"`   |
| **`name`**                    | Property     | Yes      | Official or common name of the governor                                         | String         |
| **`droopSetting`**            | Property     | No       | Percentage droop indicating how turbine speed decreases as load increases       | % (`PCT`)      |
| **`speedSetPoint`**           | Property     | No       | Target turbine speed that the governor attempts to maintain                     | RPM            |
| **`regulationRange`**         | Property     | No       | Percentage range over which the governor can adjust flow input to regulate load | % (`PCT`)      |
| **`responseTime`**            | Property     | No       | Time taken by the governor to respond to speed or load changes                  | s (`S`)        |
| **`manufacturer`**            | Property     | No       | Manufacturer or supplier of the governor                                        | String         |
| **`yearOfInstallation`**      | Property     | No       | Year in which the governor was installed                                        | Integer        |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | References to HydropowerPlant entity or entities that include this governor     | Array of URIs  |
| **`controlsTurbine`**         | Relationship | No       | References to Turbine entity or entities controlled by this governor            | Array of URIs  |
| **`isPartOfPowerHouse`**      | Relationship | No       | References to PowerHouse entity or entities housing this governor               | Array of URIs  |

