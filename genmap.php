<?php
// SPDX-License-Identifier: GPL-2.0


const MAP_COMMENT = <<<TXT
# SPDX-License-Identifier: GPL-2.0
#
# GNU/Weeb developer PGP keys
#
# U = User
# P = Public key file
#


TXT;

function genmap(string $mapfile): void
{
	$maps = [];
	$files = scandir("keys");
	foreach ($files as $file) {
		if ($file === "." || $file === "..")
			continue;

		$gen = shell_exec("gpg keys/{$file} 2>&1");
		if (preg_match_all("/uid\s+(.+)/", $gen, $m)) {
			foreach ($m[1] as $uid) {
				$maps[$uid][] = $file;
			}
		}
	}
	ksort($maps);
	$handle = fopen($mapfile, "wb");
	fwrite($handle, MAP_COMMENT);
	foreach ($maps as $uid => $files) {
		fwrite($handle, "U: {$uid}\n");
		foreach ($files as $file) {
			fwrite($handle, "P: {$file}\n");
		}
		fwrite($handle, "\n");
	}
	fwrite($handle, "# Generated at: ".gmdate("c")."\n");
	fclose($handle);
}

genmap("map.txt");
