# 📈 Observation Entity
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Observation.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 500px">
</div>

## Definition

The `Observation` entity is used to represent a single recorded measurement or data point produced by a sensor or monitoring device within an NGSI-LD-enabled system. It may include metadata like the category of observation, timestamp of modification, associated measurement value and unit, type of measurement, and any external references (e.g., for multimedia content).

This entity is typically associated with physical or environmental parameters such as temperature, humidity, pressure, energy consumption, etc., and can be linked to devices or systems in smart environments (e.g., smart buildings, energy systems, hydropower infrastructure).

---

## Attributes Specifications

| Attribute               | NGSI Type | Required | Description                                                                 | Units / Values                            |
| ----------------------- | --------- | -------- | --------------------------------------------------------------------------- | ----------------------------------------- |
| **`id`**                | Property  | ✅ Yes    | Unique NGSI-LD identifier of the observation entity                         | URI (e.g., `urn:ngsi-ld:Observation:001`) |
| **`type`**              | Property  | ✅ Yes    | NGSI-LD entity type (must be `"Observation"`)                               | `"Observation"`                           |
| **`name`**              | Property  | ❌ No     | Name or label assigned to the observation                                   | String                                    |
| **`category`**          | Property  | ❌ No     | represents types of data that can be observed or acted upon in IoT systems, such as environmental metrics (e.g., temperature, airPollution), utility usage (e.g., waterFlow, electricityConsumption), human activity (e.g., occupancy, heartRate), and system status (e.g., doorStatus, fireAlarm). They serve as standard references for consistent data modeling.                         | String (e.g., "Environmental", "Energy")  | 
| **`dateModified`**      | Property  | ❌ No     | Timestamp of the last modification to the observation                       | ISO 8601 Date-Time String                 |
| **`measurement`**       | Property  | ✅ Yes    | Value and unit of the observation (structured object)                       | Object with: `value`, `measurementUnit`   |
|     • `value`           | -         | ✅ Yes    | The numeric value of the measurement                                        | Number                                    |
|     • `measurementUnit` | -         | ✅ Yes    | Unit of measurement                                                         | String (e.g., `"M3S"`, `"°C"`, etc.)      |
| **`measurementType`**   | Property  | ❌ No     | The type of an observation measurement can be classified as either **physical** or **virtual**. A **physical** measurement is obtained directly from a single sensor, whereas a **virtual** measurement is derived or inferred by combining multiple physical measurements.| String (e.g., `virtual`, `physical`|                                   |
| **`externalLink`**      | Property  | ❌ No     | URI linking to an external media file like an image or video                | URI                                       |


