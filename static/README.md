# NGSI-LD Data Model for Hydropower Plant

## Overview

This repository contains the **NGSI-LD data model** for a **hydropower plant**, representing an extended model that provides a holistic view of hydropower infrastructure. The model, as depicted in the figure, covers the **static aspects** of a hydropower plant and offers a generalized structure that can be adapted for specific use cases. 

Since each use case may vary, certain scenarios might not include all components defined in this model. The flexibility of this approach allows for customization based on the particular needs of different hydropower systems.

![hydropowerplant_dataModel](https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/Diagrams/hydropower_plant_model.png)

## Model Creation Process
1. **Defining the Data Model (YAML File):**
   - We began by creating a **YAML file** that defines all the necessary components and their key properties.
   - This file is structured to be **comprehensive yet adaptable**, meaning additional properties may be added in future iterations.

2. **Generating the JSON Schema:**
   - Using the YAML file as a reference, we generated the **JSON schema** for the data model.
   - The JSON schema provides a structured representation, but the YAML file remains **more descriptive**.

3. **Creating the Context File:**
   - To generate the NGSI-LD context file, we used the **official FIWARE tool** available at:
     [FIWARE Understanding-At-Context](https://github.com/FIWARE/tutorials.Understanding-At-Context/tree/NGSI-LD)
   - We adapted the setup to be compatible with an **Ubuntu environment** instead of a Windows-based setup.

4. **Running the Commands to Generate Context & Markdown Documentation:**
   - After following the tutorial setup, the following commands were executed:
     
     - **To generate the context file:**
       ```sh
       ./services ngsil types.yaml
       ```
     
     - **To create the Markdown documentation for the data model:**
       ```sh
       ./services markdown types.yaml
       ```
   - The generated Markdown file provides a **detailed description of each component and its properties** in a human-readable format.

## Data Model Components
Each element plays a crucial role in defining the structure and relationships within the hydropower plant data model. You will find a detailed description of each component and its respective properties [here](https://github.com/satrai-lab/di-hydro-data-models/blob/main/static/DataModel_Description/datamodels.md).

---

