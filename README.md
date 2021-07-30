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
$ cat keys/*.asc | gpg --import
gpg: key 77F7D3EC34872326: "Arthur Lapz <rlapz@gnuweeb.org>" not changed
gpg: key C38F59C1306A6E8F: "Sprite <sprite@gnuweeb.org>" not changed
gpg: key 364FBA34FF170A4B: "Ammar Faizi <ammarfaizi2@gnuweeb.org>" not changed
gpg: key 831B1076737545DF: "Akiekano <akiekano@gnuweeb.org>" not changed
gpg: key 477471F51EACF860: "Doni Setiawan <ecxalty@gnuweeb.org>" not changed
gpg: key B905A377C78E929C: "Deo <deo@gnuweeb.org>" not changed
gpg: key 364FBA34FF170A4B: "Ammar Faizi <ammarfaizi2@gnuweeb.org>" not changed
gpg: Total number processed: 7
gpg:              unchanged: 7
```

# Pull Request
If you are a GNU/Weeb member and want to add your public key, please submit a pull request.

# License
GNU GPL-v2.0
