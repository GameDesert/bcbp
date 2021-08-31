# BCBP

A Python module to help decode IATA-standard boarding passes with barcodes.

Data is usually stored on PDF417, QR Code, Aztec, or Data Matrix barcodes as defined by IATA Resolution 792.

[Module on PyPi](https://pypi.org/project/bcbp/)

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
- `bcbp.encode("[firstname]", "[lastname]", "[pnr]", "[origin]", "[destination]", "[operator]", "[flight number]", "[date]", "[cabin class]", "[seat number]", "[check-in sequence]", [softerror])`

Parameters for the `bcbp.encode()` command:

| Parameter | Data Type | Values | Description | 
| ----------- | ----------- | ----------- | ----------- |
| Firstname | String | Any value which, when combined with Lastname, does not exceed 19 characters. | The passenger's first name, can include titles "MR","MRS","MSTR", "DR", or "MS" after the name. |
| Lastname | String | Any value which, when combined with Firstname, does not exceed 19 characters. | The passenger's last name. |
| PNR | String | Any value which does not exceed 7 characters. | The Passenger Name Reference (also referred to as a Booking Reference). |
| Origin | String | 3-character IATA airport code. | [Search Airport Codes Here (IATA Website)](https://www.iata.org/en/publications/directories/code-search/) |
| Destination | String | 3-character IATA airport code. | [Search Airport Codes Here (IATA Website)](https://www.iata.org/en/publications/directories/code-search/) |
| Operator | String | 2-character airline/operator code. | [Search Airline Codes Here (IATA Website)](https://www.iata.org/en/publications/directories/code-search/) |
| Flight Number | String | Any value which does not exceed 4 characters. | The flight number, usually preceeded by the operator code but this value must only be the number. |
| Date | String | A Python datetime date object with at least a month and a day. | A month and day which can be translated into the julian date. Must be a Python [datetime](https://docs.python.org/3/library/datetime.html) date. |
| Cabin Class | String | 1-character value. | A single character symbol that represents the class the seat is located in. |
| Seat Number | String | 4-character value. | The passenger's seat, usually a 3-digit row followed by a single character seat identifier. |
| Check-In Sequence | String | 4-character value. | A 4-digit number that shows which check-in the passenger had (e.g: 1st passenger to check in: 0001, 25th passenger to check in: 0025). |
| Softerror | Boolean | A boolean (True/False) value. | Set to `True` for the command to return an error message in the output rather than a BCBP code. Set to `false` for an exception to be raised whenever there is an error. |

---

## Planned Upgrades

- ~~Error catching when improper string is passed.~~
- ~~`bcbp.encode()` function.~~

---

## Acknowledgements

https://shaun.net/notes/whats-contained-in-a-boarding-pass-barcode/

https://gizmodo.com/hacker-builds-a-qr-code-generator-that-lets-him-into-fa-1784884083