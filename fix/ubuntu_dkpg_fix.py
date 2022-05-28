#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fix bug of ubuntu dpkg error
import re
def main():
    fix = open('fix.sh', 'w+')
    for line in open("txt"):
        pkg = re.match(re.compile('''dpkg: 警告: 无法找到软件包 (.+) '''), line)
        if pkg:
            cmd = "sudo apt-get -y install --reinstall " + pkg.group(1)
            fix.write(cmd + '\n')
	    print("OK")
if __name__ == "__main__":
    main()
