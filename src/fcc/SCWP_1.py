"""
SCWP_1 — Build a Caesar + Vigenère Cipher System

PROBLEM
-------
Build an encryption/decryption system supporting TWO classical ciphers:

1. Caesar cipher
2. Vigenère cipher

The caller must be able to choose which cipher to use for encryption and
 decryption.

TARGET API
----------
caesar_cipher(text, shift, direction=1)
vigenere_cipher(text, key, direction=1)
encrypt(message, cipher, key)
decrypt(message, cipher, key)

OPTIONAL CLI
------------
You may also build an interactive menu where the user chooses:
- Caesar or Vigenère
- Encrypt or Decrypt
and then supplies the message and the appropriate key.

The core functions above are required.

============================================================
PART 1 — CAESAR CIPHER
============================================================

REQUIREMENTS
------------
1. `shift` is an integer.
2. Positive direction shifts letters forward.
3. Negative direction shifts letters backward.
4. Wrap around the alphabet (`z -> a`, `Z -> A`).
5. Preserve uppercase/lowercase.
6. Preserve spaces, digits, punctuation, and other non-letter characters.
7. Non-letter characters must not affect the shift.
8. Large positive/negative shifts must work correctly.

EXAMPLES
--------
caesar_cipher("Hello, World!", 3)
    -> "Khoor, Zruog!"

caesar_cipher("Khoor, Zruog!", 3, -1)
    -> "Hello, World!"

caesar_cipher("xyz", 3)
    -> "abc"

============================================================
PART 2 — VIGENÈRE CIPHER
============================================================

REQUIREMENTS
------------
1. `key` must be a non-empty alphabetic string.
2. The key repeats when necessary.
3. Key values are based on alphabet position:
       a -> 0
       b -> 1
       ...
       z -> 25
4. Encryption shifts forward.
5. Decryption shifts backward.
6. Wrap around the alphabet.
7. Preserve message letter case.
8. Preserve spaces, punctuation, digits, and other non-letter characters.
9. Non-letter message characters must NOT consume a key character.
10. The key is case-insensitive.
11. Reject an empty or invalid key appropriately.

EXAMPLES
--------
vigenere_cipher("hello", "abc")
    -> "hfnlp"

vigenere_cipher("hfnlp", "abc", -1)
    -> "hello"

============================================================
PART 3 — COMMON ENCRYPT / DECRYPT INTERFACE
============================================================

The caller selects the cipher through `cipher`.

SUPPORTED VALUES
----------------
    "caesar"
    "vigenere"

You may make selection case-insensitive.

KEY RULES
---------
For Caesar:
    key = integer shift

For Vigenère:
    key = alphabetic keyword

EXAMPLES
--------
encrypt("Hello", "caesar", 3)
    -> "Khoor"

decrypt("Khoor", "caesar", 3)
    -> "Hello"

encrypt("Hello", "vigenere", "abc")
    -> "Hfnlp"

decrypt("Hfnlp", "vigenere", "abc")
    -> "Hello"

COMMON INTERFACE REQUIREMENTS
-----------------------------
1. `encrypt()` chooses the requested cipher and calls its implementation.
2. `decrypt()` chooses the requested cipher and calls its implementation.
3. Do not duplicate the complete cipher algorithms inside both dispatcher
   functions.
4. Unsupported cipher names must raise an appropriate exception.
5. Caesar must reject an invalid key type.
6. Vigenère must reject an invalid/empty key.

============================================================
PART 4 — OPTIONAL USER INTERFACE
============================================================

Create a small command-line interface that asks the user:

    Choose a cipher:
    1. Caesar
    2. Vigenère

Then:

    Choose an operation:
    1. Encrypt
    2. Decrypt

Then request:
- the message;
- the Caesar shift OR Vigenère keyword.

The CLI must use the common `encrypt()` / `decrypt()` functions instead of
 duplicating encryption/decryption logic.

============================================================
ACCEPTANCE TESTS
============================================================

encrypt("Hello, World!", "caesar", 3)
    -> "Khoor, Zruog!"

decrypt("Khoor, Zruog!", "caesar", 3)
    -> "Hello, World!"

encrypt("Hello", "vigenere", "abc")
    -> "Hfnlp"

decrypt("Hfnlp", "vigenere", "abc")
    -> "Hello"

For every valid message/key:
    decrypt(encrypt(message, cipher, key), cipher, key)
must return the original message.

CONSTRAINTS
----------
- Do not use a library implementation of Caesar or Vigenère.
- Keep the two cipher algorithms separate.
- The dispatcher functions decide which cipher to use.
- Solve the problem yourself; no solution is included.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_cipher(message, key):
    index = 0
    decrypted_message = ""
    for i in message:
        new_index = index + key
        decrypted_message.append()


def vigenere_cipher(message, key):
    pass


def encrypt():
    pass


def decrypt():
    pass


def main():
    option = input("Enter which cipher you want to use (caesar / vigenere): ")
    if option == "caesar":
        pass


# TODO: Implement the required functions/classes above this test block.
def run_tests():
    # Caesar
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar_cipher("Khoor, Zruog!", 3, -1) == "Hello, World!"
    assert caesar_cipher("xyz", 3) == "abc"
    assert caesar_cipher("ABC", 2) == "CDE"
    assert caesar_cipher("A-B-C", 26) == "A-B-C"

    # Vigenère
    assert vigenere_cipher("hello", "abc") == "hfnlp"
    assert vigenere_cipher("hfnlp", "abc", -1) == "hello"
    assert vigenere_cipher("Attack at Dawn!", "LEMON") == "Lxfopv ef Rnhr!"

    # User-selectable common interface
    assert encrypt("Hello", "caesar", 3) == "Khoor"
    assert decrypt("Khoor", "caesar", 3) == "Hello"
    assert encrypt("Hello", "vigenere", "abc") == "Hfnlp"
    assert decrypt("Hfnlp", "vigenere", "abc") == "Hello"

    # Round-trip: encryption followed by decryption restores the message.
    for cipher, key in [("caesar", 7), ("vigenere", "coding")]:
        message = "Attack at Dawn! 123"
        assert decrypt(encrypt(message, cipher, key), cipher, key) == message

    print("SCWP_1 tests passed.")


if __name__ == "__main__":
    run_tests()
