import logging
import json
from datetime import datetime


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


def save_metrics(metrics: dict, path: str):
    with open(path, 'w') as f:
        json.dump(metrics, f, indent=2, default=str)


def load_config(path: str) -> dict:
    import yaml
    with open(path, 'r') as f:
        return yaml.safe_load(f)
