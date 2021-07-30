#!/bin/sh

fix() {
  local list_key;
  local fp;

  cd keys;
  list_key=$(ls *.asc);
  for i in $list_key; do
    fp=$(printf "%s" $i | cut -d '.' -f 1);
    gpg --import $i && \
    gpg -v $i > $fp.asc.tmp && \
    gpg --armor --export $fp >> $fp.asc.tmp && \
    cp -vf $fp.asc.tmp $fp.asc && \
    rm -f $fp.asc.tmp;
  done;
}

fix;
