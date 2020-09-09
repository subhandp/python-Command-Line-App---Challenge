import click
import socket

@click.group()
def cli():
    pass

@cli.command(name="sum_infinite")
def sum_infinite():
    total = 0
    i = 0
    while True:
        i+=1
        ordinal = 'th'
        if i == 1:
            ordinal = 'st'
        elif i == 2:
            ordinal = 'nd'
        elif i == 3:
            ordinal = 'rd'
        num =  input(f"Insert {i}{ordinal} number: ")
        if num !='':
            total += int(num)
        else:
            break
        
    print("Result:",total)

if __name__ == "__main__":
    cli()

