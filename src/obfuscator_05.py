
import click

@click.group()
def cli():
    pass
@cli.command(name="obfuscate")
@click.argument("string",type=str)
def obfuscate(string):
    print(
        ''.join(
            list(
                map(
                    lambda char: f"&#{ord(char)};",list(string)
                    )
                )
            )
        )

if __name__ == "__main__":
    cli()