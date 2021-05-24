#!/usr/bin/python2
# -*- coding: UTF-8 -*-
import sys

def generate_toml(src):
    link_source = ''
    diancun = 'filecoin-proofs-api = {package = "filecoin-proofs-api", git = "https://github.com/diancun/rust-filecoin-proofs-api.git", branch = "api_v7.0.0" }'
    qiniu = 'filecoin-proofs-api = {package = "filecoin-proofs-api", git = "https://github.com/diancun/rust-filecoin-proofs-api.git", branch = "qn_700_103" }'

    if sys.argv[1] == 'diancun':
        print '****************Linking to diancun source****************.'
        link_source = diancun
    elif sys.argv[1] == 'qiniu':
        print '****************Linking to qiniu source******************.'
        link_source = qiniu
    else:
        print '****************Linking to default filecoin source***************.'
        return

    toml_file = open("rust/Cargo.toml", "r+")
    content = toml_file.read()
    lines = content.splitlines()

    index = 0
    for i in range(0, len(lines)):
        if lines[i] == '[dependencies.filecoin-proofs-api]':
            index = i
            break

    if index == 0:
        for i in range(0, len(lines)):
            if lines[i].find('filecoin-proofs-api') == 0:
                index = i
                break

    if index == 0:
        print 'ERROR: filecoin-proofs-api not found in Cargo.toml'
        return

    end = index+1
    for i in range(index+1, len(lines)):
        if len(lines[i]) == 0:
            end = i
            break

    toml_file.truncate(0)
    toml_file.seek(0, 0)
    for i in range(0, index):
        toml_file.write(lines[i])
        toml_file.write('\n')

    toml_file.write(link_source)
    toml_file.write('\n')

    for i in range(end, len(lines)):
        toml_file.write(lines[i])
        if i != len(lines)-1:
            toml_file.write('\n')

    toml_file.close()

if len(sys.argv) <= 1:
    print '*********************Linking to default filecoin source*******************.'
else:
    generate_toml(sys.argv[1])
