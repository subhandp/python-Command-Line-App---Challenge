import urllib.request
import click

@click.group()
def cli():
    pass
@cli.command(name="ip_public")
def ip_public():
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(ip)

if __name__ == "__main__":
    cli()