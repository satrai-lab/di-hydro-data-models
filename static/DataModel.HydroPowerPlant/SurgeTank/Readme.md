# Surge Tank
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/SurgeTank.png" 
       alt="SurgeTank Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **SurgeTank** is a protective reservoir in a hydropower conveyance system that mitigates rapid pressure changes (“water hammer”) in penstocks. It temporarily absorbs or supplies water to smooth out pressure surges caused by sudden flow variations, protecting piping and equipment.

## Attributes Specifications

| Attribute                         | Type         | Required | Description                                                                              | Units / Values    |
| --------------------------------- | ------------ | -------- | ---------------------------------------------------------------------------------------- | ----------------- |
| **`id`**                          | Property     | Yes      | Unique URI identifier for the surge tank                                                 | URN format        |
| **`type`**                        | Property     | Yes      | Fixed entity type                                                                        | `"SurgeTank"`     |
| **`name`**                        | Property     | Yes      | Official or common name of the surge tank                                                | String            |
| **`geographicalLocation`**        | GeoProperty  | No       | GeoJSON point indicating the surge tank’s location (longitude, latitude)                 | `[lon, lat]`      |
| **`volumeCapacity`**              | Property     | No       | Total volume the surge tank can accommodate                                              | m³ (cubic meters) |
| **`responseTime`**                | Property     | No       | Time taken for the surge tank to respond to a pressure surge                             | s (seconds)       |
| **`isPartOfHydroPowerPlant`**     | Relationship | No       | Reference to the HydropowerPlant entity or entities this surge tank belongs to           | Array of URIs     |
| **`relievesPressureForPenstock`** | Relationship | No       | Reference to the Penstock entity or entities for which this surge tank relieves pressure | Array of URIs     |
