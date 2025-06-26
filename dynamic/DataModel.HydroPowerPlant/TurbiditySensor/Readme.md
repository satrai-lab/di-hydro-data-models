# Turbidity Sensor
<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/AESystem.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 650px">
</div>

## Definition

A **Turbidity Sensor** on the platform uses an infrared LED and photodiode to detect light scattered by suspended particles in water. The scattered light is converted to an analog voltage, digitized by a 16-bit ADC, and synchronized with other measurements to provide real-time water-quality data.

> **Inheritance:**
> This entity **inherits** all core properties from the [Device](https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/refs/heads/main/dynamic/DataModel.HydroPowerPlant/GenericDevice/DataModel/type.yaml#/components/schemas/Device) base type (e.g. `id`, `type`, `name`, `onObject`, `inHPP`, `deviceType`, `observations`, etc.), and adds the following specific attributes.


## Attributes Specifications

| Attribute                     | NGSI-LD Type | Description                                            | Units / Values                         |
| ----------------------------- | ------------ | ------------------------------------------------------ | -------------------------------------- |
| **`model`**                   | Property     | Manufacturer’s model number                            | `"ZDYG-2088-01QX"`                     |
| **`measureRangeMin`**         | Property     | Minimum turbidity measurable                           | `{ "value": 0.01, "unitCode": "NTU" }` |
| **`measureRangeMax`**         | Property     | Maximum turbidity measurable                           | `{ "value": 1000, "unitCode": "NTU" }` |
| **`accuracy`**                | Property     | Maximum relative error                                 | `< ±1 % of reading`                    |
| **`pressureRangeMin`**        | Property     | Minimum process pressure                               | `{ "value": 0, "unitCode": "MPA" }`    |
| **`pressureRangeMax`**        | Property     | Maximum process pressure                               | `{ "value": 0.4, "unitCode": "MPA" }`  |
| **`calibration`**             | Property     | Supported calibration methods                          | `["sample", "slope"]`                  |
| **`sensorMaterial`**          | Property     | Wetted-part construction                               | `"SUS316L + PVC"`                      |
| **`cableMaterial`**           | Property     | Exterior cable jacket                                  | `"PVC"`                                |
| **`powerSupply`**             | Property     | Required DC supply voltage                             | `{ "value": 12, "unitCode": "V" }`     |
| **`communicationMode`**       | Property     | Field-bus interface                                    | `"RS485 (Modbus RTU)"`                 |
| **`storageTemperatureMin`**   | Property     | Minimum storage temperature                            | `{ "value": -15, "unitCode": "CEL" }`  |
| **`storageTemperatureMax`**   | Property     | Maximum storage temperature                            | `{ "value": 65, "unitCode": "CEL" }`   |
| **`operatingTemperatureMin`** | Property     | Minimum operating temperature                          | `{ "value": 0, "unitCode": "CEL" }`    |
| **`operatingTemperatureMax`** | Property     | Maximum operating temperature                          | `{ "value": 45, "unitCode": "CEL" }`   |
| **`length`**                  | Property     | Housing length                                         | `{ "value": 60, "unitCode": "MMT" }`   |
| **`diameter`**                | Property     | Housing diameter                                       | `{ "value": 25.6, "unitCode": "MMT" }` |
| **`weight`**                  | Property     | Total device mass                                      | `{ "value": 1.6, "unitCode": "KGM" }`  |
| **`protectionGrade`**         | Property     | Environmental ingress rating                           | `"IP68 / NEMA6P"`                      |
| **`cableLengthStandard`**     | Property     | Standard cable length                                  | `{ "value": 10, "unitCode": "MTR" }`   |
| **`cableLengthMax`**          | Property     | Maximum extendable cable length                        | `{ "value": 100, "unitCode": "MTR" }`  |
| **`isComponentOf`**           | Relationship | Reference to the host **MPG-6099** multiparameter node | `["urn:ngsi-ld:Device:MPG-6099"]`      |

---

