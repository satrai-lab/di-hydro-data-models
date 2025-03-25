# Verification of Data Model: Create HydropowerPlant Instance 🚀

## Overview 🌍
This README demonstrates how to verify the HydropowerPlant data model by creating and querying an NGSI‑LD instance that represents the **Ampezzo Hydropower Plant in Italy**, a real‑world hydro power plant. You will learn how to:

- Create the HydropowerPlant instance directly from our defined data model
- Perform both simple and complex queries using the NGSI‑LD API
- Understand the critical role of the JSON‑LD context file in NGSI‑LD data modelling

---
## Introduction to Ampezzo Hydropower Plant
The Ampezzo Hydropower Plant sits in Plan del Sac (municipality of Ampezzo) in Italy’s Friuli‑Venezia Giulia region at roughly 500 m above sea level. 
It captures water from the Alto Tagliamento river and its tributaries, drawn from an elevation of 980 m into the seasonal Lumiei reservoir (a 136 m-high double-curved dam with 51 Mm³ 
usable volume). A 4 km pressure tunnel and metal penstock deliver water to an underground powerhouse, where three horizontal-axis Pelton turbines (each driving a generator) 
convert hydraulic head (~480 m) into electricity.
Commissioned in 1948 and modernized between 2011–2013, Ampezzo produces around 140–150 GWh annually (62.1 MW total) and feeds the 130 kV grid.

---

## Prerequisites 🧰

### 1️⃣ Docker Engine & Docker Compose 🐳

Install Docker Desktop (which bundles Docker Engine + Compose):
- Linux/macOS: https://docs.docker.com/get-docker/
- Windows: https://docs.docker.com/desktop/install/windows-install/

Verify installation:
```bash
docker --version && docker compose version
```

### 2️⃣ WSL2 (Windows only) 💻

If you use **Ubuntu (Linux)**, skip this — you already have a native shell.
If you use **Windows**, **do not install a VM**. Instead:
1. Open Microsoft Store → install **Ubuntu**
2. Launch Ubuntu → create a UNIX username & password
3. Update packages:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

### 3️⃣ Install curl (if missing) 🔧
```bash
sudo apt update && sudo apt install -y curl
curl --version
```

### 4️⃣ Install jq (for pretty‑printing JSON) 📜
```bash
sudo apt update && sudo apt install -y jq
jq --version
```

---
## Launch Orion‑LD + MongoDB 🏭
```bash
git clone https://github.com/satrai-lab/di-hydro-data-models.git
cd di-hydro-data-models/static/Verification
docker-compose up -d
```

> 🔧 **Make sure Docker Engine is already running** — these commands create and start two containers.

Once complete:
- 🏃‍♂️ **Orion‑LD** will be running and listening on **http://localhost:1026**
- 💾 **MongoDB** will be available at **mongodb://localhost:27017**

---

## Create HydropowerPlant instance 🌊⚡
```bash
curl -X POST http://localhost:1026/ngsi-ld/v1/entities \
  -H 'Content-Type: application/ld+json' \
  --data '{
    "@context":"https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Context.jsonld",
    "id":"urn:ngsi-ld:HydropowerPlant:Ampezzo001",
    "type":"HydropowerPlant",
    "name":{"type":"Property","value":"Ampezzo Hydropower Plant"},
    "geographicalLocation":{"type":"GeoProperty","value":{"type":"Point","coordinates":[13.0935,46.3478]}},
    "powerPlantCapacity":{"type":"Property","value":{"value":150,"unitCode":"MW"}},
    "powerplantType":{"type":"Property","value":"Storage/Reservoir"},
    "hasWaterBody":{"type":"Relationship","object":"urn:ngsi-ld:WaterBody:LumieiReservoir"},
    "hasPenstocks":{"type":"Relationship","object":"urn:ngsi-ld:Penstock:AmpezzoMain"},
    "containsTurbines":{"type":"Relationship","object":["urn:ngsi-ld:Turbine:Ampezzo001","urn:ngsi-ld:Turbine:Ampezzo002","urn:ngsi-ld:Turbine:Ampezzo003"]},
    "containsGenerators":{"type":"Relationship","object":["urn:ngsi-ld:Generator:Ampezzo001","urn:ngsi-ld:Generator:Ampezzo002","urn:ngsi-ld:Generator:Ampezzo003"]}
  }'
```
Run that in your Ubuntu shell and you’ll see **201 Created**.

> [!NOTE]
> The `@context` attribute pinpoints exactly the NGSI‑LD data model that we defined [here](https://github.com/satrai-lab/di-hydro-data-models/tree/main/static) (the JSON‑LD context file), Orion‑LD should use it to map between long IRIs and compact names.
> 
---
## Retrieve & pretty‑print 📖
First retrieve the Ampezzo HydropowerPlant entity using the **same @context** so Orion‑LD knows how to compact long IRIs into short names:
```bash
curl -X GET \
  "http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:HydropowerPlant:Ampezzo001" \
  -H 'Accept: application/ld+json' \
  -H 'Link: <https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
```
Pipe into `jq` for readability:
```bash
curl -X GET \
  "http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:HydropowerPlant:Ampezzo001" \
  -H 'Accept: application/ld+json' \
  -H 'Link: <https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
  | jq
```
---
## Extract powerPlantCapacity only ⚡
```bash
curl -s -X GET \
  "http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:HydropowerPlant:Ampezzo001?attrs=powerPlantCapacity" \
  -H 'Accept: application/ld+json' \
  -H 'Link: <https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
  | jq -r '.powerPlantCapacity.value | "\(.value)\(.unitCode)"'
```
**Output:**
```
150MW
```
---
## Count turbines & generators 🔢
```bash
curl -s -X GET \
  "http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:HydropowerPlant:Ampezzo001?attrs=containsTurbines,containsGenerators" \
  -H 'Accept: application/ld+json' \
  -H 'Link: <https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
  | jq -r '"Turbines: \(.containsTurbines.object | length), Generators: \(.containsGenerators.object | length)"'
```
**Output:**
```
Turbines: 3, Generators: 3
```
### Breakdown of the command
1️⃣ **curl part (fetching data)**:
This requests only the two relationship attributes (containsTurbines and containsGenerators) from Orion‑LD, returning raw JSON:
json
{
  "containsTurbines": { "type":"Relationship", "object":[ "...","...","..." ] },
  "containsGenerators": { "type":"Relationship", "object":[ "...","...","..." ] }
}

2️⃣ **Pipe into jq (processing & formatting)**:
jq reads that JSON, counts the number of elements in each object array, and prints a concise human‑readable summary.

---
## Retrieve without context (plain JSON) 📄
```bash
curl -s http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:HydropowerPlant:Ampezzo001 \
  -H 'Accept: application/json' | jq .
```
Since we did **not** supply any @context (neither inline nor via a Link header), Orion‑LD falls back to its **Core context** when answering the GET request. Because the Core context has no knowledge of our custom property names, it cannot compact full IRIs into short attribute names. Instead, you see the **expanded IRIs** for every attribute in the output.

This contrasts with retrieving via application/ld+json **with** a custom context — which returns short, human‑friendly names by compacting IRIs according to your JSON‑LD context file.

---

## Importance of context file ❗✨

### Invalid instance (missing required “name”) ❌
According to our HydropowerPlant model, **name** is a required attribute. You might expect Orion‑LD to reject an entity missing it:

🐙 **Command:**
```bash
curl -i -X POST http://localhost:1026/ngsi-ld/v1/entities \
  -H 'Content-Type: application/ld+json' \
  --data '{
    "@context":"https://raw.githubusercontent.com/satrai-lab/di-hydro-data-models/main/static/Context.jsonld",
    "id":"urn:ngsi-ld:HydropowerPlant:Invalid001",
    "type":"HydropowerPlant"
  }'
```

#### Expected response (if validation were enforced) ✅
```http
HTTP/1.1 400 Bad Request
{
  "type":"https://uri.etsi.org/ngsi-ld/errors/BadRequestData",
  "title":"invalid value for attribute name",
  "detail":"The attribute 'name' is required for type HydropowerPlant"
}
```

#### Real response from Orion‑LD 🚀
```http
HTTP/1.1 201 Created
```

Because Orion‑LD’s default behavior is **schema‑agnostic**, it accepts any valid NGSI‑LD JSON. The context file only maps attribute names to IRIs and defines their meaning — it does **not** enforce required fields or type constraints.

> [!IMPORTANT]
> **The context file defines semantics and interoperability, not validation rules.**_

