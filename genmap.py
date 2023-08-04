#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0
import pgpy
import os
import hashlib
import zbase32
import datetime

keys = []
uids = []
map = {}
uid_fingerprints = {}

def wkd_hash(email):
    local, _ = email.split("@")
    sha1 = hashlib.sha1(local.encode()).digest()
    return zbase32.encode(sha1)

for filename in os.listdir("keys"):
    if filename.endswith(".asc"):
        key, _ = pgpy.PGPKey.from_file("keys/" + filename)
        keys.append(key)

for key in keys:
    for uid in key.userids:
        email = uid.email
        if email:
            uids.append({"uid": uid.userid, "wkd_hash": wkd_hash(email)})
            uid_fingerprints[uid.userid] = uid_fingerprints.get(uid.userid, []) + [
                str(key.fingerprint)
            ]

for uid in uids:
    map[uid["uid"]] = {
        "wkd_hash": uid["wkd_hash"],
        "fingerprints": uid_fingerprints[uid["uid"]],
    }

map = dict(sorted(map.items()))

with open("map.txt", "w") as f:
    f.write(
        """# SPDX-License-Identifier: GPL-2.0
#
# GNU/Weeb developer PGP keys
#
# U = User
# W = Web Key Directory email local part hash
# P = Public key file
#

"""
    )
    for uid, values in map.items():
        mapping = ""
        mapping += f"U: {uid}\n"
        mapping += f"W: {values['wkd_hash']}\n"
        for fingerprint in values["fingerprints"]:
            mapping += f"P: {fingerprint}.asc\n"
        mapping += "\n"
        f.write(mapping)
    f.write(f"# Generated at: {datetime.datetime.utcnow().isoformat()}\n")
