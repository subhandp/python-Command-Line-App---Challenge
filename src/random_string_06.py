import click
import random
@click.group()
def cli():
    pass
@cli.command(name="randomStr")
@click.option('--length', default=10, help='Maks length random strings')
@click.option('--letters',default=False,type=bool, help='No letters random strings')
@click.option('--uppercase',default=False,type=bool, help='uppercase random strings')
@click.option('--lowercase',default=False,type=bool, help='lowercase random strings')
@click.option('--numbers',default=False,type=bool, help='No Numbers in random string')
def randomStr(length,letters,numbers,uppercase,lowercase):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("1234567890")
    alphabetNumbers = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    result = ''
    for i in range(length):
        if numbers == True:
            wordLists = alphabet
        elif letters == True:
            wordLists = numbers
        else:
            wordLists = alphabetNumbers

        result+= str(wordLists[random.randrange(len(wordLists))])
        
        if i == length:
            break

    
    if uppercase == True:
        result = result.upper()
    if lowercase == True:
        result = result.lower()
    print(result)

if __name__ == "__main__":
    cli()