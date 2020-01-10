# python-learn
学习Python随笔
# 1.Markdown
作为笔记，首先学习Markdown语法，是一种轻量级**标记语言**  

[参考这儿](https:://github.com/younghz/Markdown "Markdown")

# 2.Python基础
  [Python 中文入门指南](http://www.pythondoc.com/pythontutorial3/index.html)  
  [Python 英文文入门指南](https://docs.python.org/3/library/index.html)  

## 2.1 变量和基本数据类型
### 2.1.1 列表
一种数据结构，可以写作中括号之间的一列逗号分隔的值。**列表中的元素不必是同一个类型**  
[列表简单介绍](https://github.com/arivon/python-learn/blob/master/%E5%88%97%E8%A1%A8.md)

## 2.2 运算符
### 2.2.1 关系运算符
关系运算符  
<div>
  <table border = "0">
    <tr>
      <th>Operator</th>
      <th>Meaning</th>
    </tr>
    <tr>
      <th><</th>
      <th>less than</th>
    </tr>    
    <tr>
      <th><=</th>
      <th>less than or equal to</th>
    </tr>
    <tr>
      <th>></th>
      <th>greater than</th>
    </tr>    
    <tr>
      <th>>=</th>
      <th>greater than or equal to</th>
    </tr>    
    <tr>
      <th>==</th>
      <th>equal to</th>
    </tr>    
    <tr>
      <th>!=</th>
      <th>not equal to</th>
    </tr>
   </table>
</div>  

### 2.2.2 逻辑运算符

包括 **and** , **not** , **or** 这几个关键词  

### 2.2.3 简写运算符

x op= expression 为简写运算符的语法形式。等价于 x = x op expression  

### 2.2.4 表达式

每个运算符左右空出一个空格，使代码更可读

## 2.3 类型转换  

<div>
  <table border = "0">
    <tr>
      <th>类型转换函数</th>
      <th>转换路径</th>
    </tr>
    <tr>
      <th>float(string)</th>
      <th>字符串 -> 浮点值</th>
    </tr>    
    <tr>
      <th>int(string)</th>
      <th>字符串 -> 整数值</th>
    </tr>
    <tr>
      <th>str(integer)</th>
      <th>整数值 -> 字符串</th>
    </tr>    
    <tr>
      <th>str(float)</th>
      <th>浮点值 -> 字符串</th>
   </table>
</div>

用法:  
		
		>>> a = 8.1234  
		>>> str(a)  

## 2.3 循环语句
### 2.3.1 while循环  
``while`` 语句的语法如下:  
```python
		while condition：
			statement 1
			statement 2
```
### 2.3.2 for循环  
### 2.3.3 continue 语句
循环中可以使用``continue``，他会跳过其后的代码回到循环开始处执行  
