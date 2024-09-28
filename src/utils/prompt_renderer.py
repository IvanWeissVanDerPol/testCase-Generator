from jinja2 import Environment, FileSystemLoader
import os
import logging

def render_prompt(template_name: str, variables: dict) -> str:
    """Renders a prompt template with the given variables."""
    templates_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'prompts')
    templates_dir = os.path.abspath(templates_dir)  # Convert to absolute path

    logging.debug(f"Templates directory: {templates_dir}")

    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=False)
    try:
        template = env.get_template(template_name)
        return template.render(variables)
    except Exception as e:
        logging.error(f"Error rendering template {template_name}: {e}")
        raise
