# Shamir
Implementation of Shamir's secret sharing scheme.
([Wikipedia](https://en.wikipedia.org/wiki/Shamir's_Secret_Sharing))

## Introduction

Shamir's secret sharing scheme is a threshold scheme which enables the user
to split a secret into `n` shares, while requiring any `k` shares to
reconstruct the original secret.

To execute, run:

        python -m Shamir.shamir


## Disclaimer
This is a proof-of-concept and should not be used for anything
important/serious!

## TODO
* Switch to GF arithmetic
* Switch to encode/decode strings/byte arrays
