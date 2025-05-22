# Future Hydropower Plant Data Model Enhancements

This document lists **new properties & entities** we plan to add to our HPP NGSI‑LD data model. All of these additions are **based on data provided by our pilot
installations**.Each entry includes:

- Property name (snake_case)

- Entity it belongs to

- Description in simple English

- Unit (if applicable)

---

## HydroPowerPlant
### **HydropowerPlant — Additional Properties:**  
- **commissioningYear**:  
  The calendar year when the plant first began operation   

- **rehabilitationYear**:  
 The calendar year when the plant underwent its most recent full rehabilitation    

- **installedCapacity**:  
  The plant’s total rated electrical capacity (MW)   

- **annualEnergyOutput**:   
  The average total energy the plant produces per year (kWh)    

- **ecologicalDischarge**:  
   Minimum flow always released downstream to keep the river healthy (m³/s)   

- **maxTailwaterLevel**:  
   Highest water‑surface elevation downstream of the turbines above mean sea level (m)    

- **grossHead**:  
  Total vertical drop from reservoir water surface to the turbine inlet before losses — the full height of water available for power generation (m)  


### **Properties to be removed:**  
- **averageWaterFlow** :  
  this describes the river’s natural flow rate and belongs on the **CatchmentArea (or waterBody) entity**, not on **HydropowerPlant**.

### **Additional Relationships (HydropowerPlant):**  
**partOfCommunity** → Community  
**hasTransformers** → Transformer  
**hasPressureTunnel** → PressureTunnel  
**boostedByPumpingStation** → PumpingStation  
Indicates which pumping station(s) increase this plant’s generation by feeding water back upstream.

---

## Reservoir 
### Additional Properties  

- **maxReservoirLevel**:  
   Highest allowed water surface elevation in the reservoir (m above sea level)  
- **normalReservoirLevel**:  
   Usual operating water surface elevation in the reservoir (m above sea level)  
- **reservoirLength**:  
   Distance the reservoir extends upstream from the dam at its normal level (km).  
  _This already mentioned in the dimensions attribute of the waterBody entity that the Reservoir inherents._  
- **maximumEnergeticVolume**:  
   Total potential energy contained in the stored water when the reservoir is full (GWh)  
- **reservoirType**:  
   Classification of reservoir operation (e.g., seasonal, weekly, daily)  

- **reservoirVolumes**:  
   Historical record of storage capacity over time — an array of objects, each containing:  
  - **year**: Measurement year  
  - **grossVolume**: Total storage capacity at normal level in that year (m³)  
  - **usefulVolume**: Usable storage capacity for power generation at normal level in that year (m³)  

Example value for **reservoirVolumes**:  
```json
"reservoirVolumes": [
  { "year": 1954, "grossVolume": 16000000, "usefulVolume": 16000000 },
  { "year": 2018, "grossVolume": 4140000, "usefulVolume": 4140000 }
]
```
### Additional Relationships  
- **hasPressureTunnel → PressureTunnel**    
Indicates which pressure tunnel(s) carry water from this reservoir downstream.

- **fedByPumpingStation → PumpingStation**  
Indicates which pumping station(s) deliver water into this reservoir.

---

## Dam 
### Additional Properties  

- **damType**:  
  Structural design of the dam (e.g., “Concrete Gravity”, “Arch Dam”, “Embankment Dam”)  
- **damCrestElevation**:  
  Elevation of the top of the dam above mean sea level (m)
  
> [!NOTE]
> Remove the existing `structuralDesignParameters` property (and its nested `structuralType`) in favor of the single, flat **damType** attribute to avoid redundancy and simplify the model.

---

## Turbine 
### Additional Properties  

- **numberOfImpellers**:  
  The number of water‑moving blades ("buckets") inside the turbine. 
- **axis**:  
  The orientation of the turbine shaft, indicating whether it is horizontal or vertical.
- **maxPower**:  
  The highest possible mechanical power the turbine can generate under extreme conditions, measured in megawatts. (Unit: MW, unit code: MW)  
  _It's different from the capacity which is normal, guaranteed output_
- **speed**:  
  The rated rotational speed of the turbine shaft, measured in revolutions per minute. (Unit: RPM, unit code: RPM)

### **Additional Relationship**

- **dischargesToReservoir** (Relationship)  
  An **array** of objects, each linking the turbine to a downstream reservoir via its pressure tunnel. Each item contains:
  
  • **tunnelLengthKm**: Length of the pressure tunnel from turbine to reservoir (km)  
  • **object**: NGSI‑LD URI of the target Reservoir entity  

**Example:**  
```json
"dischargesToReservoir": [
    {
      "type": "Relationship",
      "object": "urn:ngsi-ld:Reservoir:001",
      "tunnelLength": {
        "type": "Property",
        "value": 520,
        "unitCode": "KM"
      }
    },
    {
      "type": "Relationship",
      "object": "urn:ngsi-ld:Reservoir:002",
      "tunnelLength": {
        "type": "Property",
        "value": 390,
        "unitCode": "KM"
      }
    }
  ]
```

  ---
## Generator 
### Additional Properties  

- **generatorType**:   
Model or design identifier of the generator
   
- **axis**:   
Orientation of the rotating shaft (Horizontal or Vertical)
   
- **voltageLevel**:   
Voltage at which the generator produces electricity (kilovolts (kV))

- **ratedOutputMVA**:   
Nameplate apparent power capacity under standard conditions (megavolt‑amperes (MVA))
  
- **speed**:   
Rotational speed of the generator shaft (revolutions per minute (RPM))

- **ratedPowerFactor**:   
Ratio of real power to apparent power (unitless)

- **voltageRegulationRange**:   
Allowable percentage variation above or below nominal voltage (%)
  
- **windingInsulationClass**:   
Insulation temperature rating class of the generator windings

---

## Additional Entities
### HydroPowerCommunity
#### Properties  

- **id**: Unique identifier of the community  
- **type**: Must be set to “Community”  
- **name**: Official name of the community  
- **region**: Geographic area or administrative region covered by the community  
- **establishedYear**: Year the community organization was founded  
- **totalInstalledCapacity**: Combined rated capacity of all member plants (MW)  
- **totalAnnualEnergyOutput**: Combined yearly energy production of all member plants (kWh)  
- **governanceModel**: Organizational structure (e.g., cooperative, public utility, private consortium)  
- **contactEmail**: Primary contact email for community administration  
- **websiteURL**: Official website of the community
  
#### Relationships:
- **hasHPP**: Relationship linking to one or more HydropowerPlant entities
---
### PressureTunnel 

#### Properties  
**id**: Unique identifier of the PressureTunnel  
**type**: Must be set to “PressureTunnel”  
**length**: Length of the pressure tunnel between reservoir and penstock (metres (m))  

#### Relationships  
**fromReservoir** → Reservoir  
Links this tunnel to the upstream Reservoir entity.  
**toPenstock** → Penstock  
Links this tunnel to the downstream Penstock entity.  

---

### Transformer 

#### Properties  
- **id**: Unique identifier of the Transformer  
- **type**: Must be set to “Transformer”  
- **transformerSupplier**: Manufacturer of the transformer  
- **ratedPower**: Nameplate apparent‑power capacity under normal operating conditions (megavolt‑amperes (MVA))  
- **regulationRange**: Voltage conversion ratio, expressed as “input kV/output kV” (kilovolts (kV))  

#### Relationships  
- **belongsToGenerator** → Generator  
  Links this transformer to the single Generator it serves.
---

### PumpingStation — Entity Definition  

#### Properties  
- **id**: Unique identifier of the PumpingStation  
- **type**: Must be set to “PumpingStation”  
- **name**: Official name of the pumping station  
- **totalPower**: Total installed motor power capacity (megawatts (MW))  
- **unitCount**: Number of individual pump units (count)  
- **yearlyEnergyConsumption**: Annual electricity consumed by all pumps (kilowatt‑hours (kWh))  
- **estimatedAnnualContribution**: Estimated additional hydropower generation enabled by pumping (megawatt‑hours (MWh))  

#### Relationships  
- **feedsReservoir** → Reservoir  
  Indicates which reservoir this station pumps water into.  
- **increasesProductionAt** → HydropowerPlant  
  Links to the hydropower plant whose generation is boosted by this pumping station.




  
