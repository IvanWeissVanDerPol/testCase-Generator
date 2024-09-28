import logging.config
import json
import os

def setup_logging(default_path='config/logging_config.json', default_level=logging.INFO):
    """Set up logging configuration from a file or use defaults."""
    if os.path.exists(default_path):
        with open(default_path, 'r') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
