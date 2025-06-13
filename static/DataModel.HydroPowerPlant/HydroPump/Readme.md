# Hydro Pump
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/HydroPump.png" 
       alt="HydroPump Diagram" 
       style="max-width: 100%; height: auto; width: 346px">
</div>

## Definition
A **HydroPump** is a critical component in pumped-storage hydropower systems that moves water between reservoirs at different elevations. It operates in two modes:
1. **Pumping Mode**: Consumes electricity to pump water to a higher reservoir (energy storage)
2. **Generating Mode**: Acts as a turbine to generate electricity when water flows back down

## Attribute Specification 

| Attribute | Type | Required | Description | Units/Values | 
|-----------|------|----------|-------------|--------------|
| **`id`** | Property | Yes | Unique URI identifier | URN format | 
| **`type`** | Property | Yes | Fixed entity type | `"HydroPump"` |
| **`name`** | Property | Yes | The official or common name of the HydroPump | String |
| **`pumpCapacity`** | Property | No | Operational capacity | MW (power) or m³/s (flow) | 
| **`pumpEfficiency`** | Property | No | Energy conversion efficiency | Percentage (PCT) | 
| **`operationalMode`** | Property | No | Current activity state | `Pumping`/`Generating` | 
| **`powerConsumption`** | Property | No | Electricity used in pumping mode | MW |
| **`cycleTime`** | Property | No | Duration for full pumping cycle | Hours (H) | 
| **`PumpWaterTo`** | Relationship | No | Target reservoir(s) | Array of Reservoir URIs |
| **`isPartOfHydrPowerPlant`** | Relationship | No | Parent plant(s) | Array of Plant URIs | 
