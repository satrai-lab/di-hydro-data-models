# Data Model Description

![hydropowerplant_dataModel](https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/hydropower_plant_model.png)

## HydropowerPlant


-  `id`: Unique identifier of the Hydropower Plant
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be HydropowerPlant. One of : `HydropowerPlant`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The name of the Hydropower Plant
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the hydropower plant’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `address`: Address of the Hydropower Plant
   -  Attribute type: **Property**. 
   -  Optional
-  `size`: Electric capacity category with range interval and standard information.
   -  Attribute type: **Property**. 
   -  Optional
-  `powerPlantCapacity`: The power production capacity of the plant (in MW)
   -  Attribute type: **Property**. 
   -  Optional
-  `powerplantType`: Type of hydropower plant (e.g., storage/reservoir, Run-of-River, pumped storage, in-stream)
   -  Attribute type: **Property**. 
   -  Optional
-  `conversionEfficiency`: Conversion efficiency percentage (typically 90-95%)
   -  Attribute type: **Property**. 
   -  Optional
-  `averageWaterFlow`: Average historical water flow (in cubic meters per second)
   -  Attribute type: **Property**. 
   -  Optional
-  `hasHydroPumps`: Array of HydroPump entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasDams`: Array of Dam entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `containsGenerators`: Array of Generator entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasGovernors`: Array of Governor entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `containsTurbines`: Array of Turbine entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasIntakes`: Array of Intake entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasPowerHouses`: Array of PowerHouse entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasPenstocks`: Array of Penstock entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasValve`: Array of Valve entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasValveHouse`: Array of ValveHouse entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasWaterBody`: Array of WaterBody entity identifiers (river, lake, or reservoir)
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasSurgeTank`: Array of SurgeTank entity identifiers
   -  Attribute type: **Relationship**. 
   -  Optional



## CatchmentArea


-  `id`: Unique identifier of the WaterBody
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be CatchmentArea. One of : `CatchmentArea`.
   -  Attribute type: **Property**. 
   -  Required
-  `area`: The total area of the catchment in square kilometers
   -  Attribute type: **Property**. 
   -  Optional
-  `annualPrecipitationVolume`: The total volume of rainfall collected annually in the catchment area (in cubic meters)
   -  Attribute type: **Property**. 
   -  Optional
-  `seasonalRainfallDistribution`: Breakdown of how the annual precipitation is distributed across different seasons
   -  Attribute type: **Property**. 
   -  Optional
-  `soilType`: Classification of soil in the catchment area
   -  Attribute type: **Property**. 
   -  Optional
-  `vegetationCover`: Information on the types and extent of vegetation in the catchment
   -  Attribute type: **Property**. 
   -  Optional
-  `flowVariationProfile`: Data describing how water flow varies throughout the year
   -  Attribute type: **Property**. 
   -  Optional
-  `suppliesWaterToWaterBody`: Array of references to Water Body entities that are supplied by this catchment area
   -  Attribute type: **Relationship**. 
   -  Optional
-  `suppliesWaterToHydroPowerPlant`: Array of references to HydropowerPlant entities that are supplied by this catchment area
   -  Attribute type: **Relationship**. 
   -  Optional



## WaterBody


-  `id`: Unique identifier of the WaterBody
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be WaterBody. One of : `WaterBody`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The name of the WaterBody
   -  Attribute type: **Property**. 
   -  Required
-  `waterBodyCategory`: Indicates whether the water body is a River, Lake, Reservoir, or Other. One of : `River`, `Lake`, `Reservoir`, `Other`.
   -  Attribute type: **Property**. 
   -  Optional
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the water body’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `dimensions`: Physical dimensions of the water body. Note: Not all nested properties may be applicable to every type of water body.
   -  Attribute type: **Property**. 
   -  Optional
-  `waterFlowCharacteristics`: Flow characteristics of the water body
   -  Attribute type: **Property**. 
   -  Optional
-  `waterLevel`: Water level data
   -  Attribute type: **Property**. 
   -  Optional
-  `waterQuality`: Key water quality parameters
   -  Attribute type: **Property**. 
   -  Optional
-  `environmentalIndicators`: Environmental and ecological indicators
   -  Attribute type: **Property**. 
   -  Optional
-  `operationalData`: Operational data such as flood risk and water rights
   -  Attribute type: **Property**. 
   -  Optional
-  `isFedBy`: Array of references to the CatchmentArea entities that feed this water body
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entities of which this water body is a part
   -  Attribute type: **Relationship**. 
   -  Optional



## Reservoir


-  `id`: Unique identifier of the WaterBody
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be WaterBody. One of : `WaterBody`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The name of the WaterBody
   -  Attribute type: **Property**. 
   -  Required
-  `waterBodyCategory`: Indicates whether the water body is a River, Lake, Reservoir, or Other. One of : `River`, `Lake`, `Reservoir`, `Other`.
   -  Attribute type: **Property**. 
   -  Optional
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the water body’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `dimensions`: Physical dimensions of the water body. Note: Not all nested properties may be applicable to every type of water body.
   -  Attribute type: **Property**. 
   -  Optional
-  `waterFlowCharacteristics`: Flow characteristics of the water body
   -  Attribute type: **Property**. 
   -  Optional
-  `waterLevel`: Water level data
   -  Attribute type: **Property**. 
   -  Optional
-  `waterQuality`: Key water quality parameters
   -  Attribute type: **Property**. 
   -  Optional
-  `environmentalIndicators`: Environmental and ecological indicators
   -  Attribute type: **Property**. 
   -  Optional
-  `operationalData`: Operational data such as flood risk and water rights
   -  Attribute type: **Property**. 
   -  Optional
-  `isFedBy`: Array of references to the CatchmentArea entities that feed this water body
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entities of which this water body is a part
   -  Attribute type: **Relationship**. 
   -  Optional
-  `storageCapacity`: Total volume of water that can be stored (in cubic meters)
   -  Attribute type: **Property**. 
   -  Optional
-  `inflowCharacteristics`: Details about the water inflow regulation
   -  Attribute type: **Property**. 
   -  Optional
-  `outflowControl`: Data regarding controlled water release
   -  Attribute type: **Property**. 
   -  Optional
-  `operationalData`: Operational data such as historical water level management
   -  Attribute type: **Property**. 
   -  Optional
-  `hasDams`: Array of references to the dams of the reservoir
   -  Attribute type: **Relationship**. 
   -  Optional
-  `feedsIntakes`: Array of references to the intakes that the reservoir feeds
   -  Attribute type: **Relationship**. 
   -  Optional



## Dam


-  `id`: Unique identifier of the Dam
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Dam. One of : `Dam`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the Dam
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the dam’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `damHeight`: The vertical height from the dam’s foundation to its crest
   -  Attribute type: **Property**. 
   -  Optional
-  `damLength`: The horizontal span or width of the dam
   -  Attribute type: **Property**. 
   -  Optional
-  `constructionMaterials`: The primary materials used in constructing the dam (e.g., concrete, earth-fill). One of : `Concrete`, `Earth-fill`, `Rock-fill`, `Masonry`.
   -  Attribute type: **Property**. 
   -  Optional
-  `structuralDesignParameters`: Contains the key parameter Structural Type which defines the dam’s design
   -  Attribute type: **Property**. 
   -  Optional
-  `yearOfConstruction`: The year the dam was built
   -  Attribute type: **Property**. 
   -  Optional
-  `hasSpillway`: Array of references to the Spillway entity that is part of the dam's design to safely release excess water
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasintakes`: Array of references to the intake entities that is part of the dam
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfReservoir`: Array of references to the Reservoir entity that is supplied by this dam
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfHydroPlant`: Array of references to the HydropowerPlant entity that this dam is a component of
   -  Attribute type: **Relationship**. 
   -  Optional



## Spillway


-  `id`: Unique identifier of the Spillway
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Spillway. One of : `Spillway`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the Spillway
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the spillway’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `dischargeCapacity`: The maximum water discharge capacity of the spillway.
   -  Attribute type: **Property**. 
   -  Optional
-  `designFlowRate`: The flow rate that the spillway is engineered to handle under normal operating conditions.
   -  Attribute type: **Property**. 
   -  Optional
-  `spillwayType`: The classification or design type of the spillway. One of : `Chute Spillway`, `Side-Channel Spillway`, `Fuse Plug Spillway`.
   -  Attribute type: **Property**. 
   -  Optional
-  `crestElevation`: The elevation of the spillway's crest, which is critical for determining when it will begin to operate
   -  Attribute type: **Property**. 
   -  Optional
-  `spillwayClassification`: Indicates whether the spillway is a Principal Spillway (for regular operation) or an Emergency Spillway (for safety during extreme conditions). One of : `Principal`, `Emergency`.
   -  Attribute type: **Property**. 
   -  Optional



## HydroPump


-  `id`: Unique identifier of the HydroPump
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be HydroPump. One of : `HydroPump`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the HydroPump
   -  Attribute type: **Property**. 
   -  Required
-  `pumpCapacity`: The capacity of the pump, defined either as a volumetric flow rate (in m³/s) or as a power capacity (in MW) if the pump operates reversibly.
   -  Attribute type: **Property**. 
   -  Optional
-  `pumpEfficiency`: The efficiency of the pump, expressed as a percentage.
   -  Attribute type: **Property**. 
   -  Optional
-  `operationalMode`: Mode of operation of the pump: 'Pumping' when using electricity to lift water, or 'Generating' when producing electricity.. One of : `Pumping`, `Generating`.
   -  Attribute type: **Property**. 
   -  Optional
-  `powerConsumption`: The electrical power consumed by the pump when operating in pumping mode (in MW).
   -  Attribute type: **Property**. 
   -  Optional
-  `cycleTime`: The duration required to complete one full pumping cycle (in hours).
   -  Attribute type: **Property**. 
   -  Optional
-  `PumpWaterTo`: Array of references to Reservoir entities to which water is pumped
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfHydrPowerPlant`: Array of references to HydropowerPlant entities that this HydroPump is a component of
   -  Attribute type: **Relationship**. 
   -  Optional



## Intake


-  `id`: Unique identifier of the Intake
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Intake. One of : `Intake`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name for the Intake
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the intake’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `intakeStructureType`: Specifies the design or configuration of the intake (e.g., open channel, gated, screened, or submerged intake)
   -  Attribute type: **Property**. 
   -  Optional
-  `waterFlowRate`: Indicates the rate at which water is drawn into the intake (in m³/s)
   -  Attribute type: **Property**. 
   -  Optional
-  `filtrationOrDebrisControl`: Mechanisms (e.g., screens, gratings, or trash racks) used to prevent debris from entering the system
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfDam`: Array of references to the Dam entity that this Intake is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this Intake is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `leadsToPenstocks`: Array of references to the Penstock entity that this Intake leads to
   -  Attribute type: **Relationship**. 
   -  Optional



## Penstock


-  `id`: Unique identifier of the Penstock
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Penstock. One of : `Penstock`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the Penstock
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the penstock’s starting location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `length`: The physical length of the penstock
   -  Attribute type: **Property**. 
   -  Optional
-  `diameter`: The internal diameter of the penstock
   -  Attribute type: **Property**. 
   -  Optional
-  `material`: The construction material of the penstock (e.g., steel, reinforced concrete, or composite materials). One of : `Steel`, `Reinforced Concrete`, `Composite`.
   -  Attribute type: **Property**. 
   -  Optional
-  `designPressure`: The maximum pressure the penstock is engineered to withstand
   -  Attribute type: **Property**. 
   -  Optional
-  `flowCapacity`: The designed maximum flow capacity of the penstock
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this penstock is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToIntake`: Array of references to the Intake entity connected to this penstock
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToSurgeTank`: Array of references to the SurgeTank entity connected to this penstock
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToValve`: Array of references to the Valve entity connected to this penstock
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToValveHouse`: Array of references to the ValveHouse entity connected to this penstock
   -  Attribute type: **Relationship**. 
   -  Optional



## SurgeTank


-  `id`: Unique identifier of the SurgeTank
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be SurgeTank. One of : `SurgeTank`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the SurgeTank
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the surge tank’s location. The first element in coordinates is longitude, and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `volumeCapacity`: The total volume that the surge tank can accommodate (in cubic meters)
   -  Attribute type: **Property**. 
   -  Optional
-  `responseTime`: The time it takes for the surge tank to respond to a pressure surge (in seconds)
   -  Attribute type: **Property**. 
   -  Optional
-  `relievesPressureForPenstock`: Array of references to the Penstock entity that the surge tank relieves pressure for
   -  Attribute type: **Relationship**. 
   -  Optional



## ValveHouse


-  `id`: Unique identifier of the ValveHouse
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be ValveHouse. One of : `ValveHouse`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the ValveHouse
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the location of the ValveHouse. The first element in coordinates is longitude and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this ValveHouse is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `containsValves`: Array of references to Valve entities contained within this ValveHouse
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToPenstock`: Array of references to the Penstock entity connected to this ValveHouse
   -  Attribute type: **Relationship**. 
   -  Optional



## Valve


-  `id`: Unique identifier for the valve
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Valve. One of : `Valve`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the valve
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' indicating the physical location of the valve (e.g., along the penstock or within the valve house).
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `valveType`: Classification or design of the valve. One of : `Gate Valve`, `Butterfly Valve`, `Ball Valve`, `Sluice Gate`.
   -  Attribute type: **Property**. 
   -  Optional
-  `material`: Construction material of the valve. One of : `Stainless Steel`, `Cast Iron`, `Composite`.
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this valve is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfValveHouse`: Array of references to the ValveHouse entity that this valve is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToPenstock`: Array of references to the Penstock entity connected to this valve
   -  Attribute type: **Relationship**. 
   -  Optional



## Turbine


-  `id`: Unique identifier of the Turbine
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Turbine. One of : `Turbine`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the Turbine
   -  Attribute type: **Property**. 
   -  Required
-  `turbineType`: Classification of the turbine (e.g., Francis, Kaplan, Pelton, or other types). One of : `Francis`, `Kaplan`, `Pelton`, `Other`.
   -  Attribute type: **Property**. 
   -  Required
-  `capacity`: Rated power capacity of the turbine (in MW)
   -  Attribute type: **Property**. 
   -  Optional
-  `efficiency`: Conversion efficiency of the turbine (in percentage)
   -  Attribute type: **Property**. 
   -  Optional
-  `operatingFlowRate`: Water flow rate required for the turbine's operation (in m³/s)
   -  Attribute type: **Property**. 
   -  Optional
-  `head`: Effective head (vertical drop) available across the turbine (in meters)
   -  Attribute type: **Property**. 
   -  Optional
-  `manufacturer`: Name or details of the manufacturer of the turbine
   -  Attribute type: **Property**. 
   -  Optional
-  `yearOfInstallation`: The year when the turbine was installed
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this Turbine is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `drivesGenerators`: Array of references to the Generator entities driven by this Turbine
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfPowerHouse`: Array of references to the PowerHouse entity that houses this Turbine
   -  Attribute type: **Relationship**. 
   -  Optional
-  `controlledByGovernor`: Array of references to the Governor entity that controls this Turbine
   -  Attribute type: **Relationship**. 
   -  Optional



## Generator


-  `id`: Unique identifier of the Generator
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Generator. One of : `Generator`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the Generator
   -  Attribute type: **Property**. 
   -  Required
-  `ratedCapacity`: The rated electrical capacity of the generator (in MW). Short Explanation: It indicates the maximum power output the generator is designed to produce under normal operating conditions.
   -  Attribute type: **Property**. 
   -  Optional
-  `efficiency`: The conversion efficiency of the generator, expressed as a percentage.
   -  Attribute type: **Property**. 
   -  Optional
-  `manufacturer`: The name or details of the manufacturer of the generator
   -  Attribute type: **Property**. 
   -  Optional
-  `yearOfInstallation`: The year when the generator was installed
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this Generator is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isDrivenByTurbines`: Array of references to the Turbine entities that drive this Generator
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfPowerHouse`: Array of references to the PowerHouse entity that houses this Generator
   -  Attribute type: **Relationship**. 
   -  Optional



## Governor


-  `id`: Unique identifier of the Governor
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be Governor. One of : `Governor`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the Governor
   -  Attribute type: **Property**. 
   -  Required
-  `controlParameters`: Key control settings that determine how the governor regulates the turbine. At least one parameter should be provided.
   -  Attribute type: **Property**. 
   -  Optional
-  `responseTime`: The time it takes for the governor to react to changes in load or turbine speed.
   -  Attribute type: **Property**. 
   -  Optional
-  `manufacturer`: The name or details of the manufacturer of the governor
   -  Attribute type: **Property**. 
   -  Optional
-  `yearOfInstallation`: The year when the governor was installed
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this Governor is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `controlsTurbine`: Array of references to the Turbine entity (or entities) controlled by this Governor
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isPartOfPowerHouse`: Array of references to the PowerHouse entity that houses this Governor
   -  Attribute type: **Relationship**. 
   -  Optional



## PowerHouse


-  `id`: Unique identifier of the PowerHouse
   -  Attribute type: **Property**. 
   -  Required
-  `type`: NGSI Entity type. It has to be PowerHouse. One of : `PowerHouse`.
   -  Attribute type: **Property**. 
   -  Required
-  `name`: The official or common name of the PowerHouse
   -  Attribute type: **Property**. 
   -  Required
-  `geographicalLocation`: GeoJSON property of type 'Point' representing the location of the PowerHouse. The first element in coordinates is longitude and the second is latitude.
   -  Attribute type: **GeoProperty**. 
   -  Optional
-  `address`: The physical address of the PowerHouse
   -  Attribute type: **Property**. 
   -  Optional
-  `buildingArea`: The total floor area of the PowerHouse (in square meters)
   -  Attribute type: **Property**. 
   -  Optional
-  `numberOfFloors`: The number of floors or levels within the PowerHouse
   -  Attribute type: **Property**. 
   -  Optional
-  `isPartOfHydroPowerPlant`: Array of references to the HydropowerPlant entity that this PowerHouse is part of
   -  Attribute type: **Relationship**. 
   -  Optional
-  `containsGenerators`: Array of references to the Generator entities contained in the PowerHouse
   -  Attribute type: **Relationship**. 
   -  Optional
-  `containsTurbines`: Array of references to the Turbine entities contained in the PowerHouse
   -  Attribute type: **Relationship**. 
   -  Optional
-  `isConnectedToPenstock`: Array of references to the Penstock entities connected to the PowerHouse
   -  Attribute type: **Relationship**. 
   -  Optional
-  `hasGovernors`: Array of references to the Governor entities present in the PowerHouse
   -  Attribute type: **Relationship**. 
   -  Optional



## Examples

### OK


