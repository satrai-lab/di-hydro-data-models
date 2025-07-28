# Generic Device

> **Base Data Model:**
> This **Device** schema is the foundational data model for all hydropower‐plant devices in our NGSI-LD framework. Every specialized sensor or actuator (e.g. `AEPZTSensor`, `CrackGrowthSensor`, `AESystem`) **inherits** these core properties.

---

## Definition

A **Device** represents any hardware component—sensor, actuator, or combined sensor/actuator—installed within a hydropower plant. It tracks both its identity and placement within the plant, plus the observations and actuations it produces or controls.

---

## Attribute Specifications

| Attribute                   | NGSI-LD Type | Required | Description                                                                      | Units / Values                                                                                                                                                               |
| --------------------------- | ------------ | -------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`id`**                    | Property     | Yes      | Unique URI identifier of the entity                                              | URN format (e.g. `urn:ngsi-ld:Device:0001`)                                                                                                                                  |
| **`type`**                  | Property     | Yes      | Fixed entity type (must be `Device`)                                             | `"Device"`                                                                                                                                                                   |
| **`name`**                  | Property     | No       | Human-readable name of the device                                                | String                                                                                                                                                                       |
| **`onObject`**              | Relationship | No       | Component(s) of the hydropower plant on which this device is installed           | Array of URIs (e.g. `["urn:ngsi-ld:HydroTurbine:HT-123"]`)                                                                                                                   |
| **`inHPP`**                 | Relationship | No       | Hydropower plant that this device belongs to                                     | Single URI (e.g. `"urn:ngsi-ld:HydropowerPlant:Plant-XYZ"`)                                                                                                                  |
| **`controlledObservation`** | Property     | No       | Types of observations this device can initiate or control                        | Array of strings (e.g. `["Temperature","Vibration"]`)                                                                                                                        |
| **`observations`**          | Relationship | No       | Observation entities produced by or connected to this device                     | Array of URIs (e.g. `["urn:ngsi-ld:Observation:Temp:1001", "urn:ngsi-ld:Observation:Vib:1002"]`)                                                                             |
| **`controlledActuation`**   | Property     | No       | Types of actuations this device can initiate or control                          | Array of strings (e.g. `["ValveOpen","ValveClose"]`)                                                                                                                         |
| **`actuations`**            | Relationship | No       | Actuation entities produced by or connected to this device                       | Array of URIs (e.g. `["urn:ngsi-ld:Actuation:Valve:2001"]`)                                                                                                                  |
| **`deviceType`**            | Property     | No       | Indicates whether this is a sensor, actuator, or both                            | One of `"sensor"`, `"actuator"`, `"sensorActuator"`, `"Device"`, `"System"`                                                                                                  |
| **`relativePosition`**      | Property     | No       | Relative 2D/3D position of the device                                            | Geo‐object with:<br>• `type`: `"Point"`, `"LineString"`, `"Polygon"`, etc.<br>• `measurementUnit` e.g. `"m"`<br>• `dimensions`: `"2D"` or `"3D"`<br>• `coordinates`, `faces` |
| **`status`**                | Property     | No       | The status of the device (e.g. if it functions normally or is under maintenance) | String (e.g. `"normal"`, `"underMaintenance"`)                                                                                                                               |
| **`monitoringType`**        | Property     | No       | Category of monitoring application for this sensor                               | Enum: `"StructuralHealthAndConditionMonitoring"`, `"EnvironmentalMonitoring"`, `"BiodiversityMonitoring"`                                                                    |



---
