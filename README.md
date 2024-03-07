# Base Prime Equivalence

## What is Base Prime?

In this project, we first must define the term `base prime`.
Similar to the notion of number bases, base prime is a way to express a number.
However, base prime uses a unique notation.

We will indicate the index of a position as `i`, where the right-most position is `0` and `i` increases as we go left.

The value in each position will be defined as `a_i`.

From here, the i'th number is associated with the i'th prime, where p_0, indicating the 0'th prime, is 2, then 3, 5, 7, etc.

Now to construct a number, the full formula is `(2^a_0) * (3^a_1) * ... * (p_n^a_n)`.

In effect, base prime denotes the prime factorization of a given number.

## The Goal

The goal of this project is to find number representations that I will refer to as equivalent.
This means that some number's representation in base prime is the same as in another base. 

For example, 12 (base prime) == 12 (base 10).

This project will attempt to develop an algorithm to find these equivalent numbers in base 10 and other bases.

Currently, the only number found so far is 12, searching base 10 up to 1 billion, and base 2 up to 100 million.