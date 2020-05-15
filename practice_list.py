#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:22:50 2020

@author: takeomiyamoto
"""
a = ["はほ", "ううそ", "在日でーす", "あへ", "ほあ", "みかん"]
NG_words = ["アホ", "阿呆", "バカ", "馬鹿", "在日", "クソサヨ", "ネトウヨ",
            "バヨ", "パヨ", "？", "?", "変なスレ"]

for i in range(len(NG_words)):
    a = [s for s in a if not NG_words[i] in s]

print(a)