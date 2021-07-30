#!/bin/sh
# SPDX-License-Identifier: GPL-2.0

search_key() {
  grep -il "$1" keys/*.asc;
}

search_key "$1";
