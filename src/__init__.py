import click
from src.string_transformation_01 import lowercase,uppercase,capitalize 
from src.arithmetic_02 import add,substract,divide,multiply 
from src.infinite_inputs_09 import sum_infinite


@click.group()
def cli():
    pass

cli.add_command(lowercase)
cli.add_command(uppercase)
cli.add_command(capitalize)

cli.add_command(add)
cli.add_command(substract)
cli.add_command(divide)
cli.add_command(multiply)

cli.add_command(sum_infinite)



if __name__ == "__main__":
    cli()