import click
from generators.generate_suites_cases import generate_test_cases_from_suite
from documentation.document_generator import create_test_suite

@click.group()
def cli():
    pass

@click.command()
@click.argument('suite_path')
def generate_test_cases(suite_path):
    """Generate test cases from a test suite."""
    generate_test_cases_from_suite(suite_path)

@click.command()
@click.argument('prompt')
def generate_suite(prompt):
    """Generate a test suite based on a given prompt."""
    create_test_suite(prompt)

cli.add_command(generate_test_cases)
cli.add_command(generate_suite)

if __name__ == '__main__':
    cli()
