import click
import socket

@click.group()
def cli():
    pass

@cli.command(name="sum_infinite")
def sum_infinite():
    num = click.prompt('Insert 1st number ', type=int)
    angka = num
    total = int(num)
    i = 1
    while num != '' and angka != '':
        i+=1
        ordinal = 'th'
        if i == 2:
            ordinal = 'nd'
        elif i == 3:
            ordinal = 'rd'
        angka =  input(f"Insert {i}{ordinal} number: ")
        if angka !='':
            total += int(angka)
        
    print("Result:",total)

if __name__ == "__main__":
    cli()

