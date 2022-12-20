#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import module

if __name__ == "__main__":
    test_list = [1, 2, 3, 5, 0, -13, 100]
    test_tuple = [1.5, 2, 123, 5, 0, -167, 100]

    print(f'Max of entered list: {module.func_1()(test_list)}')
    print(f'Min of entered tuple: {module.func_1("min")(test_tuple)}')
