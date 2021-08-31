# BCBP

A Python module to help decode IATA-standard boarding passes with barcodes.

Data is usually stored on PDF417, QR Code, Aztec, or Data Matrix barcodes as defined by IATA Resolution 792.


Read more about the standard:

[On the IATA website](https://www.iata.org/contentassets/1dccc9ed041b4f3bbdcf8ee8682e75c4/2021_03_02-bcbp-implementation-guide-version-7-.pdf)

---

Available under the GNU GPLv3 Licence.

Published under the name "hattr".

---

## Usage

Install BCBP using `pip install bcbp`.

You will need the `datetime`, `re`, and `json` modules installed for BCBP to function properly.

The following commands are available in BCBP:

- `bcbp.decode("[IATA Resolution 792-standard BCBP data string.]")`

---

## Planned Upgrades

- Error catching when improper string is passed.
- `bcbp.encode()` function.

---

## Acknowledgements

https://shaun.net/notes/whats-contained-in-a-boarding-pass-barcode/

https://gizmodo.com/hacker-builds-a-qr-code-generator-that-lets-him-into-fa-1784884083