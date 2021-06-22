# Imports the Google Cloud Client Library.
from google.cloud import spanner
import os

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=path+"/capacityapi.json"

# Instantiate a client.
spanner_client = spanner.Client()

# Your Cloud Spanner instance ID.
instance_id = "test-instance"

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)

# Your Cloud Spanner database ID.
database_id = "example-db"

# Get a Cloud Spanner database by ID.
database = instance.database(database_id)

# Execute a simple SQL statement.
with database.snapshot() as snapshot:
    results = snapshot.execute_sql("SELECT  * from resources")

    for row in results:
        print(row)