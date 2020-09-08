import click
import operator
from functools import reduce

@click.group()
def cli():
    pass

@cli.command(name="add")
@click.argument("numberss",type=int,nargs= -1)
def add(numbers):
    print(reduce(lambda a,b : a + b,numbers))

@cli.command(name="substract")
@click.argument("numbers",type=int,nargs= -1)
def substract (numbers):
    print(reduce(lambda a,b : a - b,numbers))

@cli.command(name="multiply")
@click.argument("numbers",type=int,nargs= -1)
def multiply(numbers):
    print(reduce(lambda a,b : a * b,numbers))

@cli.command(name="divide")
@click.argument("numbers",type=int,nargs= -1)
def divide(numbers):
    print(reduce(lambda a,b : a + b,numbers))


if __name__ == "__main__":
    cli()