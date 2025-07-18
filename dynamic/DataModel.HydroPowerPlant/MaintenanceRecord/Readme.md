# 🛠️ Maintenance Record 


<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/MaintenanceRecord.png" 
       alt="HydroPowerPlantCommunity Actuation Diagram" 
       style="max-width: 100%; height: auto; width: 600px">
</div>

## Definition

The `MaintenanceRecord` entity captures a single maintenance event performed on equipment within an NGSI‑LD-enabled system. It links the work to a specific hydro‑power‑plant (HPP), component, and device, and records metadata such as the type of maintenance, specific work category, timestamp, findings, actions taken, duration, and the responsible party (technician or company).


## Attributes Specifications

| Attribute             | NGSI‑LD Type | Required | Description                                                                                | Units / Values                                                       |            
| --------------------- | ------------ | -------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | 
| **`@id`**             | —            | ✅ Yes    | Unique NGSI‑LD identifier of the maintenance record                                        | URI (e.g. `urn:ngsi-ld:MaintenanceRecord:1234`)                      |            
| **`@type`**           | —            | ✅ Yes    | NGSI‑LD entity type (must be `"MaintenanceRecord"`)                                        | `"MaintenanceRecord"`                                                |            
| **`inHPP`**           | Relationship | ✅ Yes    | Reference to the Hydro‑Power‑Plant (HPP) entity this record belongs to                     | URI of an `HPP` entity                                               |            
| **`onHPPComponent`**  | Relationship | ✅ Yes    | Reference to the specific HPP component serviced                                           | URI of a `Component` entity                                          |            
| **`onDevice`**        | Relationship | ✅ Yes    | Reference to the device (e.g. sensor, actuator) on which work was performed                | URI of a `Device` entity                                             |            
| **`maintenanceType`** | Property     | ✅ Yes    | High-level category of maintenance performed                                               | String (e.g. `Preventive`, `Corrective`, `Predictive`, `annaul`)     |            
| **`workType`**        | Property     | ✅ Yes    | Specific work category or discipline involved                                              | String (e.g. `Cleaning`, `Lubrication`, `Inspection`, `Replacement`) |            
| **`datePerformed`**   | Property     | ✅ Yes    | ISO 8601 date‑time when the maintenance was carried out                                    | ISO 8601 date-time (e.g. `2023-05-10T14:30:00Z`)                     |            
| **`issueFound`**      | Property     | ❌ No     | Description of any anomaly or problem detected during the maintenance (empty if none)      | String                                                               |            
| **`workPerformed`**   | Property     | ✅ Yes    | Detailed free‑text description of the actions taken                                        | String (e.g. `Cleaned filters; replaced ΔP sensor`)                  |            
| **`durationMinutes`** | Property     | ❌ No     | Total time spent on the maintenance activity                                               | Integer (minutes)                                                    |            
| **`technician`**      | Relationship | ✅ Yes    | Reference to the Technician or Company entity that performed the work                      | URI of a `Technician` or `Organization` entity                       |            
| **`responsibleType`** | Property     | ✅ Yes    | Specifies whether the responsible party is an individual technician or an external company | `Technician`,   `Company`                                                   

---


