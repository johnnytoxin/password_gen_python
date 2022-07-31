# password_gen_python
A password generator for personal use. Written in Python.

## Requirements
* Python 3.10.0+
* pip 21.2.3+
* cryptography 37.0.4+

## Overview
Ever get tired of having to come up with new passwords every few months? This password generator was created to resolve this issue for myself.

### Features

This application provides two options for creating new passwords.

1) Word key

The generator pulls one word from three different files organized by category: (a full, or partial, video game title), a place (country, town, building, etc.), and an animal. The words are concatenated with a random number and an underscore character.

2) Character key

The user is prompted for a password length and given a randomly generated assortment of characters, with an optional special character inserted at random.

3) Decryption

The application offers the option to save the resultant password to disk. The generated password is encrypted with a master password provided by the user. The application may also load previously saved files from disk. To decrypt the file, the master password must be provided.

## Running the App
```
python app/passgen.py
```
