import click
import statistics

@click.group()
def cli():
    pass
@cli.command(name="mean")
@click.argument("numbers",type=int,nargs= -1)
def mean(numbers):
    print(statistics.mean(numbers))

@cli.command(name="median")
@click.argument("numbers",type=int,nargs= -1)
def median (numbers):
    print(statistics.median(numbers))

@cli.command(name="mode")
@click.argument("numbers",type=int,nargs= -1)
def mode(numbers):
    print(statistics.mode(numbers))

@cli.command(name="fmean")
@click.argument("numbers",nargs= -1)
def fmean(numbers):
    print(statistics.fmean(numbers))


if __name__ == "__main__":
    cli()