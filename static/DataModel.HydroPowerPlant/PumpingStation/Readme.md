# Pumping Station

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/PumpingStation.png" 
       alt="PumpingStation Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **PumpingStation** is a facility that moves water from one location to another—such as from a river or lower reservoir up to an upper reservoir or between network segments—using electrically driven pumps.

## Attributes Specifications

| Attribute                         | Type         | Required | Description                                                                                      | Units / Values       |
| --------------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------ | -------------------- |
| **`id`**                          | Property     | Yes      | Unique URI identifier for the pumping station                                                    | URN format           |
| **`type`**                        | Property     | Yes      | Fixed entity type                                                                                | `"PumpingStation"`   |
| **`name`**                        | Property     | Yes      | Official or common name of the pumping station                                                   | String               |
| **`totalPower`**                  | Property     | No       | Total installed motor power capacity                                                             | MW (megawatts)       |
| **`unitCount`**                   | Property     | No       | Number of individual pump units                                                                  | Integer              |
| **`yearlyEnergyConsumption`**     | Property     | No       | Annual electricity consumed by all pumps                                                         | kWh (kilowatt-hours) |
| **`estimatedAnnualContribution`** | Property     | No       | Estimated additional generation enabled by pumping                                               | MWh (megawatt-hours) |
| **`feedsReservoir`**              | Relationship | No       | References to Reservoir entity or entities into which this station pumps water                   | Array of URIs        |
| **`increasesProductionAt`**       | Relationship | No       | References to HydropowerPlant entity or entities whose output is boosted by this pumping station | Array of URIs        |
