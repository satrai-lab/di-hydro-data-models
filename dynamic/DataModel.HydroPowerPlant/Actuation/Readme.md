# ⚙️ Actuation Entity

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/Actuation.png" 
       alt="HydroPowerPlantCommunity Actuation Diagram" 
       style="max-width: 100%; height: auto; width: 500px">
</div>

## Definition

The `Actuation` entity represents an action or control command issued by a system to a device or component within an NGSI-LD-enabled infrastructure. This entity is used to log and track control events such as switching, adjusting, or triggering a mechanism based on system decisions or user input.

It captures key details like the command issued, the result of the actuation, execution time, and relationships to the devices or components affected. `Actuation` is essential for enabling reactive and automated behavior in smart systems such as energy grids, hydropower plants, and smart buildings.

---

## Attribute Specifications

| Attribute                | NGSI Type    | Required | Description                                                                                                                                                                                                                  | Units / Values                               |
| ------------------------ | ------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **`id`**                 | Property     | ✅ Yes    | Unique NGSI-LD identifier of the actuation entity                                                                                                                                                                            | URI (e.g., `urn:ngsi-ld:Actuation:001`)      |
| **`type`**               | Property     | ✅ Yes    | NGSI-LD entity type (must be `"Actuation"`)                                                                                                                                                                                  | `"Actuation"`                                |
| **`name`**               | Property     | ❌ No     | Human-readable name or label assigned to the actuation                                                                                                                                                                       | String                                       |
| **`category`**           | Property     | ❌ No     | Represents types of data that can be observed or acted upon in IoT systems, such as environmental metrics, utility usage, human activity, and system status. They serve as standard references for consistent data modeling. | String (e.g., `"Energy"`, `"Environmental"`) |
| **`dateModified`**       | Property     | ❌ No     | Timestamp indicating when the actuation was last updated                                                                                                                                                                     | ISO 8601 Date-Time String                    |
| **`command`**            | Property     | ✅ Yes    | The control instruction or command issued (e.g., `openValve`, `startPump`)                                                                                                                                                   | String                                       |
| **`commandResult`**      | Property     | ❌ No     | Result or output returned after executing the command                                                                                                                                                                        | String                                       |
| **`duration`**           | Property     | ❌ No     | Time taken to execute the command                                                                                                                                                                                            | Number (seconds)                             |
| **`controlsDevices`**    | Relationship | ❌ No     | Relationship to one or more devices that this actuation controls                                                                                                                                                             | Array of URIs                                |
| **`controlsComponents`** | Relationship | ❌ No     | Relationship to one or more components (e.g., turbines, sensors) controlled by this actuation                                                                                                                                | Array of URIs                                |


