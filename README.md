# Xunity-DeepSeekTranslate
Using DeepSeek for XUnity.AutoTranslator

基于[XUnity-Auto-Translator-Gemini](https://github.com/MediocreYYYY/XUnity-Auto-Translator-Gemini)的代码使用AI进行修改，调用DeepSeek的API用于翻译

# AutoTranslatorConfig.ini
修改设置

[Service]
Endpoint=CustomTranslate

---

[Custom]

Url=http://127.0.0.1:5000/translate

# Python
修改API后使用Python运行
Python trans.py

Gemini国内需要代理，用于翻译不稳定。
DeepSeek无须设置代理
