# Pumping Station

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/PumpingStation.png" 
       alt="PumpingStation Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **PumpingStation** is an installation within a hydropower system that lifts water from a lower elevation back into an upstream reservoir—often as part of a pumped storage scheme. It consists of electrically driven pumps, motors, and associated controls, boosting stored potential energy and enabling additional generation capacity during peak demand.

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
