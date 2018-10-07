# military-crypto [pwn]

```
We take security seriously so instead of shipping our own crypto we simply use proven military grade technology for our firmware updates.

nc military-crypto.ctf.hackover.de 1337
```

# do
- アクセスする。ワカラン。

```
vagrant@vagrant:~$ nc military-crypto.ctf.hackover.de 1337
====================================================
    == secure update service

    we didn't roll our own, powered by the
    best crypto known to humanity
====================================================
1) Update firmware    3) Current firmware
2) Download firmware  4) Quit
> 3
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Version: 1.0
Created: 2018-10-03
Audited: KRYPTOCHEF

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEwSuuOHnM9KfOOGG3QoUB03HVrd8FAlu2ra4ACgkQQoUB03HV
rd9kow//b/uQQonqD02g7VXMBYIUcCljLsGaOgvdEXSA6r6y5iym4DVLrDuZrIHP
ryAV30SJkm6gaxjcA19zYBg79tqcolhJPq4Tsd8bCOBEWG31Gk1LN7mzJbCk5TMO
ylf02qYbgpCULPkNxH87s4S8Oo7z0buR50jWAbe28fPkqyF0AG4iConSeIhKtMYB
LNFIdxXm3u99su5BATf13jSGrIIg+iO8aT7xrohOyaY75FlvsB6DBeDLTwf/9z//
SKVixZVKuoh+b4hevECqmwRB3t/NvyIbHz8e70WHXhWg6CXJMMz41YZylGhwNeDF
I3sHjIJ1wx4FDzH1WSlVcrYSOP4UZacgPzwxjMehvnUW2IGFXRiwsh1z21HI8Nlx
N0YZ5b+uwpj75AmP4mNDYvoGHHk1+fqna4a39y2t7qQEWMkEq2YQiuDQjCGAprC+
Q++8HAtODf566z2pB1h8dsdvOWDzzfMS8z3RC6LFydMEiRzVi7sL0tawY60JPBxH
DX2D6njzPi5XjRCNJiGqrK2qsL2aNxDn7zBQExvEUmgLsSR574YUILLa0xsMhMTA
Zn3ht/Rx7yxZJoN8FM0UvajbFdcDmgj2iullEq3aIpmQChoVnb/yygpCq0353UtY
OWZKfxCcH9mQSbcQCjDUFgr91nTXehMQ6d64bSbLxgZuqWwPoy4=
=IbNc
-----END PGP SIGNATURE-----
====================================================
    == secure update service

    we didn't roll our own, powered by the
    best crypto known to humanity
====================================================
1) Update firmware    3) Current firmware
2) Download firmware  4) Quit
> 2
Firmware:
IyEvYmluL2Jhc2gKc2V0IC1ldQoKU0VMRj0kKHB3ZCkvJDAKRElSPSQobWt0ZW1wIC1kKQpjZCAiJERJUiIKCmNwIC1yIC9ob21lL2N0Zi8uZ251cGcgLgpleHBvcnQgR05VUEdIT01FPSIke0RJUn0vLmdudXBnIgpjaG1vZCBvLXJ4IC5nbnVwZwoKbWVudSgpIHsKY2F0IDw8RU9GCj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KICAgID09IHNlY3VyZSB1cGRhdGUgc2VydmljZQoKICAgIHdlIGRpZG4ndCByb2xsIG91ciBvd24sIHBvd2VyZWQgYnkgdGhlCiAgICBiZXN0IGNyeXB0byBrbm93biB0byBodW1hbml0eQo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CkVPRgogICAgUFMzPSI+ICIKICAgIG9wdHM9KCJVcGRhdGUgZmlybXdhcmUiICJEb3dubG9hZCBmaXJtd2FyZSIgIkN1cnJlbnQgZmlybXdhcmUiICJRdWl0IikKICAgIHNlbGVjdCBvcHQgaW4gIiR7b3B0c1tAXX0iOyBkbwogICAgY2FzZSAiJHtSRVBMWX0iIGluCiAgICAgICAgMSApIHVwZGF0ZV9maXJtd2FyZTsgYnJlYWs7OwogICAgICAgIDIgKSBkb3dubG9hZF9maXJtd2FyZTsgYnJlYWs7OwogICAgICAgIDMgKSBjdXJyZW50X2Zpcm13YXJlOyBicmVhazs7CiAgICAgICAgNCApIGVjaG8gIkVPRiEiOyBleGl0IDA7OwogICAgICAgICopIGVjaG8gIlVua25vd24gb3B0aW9uIjsgY29udGludWU7OwogICAgZXNhYzsgZG9uZQp9Cgp1cGRhdGVfZmlybXdhcmUoKSB7CiAgIGNhdCA8PEVPRgo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiAgICAxKSBzZW5kIHVwZGF0ZSBiaW5hcnkgYXMgYmFzZTY0CiAgICAyKSBmaW5pc2ggd2l0aCBhbiBlbXB0eSBsaW5lCiAgICAzKSBzZW5kIGRldGFjaGVkIHNpZ25hdHVyZSBhcyBiYXNlNjQKICAgIDQpIGZpbmlzaCB3aXRoIGFuIGVtcHR5IGxpbmUKPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQpFT0YKICAgZWNobyAnUmVhZGluZyBmaXJtd2FyZS4uLicKICAgdG91Y2ggdXBkYXRlLmJpbi5iNjQKICAgd2hpbGUgSUZTPScnIHJlYWQgLXIgZmlybXdhcmU7IGRvCiAgICAgICBpZiBbIC16ICIkZmlybXdhcmUiIF07IHRoZW4gYnJlYWs7IGZpCiAgICAgICBlY2hvICIkZmlybXdhcmUiID4+IHVwZGF0ZS5iaW4uYjY0CiAgIGRvbmUKICAgYmFzZTY0IC1kIHVwZGF0ZS5iaW4uYjY0ID4gdXBkYXRlLmJpbgogICBybSB1cGRhdGUuYmluLmI2NAoKICAgZWNobyAnUmVhZGluZyBkZXRhdGNoZWQgc2lnbmF1cmUuLi4nCiAgIHRvdWNoIHVwZGF0ZS5iaW4uc2lnCiAgIHdoaWxlIElGUz0nJyByZWFkIC1yIHNpZ25hdHVyZTsgZG8KICAgICAgIGlmIFsgLXogIiRzaWduYXR1cmUiIF07IHRoZW4gYnJlYWs7IGZpCiAgICAgICBlY2hvICIkc2lnbmF0dXJlIiA+PiB1cGRhdGUuYmluLnNpZy5iNjQKICAgZG9uZQogICBiYXNlNjQgLWQgdXBkYXRlLmJpbi5zaWcuYjY0ID4gdXBkYXRlLmJpbi5zaWcKICAgcm0gdXBkYXRlLmJpbi5zaWcuYjY0CgogICBpZiAhIGdwZyAtLXZlcmlmeSB1cGRhdGUuYmluLnNpZzsgdGhlbgogICAgICAgc2V0ICt4CiAgICAgICBlY2hvICchISEhISEhISEhISEhISEhISEhISEhIScKICAgICAgIGVjaG8gJyEhIElOVkFMSUQgU0lHTkFUVVJFICEhJwogICAgICAgZWNobyAnISEhISEhISEhISEhISEhISEhISEhISEnCiAgICAgICBleGl0IDEKICAgZWxzZQogICAgICAgY2htb2QgK3ggdXBkYXRlLmJpbgogICAgICAgZWNobyAnVXBkYXRpbmcuLi4uJwogICAgICAgLi91cGRhdGUuYmluCiAgICAgICBlY2hvICdSZWJvb3RpbmcuLi4uJwogICAgICAgZXhpdCAwCiAgIGZpCn0KCmRvd25sb2FkX2Zpcm13YXJlKCkgewogICAgZWNobyAiRmlybXdhcmU6IgogICAgY2F0ICIke1NFTEZ9InxiYXNlNjR8dHIgLWQgJ1xuJwogICAgZWNobwogICAgZWNobyAiU2lnbmF0dXJlOiIKICAgIGNhdCAiJHtTRUxGfS5zaWcifGJhc2U2NHx0ciAtZCAnXG4nCiAgICBlY2hvCn0KCmN1cnJlbnRfZmlybXdhcmUoKSB7CmNhdCA8PEVPRgotLS0tLUJFR0lOIFBHUCBTSUdORUQgTUVTU0FHRS0tLS0tCkhhc2g6IFNIQTI1NgoKVmVyc2lvbjogMS4wCkNyZWF0ZWQ6IDIwMTgtMTAtMDMKQXVkaXRlZDogS1JZUFRPQ0hFRgoKLS0tLS1CRUdJTiBQR1AgU0lHTkFUVVJFLS0tLS0KCmlRSXpCQUVCQ0FBZEZpRUV3U3V1T0huTTlLZk9PR0czUW9VQjAzSFZyZDhGQWx1MnJhNEFDZ2tRUW9VQjAzSFYKcmQ5a293Ly9iL3VRUW9ucUQwMmc3VlhNQllJVWNDbGpMc0dhT2d2ZEVYU0E2cjZ5NWl5bTREVkxyRHVacklIUApyeUFWMzBTSmttNmdheGpjQTE5ellCZzc5dHFjb2xoSlBxNFRzZDhiQ09CRVdHMzFHazFMTjdtekpiQ2s1VE1PCnlsZjAycVliZ3BDVUxQa054SDg3czRTOE9vN3owYnVSNTBqV0FiZTI4ZlBrcXlGMEFHNGlDb25TZUloS3RNWUIKTE5GSWR4WG0zdTk5c3U1QkFUZjEzalNHcklJZytpTzhhVDd4cm9oT3lhWTc1Rmx2c0I2REJlRExUd2YvOXovLwpTS1ZpeFpWS3VvaCtiNGhldkVDcW13UkIzdC9OdnlJYkh6OGU3MFdIWGhXZzZDWEpNTXo0MVlaeWxHaHdOZURGCkkzc0hqSUoxd3g0RkR6SDFXU2xWY3JZU09QNFVaYWNnUHp3eGpNZWh2blVXMklHRlhSaXdzaDF6MjFISThObHgKTjBZWjViK3V3cGo3NUFtUDRtTkRZdm9HSEhrMStmcW5hNGEzOXkydDdxUUVXTWtFcTJZUWl1RFFqQ0dBcHJDKwpRKys4SEF0T0RmNTY2ejJwQjFoOGRzZHZPV0R6emZNUzh6M1JDNkxGeWRNRWlSelZpN3NMMHRhd1k2MEpQQnhICkRYMkQ2bmp6UGk1WGpSQ05KaUdxcksycXNMMmFOeERuN3pCUUV4dkVVbWdMc1NSNTc0WVVJTExhMHhzTWhNVEEKWm4zaHQvUng3eXhaSm9OOEZNMFV2YWpiRmRjRG1najJpdWxsRXEzYUlwbVFDaG9WbmIveXlncENxMDM1M1V0WQpPV1pLZnhDY0g5bVFTYmNRQ2pEVUZncjkxblRYZWhNUTZkNjRiU2JMeGdadXFXd1BveTQ9Cj1JYk5jCi0tLS0tRU5EIFBHUCBTSUdOQVRVUkUtLS0tLQpFT0YKfQoKd2hpbGUgdHJ1ZTsgZG8KICAgIG1lbnUKZG9uZQo=
Signature:
iQIzBAABCAAdFiEEwSuuOHnM9KfOOGG3QoUB03HVrd8FAlu2riEACgkQQoUB03HVrd+6Bg/+L6LxTcuDg4wgWiFM8mn6ra95Tz6kCTSjk1xWB6eCAZ2RQJZs8kZ+g1pI4Us2W6nVNaUwJ3Db/ozbm6tDymfOmq2A6jwIWV9rSgMYjHxNehh9jhElf+b70zg6ROow+5tCYrPwey+6oIWDYkfXql8sjfr0rKOghp2Myq8qIn7JDI4KXMO7O/YHuL0TCPFQ+36JnMjmg/U46A9IVb3Kt5/ObtAulT9ItJP1j99XlPMZ4riRCCNLbYUuQDyP6IAjErTbipwFPOpUcs2N2P+MhBAi+43EXfGNTAF04Lui87qtNw4dVamnvp4gnAuTB8BL502UvVM0i6IbNkQbkMQX3pI24UCP7Yuebpj3mqDBchWi30+/tA4eHFlRs2XbXxyYQrGJx4lgOBr2tCPwQlk4VzSqSz0cfXZdbyUbHHF2dHAKgsuJyx22orIpZoEt9lvjDqe2DWtHHXB/R6jds+u3/1X549OM/PnbIdpRV+TRuyavmEJt8SPp7m8HrWAxidQcCYltD01n2mfoMVrATJqjRzcZ9YLJc84qgDT6+86j7cmTRVdc8IbXDuA1DF8HFYHxvLSj5zx1VF9CYBLB1QYL2zhQUjfAU5QICAc9dlM1kSvzouJ60lYVoA/O6N+WYqWA2QKRZTSyw96dwBIwDY4f6nG2ab8gs5rIPh9kmZxA0bLDamM=
====================================================
    == secure update service

    we didn't roll our own, powered by the
    best crypto known to humanity
====================================================
1) Update firmware    3) Current firmware
2) Download firmware  4) Quit
> 4
EOF!

```
- SingnatureもFirmwareもbase64っぽい。
- Firmware
```
'#!/bin/bash\nset -eu\n\nSELF=$(pwd)/$0\nDIR=$(mktemp -d)\ncd "$DIR"\n\ncp -r /home/ctf/.gnupg .\nexport GNUPGHOME="${DIR}/.gnupg"\nchmod o-rx .gnupg\n\nmenu() {\ncat <<EOF\n====================================================\n    == secure update service\n\n    we didn\'t roll our own, powered by the\n    best crypto known to humanity\n====================================================\nEOF\n    PS3="> "\n    opts=("Update firmware" "Download firmware" "Current firmware" "Quit")\n    select opt in "${opts[@]}"; do\n    case "${REPLY}" in\n        1 ) update_firmware; break;;\n        2 ) download_firmware; break;;\n        3 ) current_firmware; break;;\n        4 ) echo "EOF!"; exit 0;;\n        *) echo "Unknown option"; continue;;\n    esac; done\n}\n\nupdate_firmware() {\n   cat <<EOF\n====================================================\n    1) send update binary as base64\n    2) finish with an empty line\n    3) send detached signature as base64\n    4) finish with an empty line\n====================================================\nEOF\n   echo \'Reading firmware...\'\n   touch update.bin.b64\n   while IFS=\'\' read -r firmware; do\n       if [ -z "$firmware" ]; then break; fi\n       echo "$firmware" >> update.bin.b64\n   done\n   base64 -d update.bin.b64 > update.bin\n   rm update.bin.b64\n\n   echo \'Reading detatched signaure...\'\n   touch update.bin.sig\n   while IFS=\'\' read -r signature; do\n       if [ -z "$signature" ]; then break; fi\n       echo "$signature" >> update.bin.sig.b64\n   done\n   base64 -d update.bin.sig.b64 > update.bin.sig\n   rm update.bin.sig.b64\n\n   if ! gpg --verify update.bin.sig; then\n       set +x\n       echo \'!!!!!!!!!!!!!!!!!!!!!!!\'\n       echo \'!! INVALID SIGNATURE !!\'\n       echo \'!!!!!!!!!!!!!!!!!!!!!!!\'\n       exit 1\n   else\n       chmod +x update.bin\n       echo \'Updating....\'\n       ./update.bin\n       echo \'Rebooting....\'\n       exit 0\n   fi\n}\n\ndownload_firmware() {\n    echo "Firmware:"\n    cat "${SELF}"|base64|tr -d \'\\n\'\n    echo\n    echo "Signature:"\n    cat "${SELF}.sig"|base64|tr -d \'\\n\'\n    echo\n}\n\ncurrent_firmware() {\ncat <<EOF\n-----BEGIN PGP SIGNED MESSAGE-----\nHash: SHA256\n\nVersion: 1.0\nCreated: 2018-10-03\nAudited: KRYPTOCHEF\n\n-----BEGIN PGP SIGNATURE-----\n\niQIzBAEBCAAdFiEEwSuuOHnM9KfOOGG3QoUB03HVrd8FAlu2ra4ACgkQQoUB03HV\nrd9kow//b/uQQonqD02g7VXMBYIUcCljLsGaOgvdEXSA6r6y5iym4DVLrDuZrIHP\nryAV30SJkm6gaxjcA19zYBg79tqcolhJPq4Tsd8bCOBEWG31Gk1LN7mzJbCk5TMO\nylf02qYbgpCULPkNxH87s4S8Oo7z0buR50jWAbe28fPkqyF0AG4iConSeIhKtMYB\nLNFIdxXm3u99su5BATf13jSGrIIg+iO8aT7xrohOyaY75FlvsB6DBeDLTwf/9z//\nSKVixZVKuoh+b4hevECqmwRB3t/NvyIbHz8e70WHXhWg6CXJMMz41YZylGhwNeDF\nI3sHjIJ1wx4FDzH1WSlVcrYSOP4UZacgPzwxjMehvnUW2IGFXRiwsh1z21HI8Nlx\nN0YZ5b+uwpj75AmP4mNDYvoGHHk1+fqna4a39y2t7qQEWMkEq2YQiuDQjCGAprC+\nQ++8HAtODf566z2pB1h8dsdvOWDzzfMS8z3RC6LFydMEiRzVi7sL0tawY60JPBxH\nDX2D6njzPi5XjRCNJiGqrK2qsL2aNxDn7zBQExvEUmgLsSR574YUILLa0xsMhMTA\nZn3ht/Rx7yxZJoN8FM0UvajbFdcDmgj2iullEq3aIpmQChoVnb/yygpCq0353UtY\nOWZKfxCcH9mQSbcQCjDUFgr91nTXehMQ6d64bSbLxgZuqWwPoy4=\n=IbNc\n-----END PGP SIGNATURE-----\nEOF\n}\n\nwhile true; do\n    menu\ndone\n'
```
- なんか意味ありげなのが出てきた。
- download Firmwareすれば現在のバージョンのが見れるっぽい。
- pgp keyかと思ったらSignature?
- 見づらいので、pythonの変数に変換して`print s`した

```
#!/bin/bash
set -eu

SELF=$(pwd)/$0
DIR=$(mktemp -d)
cd "$DIR"

cp -r /home/ctf/.gnupg .
export GNUPGHOME="${DIR}/.gnupg"
chmod o-rx .gnupg

menu() {
cat <<EOF
====================================================
    == secure update service

    we didn't roll our own, powered by the
    best crypto known to humanity
====================================================
EOF
    PS3="> "
    opts=("Update firmware" "Download firmware" "Current firmware" "Quit")
    select opt in "${opts[@]}"; do
    case "${REPLY}" in
        1 ) update_firmware; break;;
        2 ) download_firmware; break;;
        3 ) current_firmware; break;;
        4 ) echo "EOF!"; exit 0;;
        *) echo "Unknown option"; continue;;
    esac; done
}

update_firmware() {
   cat <<EOF
====================================================
    1) send update binary as base64
    2) finish with an empty line
    3) send detached signature as base64
    4) finish with an empty line
====================================================
EOF
   echo 'Reading firmware...'
   touch update.bin.b64
   while IFS='' read -r firmware; do
       if [ -z "$firmware" ]; then break; fi
       echo "$firmware" >> update.bin.b64
   done
   base64 -d update.bin.b64 > update.bin
   rm update.bin.b64

   echo 'Reading detatched signaure...'
   touch update.bin.sig
   while IFS='' read -r signature; do
       if [ -z "$signature" ]; then break; fi
       echo "$signature" >> update.bin.sig.b64
   done
   base64 -d update.bin.sig.b64 > update.bin.sig
   rm update.bin.sig.b64

   if ! gpg --verify update.bin.sig; then
       set +x
       echo '!!!!!!!!!!!!!!!!!!!!!!!'
       echo '!! INVALID SIGNATURE !!'
       echo '!!!!!!!!!!!!!!!!!!!!!!!'
       exit 1
   else
       chmod +x update.bin
       echo 'Updating....'
       ./update.bin
       echo 'Rebooting....'
       exit 0
   fi
}

download_firmware() {
    echo "Firmware:"
    cat "${SELF}"|base64|tr -d '\n'
    echo
    echo "Signature:"
    cat "${SELF}.sig"|base64|tr -d '\n'
    echo
}

current_firmware() {
cat <<EOF
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Version: 1.0
Created: 2018-10-03
Audited: KRYPTOCHEF

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEwSuuOHnM9KfOOGG3QoUB03HVrd8FAlu2ra4ACgkQQoUB03HV
rd9kow//b/uQQonqD02g7VXMBYIUcCljLsGaOgvdEXSA6r6y5iym4DVLrDuZrIHP
ryAV30SJkm6gaxjcA19zYBg79tqcolhJPq4Tsd8bCOBEWG31Gk1LN7mzJbCk5TMO
ylf02qYbgpCULPkNxH87s4S8Oo7z0buR50jWAbe28fPkqyF0AG4iConSeIhKtMYB
LNFIdxXm3u99su5BATf13jSGrIIg+iO8aT7xrohOyaY75FlvsB6DBeDLTwf/9z//
SKVixZVKuoh+b4hevECqmwRB3t/NvyIbHz8e70WHXhWg6CXJMMz41YZylGhwNeDF
I3sHjIJ1wx4FDzH1WSlVcrYSOP4UZacgPzwxjMehvnUW2IGFXRiwsh1z21HI8Nlx
N0YZ5b+uwpj75AmP4mNDYvoGHHk1+fqna4a39y2t7qQEWMkEq2YQiuDQjCGAprC+
Q++8HAtODf566z2pB1h8dsdvOWDzzfMS8z3RC6LFydMEiRzVi7sL0tawY60JPBxH
DX2D6njzPi5XjRCNJiGqrK2qsL2aNxDn7zBQExvEUmgLsSR574YUILLa0xsMhMTA
Zn3ht/Rx7yxZJoN8FM0UvajbFdcDmgj2iullEq3aIpmQChoVnb/yygpCq0353UtY
OWZKfxCcH9mQSbcQCjDUFgr91nTXehMQ6d64bSbLxgZuqWwPoy4=
=IbNc
-----END PGP SIGNATURE-----
EOF
}

while true; do
    menu
done

```
- なるほど、updateして何か送り込んでflagげっとみたいなノリか。

```
====================================================
1) Update firmware    3) Current firmware
2) Download firmware  4) Quit
> 1
====================================================
    1) send update binary as base64
    2) finish with an empty line
    3) send detached signature as base64
    4) finish with an empty line
====================================================
Reading firmware...
11111111111111
11111111111111

Reading detatched signaure...
11111111111111
11111111111111

gpg: no valid OpenPGP data found.
gpg: the signature could not be verified.
Please remember that the signature file (.sig or .asc)
should be the first file given on the command line.
!!!!!!!!!!!!!!!!!!!!!!!
!! INVALID SIGNATURE !!
!!!!!!!!!!!!!!!!!!!!!!!
```
- 適当にやるとinvalidがきた。どうやら、改行込みで入力し、最後に空行で送信っぽい？
- binをls -alにして、それに合うPGP Signatureを入れて、それでfirmwareをupdateするみたいなノリか？
- ls -al -> bHMgLWFs
- これに合うSignatureを作る。これだけだとはじかれなので、たぶんFirmwareとともに鍵も記入する必要がある？

- なんか[PGP Signature Decoder](https://cirw.in/gpg-decoder/)というとこに投げたら何か出てきた

```
Signature Packet (0x2)
  cipherTypeByte: "137"
  length: "563"
  version: "4"
  signatureType: "Signature of a canonical text document. (0x1)"
  publicKeyAlgorithm: "RSA (Encrypt or Sign) (0x1)"
  hashAlgorithm: "SHA256 (0x8)"
  hashedDataCount: "29"
  subpackets:
    length:"22"
    subpacketType:"undefined (0x21)"
    data:"04c12bae3879ccf4a7ce3861b7428501d371d5addf"
    length:"5"
    subpacketType:"Signature Creation Time (0x2)"
    creationTime:"Fri Oct 05 2018 09:17:50 GMT+0900 (日本標準時)"
  unhashedDataCount: "10"
  subpackets:
    length:"9"
    subpacketType:"Issuer (0x10)"
    keyId:"428501d371d5addf"
  signedHashValuePrefix: "64a3"
  signature: "6ffb904289ea0f4da0ed55cc0582147029632ec19a3a0bdd117480eabeb2e62ca6e0354bac3b99ac81cfaf2015df4489926ea06b18dc035f7360183bf6da9ca258493eae13b1df1b08e044586df51a4d4b37b9b325b0a4e5330eca57f4daa61b8290942cf90dc47f3bb384bc3a8ef3d1bb91e748d601b7b6f1f3e4ab2174006e220a89d278884ab4c6012cd1487715e6deef7db2ee410137f5de3486ac8220fa23bc693ef1ae884ec9a63be4596fb01e8305e0cb4f07fff73fff48a562c5954aba887e6f885ebc40aa9b0441dedfcdbf221b1f3f1eef45875e15a0e825c930ccf8d5867294687035e0c5237b078c8275c31e050f31f559295572b61238fe1465a7203f3c318cc7a1be7516d881855d18b0b21d73db51c8f0d971374619e5bfaec298fbe4098fe2634362fa061c7935f9faa76b86b7f72dadeea40458c904ab66108ae0d08c2180a6b0be43efbc1c0b4e0dfe7aeb3da907587c76c76f3960f3cdf312f33dd10ba2c5c9d304891cd58bbb0bd2d6b063ad093c1c470d7d83ea78f33e2e578d108d2621aaacadaab0bd9a3710e7ef3050131bc452680bb12479ef861420b2dad31b0c84c4c0667de1b7f471ef2c5926837c14cd14bda8db15d7039a08f68ae96512adda2299900a1a159dbff2ca0a42ab4df9dd4b5839664a7f109c1fd99049b7100a30d4160afdd674d77a1310e9deb86d26cbc6066ea96c0fa32e"
```
- 秘密鍵が必要？よく分かんない。撤退。