<div align="center">

[**🇺🇸 English**](../../README.md)

</div>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/robonamari/Hadith?style=flat" alt="Code Size">
  <img src="https://tokei.rs/b1/github/robonamari/Hadith?style=flat" alt="Total lines">
  <img src="https://img.shields.io/badge/all%20languages-all%20Versions-blue" alt="All Versions">
  <img src="https://img.shields.io/github/license/robonamari/Hadith" alt="GitHub license">
</p>

---

<p dir="rtl">
این پروژه شامل مجموعه ای از حدیث است که در قالب یک فایل JSON ارائه شده اند. این مجموعه می تواند در برنامه ها و سرویس های مختلف برای نمایش به کاربران استفاده شود.

## ویژگی ها

- دریافت محتوا از یک پایگاه داده آنلاین JSON.
- شامل فقط لینک های کوتاه برای دسترسی سریع.

| عکس | ویدیو | متن | گیف | کل  |
| :-: | :---: | :-: | :-: | :-: |
| :x: |  :x:  | 18  | :x: | 18  |

## کمک

نمونه ای برای دریافت لینک ها به زبان پایتون:

```python
import random

import requests  # pip install requests==2.32.3

request = random.choice(
    requests.get("https://Hadith.robonamari.com/database.json").json()["texts"]
)

print(request["text"])
print(request["name"])
```

</p>
