# Transformer
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/Transformer.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 350px">
</div>

## Definition

A **Transformer** in a hydropower plant is an electrical device that steps up or steps down the generator’s voltage to the appropriate transmission or distribution level. It consists of primary and secondary windings around a magnetic core, enabling efficient voltage conversion while maintaining power balance.

## Attributes Specifications

| Attribute                 | Type         | Required | Description                                                                | Units / Format         |
| ------------------------- | ------------ | -------- | -------------------------------------------------------------------------- | ---------------------- |
| **`id`**                  | Property     | Yes      | Unique URI identifier for the transformer                                  | URN format             |
| **`type`**                | Property     | Yes      | Fixed entity type                                                          | `"Transformer"`        |
| **`transformerSupplier`** | Property     | No       | Manufacturer or supplier of the transformer                                | String                 |
| **`ratedPower`**          | Property     | No       | Nameplate apparent-power capacity under normal operating conditions        | MVA (megavolt-amperes) |
| **`regulationRange`**     | Property     | No       | Voltage conversion ratio expressed as input kV/output kV                   | KV (kilovolts)         |
| **`belongsToGenerator`**  | Relationship | No       | Reference to the Generator entity or entities that this transformer serves | Array of URIs          |



