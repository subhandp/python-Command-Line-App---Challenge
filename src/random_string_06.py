import click
import random
@click.group()
def cli():
    pass
@cli.command(name="randomStr")
@click.option('--length', default=5, help='Maks length random strings')
@click.option('--letters',default=False,type=bool, help='No letters random strings')
@click.option('--uppercase',default=False,type=bool, help='uppercase random strings')
@click.option('--lowercase',default=False,type=bool, help='lowercase random strings')
@click.option('--numbers',default=False,type=bool, help='No Numbers in random string')
def randomStr(length,letters,numbers,uppercase,lowercase):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("1234567890")
    result = ''
    for i in enumerate(alphabet):
        charnum = list([alphabet,numbers])
        select = random.randrange(0,2)
        if numbers == True:
            select = 1
        if letters == True:
            select = 0

        result+=charnum[select][random.randrange(0, len(charnum[select]), 3)]
        
        if i == length:
            break

    
    if uppercase == True:
        output = output.upper()
    if lowercase == True:
        output = output.lower()
    # if number == False
    print(output)
    print(length)

if __name__ == "__main__":
    cli()