# Super Mario Implementation in Python

This is inspired by Meth-Meth-Method's [super mario game](https://github.com/meth-meth-method/super-mario/)

## Running

* $ pip install -r requirements.txt
* $ python pcg_mario.py
* $ python main.py

## Standalone windows build

* $ pip install py2exe
* $ python compile.py py2exe

## Controls

* Left: Move left  
* Right: Move right  
* Space: Jump  
* Shift: Boost   
* Left/Right Mouseclick: secret   

## Current state:
![Alt text](img/pics.png "current state")

## Dependencies	
* pygame	
* scipy	

## Contribution

Added Basic Procedural Generation w/ Cellular Automata for basic game structure, Perlin Noise for Pipes and created ground by expanding froma randomly initialized seed.
