# Animation of Collatz Conjecture in 3D

This Python script generates an animated 3D visualization of the Collatz Conjecture using matplotlib. The Collatz Conjecture is a famous unsolved mathematical problem also known as the "3x+1 problem".

<div align="center">
  <img src="Animations/Animation_Collatz Conjecture.gif.gif" alt="Collatz Conjecture Animation">
  <h5>Collatz Conjecture Animation</h5>
</div>

The Collatz Conjecture, named after the German mathematician Lothar Collatz, is a sequence defined as follows:

1. Start with any positive integer \( n \).
2. If \( n \) is even, divide it by 2 to get \( n/2 \).
3. If \( n \) is odd, multiply it by 3 and add 1 to get \( 3n + 1 \).
4. Repeat the process indefinitely.

> The conjecture posits that no matter which positive integer you start with, 
> the sequence will always eventually reach the number 1. Despite extensive computational 
> evidence supporting this conjecture, a formal proof remains elusive, making it one 
> of the many intriguing unsolved problems in mathematics.

## Requirements

- Python 3.x
- matplotlib

## Installation

Clone the repository:

```sh
bash
git clone https://github.com/AtlasCJr/Collatz-Conjecture
cd Collatz-Conjecture
```

Install dependencies:

```sh
pip install matplotlib
```

## Usage

Run the script to generate the animated GIF:

    Collatz Conjecture.py

The animation will be saved as _Animation_Collatz_Conjecture.gif_ in the Animations directory.

## Description

The script initializes a set of points and iteratively applies rotations and scaling based on specific rules related to the Collatz Conjecture:
+ Points are represented in 3D space.
+ Each point is updated and rotated based on its current state and position.
+ The animation evolves over 180 frames, with each frame updated every 50 millisecond