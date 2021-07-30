#!/bin/sh

search_key() {
  grep -il "$1" keys/*.asc;
}

search_key "$1";
