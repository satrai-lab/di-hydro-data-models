# Turbine

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Turbine.png" 
       alt="Turbine Diagram" 
       style="max-width: 100%; height: auto; width: 100%">
</div>

## Definition

A **Turbine** is the mechanical engine in a hydropower plant that converts the potential and kinetic energy of flowing water into rotational mechanical energy. It consists of a runner (with buckets or blades) mounted on a shaft; as water passes through under pressure (the “head”), it spins the runner, which then drives the electrical generator.

## Attributes Specifications

| Attribute                     | Type         | Required | Description                                                                                 | Units / Values                                 |
| ----------------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **`id`**                      | Property     | Yes      | Unique URI identifier                                                                       | URN format                                     |
| **`type`**                    | Property     | Yes      | Fixed entity type                                                                           | `"Turbine"`                                    |
| **`name`**                    | Property     | Yes      | Official or common name                                                                     | String                                         |
| **`turbineType`**             | Property     | Yes      | Classification of the turbine—design optimized to particular flow and head conditions       | `"Francis"`, `"Kaplan"`, `"Pelton"`, `"Other"` |
| **`capacity`**                | Property     | No       | Rated power capacity the turbine can deliver under normal conditions                        | MW                                             |
| **`efficiency`**              | Property     | No       | Conversion efficiency of water energy to mechanical power                                   | PCT                                            |
| **`operatingFlowRate`**       | Property     | No       | Volumetric flow of water required to run at rated capacity                                  | m³/s                                           |
| **`head`**                    | Property     | No       | Effective vertical drop (pressure head) used by the turbine                                 | m                                              |
| **`manufacturer`**            | Property     | No       | Name or details of the turbine’s manufacturer                                               | String                                         |
| **`yearOfInstallation`**      | Property     | No       | Calendar year when the turbine was commissioned                                             | Integer                                        |
| **`numberOfImpellers`**       | Property     | No       | Number of buckets or blades on the runner                                                   | Integer                                        |
| **`axis`**                    | Property     | No       | Orientation of the turbine shaft                                                            | `"horizontal"`, `"vertical"`                   |
| **`maxPower`**                | Property     | No       | Maximum mechanical power achievable under extreme or peak conditions                        | MW                                             |
| **`speed`**                   | Property     | No       | Rated rotational speed of the runner                                                        | RPM                                            |
| **`dischargesToReservoir`**   | Relationship | No       | Downstream reservoir(s) receiving water via the outlet pressure tunnel, with tunnel lengths | Array of `{ tunnelLength (KM), URI }`          |
| **`isPartOfHydroPowerPlant`** | Relationship | No       | Parent hydropower plant entity                                                              | Array of URIs                                  |
| **`drivesGenerators`**        | Relationship | No       | Generator entity or entities driven by this turbine                                         | Array of URIs                                  |
| **`isPartOfPowerHouse`**      | Relationship | No       | PowerHouse entity housing this turbine                                                      | Array of URIs                                  |
| **`controlledByGovernor`**    | Relationship | No       | Governor device(s) that regulate flow or speed of this turbine                              | Array of URIs                                  |

