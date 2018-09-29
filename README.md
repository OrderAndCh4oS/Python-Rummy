[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/sarcoma/Python-Rummy.svg?branch=master)](https://travis-ci.org/sarcoma/Python-Rummy) [![codecov](https://codecov.io/gh/sarcoma/Python-Rummy/branch/master/graph/badge.svg)](https://codecov.io/gh/sarcoma/Python-Rummy)

# Command Line Rummy in Python 3

This is a one to four player command line version of the card game Rummy.

Play against friends or AI

## Installation

`pip install rummy`

## Demo

![Python Rummy Demo](rummy-player-vs-ai.gif)

## Usage

Run `rummy` in terminal

Select number of players then the number of AI opponents

## Rules

Players must make melds of three or more cards _eg_  A♠ 2♠ 3♠ or 4♠ 4♥ 4♣

Unmelded cards score points as follows:
A = 1, J = 11, Q = 12, K = 13, number cards = face value

Players may knock once their hand is worth less than 10 points

Each other player then has one last turn before the round ends

At the end of each round players add their scores to their game total

The game ends once a player reaches 100 or more

The winner is the player with the lowest score

### This project was created for EDx CS50 Final Project 2016

Final CS50 project video:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=JghRYmAkpXI
" target="_blank"><img src="http://img.youtube.com/vi/JghRYmAkpXI/3.jpg"
alt="Python 3 Rummy AI battle" width="240" height="180" border="10" /></a>
