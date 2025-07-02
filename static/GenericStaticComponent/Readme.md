# GenericStaticComponent

## Definition

A **GenericStaticComponent** represents any static structural or infrastructural element of a hydropower plant. It serves as a reusable base model for all physical, non-moving components—such as dams, spillways, intakes, or draft tubes—allowing consistent linking to the hydropower plant entity, devices, observations, and geolocation. This abstraction ensures interoperability and simplifies inheritance when defining specialized components.

---

## Attributes Specifications

| Attribute                 | Type           | Description                                                | Units / Values               |
| ------------------------- | -------------- | ---------------------------------------------------------- | ---------------------------- |
| `id`                      | `Property`     | Unique URI identifier for the component                    | URN format                   |
| `type`                    | `Property`     | Fixed type                                                 | `"GenericStaticComponent"`   |
| `name`                    | `Property`     | The name of the component                                  | String                       |
| `isPartOfHydroPowerPlant` | `Relationship` | Links the component to its parent hydropower plant         | URI                          |
| `hasDevices`              | `Relationship` | Links sensors, meters, or embedded systems                 | Array of URIs                |
| `observations`            | `Relationship` | Refers to NGSI-LD Observation entities produced by sensors | Array of URIs                |
| `actuations`              | `Relationship` | Refers to NGSI-LD Actuation entities (e.g., gate opening)  | Array of URIs                |
| `geographicalLocation`    | `GeoProperty`  | Point location of the component in GeoJSON format          | `[lon, lat]` (GeoJSON Point) |
