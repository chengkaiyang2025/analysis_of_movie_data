# report_501

### Goals
- Complete an IEEE report.
- Ask the teacher: Do we need to implement all the code?
- Ask the teacher: Do we need to prepare a presentation for the IEEE report?

### Task
#### Main body of the report:
- **Data Collection and Preparation using Data Warehouse (non - trivial): 50%**
    - **Software architecture (Kai)**:
        - Tools for building a traditional data warehouse: MySQL.
        - Scheduling tool: Python (How to schedule).
        - Visualization tools: PyCharm/Datagrip.
        - What tools are commonly used in the industry to build data warehouses.
    - **Concept of data warehouse (Kai)**:
        - Data warehouses in the industry.
        - Full - volume data update and incremental data update.
    - **Subject division (Kai, Kovvy)**:
        - **ODS (Operational Data Store)**:
            - Data sources:
                - CUM: https://www.cs.cmu.edu/~ark/personas/
                - IMDB: https://developer.imdb.com/non - commercial - datasets/
                - https://grouplens.org/datasets/movielens/
                - Dataset from Kaggle: https://www.kaggle.com/code/ibtesama/getting - started - with - a - movie - recommendation - system/input
                - Actors and movies: https://www.kaggle.com/code/mpwolke/imdb - films - by - actor
        - **DWD (Data Warehouse Detail)**: Aggregate data from different sources to form the following subjects:
            - Movie basic information theme (dimension table).
            - Actor basic information theme (dimension table).
            - Production company (dimension table).
            - User ratings (fact table).
            - Movie - actor list (fact table).
        - **ADS (Application Data Store)**: Display, see Data Analysis and Visualization.
- **Data Analysis and Visualization: 40%**
    - Write about 5 - 6 SQL statements at the DWD layer to generate ADS reports. For example:
        - Which types of movies receive higher ratings from users.
        - Which production companies receive higher ratings.
    - Write 3 - 4 Cypher statements in Neo4j for demonstration:
        - Relationships between actors and movies.
        - Actors who cooperate most frequently.
        - Actors who often appear in a certain part.
- **Insight Discovery: 10%**
    - Draw conclusions based on the above analysis.
- **Others: 0% - 10%**
    - Real - time data warehouse and real - time SQL.
    - Real - time SQL

The source code and the report can be hosted on GitHub:

https://github.com/chengkaiyang2025/analysis_of_movie_data/tree/dev

Online tools:

https://www.overleaf.com/project/67cfc947975839344c27f831 
