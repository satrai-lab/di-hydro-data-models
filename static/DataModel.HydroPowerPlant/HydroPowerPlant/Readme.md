# Hydro Power Plant
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/HydroPowerPlant.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 100%">
</div>

## Definition
A **HydropowerPlant** represents a physical facility that converts the energy of flowing water into electrical power. It encompasses all infrastructure components (dams, turbines, generators, etc.) and operational parameters required for electricity generation. This entity serves as the central hub in hydropower data models, linking to all physical and organizational elements of a hydroelectric facility.

## Attribute Specifications

| Attribute               | Type          | Data Type      | Required | Description & Importance                                                                                                | Units/Format                   |  
|-------------------------|---------------|---------------|----------|------------------------------------------------------------------------------------------------------------------------|--------------------------------|  
| **`id`**                | Property      | URI           | Yes      | Unique URI identifier for the plant. Critical for data integrity and relationships.                                    | `urn:ngsi-ld:HydropowerPlant:{id}` |  
| **`type`**              | Property      | String        | Yes      | Fixed entity type identifier. Must be `HydropowerPlant`.                                                               | -                              |  
| **`name`**              | Property      | String        | Yes      | Official name of the facility. Used in operational and regulatory contexts.                                            | -                              |  
| **`geographicalLocation`** | GeoProperty | GeoJSON Point | No       | Plant's geospatial coordinates. Essential for environmental impact analysis and grid connectivity.                    | `{"type":"Point","coordinates":[lon,lat]}` |  
| **`address`**           | Property      | String        | No       | Physical address. Supports maintenance and regulatory reporting.                                                       | -                              |  
| **`size`**              | Property      | Object        | No       | Capacity category with min/max ranges. Classifies plant scale for regulatory purposes.                                 | `{category, interval:{min, max}, standard}` |  
| **`powerPlantCapacity`**| Property      | Object        | No       | Rated electrical output. Key metric for grid contribution and revenue calculation.                                     | `{value, unitCode:"MW"}`       |  
| **`powerplantType`**    | Property      | String        | No       | Operational design (e.g., reservoir, run-of-river). Determines control strategies and environmental impact.           | -                              |  
| **`conversionEfficiency`**| Property    | Number        | No       | Energy conversion rate (%). Indicates turbine-generator performance.                                                  | % (e.g., `92.5`)               |  
| **`commissioningYear`** | Property      | Integer       | No       | Initial operation year. Critical for asset lifecycle management.                                                      | Year (e.g., `1985`)            |  
| **`rehabilitationYear`**| Property      | Integer       | No       | Last major upgrade year. Tracks modernization investments.                                                            | Year (e.g., `2010`)            |  
| **`installedCapacity`** | Property      | Number        | No       | Total rated electrical capacity. Primary metric for capacity planning.                                                | MW                             |  
| **`annualEnergyOutput`**| Property      | Number        | No       | Average yearly energy production. Basis for revenue forecasts.                                                        | kWh                            |  
| **`ecologicalDischarge`**| Property     | Number        | No       | Minimum downstream flow. Ensures environmental compliance.                                                            | m³/s                           |  
| **`maxTailwaterLevel`** | Property      | Number        | No       | Highest downstream water level. Critical for flood control and turbine efficiency.                                    | m                              |  
| **`grossHead`**         | Property      | Number        | No       | Total vertical water drop. Determines potential energy conversion.                                                    | m                              |  
| **`partOfCommunity`**   | Relationship  | URI[]         | No       | Links to HydroPowerCommunity entity. Establishes organizational hierarchy.                                            | Array of URIs                  |  
| **`hasPressureTunnel`** | Relationship  | URI[]         | No       | Connects to pressure tunnel infrastructure. Maps water conveyance system.                                             | Array of URIs                  |  
| **`boostedByPumpingStation`**| Relationship | URI[]    | No       | Links to pumping stations. For pumped-storage facilities.                                                             | Array of URIs                  |  
| **`hasHydroPumps`**     | Relationship  | URI[]         | No       | Associated pump entities. Required for pumped-storage plants.                                                         | Array of URIs                  |  
| **`hasDams`**           | Relationship  | URI[]         | No       | Connected dam structures. Maps flood control and water storage assets.                                                | Array of URIs                  |  
| **`containsGenerators`**| Relationship  | URI[]         | No       | Generator equipment. Core power generation components.                                                                | Array of URIs                  |  
| **`hasGovernors`**      | Relationship  | URI[]         | No       | Speed control systems. Ensures grid frequency stability.                                                              | Array of URIs                  |  
| **`containsTurbines`**  | Relationship  | URI[]         | No       | Turbine units. Primary energy conversion equipment.                                                                   | Array of URIs                  |  
| **`hasIntakes`**        | Relationship  | URI[]         | No       | Water intake structures. Critical for sedimentation management.                                                       | Array of URIs                  |  
| **`hasPowerHouses`**    | Relationship  | URI[]         | No       | Powerhouse buildings. Groups generation equipment.                                                                    | Array of URIs                  |  
| **`hasPenstocks`**      | Relationship  | URI[]         | No       | Penstock pipelines. High-pressure water conduits to turbines.                                                         | Array of URIs                  |  
| **`hasValve`**          | Relationship  | URI[]         | No       | Control valves. Regulates water flow to turbines.                                                                     | Array of URIs                  |  
| **`hasValveHouse`**     | Relationship  | URI[]         | No       | Valve housing structures. Protects critical flow controls.                                                            | Array of URIs                  |  
| **`hasWaterBody`**      | Relationship  | URI[]         | No       | Connected water sources (rivers/reservoirs). Maps water rights and sources.                                           | Array of URIs                  |  
| **`hasSurgeTank`**      | Relationship  | URI[]         | No       | Surge suppression tanks. Prevents water hammer damage.                                                                | Array of URIs                  |  



