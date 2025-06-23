
# AE System

<div style="display: flex; justify-content: center; margin: 20px 0">
  <img src="https://github.com/satrai-lab/di-hydro-data-models/blob/main/dynamic/Diagrams/AESystem.png" 
       alt="HydroPowerPlantCommunity Diagram" 
       style="max-width: 100%; height: auto; width: 650px">
</div>


## Definition

An **AE System** (Acoustic Emission System) is a data acquisition and processing platform for structural health and condition monitoring. It interfaces with piezoelectric PZT sensors mounted on a structure, digitizes their high-frequency voltage signals, applies configurable analog and digital filtering, and extracts key features (e.g., amplitude, RMS, energy, average signal level) in real time. It supports both timed and continuous acquisition modes, and can operate on external power or internal battery.

---

## Attributes Specifications

| Attribute                   | Type         | Required | Description                                                                                                     | Units / Values                                                                    |
| --------------------------- | ------------ | -------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **`id`**                    | Property     | Yes      | Unique URI identifier for this AE system                                                                        | URN format (e.g. `urn:ngsi-ld:AESystem:01`)                                       |
| **`type`**                  | Property     | Yes      | Fixed entity type                                                                                               | `"AESystem"`                                                                      |
| **`frequencyBandwidthMin`** | Property     | No       | Minimum frequency bandwidth the system can capture                                                              | Object with:<br>• `value`: number<br>• `unitCode`: `"kHz"`                        |
| **`frequencyBandwidthMax`** | Property     | No       | Maximum frequency bandwidth the system can capture                                                              | Object with:<br>• `value`: number<br>• `unitCode`: `"kHz"`                        |
| **`acquisitionMode`**       | Property     | No       | Supported acquisition modes                                                                                     | Object with:<br>• `value`: `"Timed"`, `"Continuous"`, or `"Timed and Continuous"` |
| **`samplingRate`**          | Property     | No       | Maximum ADC sampling rate                                                                                       | Object with:<br>• `value`: number<br>• `unitCode`: `"1/s"`                        |
| **`systemNoise`**           | Property     | No       | System self-noise level                                                                                         | Object with:<br>• `value`: number<br>• `unitCode`: `"dB"`                         |
| **`samplingLength`**        | Property     | No       | Maximum number of samples captured per acoustic-event hit                                                       | Object with:<br>• `value`: integer<br>• `unitCode`: `"count"`                     |
| **`analogueFilterMin`**     | Property     | No       | Lower cutoff frequency of the analog anti-aliasing filter                                                       | Object with:<br>• `value`: number<br>• `unitCode`: `"kHz"`                        |
| **`analogueFilterMax`**     | Property     | No       | Upper cutoff frequency of the analog anti-aliasing filter                                                       | Object with:<br>• `value`: number<br>• `unitCode`: `"kHz"`                        |
| **`digitalFilterMin`**      | Property     | No       | Lower cutoff frequency of the digital signal-processing filter                                                  | Object with:<br>• `value`: number<br>• `unitCode`: `"kHz"`                        |
| **`digitalFilterMax`**      | Property     | No       | Upper cutoff frequency of the digital signal-processing filter                                                  | Object with:<br>• `value`: number<br>• `unitCode`: `"kHz"`                        |
| **`dataOutput`**            | Property     | No       | Comma-separated list of computed AE features                                                                    | Object with:<br>• `value`: string (e.g. `"Amplitude,RMS,Energy,ASL"`)             |
| **`temperatureMin`**        | Property     | No       | Minimum ambient operating temperature                                                                           | Object with:<br>• `value`: number<br>• `unitCode`: `"CEL"`                        |
| **`temperatureMax`**        | Property     | No       | Maximum ambient operating temperature                                                                           | Object with:<br>• `value`: number<br>• `unitCode`: `"CEL"`                        |
| **`powerSupply`**           | Property     | No       | Nominal system power-supply voltage                                                                             | Object with:<br>• `value`: number<br>• `unitCode`: `"V"`                          |
| **`powerMode`**             | Property     | No       | Power-source configuration (external, battery, or both)                                                         | Object with:<br>• `value`: `"External"`, `"Battery"`, or `"External or Battery"`  |
| **`chargingVoltage`**       | Property     | No       | Internal-battery charging voltage                                                                               | Object with:<br>• `value`: number<br>• `unitCode`: `"V"`                          |
| **`operatingVoltage`**      | Property     | No       | Internal-battery operating voltage                                                                              | Object with:<br>• `value`: number<br>• `unitCode`: `"V"`                          |
| **`sleepModeCurrent`**      | Property     | No       | Current draw when in low-power (sleep) mode                                                                     | Object with:<br>• `value`: number<br>• `unitCode`: `"mA"`                         |
| **`hasComponent`**          | Relationship | No       | References to **AE PZT Sensor** entities that are part of this AE system                                        | Array of URIs (e.g. `["urn:ngsi-ld:AEPZTSensor:001"]`)                            |
| **`hasObservation`**        | Relationship | No       | References to **Observation** entities (i.e., AE event records or waveform captures) produced by this AE system | Array of URIs (e.g. `["urn:ngsi-ld:Observation:obsAE001"]`)                       |

---

