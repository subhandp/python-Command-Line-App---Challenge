import click

@click.group()
def cli():
    pass
@cli.command(name="palindrome")
@click.argument("string",type=str)
def palindrome(string):
    result = string == string[::-1]
    if result:
        print("IS palindrome")
    else:
        print("NOT palindrome") 

if __name__ == "__main__":
    cli()