import click

from src.string_transformation_01 import lowercase,uppercase,capitalize 
from src.arithmetic_02 import add,substract,divide,multiply 
from src.statistic_03 import mean,median,mode,fmean
from src.palindrome_04 import palindrome
from src.obfuscator_05 import obfuscate
from src.random_string_06 import randomStr
from src.ip_private_07 import ip_private
from src.ip_public_08 import ip_public
from src.infinite_inputs_09 import sum_infinite
# from src.crud_10 import create,read,readid,delete

@click.group()
def cli():
    pass

cli.add_command(lowercase)
cli.add_command(uppercase)
cli.add_command(capitalize)

cli.add_command(add)
cli.add_command(substract)
cli.add_command(divide)
cli.add_command(multiply)

cli.add_command(mean)
cli.add_command(median)
cli.add_command(mode)
cli.add_command(fmean)

cli.add_command(palindrome)

cli.add_command(obfuscate)

cli.add_command(randomStr)

cli.add_command(ip_private)

cli.add_command(ip_public)

cli.add_command(sum_infinite)

# cli.add_command(create)
# cli.add_command(read)
# cli.add_command(readid)
# cli.add_command(delete)


if __name__ == "__main__":
    cli()