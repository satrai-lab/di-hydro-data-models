## Ultrasonic Transducer
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/UltrasonicTransducer.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 600px">
</div>

----

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/BiofoulingSystem.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 700px">
</div>



## **Definition**

The **Ultrasonic Transducer** is a piezoelectric component that converts electrical signals from an ultrasonic generator into mechanical ultrasonic vibrations. When driven, it emits high-frequency sound waves through submerged surfaces, creating cavitation bubbles that disrupt biofouling. These transducers are waterproof, mountable directly on metal structures, and tuned to specific resonant frequencies for optimal antifouling performance. As an NGSI-LD entity, it inherits all common **Device** attributes.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


### Attribute Specifications

| **Attribute**           | **NGSI-LD Type** | **Description**                                               | **Units / Values**                                            |
| ----------------------- | ---------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| **`id`**                | Identifier       | Unique URI identifier                                         | e.g. `urn:ngsi-ld:UltrasonicTransducer:001`                   |
| **`type`**              | Type             | Fixed entity type                                             | `"UltrasonicTransducer"`                                      |
| **`status`**            | Property         | Operational status                                            | e.g. `"receiving_signal"`, `"idle"`                           |
| **`model`**             | Property         | Device model                                                  | e.g. `"UTX-40PZ"`                                             |
| **`manufacturer`**      | Property         | Manufacturer name                                             | e.g. `"PiezoWave Technologies"`                               |
| **`resonantFrequency`** | Property         | Operating frequency                                           | Object `{ value: number, unitCode: "kHz" }`                   |
| **`powerRating`**       | Property         | Maximum power handling                                        | Object `{ value: number, unitCode: "W" }`                     |
| **`material`**          | Property         | Main construction material                                    | e.g. `"Piezoelectric ceramic"`                                |
| **`mountType`**         | Property         | Installation method                                           | `"adhesive"`, `"magnetic"`                                    |
| **`diameter`**          | Property         | Transducer face diameter                                      | Object `{ value: number, unitCode: "MMT" }`                   |
| **`thickness`**         | Property         | Transducer thickness                                          | Object `{ value: number, unitCode: "MMT" }`                   |
| **`protectionGrade`**   | Property         | Ingress protection rating                                     | e.g. `"IP68"`                                                 |
| **`controlledBy`**      | Relationship     | Reference to the Ultrasonic Generator driving this transducer | Array of URIs, e.g. `["urn:ngsi-ld:UltrasonicGenerator:001"]` |

