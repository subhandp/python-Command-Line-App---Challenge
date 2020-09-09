import click

@click.group()
def cli():
    pass
@cli.command(name="lowercase")
@click.argument("string",type=str)
def lowercase(string):
    print(string.lower())

@cli.command(name="uppercase")
@click.argument("string",type=str)
def uppercase(string):
    print(string.upper())

@cli.command(name="capitalize")
@click.argument("string",type=str)
def capitalize(string):
    print(string.title())

if __name__ == "__main__":
    cli()