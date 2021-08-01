# GNU/Weeb developer PGP keys
This repository contains a collection of GNU/Weeb developer PGP keys.

To search for public key, you can use `search_key.sh` script.
```
# Search for public key that contains "ammar".
$ sh search_key.sh ammar
keys/E893726DC8E4C0DE3BA20107364FBA34FF170A4B.asc

# Import the public key.
$ gpg --import < keys/E893726DC8E4C0DE3BA20107364FBA34FF170A4B.asc
```

To import all public keys, you can do the following:
```
$ gpg --import keys/*.asc
gpg: key F15D5AA1A4865B8C: public key "mdv16h <deo@gnuweeb.org>" imported
gpg: key A01EDC09AA8ABA95: public key "Ammar Faizi <ammarfaizi2@gmail.com>" imported
gpg: key 831B1076737545DF: public key "Akiekano <akiekano@gnuweeb.org>" imported
gpg: key 477471F51EACF860: public key "Doni Setiawan <ecxalty@gnuweeb.org>" imported
gpg: key CC8CDAF7A2DC6FE8: public key "Ammar Faizi <ammarfaizi2@gmail.com>" imported
gpg: key 77F7D3EC34872326: public key "Arthur Lapz <rlapz@gnuweeb.org>" imported
gpg: key C38F59C1306A6E8F: public key "Sprite <sprite@gnuweeb.org>" imported
gpg: key D4BBA3279003375B: public key "Ammar Faizi <ammarfaizi2@gmail.com>" imported
gpg: key 364FBA34FF170A4B: public key "Ammar Faizi <ammarfaizi2@gnuweeb.org>" imported
gpg: Total number processed: 9
gpg:              unchanged: 9
```

# Pull Request
If you are a GNU/Weeb member and want to add your public key, please submit a pull request.

# License
GNU GPL-v2.0
