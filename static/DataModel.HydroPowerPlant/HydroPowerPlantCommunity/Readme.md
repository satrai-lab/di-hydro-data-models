# Hydro Power Plant Commmunity

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Diagrams/HydroPowerPlantCommunity.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 346px">
</div>

## Definition
The **HydroPowerCommunity** entity represents an **organization**, **consortium**, or **company** that owns/manages one or more hydropower plants. It serves as the central administrative and strategic unit responsible for coordinating resources, compliance, and operations across its portfolio of plants

## Attribute Specifications

| Attribute Name             | Type        | Required | Description & Importance                                                                                             |
|----------------------------|-------------|----------|---------------------------------------------------------------------------------------------------------------------|
| **`id`**                   | Property    | Yes      | Unique identifier for the community. Critical for data integrity, relationships, and avoiding duplication.           |
| **`type`**                 | Property    | Yes      | Fixed value `'Community'`. Explicitly classifies the entity type for system consistency and filtering.              |
| **`name`**                 | Property    | Yes      | Official name of the organization. Identifies the entity in legal, regulatory, and operational contexts.            |
| **`region`**               | Property    | No       | Geographic/administrative coverage. Links plants to regulatory jurisdictions and regional grids.                    |
| **`establishedYear`**      | Property    | No       | Year the community was founded. Indicates institutional experience for stakeholders/investors.                      |
| **`totalInstalledCapacity`**| Property    | No       | Combined rated capacity of all plants (MW). Measures scale for grid contribution and investment.                     |
| **`totalAnnualEnergyOutput`**| Property  | No       | Combined yearly energy production (kWh). Key metric for revenue forecasting and sustainability reporting.           |
| **`governanceModel`**      | Property    | No       | Organizational structure (e.g., cooperative, public utility). Explains decision-making hierarchy to stakeholders.    |
| **`contactEmail`**         | Property    | No       | Primary administrative contact. Critical for stakeholder communication and emergency coordination.                  |
| **`websiteURL`**           | Property    | No       | Official information portal. Provides public transparency and resource access.                                      |
| **`hasHPP`**               | Relationship| No       | Links to HydropowerPlant entities. Core relationship enabling portfolio management and operational analytics.        |


### Key Notes:
1. **Required Attributes**: Only `id`, `type`, and `name` are mandatory - essential for basic entity identification.
2. **Optional Attributes**: 
   - Operational metrics (`totalInstalledCapacity`, `totalAnnualEnergyOutput`) can be added as plants come online
   - Descriptive fields (`region`, `governanceModel`) support stakeholder reporting
3. **Relationship Flexibility**: 
   - `hasHPP` optionality accommodates new communities without plants
   - Allows smooth ownership transfers between communities
4. **Type Enforcement**: Fixed `type='Community'` enables easy filtering in multi-entity systems.
