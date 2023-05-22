import mlflow
import pandas as pd

from mlflow.tracking import MlflowClient


EXPERIMENT_NAME = "mlflow-demo"

client = MlflowClient()

# Retrieve Experiment information
EXPERIMENT_ID = client.get_experiment_by_name(EXPERIMENT_NAME).experiment_id

# Retrieve Runs information (parameter 'depth', metric 'accuracy')
ALL_RUNS_INFO = client.list_run_infos(EXPERIMENT_ID)
ALL_RUNS_ID = [run.run_id for run in ALL_RUNS_INFO]
ALL_PARAM = [client.get_run(run_id).data.params["depth"] for run_id in ALL_RUNS_ID]
ALL_METRIC = [client.get_run(run_id).data.metrics["accuracy"] for run_id in ALL_RUNS_ID]

# View Runs information
run_data = pd.DataFrame({"Run ID": ALL_RUNS_ID, "Params": ALL_PARAM, "Metrics": ALL_METRIC})

# Retrieve Artifact from best run
best_run_id = run_data.sort_values("Metrics", ascending=False).iloc[0]["Run ID"]
best_model_path = client.download_artifacts(best_run_id, "classifier")
best_model = mlflow.sklearn.load_model(best_model_path)

# Delete runs (DO NOT USE UNLESS CERTAIN)
for run_id in ALL_RUNS_ID:
    client.delete_run(run_id)

# Delete experiment (DO NOT USE UNLESS CERTAIN)
client.delete_experiment(EXPERIMENT_ID)