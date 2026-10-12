# issue2pr-sandbox

[Issue2PR](https://github.com/wudi091/Issue2PR) 的测试靶场。

一个玩具工具库（文本、统计、解析），自带测试。**故意留了 bug**——
用来验证 Issue2PR 能不能自己定位、改对、让测试全绿。

## 跑测试

```bash
python -m pytest
```

## 结构

```
issue2pr_sandbox/
  text.py     字符串：word_count / slugify / truncate
  stats.py    统计：mean / median / percentile
  parse.py    解析：parse_duration / parse_size
tests/
  test_text.py
  test_stats.py
  test_parse.py
```
