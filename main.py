from src.log.log import log
from src.source.get_data import get_data
from src.target.upload import write_data


log("Launch application")
data = get_data()
print(data)
result = write_data(data,"csv")
print("Готово!")



##ToDo
## UseCase A: Create Query
## A.1. Ask DB for metadata (column names and types)
## A.2. Chose columns to get (connect types, etc.)
## A.3. Save Metadata into metadata DB
## A.4. Query data from source DB
## +
## UseCase B: Correct Query
## B.1. Ask DB for metadata (column names and types)
## B.2. Compare new metadata to saved metadata
## B.3. Update metadata DB
## +
## UseCase C: Use Query
## C.1. Ask DB for metadata (column names and types)
## C.2. Compare new metadata to saved metadata
## C.2.5 Ask user to correct the scheme if old!=new, save metadata changes
## C.3 Query data from source DB

