## JavaScript 学习笔记
> 2019/4/22 起 大连 Panasonic 现场
>   [ [MDN JavaScript 指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Introduction) \][【附某前端总结链接】](https://www.cnblogs.com/onepixel/p/7021506.html)[[ECMAScript 6 入门]](http://es6.ruanyifeng.com/#README) [[网道JavaScript 教程]](https://wangdoc.com/javascript/basic/history.html)

#### 1. 基础
* **声明**: 变量以字母, _, $, 这三种开头
  * `var` 全局作用域， ES6后不推荐
  * `let` 局部作用域， 推荐使用
  * `const` 只读属性， 但不能定义只读的`Array`与`Object`，无效
* **数据结构与类型**：六种基本类型 + `Object`

  * `Boolean`
  * `null`
  * `undefined`
  * `String`
  * `Number`
  * `Symbol`，一种实例是唯一不可改变的数据类型，ES6+
  
- **`Map`和`Object`**：
	> - 一个 `Object` 的键只能是字符串或者 `Symbols`，但一个`Map`的键可以是任意值，包括函数、对象、基本类型。
	> - `Map` 中的键值是有序的，而添加到对象中的键则不是。因此，当对它进行遍历时，`Map` 对象是按插入的顺序返回键值。（`for...of`）
	> - 你可以通过 `size` 属性直接获取一个 `Map` 的键值对个数，而 `Object` 的键值对个数只能手动计算。
	> - `Map` 可直接进行迭代，而 `Object` 的迭代需要先获取它的键数组，然后再进行迭代。
	> **`Map`对象常用属性与方法**：[[ MDN Map对象属性与方法 ]](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Map)
	>- `Map.prototype.size` 返回`Map`对象的键/值对的数量。
	>- `Map.prototype.clear()` 移除Map对象的所有键/值对 。
	>- `Map.prototype.delete(key)` 如果 Map 对象中存在该元素，则移除它并返回 true；否则如果该元素不存在则返回 false
	>- `Map.prototype.get(key)` 返回键对应的值，如果不存在，则返回undefined。
	>- `Map.prototype.has(key)` 返回一个布尔值，表示Map实例是否包含键对应的值。
	>- `Map.prototype.set(key, value)` 设置Map对象中键的值。返回该Map对象。
* **`Set`**  [MDN-Set说明](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Set)
	```javascript
	let set = new Set();
	set.add()
	set.has()
	set.delete()
	set.size()
	let arr = Array.from(new Set(arr));
	```
  
* **字面量**， 特殊字符\n, 转义字符\\

#### 2. 流程控制与错误处理
- `false`等效值6个：`undefined` `false` `null` `0` `NaN` `""`；
    > 不要混淆原始的布尔值 `true` `false` 与`Boolean` 对象的真和假；
    
	```javascript
	var b = new Boolean (false);
	if (b) // true
	if (b === true) // false
	```
- 错误处理：`throw...try catch finally`；  
- `Error` 对象：`thorw (new Error('msg'))` ；
- `Promises`:
	- `pending` 正在执行 
	- `rejected` 失败 
	- `fulfilled` 成功 
	- `settled` 处于`fulfilled`或`rejected`中任意一个
		
#### 3.循环与迭代

-  `label`
> 一个`label`提供一个引用到程序其他位置的标识符，如`label`标识循环使用`break,continue`跳转到其位置；  
```javascript
labelLoop: while (true) {
    break labelLoop;
}
```
- `for...in`：循环一个指定的变量来循环一个**对象**所有可枚举的属性；遍历的结果和数组元素的下标不同；
- `for...of`：在可迭代的对象`Array,Map,Set,参数对象Arguments`创建了一个循环，对值的每一个独特的属性调用一个将被执行的自定义的和语句挂钩的迭代；遍历的结果是元素的值；
#### 4. 函数
- 闭包， `arguments`，默认参数`function(a, b = 1)`，剩余参数`function(a, ...b)`
- 预定义函数
> - `eval()`// 对一串字符串形式的JavaScript代码字符求值。
> - `isFinite()` // 判断传入的值是否是有限的数值，如果需要的话，其参数首先被转换为一个数值
> - `isNaN()` // 判断一个值是否是NaN
> - `parseFloat()` // 解析字符串参数，并返回一个浮点数
> - `parseInt()` // 解析字符串参数，并返回指定的基数的整数
> - `encodeURI() / decodeURI()` // 用以一个，两个，三个或四个转义序列表示字符的UTF-8编码替换统一资源标识符（URI）的某些字符来进行编码（每个字符对应四个转义序列，这四个序列组了两个”替代“字符）/ 对应解码
> - `encodeURIComponent() / decodeURIcomponent()` // 用以一个，两个，三个或四个转义序列表示字符的UTF-8编码替换统一资源标识符（URI）的每个字符来进行编码（每个字符对应四个转义序列，这四个序列组了两个”替代“字符）/ 对应解码
#### 4.1 面向对象编程
- 生成实例对象：
> `构造函数 new func()`作为模板，可以生成实例对象。但是，有时拿不到构造函数，只能拿到一个现有的对象。我们希望以这个现有的对象作为模板，生成新的实例对象，这时就可以使用`Object.create()`方法。
- `this`
> 简单说，`this`就是属性或方法“当前”所在的对象。
> （注意箭头函数内的`this`指向外层对象，多层对象嵌套里箭头函数里`this`是和最最外层保持一致的。）
> `JavaScript` 提供了`call`、`apply`、`bind`这三个方法，来切换/固定`this`的指向。[【绑定 this 的方法】](https://wangdoc.com/javascript/oop/this.html#%E7%BB%91%E5%AE%9A-this-%E7%9A%84%E6%96%B9%E6%B3%95)
> - `call`: 函数实例的`call`方法，可以指定函数内部`this`的指向（即函数执行时所在的作用域），然后在所指定的作用域中，调用该函数。
> - `apply`: `apply`方法的作用与`call`方法类似，也是改变`this`指向，然后再调用该函数。唯一的区别就是，它接收一个数组作为函数执行时的参数，
> - `bind`: `bind`方法用于将函数体内的`this`绑定到某个对象，然后返回一个新函数。
- 原型链
> - 原型链的尽头是`null`；
> - `prototype`对象有一个`constructor`属性，默认指向`prototype`对象所在的构造函数。修改原型对象时，一般要同时修改`constructor`属性的指向。`'func'.constructor.name`可以从实例得到构造函数的名称。
> - `instanceof`运算符返回一个布尔值，表示对象是否为某个构造函数的实例。由于任意对象（除了`null`）都是`Object`的实例，所以`instanceof`运算符可以判断一个值是否为非`null`的对象。注意，`instanceof`运算符只能用于对象，不适用原始类型的值。对于`undefined`和`null`，`instanceof`运算符总是返回`false`。
> - 取实例对象`obj`的原型对象，有三种方法:（前两种都不是很可靠）
> `obj.__proto__
 obj.constructor.prototype
 Object.getPrototypeOf(obj)`
> - 继承 [构造函数的继承](https://wangdoc.com/javascript/oop/prototype.html#%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0%E7%9A%84%E7%BB%A7%E6%89%BF)
- 模块 封装立即执行函数或`ES6+`
- 严格模式 `use strict`
> - 只读属性不可写
> - `eval`、`arguments` 不可用作标识名
> - 禁止八进制的前缀`0`表示法
> - 函数不能有重名的参数
> - 全局变量显式声明
> - 禁止 `this` 关键字指向全局对象
> 严格模式对动态绑定做了一些限制。属性和方法到底归属哪个对象，必须在编译阶段就确定。
> - 禁止使用 `with` 语句
> - 正常模式下，`JavaScript` 语言有两种变量作用域（`scope`）：全局作用域和函数作用域。严格模式创设了第三种作用域：`eval` 作用域。严格模式下，`eval` 语句本身就是一个作用域
#### 4.2 异步操作 （任务队列和事件循环）
- 回调函数
- 事件监听
- 发布/订阅  
> 事件完全可以理解成“信号”，如果存在一个“信号中心”，某个任务执行完成，就向信号中心“发布”（publish）一个信号，其他任务可以向信号中心“订阅”（subscribe）这个信号，从而知道什么时候自己可以开始执行。这就叫做”**发布/订阅模式**”

`setTimeout(f, 0)`有几个非常重要的用途。可以调整事件的发生顺序。
- `Promise` [【Promise对象】](http://es6.ruanyifeng.com/#docs/promise)
#### 4.3 `DOM`
- `DOM` 是 `JavaScript` 操作网页的接口，全称为“文档对象模型`（Document Object Model）`。它的作用是将网页转为一个 `JavaScript` 对象，从而可以用脚本进行各种操作。浏览器原生提供`document`节点，代表整个文档。
- **`Cookie`** 
> `Cookie` 是服务器保存在浏览器的一小段文本信息，每个 `Cookie` 的大小一般不能超过`4KB`。浏览器每次向服务器发出请求，就会自动附上这段信息。
#### 5. 表达式与运算符
- **解构赋值**：使得将值从数组，或属性从对象，提取到不同的变量中
	```javascript
	var [a, b, ...rest] = [1, 2, 3, 4, 5] // a = 1, b = 2, rest = [3, 4, 5];
	var o = {p: 1, q: 2};
	var {p, q} = o;
	var {a = 10, b = 5} = {a: 3}; // {a: 3, b: 5};
	
	function f({msg= 'message', options= { x: 0, y: 0 }, name = 'admin'} = {}){
	  console.log(name, msg, options);
	}// 不传参数直接调用也是很好的函数写法
	
	f({
	  options: { x: 18, y: 30 },
	  msg: 'Hi'
	});
	f();
	```
- **`Spread`扩展运算符**：扩展运算符用三个点号表示`'...'`，把数组或类数组对象展开成一系列用逗号隔开的值
	```javascript
	var foo = function(a, b, c) {
		// pass
	}
	foo(arr[0], arr[1], arr[2]); // 传统用法
	foo(...arr); // ES6扩展运算符
	////
	// 数组深拷贝
	var arr2 = arr;
	var arr3 = [...arr];
	console.log(arr===arr2); //true, 说明arr和arr2指向同一个数组
	console.log(arr===arr3); //false, 说明arr3和arr指向不同数组
	```
- **`Rest`运算符**：rest运算符也是三个点号，不过其功能与扩展运算符恰好相反，把逗号隔开的值序列组合成一个数组
	```javascript
	var [a, ...rest] = [1, 2, 3, 4];
	console.log(a);      //1
	console.log(rest);   //[2, 3, 4] 函数调用同理
	```
- **短路求值** `&&`， `||` 
	```javascript
	var a = undefined && 1; // a = undefined
	var a = undefined || 1; // a = 1
	var a = ! undefinde; // a = true
	```
- `in`：如果所指定的属性确实存在于所指定的对象中，则会返回`true`
- `instanceof`：如果所判别的对象确实是所指定的类型，则返回`true`
	```javascript
	var a = new Date;
	a instanceof Date // true
	'abc' instanceof String // false
	```
```
- 扩展语句：允许一个表达式在原地展开
	```javascript
	var a = [1, 2, 3];
	var b = [0, ...a, 4, 5, 6];
```
#### 6. 数字和日期
- 整数数据在运算完毕后，其值在 ± (2<sup>53</sup> − 1)内 可以认为是准确的
- `Number Math Date对象`
 ```javascript
  var date = new Date([parameters]) // para: () / "月 日, 年 时:分:秒." / '年，月，日，时，分，秒'
 ```
#### 7. 文字格式
- `Unicode`字元逸出：任何字符都可以用16进制数转义, 这使得通过`Unicode`转义表示大于`0x10FFFF`的字符成为可能
- 字符串对象
  - 字符串对象方法 [MDN String 对象方法](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Text_formatting)

#### * 小记
##### 1. 区分`Array Object arguments`等的方法之一: 
```javascript
Object.prototype.toString.call([]) // [Object Array]
```
##### 2. `Array`对象 `地址共用` 错误使用记录：
```javascript
var arr = [1, 2, 3];
var re_arr = arr.reverse();
console.log(re_arr) // [3, 2, 1]
console.log(arr)    // [3, 2, 1] 此时相等，注意数组地址共用
////
var arr = [1, 2, 3];
var re_arr = arr.slice().reverse();
console.log(re_arr) // [3, 2, 1]
console.log(arr)    // [1, 2, 3] 此时为复制了arr再反转，不改变原数组
```
##### 3. `Sring`赋值无效（`a`, `b` 换成数组即正常） 原因不明？
```javascript
let a = 'hello';
let b = 'olleh';
a[0] = b[0];
console.log(a) // hello
console.log(b) // olleh
```
##### 3. 牛顿迭代公式 求平方根[【公式链接】](https://blog.csdn.net/u014485485/article/details/77599953)
> [附：MakrDown公式编辑规则](https://www.zybuluo.com/codeep/note/163962)
> 图片格式![防公式不显示](./捕获.PNG)

$$ x_{k + 1} = \frac {1} {2}\left( x_k + \frac {a} {x_k} \right)$$

- 算法题
```javascript
var mySqrt = function(x) {
    // return Math.floor(Math.sqrt(x));
    if (!x) return 0;
    let x1 = 1, x2 = 0;
    while (x1 !== x2) {
        x2 = x1;
        x1 = (x1 + x / x1) / 2;
    }
    return Math.floor(x1);
};
```
##### 4. **时间复杂度**与**空间复杂度**
> - 一个算法的`空间复杂度S(n)`定义为该算法所耗费的存储空间, 是对一个算法在运行过程中临时占用存储空间大小的量度;记作; S(n)=O(f(n))
> - 语句总的执行次数T(n)是关于问题规模n的函数，进而分析T(n)随n的变化情况并确定T(n)的数量级。算法的`时间复杂度T(n)`，也就是算法的时间量度，表示随问题规模n的增大，算法执行时间的增长率和f(n)的增长率相同, f(n)是问题规模n的某个函数, 记作：T(n)= O(f(n))。
##### 5. 杨辉三角元素计算公式
```javascript
let item = 1;
let arr = [];
for (let i = 0; i <= rowNumber; i++) {
    arr.push(item); // item为指定行中的每一项， rowNumber为指定的行
    item = item * (rowNumber- i) / (i + 1); // 求元素公式
}
```
##### 6. 摩尔投票法
> 给定一个整型数组，找出该数组中出现次数大于数组长度一半的值。查询知在任何数组中，出现次数大于该数组长度一半的值只能有一个。
> **摩尔投票法**的基本思想很简单，在每一轮投票过程中，从数组中找出一对不同的元素，将其从数组中删除。这样不断的删除直到无法再进行投票，如果数组为空，则没有任何元素出现的次数超过该数组长度的一半。如果只存在一种元素，那么这个元素则可能为目标元素。
##### 7. 冒泡排序与快速排序（C语言版）
```C
void bubbleSort(int* nums, int numSize)
{
    int i = 0, j = 0, temp = 0;
    bool sts = false;
    for(i = 0; i < numSize - 1; i++)
    {
        sts = false;
        for(j = 0; j < numSize - i - 1; j++)
        {
            if(nums[j] > nums[j + 1])
            {
                sts = true;
                temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
        if(!sts)
        {
            break;
        }
    }
}

void quickSort(int* nums, int left, int right)
{
    if(left >= right) return;
    int i = left, j = right, mid = nums[left];
    while(i < j)
    {
        while(i < j && nums[j] > mid)  j--;
        nums[i] = nums[j];
        while(i < j && nums[i] <= mid) i++;
        nums[j] = nums[i];
    }
    nums[i] = mid;
    quickSort(nums, left, i - 1);
    quickSort(nums, i + 1, right);
}

qucikSort(nums, 0, len - 1);
```
##### 8. `1+3+5+7+9+…+(2n-1)=n^2`，即完全平方数是前n个连续奇数的和
##### 9.  Question ???
```javascript
let str = 'abc';
console.log(str[2]) // 'c'
str[2] = '1';
console.log(str)    // 'abc' ?
str = '1';
console.log(str)    // '1'
```





