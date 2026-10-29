#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def filter_jp_fast(input_file, output_file="ip/jp/jp_entries.txt"):
    """高效筛选 #JP 条目，适合大文件"""
    
    count = 0
    try:
        with open(input_file, 'r', encoding='utf-8') as fin, \
             open(output_file, 'w', encoding='utf-8') as fout:
            
            for line in fin:
                if '#JP' in line:
                    fout.write(line)
                    count += 1
        
        print(f"筛选完成，共找到 {count} 个 #JP 条目")
        print(f"结果已保存到: {output_file}")
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {input_file}")
        sys.exit(1)

if __name__ == "__main__":
    filter_jp_fast("ip/jp/all.txt")