#!/usr/bin/env python
import click

@click.command()
@click.option('--name', prompt='Welcome! What is your name?',
              help='The person to greet.')
              
def hello(name):
    click.echo('Hello %s!' % (name))
    
if __name__ == '__main__':
    hello()