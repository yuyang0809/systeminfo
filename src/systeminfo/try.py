#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sysinfo

def main():
    output = sysinfo.get_platform_info()
    return(output)

if __name__ == "__main__":
    main()
