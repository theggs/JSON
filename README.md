# JSON

这是个自己玩写的 JSON 生成器和解释器。

## NOTE

目前专注于逻辑、代码质量、对编码的学习，暂时不对如下情况进行处理：

JSON 的 object 的 key 应为 string 类型，所以
python 自带的 JSON 生成器中，如果 dictionary 的 key 是 str, num, bool，会被生成为 str；如果是合法的 tuple，会报错。

## dumps.py

生成器。

## loads.py

解释器。

## examples
### txt

保存了 JSON 格式的测试内容，用于测试解释器。
### examples.py

保存了用于测试生成器的内容。

output function 输出内容为txt，供测试解释器使用。

## test.py

测试

## TODO
- 在 string 中增加 unicode 部分
- 在 num 中增加 科学数字 部分

