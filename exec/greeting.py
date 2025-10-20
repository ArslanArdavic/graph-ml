import neptune
from neptune.integrations.python_logger import NeptuneHandler
import logging
import argparse
import os


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, default="Hello, Neptune!")
    args = parser.parse_args()

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Initialize Neptune run, add handler and cmd args
    run = neptune.init_run(
        project="ALLab-Boun/graph-ml",
        api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiJjYjlhZjMxMS1mZjgyLTQ4Y2YtYmY5ZC1mMjVjOWU2YmI4YWMifQ==",
        name="Greeting",
        description="Simple greeting script",
        tags=["Hello World"],
    )
    
    # Set default logging information
    logger.addHandler(NeptuneHandler(run=run))
    run["cmd-args"] = args
    
    # Make sure these are non-empty strings
    job_id = os.environ.get("SLURM_ARRAY_JOB_ID") or os.environ.get("SLURM_JOB_ID") or "UNKNOWN"
    stdout_path = os.environ.get("SLURM_STDOUT_PATH") or f"slurm/log/greeting_{job_id}.out"
    stderr_path = os.environ.get("SLURM_STDERR_PATH") or f"slurm/log/greeting_{job_id}.err"

    # Log as a small namespace/dict (shows in metadata even if values are empty strings)
    run["slurm"] = {
        "job_id": job_id,
        "stdout_path": stdout_path,
        "stderr_path": stderr_path,
    }


    logger.info("Hello, Neptune!")

    run.stop()