import click
import socket

@click.group()
def cli():
    pass
@cli.command(name="ip_private")
def ip_private():
    name = socket.gethostname()  
    print(socket.gethostbyname(name))

if __name__ == "__main__":
    cli()