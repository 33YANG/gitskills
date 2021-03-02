Work-Record

![MarkDown 命令大全 思维导图模式](https://segmentfault.com/img/bVbu7kA?w=820&h=619)

[【前端工程师手册】]( https://www.gitbook.com/book/leohxj/front-end-database )

***

### 1.相关知识

#### 1.1 网关
- **独占网关** [【独占与非独占链接】](https://docs.informatica.com/zh_cn/data-integration/data-services/10-2/_developer-workflow-guide-workflow-guide_data-services_10-2_ditamap/GUID-7BF72390-ABCA-4C7A-901A-6CD0355B6D2A/GUID-8144A106-7B8B-4FD3-A906-04650350D928.html)

> 使用独占网关可从一个序列流创建多个分支，然后运行其中一个分支上的对象。
> 数据集成服务会按照您在传出网关属性中指定的顺序，为每个序列流上的条件计算。如果某个条件的计算结果为 true，数据集成服务会沿着该序列流所代表的分支执行，而且不会再对其他分支进行计算。如果某个条件的计算结果为 false，数据集成服务会跳过该分支，继续对下一个序列流上的条件进行计算。完成分支上的对象后，数据集成服务会将数据传递给传入独占网关。

- **非独占网关**

> 使用非独占网关可从一个序列流创建多个分支，然后并行运行一个或多个分支上的对象。数据集成服务运行序列流条件计算结果为 true 的每个分支上的对象。

- **并行网关**  [【并行与排他链接】](https://blog.csdn.net/a67474506/article/details/40428709)

> 允许将流程分成多条分支，也可以把多条分支汇聚到一起。

- **排他网关**

> 排他网关（也叫异或（XOR）网关，或更技术性的叫法基于数据的排他网关），用来在流程中实现决策。当流程执行到这个网关，所有外出顺序流都会被处理一遍。其中条件解析为true的顺序（或者没有设置条件，概念上在顺序流上定义了一个'true'）会被选中，让流程继续运行。

#### 1.2 浏览器

#### console

**1. 使用 `console.assert()` 显示条件性错误消息**

`console.assert()` 方法可以仅在其第一个参数为 `false` 时有条件地显示错误字符串（其第二个参数）。

`console.count()` 对打印的字符串的次数进行计数，并在其旁边打印计数 

`console.trace()` 打印函数的调用堆栈踪迹 

**2. 字符串替代和格式设置**

格式：`%格式`。

举例：`console.log("%s has %d points", "Sam", 100);`

- `%s` 将值格式化为字符串
- `%i` 或 `%d` 将值格式化为整型
- `%f` 将值格式化为浮点值
- `%o` 将值格式化为可扩展 DOM 元素。如同在 Elements 面板中显示的一样
- <u>`%O` 将值格式化为可扩展 JavaScript 对象可用于将 DOM 元素格式化为 JavaScript 对象。 也可以使用 console.dir 达到同样的效果 </u>
- `%c` 将 CSS 样式规则应用到第二个参数指定的输出字符串

> `console.log("This is %cMy stylish message", "color: yellow; font-style: italic; background-color: blue;padding: 2px");`

**3. 测量执行时间**

使用 `console.time(label)` 和 `console.timeEnd(label)` 跟踪代码执行点之间经过的时间。

**4. 复制到粘贴板** 

 `copy(object)` 将指定对象的字符串表示形式复制到剪贴板。 

**5. 表达式**

 `$0` 返回最近一次选择的元素或 JavaScript 对象，以此类推。 

 `$()`: 返回与指定 CSS 选择器匹配的第一个元素。 `document.querySelector()` 的快捷键。 

### 2.`JavaScript`知识

#### 2.1 Webpack
本质上，**`webpack`** 是一个现代 `JavaScript` 应用程序的静态模块打包器`(module bundler)`。当 `webpack` 处理应用程序时，它会递归地构建一个依赖关系图`(dependency graph)`，其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个` bundle`。

- **入口 entry**

> 单个入口语法
>
> 对象语法

- **输出 output**

  ```javascript
    output: {
      filename: '[name].js',
      path:  __dirname + '/dist'
    }
  ```

- **模式 mode**

>  development   会将 `process.env.NODE_ENV` 的值设为 `development` 
>
>  production  会将 `process.env.NODE_ENV` 的值设为 `production` 

- **loader**

loader 用于对模块的源代码进行转换，loader 可以使你在 `import` 或"加载"模块时**预处理文件**。因此，loader 类似于其他构建工具中“任务(task)”，并提供了处理前端构建步骤的强大方法。 

 [`module.rules`](https://www.webpackjs.com/configuration/module/#module-rules) 允许你在 webpack 配置中指定多个 loader。 

```js
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          { loader: 'style-loader' },
          {
            loader: 'css-loader',
            options: {
              modules: true
            }
          }
        ]
      }
    ]
  }
```

- **Runtime**

>  runtime 包含：在模块交互时，连接模块所需的加载和解析逻辑。包括浏览器中的已加载模块的连接，以及懒加载模块的执行逻辑。 

- **Manifest**

>  当编译器(compiler)开始执行、解析和映射应用程序时，它会保留所有模块的详细要点。这个数据集合称为 "Manifest"，当完成打包并发送到浏览器时，会在运行时通过 Manifest 来解析和加载模块。无论你选择哪种[模块语法](https://www.webpackjs.com/api/module-methods)，那些 `import` 或 `require` 语句现在都已经转换为 `__webpack_require__` 方法，此方法指向模块标识符(module identifier)。通过使用 manifest 中的数据，runtime 将能够查询模块标识符，检索出背后对应的模块。 

####	2.2 `<script>`里的`defer`和`async`

>`defer`与`async`的区别是：`defer`要等到整个页面在内存中正常渲染结束（DOM 结构完全生成，以及其他脚本执行完成），才会执行；`async`一旦下载完，渲染引擎就会中断渲染，执行这个脚本以后，再继续渲染。
>
>一句话，`defer`是“渲染完再执行”，`async`是“下载完就执行”。
>
>另外，如果有多个`defer`脚本，会按照它们在页面出现的顺序加载，而多个`async`脚本是不能保证加载顺序的。 

#### 2.3 浏览器渲染引擎

> [【浏览器内核】]( https://juejin.im/entry/5a05a25c51882535cd4a4c6b )
>
> [【浏览器原理 掘金】]( https://juejin.im/post/5b0a6f1af265da0ddb63ecd9#heading-27 )
>
> 市面上使用的主流浏览器内核有5类：
>
> - Trident（IE）
> - Gecko（FireFox）
> - Presto（原Oprea）
> - Webkit（Safari）
> - Blink（Chrome）blink源于开源项目chromium， 是webkit的一个分支。

![【浏览器工作原理】](https://user-gold-cdn.xitu.io/2018/5/27/163a0b9b42ae4d1c?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

- **网页的渲染过程**

 网页的生成过程，大致可以分成五步。 

> 1. HTML代码转化成DOM
> 2. CSS代码转化成CSSOM（CSS Object Model）
> 3. 结合DOM和CSSOM，生成一棵渲染树（包含每个节点的视觉信息）
> 4. 生成布局（layout），即将所有渲染树的所有节点进行平面合成
> 5. 将布局绘制（paint）在屏幕上

 **"生成布局"（flow）和"绘制"（paint）这两步，合称为"渲染"（render）。** 

**网页生成的时候，至少会渲染一次。用户访问的过程中，还会不断重新渲染。**

以下三种情况，会导致网页重新渲染。

> - 修改DOM
> - 修改样式表
> - 用户事件（比如鼠标悬停、页面滚动、输入框键入文字、改变窗口大小等等）

**重新渲染，就需要重新生成布局和重新绘制。前者叫做"重排"（reflow），后者叫做"重绘"（repaint）。**

**"重绘"不一定需要"重排"**，比如改变某个网页元素的颜色。但是，**"重排"必然导致"重绘"**，比如改变一个网页元素的位置，就会同时触发"重排"和"重绘"。

- **提高性能的技巧**

>   - 不要编写强制浏览器重新计算布局的JavaScript。分离读写函数，并首先执行读取。
>   - 不要使您的CSS过于复杂。使用更少的CSS和保持你的CSS选择器简单。通过改变class，或者csstext属性，一次性地改变样式。尽可能多避免layout。
>   - 总是选择不触发layout的CSS。
>   - 绘画可能占用比任何其他渲染活动更多的时间。注意绘制瓶颈。
>
>   - window.requestAnimationFrame() 方法。它可以将某些代码放到下一次重新渲染时执行。
>
>   - window.requestIdleCallback()， 也可以用来调节重新渲染。

![](https://user-gold-cdn.xitu.io/2018/5/27/163a0b9b429160eb?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/5/27/163a0b9b42c91981?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

[【浏览器performanceAPI】]( https://juejin.im/entry/58ba9cb5128fe100643da2cc )

#### 2.4 ES新方法：数组 字符串
> - `Array.includes()`  检查数集合中是否包含指定的元素 , 参数是一个字符串。	
> -  `Array.some()`   测试数组中是不是至少有1个元素通过了被提供的函数测试。它返回的是一个Boolean类型的值。 
> - `Array.every()`  循环遍历数组，检查数组中的每个元素项，并返回 `true` 或 `false` 。每一项都必须通过条件表达式 
> - `Array.filter(item => item === '')` 回调函数不能加`{}`？ 
> - `Array.concat()`

------

> - `String.padStart(maxLength, fillString='')` 在字符串开始使用 `fillString` 填充，直到字符串长度为 `maxLength` 。
> - `String.padEnd()` 结束...
> - `String.charAt()`
-----
> **`Set`** 对象允许你存储任何类型的唯一值，无论是[原始值](https://developer.mozilla.org/zh-CN/docs/Glossary/Primitive)或者是对象引用。 
>
> **`Map`**  对象保存键值对，并且能够记住键的原始插入顺序。任何值(对象或者[原始值](https://developer.mozilla.org/zh-CN/docs/Glossary/Primitive)) 都可以作为一个键或一个值。 
>
> **`Symbol`** 是一种基本数据类型， 每个从`Symbol()`返回的symbol值都是唯一的。一个symbol值能作为对象属性的标识符；这是该数据类型仅有的目的。 
>
> **` Proxy `**  对象用于定义基本操作的自定义行为（如属性查找、赋值、枚举、函数调用等）。 **Proxy** 对象用于创建一个对象的代理，从而实现基本操作的拦截和自定义（如属性查找、赋值、枚举、函数调用等）。`const p = new Proxy(target, handler)`
>
> 
>
> **`Reflect`** 是一个内置的对象，它提供拦截 JavaScript 操作的方法。这些方法与[proxy handlers](https://wiki.developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler)的方法相同。Reflect 不是一个函数对象，因此它是不可构造的。 
>
> 	- 检测一个对象是否存在特定属性 Reflect.has(obj, key);
> 	- 返回这个对象自身的属性 Reflect.ownKeys(obj);
> 	- 为这个对象添加一个新的属性 Reflect.set(obj, key, value);
-----

> - **WeakMap**
>
>  **`WeakMap`** 对象是一组键/值对的集合，其中的键是弱引用的。其键必须是对象，而值可以是任意的。 

#### 2.5 栈 异步 事件循环 任务队列

![](https://segmentfault.com/img/bVU9kG?w=922&h=706/view)

>  Js引擎是单线程的，如上图中，它负责维护任务队列，并通过 Event Loop 的机制，按顺序把任务放入栈中执行。而图中的异步处理模块，就是 运行环境 提供的，拥有和Js引擎互不干扰的线程 

- Js 中，有两类任务队列：宏任务队列（macro tasks）和微任务队列（micro tasks）。宏任务队列可以有多个，微任务队列只有一个。

> - 宏任务：script（全局任务）, setTimeout, setInterval, setImmediate, I/O, UI rendering.
> - 微任务：process.nextTick, Promise, Object.observer, MutationObserver.

- 执行顺序：全局任务 ==》微任务Event Queue ==》宏任务队列 Event Queue

> 事件的执行顺序，是先执行宏任务，然后执行微任务，这个是基础，任务可以有同步任务和异步任务，同步的进入主线程，异步的进入Event Table并注册函数，异步事件完成后，会将回调函数放入Event Queue中(宏任务和微任务是不同的Event Queue)，同步任务执行完成后，会从Event Queue中读取事件放入主线程执行，回调函数中可能还会包含不同的任务，因此会循环执行上述操作。
>
注意：setTimeOut并不是直接的把你的回掉函数放进上述的异步队列中去，而是在定时器的时间到了之后，把回掉函数放到执行异步队列中去。如果此时这个队列已经有很多任务了，那就排在他们的后面。 

- setTimeOut执行需要满足两个条件 :

> 1. 主进程必须是空闲的状态，如果到时间了，主进程不空闲也不会执行你的回掉函数 
>2. 这个回掉函数需要等到插入异步队列时前面的异步函数都执行完了，才会执行 

- Promise async/await

> 1.  首先，new Promise是同步的任务，会被放到主进程中去立即执行。而**.then()函数是异步任务**会放到异步队列中去，那什么时候放到异步队列中去呢？当你的promise状态结束的时候，就会立即放进异步队列中去了。 
> 2.  带async关键字的函数会返回一个promise对象，如果里面没有await，执行起来等同于普通函数； 
> 3. await 关键字要在 async 关键字函数的内部，await 写在外面会报错；await如其的语意，就是在等待右侧的表达式完成。此时的await会让出线程，阻塞async内后续的代码，先去执行async外的代码。等外面的同步代码执行完毕，才会执行里面的后续代码。就算await的不是promise对象，是一个同步函数，也会等这样操作。

- **Promise**

> 1. pengding (unresolved)
> 2. fulfilled (resolved successful)
> 3. reject (resloved unsuccessful)
>
> [Resolved different with Fulfilled]( https://stackoverflow.com/questions/35398365/js-promises-fulfill-vs-resolve )

[微任务 宏任务]( https://segmentfault.com/a/1190000011198232 )

#### 2.7 JavaScript模块化编程
- 1. Common.js规范
	> 适用于Node.js，使用`require('module')`同步加载 运行时动态加载
- 2. AMD规范（Asynchronous Module Definition 异步模块定义） 

> 适用于浏览器环境，采用require([module], callback);方式异步加载模块
> 基于AMD规范 有require.js库用来实现浏览器环境下的js模块加载 改库也可用于其他js环境
>
> >   <script src="js/require.js" data-main="js/main"></script>  
> >data-main属性的作用是，指定网页程序的主模块。 
> >  
> >// main.js
> > 
> >require(['moduleA', 'moduleB', 'moduleC'], function (moduleA, moduleB, moduleC){
> > 
> >　　// some code here
> > 
> >});

- 3. ES6 模块化
	> 编译时加载/静态加载
	> 浏览器加载 ES6 模块，也使用<script>标签，但是要加入type="module"属性。浏览器对于带有type="module"的<script>，都是异步加载，不会造成堵塞浏览器，即等到整个页面渲染完，再执行模块脚本，等同于打开了<script>标签的defer属性。
	> 如果网页有多个<script type="module">，它们会按照在页面出现的顺序依次执行。
	> 一旦使用了async属性，<script type="module">就不会按照在页面出现的顺序执行，而是只要该模块加载完成，就执行该模块。
-  4. ES6模块与Node Common.js区别
	> - CommonJS 模块输出的是一个值的拷贝，ES6 模块输出的是值的引用。
	>
	> - CommonJS 模块是运行时加载，ES6 模块是编译时输出接口。
	>
	>   第二个差异是因为 CommonJS 加载的是一个对象（即module.exports属性），该对象只有在脚本运行完才会生成。而 ES6 模块不是对象，它的对外接口只是一种静态定义，在代码静态解析阶段就会生成。
	>   
	> - Node.js 中使用 ES6 模块采用.mjs后缀文件名。也就是说，只要脚本文件里面使用import或者export命令，那么就必须采用.mjs后缀名。
	> 
- 5. 循环加载 [CommonJS与ES6模块的循环加载](https://es6.ruanyifeng.com/#docs/module-loader#%E5%BE%AA%E7%8E%AF%E5%8A%A0%E8%BD%BD)

#### 2.8 闭包

函数和对其周围状态（**lexical environment，词法环境**）的引用捆绑在一起构成**闭包**（**closure**） 
>闭包很有用，因为它允许将函数与其所操作的某些数据（环境）关联起来。 
>
>- 用闭包模拟对象私有方法
>- 用于dom节点绑定的回调方法
>
>不是特殊情况下不必使用闭包，闭包对性能的消耗与内存的占用具有负面影响

#### 2.9 **变量作用域**

>  块级作用域包括变量定义的顶层块中包含的任何子块。 

#### 2.10 JS取模运算（mod） 快排与冒泡

```js
Number.prototype.mod = function(n) {
  return ((this % n) + n) % n;
}
```

Or use:

```js
function mod(n, m) {
  return ((n % m) + m) % m;
}
```

**快速排序 **

```js
var quickSort = function(arr, left = 0, right = arr.length - 1) {
  if (left >= right) return
  let i = left
  let j = right
  let midVal = arr[j]
  while(i < j) {
    while(i < j && arr[i] <= midVal) i++
    arr[j] = arr[i]
    while(i < j && arr[j] > midVal) j--
    arr[i] = arr[j]
  }
  arr[j] = midVal
  quickSort(arr, left, i - 1)
  quickSort(arr, j, right)
}
```

**冒泡排序**

```js
var bubbleSort = function(arr) {
  for(let i = 0; i < arr.length; i++) {
    for(let j = i + 1; j < arr.length; j++) {
      if (arr[i] > arr[j]) {
        let temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
      }
    }
  }
}
```



#### 2.11 **Object方法，原型链与继承**

>  `hasOwnProperty` 是 JavaScript 中唯一一个处理属性并且**不会**遍历原型链的方法。（另一种这样的方法：`Object.keys()`） 

当你执行：

```js
var o = new Foo();
```

JavaScript 实际上执行的是：

```js
var o = new Object();
o.__proto__ = Foo.prototype;
Foo.call(o);
```

[继承与原型链]( https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Inheritance_and_the_prototype_chain )

```js
function Person(name) {
    this.name = name
}
function School(school) {
    this.school = school
}
// 情况一
Person.prototype = new School()
Person.prototype.constructor = Person
let me = new Person()
console.log(me) //Person {name: undefined}
let him = Object.create(me)
console.log(him) //Person {}

// 情况二
Person.prototype = new School()
//Person.prototype.constructor = Person
let me = new Person()
console.log(me) //Person {name: undefined}
let him = Object.create(me)
console.log(him) //School {}
```
##### **for in**

> **`for...in`语句**以任意顺序遍历一个对象的除[Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)以外的[可枚举](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)属性 （包括它的原型链上的可枚举属性） 。  

##### **for of**

>  **`for...of`语句**在[可迭代对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/iterable)（包括 [`Array`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Array)，[`Map`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Map)，[`Set`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Set)，[`String`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/String)，[`TypedArray`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)，[arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions_and_function_scope/arguments) 对象等等）上创建一个迭代循环，调用自定义迭代钩子，并为每个不同属性的值执行语句 

##### **可枚举属性**

> 可枚举属性是指那些内部 “可枚举 enumerable” 标志设置为 true 的属性，对于通过直接的赋值和属性初始化的属性，该标识值默认为即为 true，对于通过 Object.defineProperty 等定义的属性，该标识值默认为 false。可枚举的属性可以通过 for...in 循环进行遍历（除非该属性名是一个 Symbol）。

##### Object构造函数的属性

- **Object.prototype**

  >  `Object.prototype` 属性表示 [`Object`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object) 的原型**对象**。 (构造函数.prototype属性表示构造函数的原型**对象**，包涵 constructor 和 `__proto__`属性等)

##### Object构造函数的方法

- **Object.create()**

> ```js
> function Constructor(){}
> o = new Constructor();
> // 上面的一句就相当于:
> o = Object.create(Constructor.prototype);
> // 当然,如果在Constructor函数中有一些初始化代码,Object.create不能执行那些代码
> ```

- **Object.assgin()**

>  `Object.assign()` 方法用于将所有可枚举属性的值从一个或多个源对象复制到目标对象。它将返回目标对象。
>
> Object.assign(target, ...sources)

- **Object.values**

>  `Object.values()`方法返回一个给定对象自身的所有可枚举属性值的数组，值的顺序与使用[`for...in`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for...in)循环的顺序相同 ( 区别在于 for-in 循环枚举原型链中的属性 )。 

- **Object.entries()**

>  `Object.entries()`方法返回一个给定对象自身可枚举属性的键值对数组，其排列与使用 [`for...in`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for...in) 循环遍历该对象时返回的顺序一致（区别在于 for-in 循环还会枚举原型链中的属性）。 
>
> `Object.fromEntries()` 是 [`Object.entries()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) 的反转函数。 `Object.fromEntries()` 方法把键值对列表转换为一个对象。 

- **Object.keys()**

>  `Object.keys()` 方法会返回一个由一个给定对象的自身可枚举属性组成的数组，数组中属性名的排列顺序和正常循环遍历该对象时返回的顺序一致 。 

- **Object.getOwnPropertyDescriptors()**

> `Object.getOwnPropertyDescriptors() ` 返回对象的所有自有（非继承的）属性描述符。 (返回defineProperty定义的属性)

- **Object.getOwnPropertyNames()**

>  **`Object.getOwnPropertyNames()`**方法返回一个由指定对象的所有自身属性的属性名（包括不可枚举属性但不包括Symbol值作为名称的属性）组成的数组。 
>
>  数组中枚举属性的顺序与通过 [`for...in`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for...in) 循环（或 [`Object.keys`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)）迭代该对象属性时一致。数组中不可枚举属性的顺序未定义。 

- **Object.defineProperty()**

>  `Object.defineProperty()` 方法会直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，并返回此对象。 
>
>  对象里目前存在的属性描述符有两种主要形式：*数据描述符*和*存取描述符*。*数据描述符*是一个具有值的属性，该值可以是可写的，也可以是不可写的。*存取描述符*是由 getter 函数和 setter 函数所描述的属性。 
>
> ```js
> Object.defineProperty(obj, prop, descriptor)
> ```
>
> - 拥有布尔值的键 `configurable`、`enumerable` 和 `writable` 的默认值都是 `false`。
> - 属性值和函数的键 `value`、`get` 和 `set` 字段的默认值为 `undefined`。
>
> ```js
> var o = {};
> 
> o.a = 1;
> // 等同于：
> Object.defineProperty(o, "a", {
>   value: 1,
>   writable: true,
>   configurable: true,
>   enumerable: true
> });
> 
> // 另一方面，
> Object.defineProperty(o, "a", { value : 1 });
> // 等同于：
> Object.defineProperty(o, "a", {
>   value: 1,
>   writable: false,
>   configurable: false,
>   enumerable: false
> });
> ```

- **Object.defineProperties()**

> ```js
> var obj = {};
> Object.defineProperties(obj, {
>   'property1': {
>     value: true,
>     writable: true
>   },
>   'property2': {
>     value: 'Hello',
>     writable: false
>   }
>   // etc. etc.
> });
> ```

- **Object.freeze()**

> **`Object.freeze()`** 方法可以**冻结**一个对象（数组）。浅冻结。一个被冻结的对象再也不能被修改；冻结了一个对象则不能向这个对象添加新的属性，不能删除已有属性，不能修改该对象已有属性的可枚举性、可配置性、可写性，以及不能修改已有属性的值。此外，冻结一个对象后该对象的原型也不能被修改。`freeze()` 返回和传入的参数相同的对象。 

- **Object.is(val, val)**

>  这与 [`===`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Identity) 运算符的判定方式也不一样。[`===`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Identity) 运算符（和[`==`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Comparison_Operators#Equality) 运算符）将数字值 `-0` 和 `+0` 视为相等，并认为 [`Number.NaN`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN) 不等于 [`NaN`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/NaN)。 

- **Object.setPrototypeOf()**

>  `Object.setPrototypeOf()` 方法设置一个指定的对象的原型 ( 即, 内部[[Prototype]]属性）到另一个对象或  [`null`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/null)。 
>
> 语法：
>
> ```
> Object.setPrototypeOf(obj, prototype)
> ```

##### Object实例和Object原型对象
###### 1.属性
- **Object.prototype.constructor** 特定的函数，用于创建一个对象的原型。
- **`Object.prototype.__proto__`**  指向当对象被实例化的时候，用作原型的对象。

###### 2.方法
- **Object.prototype.hasOwnProperty()**  返回一个布尔值 ，表示某个对象是否含有指定的属性，而且此属性非原型链继承的。

- **Object.prototype.isPrototypeOf() ** 返回一个布尔值，表示指定的对象是否在本对象的原型链中。

> `isPrototypeOf()` 方法用于测试一个对象是否存在于另一个对象的原型链上。
>
> `isPrototypeOf()` 与 [`instanceof`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/instanceof) 运算符不同。在表达式 "`object instanceof AFunction`"中，`object` 的原型链是针对 `AFunction.prototype` 进行检查的，而不是针对 `AFunction` 本身。
>
> 语法：
>
> ```js
> prototypeObj.isPrototypeOf(object)
> ```

- **Object.prototype.propertyIsEnumerable()**  返回一个布尔值，表示指定的属性是否可枚举。 用法：
```js
obj.propertyIsEnumerable(prop)
```

#### 2.13 Document对象
`document.write`方法将一个文本字符串写入一个由 [`document.open()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/open) 打开的文档流。

若文档流已关闭则写入内容会覆盖原有的文档。

向一个已经加载，并且没有调用过 [`document.open()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/open) 的文档写入数据时，会自动调用 `document.open`。使用`document.close`关闭文档流。

#### 2.14 `this`

[【MDN-this】](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/this)

在绝大多数情况下，函数的调用方式决定了 `this` 的值（运行时绑定）。`this` 不能在执行期间被赋值，并且在每次函数被调用时 `this` 的值也可能会不同。ES5 引入了 [bind](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) 方法来设置函数的 `this` 值，而不用考虑函数如何被调用的。ES2015 引入了[箭头函数](https://wiki.developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/Arrow_functions)，箭头函数不提供自身的 this 绑定（`this` 的值将保持为闭合词法上下文的值）。在[严格模式](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode)和非严格模式之间也会有一些差别。

- 无论是否在严格模式下，在全局执行环境中（在任何函数体外部）`this` 都指向全局对象。
- 在函数内部，`this`的值取决于函数被调用的方式。
- `this` 在 [类](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes) 中的表现与在函数中类似，因为类本质上也是函数，但也有一些区别和注意事项。在类的构造函数中，`this` 是一个常规对象。类中所有非静态的方法都会被添加到 `this` 的原型中。
- 当函数作为对象里的方法被调用时，`this` 被设置为调用该函数的对象。
- 对于在对象原型链上某处定义的方法，同样的概念也适用。如果该方法存在于一个对象的原型链上，那么 `this` 指向的是调用这个方法的对象，就像该方法就在这个对象上一样。
- 当一个函数用作构造函数时（使用[new](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new)关键字），它的`this`被绑定到正在构造的新对象。
- 当函数被用作事件处理函数时，它的 `this` 指向触发事件的元素。
- 当代码被内联 on-event 处理函数 调用时，它的this指向监听器所在的DOM元素：

- 箭头函数

在[箭头函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/Arrow_functions)中，`this`与封闭词法环境的`this`保持一致。在全局代码中，它将被设置为全局对象。

箭头函数的this被永久绑定到了它外层函数的this。

如果将`this`传递给`call`、`bind`、或者`apply`来调用箭头函数，它将被忽略。

```js
// 创建一个含有bar方法的obj对象，
// bar返回一个函数，这个函数返回this，这个返回的函数是以箭头函数创建的，所以它的this被永久绑定到了它外层函数的this。
// bar的值可以在调用中设置，这反过来又设置了返回函数的值。
var obj = {
  bar: function() {
    var x = (() => this);
    return x;
  }
};
// 作为obj对象的一个方法来调用bar，把它的this绑定到obj。将返回的函数的引用赋值给fn。
var fn = obj.bar();
// 直接调用fn而不设置this，通常(即不使用箭头函数的情况)默认为全局对象 若在严格模式则为undefined
console.log(fn() === obj); // true
// 但是注意，如果你只是引用obj的方法，而没有调用它
var fn2 = obj.bar;
// 那么调用箭头函数后，this指向window，因为它从 bar 继承了this。
console.log(fn2()() == window); // true
```



#### 2.15 解构赋值 剩余参数

- **解构赋值**语法是一种 Javascript 表达式。通过**解构赋值,** 可以将属性/值从对象/数组中取出,赋值给其他变量。

- **剩余参数**语法允许我们将一个不定数量的参数表示为一个数组。

> 如果函数的最后一个命名参数以`...`为前缀，则它将成为一个由剩余参数组成的真数组，其中从`0`（包括）到`theArgs.length`（排除）的元素由传递给函数的实际参数提供。

> 剩余参数和 `arguments`对象之间的区别主要有三个：
>
> - 剩余参数只包含那些没有对应形参的实参，而 `arguments` 对象包含了传给函数的所有实参。
> - `arguments`对象不是一个真正的数组，而剩余参数是真正的 `Array`实例，也就是说你能够在它上面直接使用所有的数组方法，比如 `sort`，`map`，`forEach`或`pop`。
> - `arguments`对象还有一些附加的属性 （如`callee`属性）。



#### 2.16 防抖与节流

函数防抖关注一定时间连续触发的事件只在最后执行一次，而函数节流侧重于一段时间内只执行一次。

- debounce

```js
function debounce(fn, delay) {
    const timer; // 维护一个 timer
    return function () {
        const args = arguments;
        if (timer) {
            clearTimeout(timer);
        }
        timer = setTimeout(() => {
            fn.apply(this, args); // 用apply指向调用debounce的对象，相当于_this.fn(args);
        }, delay);
    };
}
```

> - 搜索框搜索输入。只需用户最后一次输入完，再发送请求
> - 手机号、邮箱验证输入检测
> - 窗口大小Resize。只需窗口调整完成后，计算窗口大小。防止重复渲染。

- throttle

```js
function throttle(fn, delay) {
    const timer;
    return function () {
        var args = arguments;
        if (timer) {
            return;
        }
        timer = setTimeout(function () {
            fn.apply(this, args);
            timer = null; // 在delay后执行完fn之后清空timer，此时timer为假，throttle触发可以进入计时器
        }, delay)
    }
}
```

> - 滚动加载，加载更多或滚到底部监听
> - 谷歌搜索框，搜索联想功能
> - 高频点击提交，表单重复提交

### 3. CSS

> 1`inch` = 2.54 `cm`  1 `ft` = 30.48 `cm`

#### 3.1 [CSS垂直居中方法]( https://juejin.im/post/5a5ca65a6fb9a01ca3254537 )
- Flex 弹性布局
```css
#father {
    width: 300px;
    height: 300px;
    background: #ddd;
    display: flex;
    align-items: center;
}
#child {
    width: 300px;
    height: 100px;
    background: orange;
}
```
#### 3.2 CSS伪元素与伪类
- 伪元素与伪类

> **伪元素：** 是一个附加至选择器末的关键词，允许你对被选择元素的特定部分修改样式 ，用于将特殊的效果添加到某些选择器。 
>
> `::first-letter ::first-line ::before ::after`
>
> **伪类：**  是添加到选择器的关键字，指定要选择的元素的特殊状态 ，用于向某些选择器添加特殊的效果。 
>
> `:visited :focus :hover :checked :active :link :first-child :lang`

#### 3.3 CSS `Flex`布局

 `Flex` 是 `Flexible Box` 的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。

> Webkit 内核的浏览器，必须加上`-webkit`前缀。 
>
> 设为 Flex 布局以后，子元素的`float`、`clear`和`vertical-align`（用来指定行内元素（inline）或表格单元格（table-cell）元素的垂直对齐方式。）属性将失效。 
>
> - `flex: initial`  是把flex元素重置为Flexbox的初始值，它相当于 `flex: 0 1 auto`。 
> - `flex: auto`  等同于 `flex: 1 1 auto`；  和上面的 `flex:initial` 基本相同，但是这种情况下，flex元素在需要的时候既可以拉伸也可以收缩。 
> - `flex: none`  可以把flex元素设置为不可伸缩。它和设置为 `flex: 0 0 auto` 是一样的。元素既不能拉伸或者收缩，但是元素会按具有 `flex-basis: auto` 属性的flexbox进行布局。 
> -  常看到的 `flex: 1` 或者 `flex: 2` 等等。它相当于`flex: 1 1 0`。元素可以在`flex-basis`为0的基础上伸缩。 
>
> ![【Flex布局】](http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071004.png)

##### 3.3.1. 容器属性

- `flex-direction` 
> 决定主轴的方向（即项目的排列方向）。 
>
> `row (default) | row-reverse | column | column-reverse`
- `flex-wrap`
> 属性定义，如果一条轴线排不下，如何换行。
>
> `nowrap | wrap | wrap-reverse`

- `flex-flow`

>  属性是`flex-direction`属性和`flex-wrap`属性的简写形式，默认值为`row nowrap`。 
>
> `<flex-direction> || <flex-wrap>`

- `justifly-content`

>  属性定义了项目在主轴上的对齐方式。 
>
> `flex-start | flex-end | center | space-between（两端对齐，间隔相等） | space-around（子元素两侧间隔相等，即两元素之间间隔为一个元素间隔二倍）`

- `align-items`

>  属性定义项目在交叉轴上如何对齐。 
>
> `flex-start | flex-end | center | baseline（以第一行文字为基线对齐） | stretch`

- `align-content`

>  属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。 
>
> `flex-start | flex-end | center | space-between | space-around | stretch`

##### 3.3.2 成员属性

- `order`

>  属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。 

- `flex-grow`

>  属性定义项目的放大比例，默认为`0`，即如果存在剩余空间，也不放大。如果所有项目的`flex-grow`属性都为1，则它们将等分剩余空间（如果有的话）。如果一个项目的`flex-grow`属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。 

- `flex-shrink`

>  属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。 
>
>  如果所有项目的`flex-shrink`属性都为1，当空间不足时，都将等比例缩小。如果一个项目的`flex-shrink`属性为0，其他项目都为1，则空间不足时，前者不缩小。 

- `flex-basis`

>  属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为`auto`，即项目的本来大小。 
>
> `<length> | auto`

- `flex`

> 属性是`flex-grow`, `flex-shrink` 和 `flex-basis`的简写，默认值为`0 1 auto`。后两个属性可选。 建议优先使用这个属性，而不是单独写三个分离的属性 。

- `align-self`

>  属性允许单个项目有与其他项目不一样的对齐方式，可覆盖`align-items`属性。默认值为`auto`，表示继承父元素的`align-items`属性，如果没有父元素，则等同于`stretch`。 
>
> `auto | flex-start | flex-end | center | baseline | stretch`

#### 3.4 `position`定位

可以修改`top, left, bottom, right`值

- `static` 默认

-  `relative` 

> 设置了相对定位之后，元素会在自身文档流所在位置上被移动，其他的元素则不会调整位置来弥补它偏离后剩下的空隙。 

- `absolute`

>  设置了绝对定位之后，元素脱离文档流，其他的元素会调整位置来弥补它偏离后剩下的空隙。元素偏移是相对于是它最近的设置了定位属性（`position`值不为static）的元素。 

- `fixed`

>  设置了固定定位之后，元素相对的偏移的参考是可视窗口，即使页面滚动，元素仍然会在固定位置。 

- `sticky`

>  粘性定位可以被认为是相对定位和固定定位的混合。元素在跨越特定阈值前为相对定位，之后为固定定位。 

#### 3.5 CSS 书写顺序

> 1. 位置属性(`position, top, right, z-index, display, float等)`
> 2. 大小`(width, height, padding, margin)`
> 3. 文字系列`(font, line-height, letter-spacing, color- text-align等)`
> 4. 背景`(background, border等)`
> 5. 其他`(animation, transition等)`

#### 3.6 CSS关系选择器

| 选择器        | 选择的元素                                                   |
| ------------- | ------------------------------------------------------------ |
| A E           | 元素A的任一后代元素E (后代节点指A的子节点，子节点的子节点，以此类推) |
| A>E           | 元素A的任一子元素E(也就是直系后代)                           |
| E:first-child | 任一是其父母结点的第一个子节点的元素E                        |
| B+E           | 元素B的任一下一个兄弟元素E                                   |
| B~E           | B元素后面的拥有共同父元素的兄弟元素E                         |

#### 3.7 `display`

- `block`

> 1. block元素会独占一行，多个block元素会各自新起一行。默认情况下，block元素宽度自动填满其父元素宽度。
> 2. block元素可以设置width,height属性。块级元素即使设置了宽度,仍然是独占一行。
> 3. block元素可以设置margin和padding属性。

- `inline`

> 1. inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化。
> 2. inline元素设置width,height属性无效。
> 3. inline元素的margin和padding属性，水平方向的padding-left, padding-right, margin-left, margin-right都产生边距效果；但竖直方向的padding-top, padding-bottom, margin-top, margin-bottom不会产生边距效果。

- `inline-block`

> 1. 简单来说就是将对象呈现为inline对象，但是对象的内容作为block对象呈现。之后的内联对象会被排列在同一行内。比如我们可以给一个link（a元素）inline-block属性值，使其既具有block的宽度高度特性又具有inline的同行特性。

#### 3.8 `filter`

>  **`filter `**CSS属性将模糊或颜色偏移等图形效果应用于元素。滤镜通常用于调整图像，背景和边框的渲染。 
>
>  ` url() blur() brightness() contrast() drop-shadow() grayscale() `等等

#### 3.9 `outline`与`border`与`box-shadow`
- 边界`border`和轮廓`outline`很相似。然而轮廓在以下方面与边界不同

> 1. 轮廓不占据空间，他们在元素内容之外绘制
> 2. 根据规范，轮廓不必为矩形，尽管通常是矩形。

- border

> border-width: (top bottom right left) thin细 medium中 thick宽、像素单位
>
> border-style： none hidden（权重大于none） dotted（一系列圆点） dashed（方形虚线） solid （实线） double（双实线） groove（雕刻） ridge（浮雕 与groove相反） inset（陷入） outset（突出）
>
> border-color：（top bottom right left）（ horizontal 水平 vertical 垂直）

-  CSS的`outline`属性是用来设置一个或多个单独的轮廓属性的简写属性

> outline-width outline-style outline-color

- box-shadow

> box-shadow: (inset) x-offset y-offset blur-radius spread-radius color
>
> inset 0 0 2px 2px #333

#### 3.10 `Less` 常用颜色操作函数

> - saturate(#fff, 10%)    增加一定数值的颜色饱和度。 变亮
> - desaturate(#fff, 10%)   降低一定数值的颜色饱和度。 变暗
> - lighten()   增加一定数值的颜色亮度。 
> - darken()   降低一定数值的颜色亮度。 
> - fadein()   降低颜色的透明度（或增加不透明度），令其更不透明。 
> - fadeout()   增加颜色的透明度（或降低不透明度），令其更透明。对不透明的颜色无效。 
> - fade()   给颜色（包括不透明的颜色）设定一定数值的透明度。 
> - spin()   任意方向旋转颜色的色相角度 (hue angle)。 
> - mix()   根据比例混合两种颜色，包括计算不透明度。 
> - greyscale()   完全移除颜色的饱和度，与 `desaturate(@color, 100%)` 函数效果相同。 
> - contrast()   选择两种颜色相比较，得出哪种颜色的对比度最大就倾向于对比度最大的颜色。 

#### 3.11 overflow word-break与white-space

1. `overflow`

>  为使 `overflow `有效果，块级容器必须有一个指定的高度（`height`或者`max-height`）或者将`white-space`设置为`nowrap`。 
>
>  **注意:** 设置一个轴为`visible`（默认值），同时设置另一个轴为不同的值，会导致设置`visible`的轴的行为会变成`auto`。  
>
>  **注意**: 即使将overflow设置为hidden，也可以使用JavaScript [`Element.scrollTop`](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/scrollTop) 属性来滚动HTML元素。

2. `word-break`

  CSS 属性 `word-break` 指定了怎样在单词内断行。 

> - normal
> - break-all  对于non-CJK (CJK 指中文/日文/韩文) 文本，可在任意字符间断行。 
> - keep-all  CJK 文本不断行。 Non-CJK 文本表现同 `normal`。 

3. `white-space`

 **`white-space`** CSS 属性是用来设置如何处理元素中的 [空白](https://developer.mozilla.org/en-US/docs/Glossary/whitespace)。 

> - normal  连续的空白符会被合并，换行符会被当作空白符来处理。换行在填充「行框盒子([line boxes](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting))」时是必要。 
> - nowrap  和 normal 一样，连续的空白符会被合并。但文本内的换行无效。 
> - pre  连续的空白符会被保留。在遇到换行符或者[` `](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br)元素时才会换行。 
> - pre-wrap  连续的空白符会被保留。在遇到换行符或者[` `](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br)元素，或者需要为了填充「行框盒子([line boxes](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting))」时才会换行。 
> - pre-line  连续的空白符会被合并。在遇到换行符或者[` `](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br)元素，或者需要为了填充「行框盒子([line boxes](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting))」时会换行。 
> - break-space 与 `pre-wrap`的行为相同，除了：
>   - 任何保留的空白序列总是占用空间，包括在行尾。
>   - 每个保留的空格字符后都存在换行机会，包括空格字符之间。
>   - 这样保留的空间占用空间而不会挂起，从而影响盒子的固有尺寸（最小内容大小和最大内容大小）。

#### 3.12 Background

 **`background`** 是一种CSS简写属性， 可以在一次声明中定义一个或多个属性

- `background` 属性被指定多个背景层时，使用逗号分隔每个背景层。

- 在每一层中，下面的值可能出现0次或者1次：

	- <attachment>
	- <bg-image>
	- <position>
	- <bg-size>
	- <repeat-style>

- <bg-size>只能接着<position>出现， 以‘/’分割，如：‘center/80%’
-  [`background-color`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-color) 只能在background的最后一个属性上定义，因为整个元素只有一种背景颜色。 

| 属性名                                                       | 可能的值                                                     | 默认值      |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :---------- |
| [background](http://www.w3.org/TR/css3-background/#background) | 是一种简写方式：bg-image \|\| bg-position \|\| / bg-size \|\| repeat-style \|\| attachment \|\| bg-origin，最后一个背景层可以设置background-color |             |
| [background-attachment](http://www.w3.org/TR/css3-background/#background-attachment) | scroll \| fixed \| local                                     | scroll      |
| [background-clip](http://www.w3.org/TR/css3-background/#background-clip) | border-box \| padding-box 表示背景渲染的方法：padding box表示背景在padding box内渲染；border-box表示背景在border-box内渲染 | border-box  |
| [background-color](http://www.w3.org/TR/css3-background/#background-color) | <color>                                                      | transparent |
| [background-image](http://www.w3.org/TR/css3-background/#background-image) | image \| none 可以设置多个背景图，以逗号（,）分隔开。none也代表一个背景层 | none        |
| [background-origin](http://www.w3.org/TR/css3-background/#background-origin) | border-box \| padding-box \| content-box 背景相对的位置，相对于上面3个值中的一个。 | padding-box |
| [background-position](http://www.w3.org/TR/css3-background/#background-position) | % length top right bottom left center 这些属性的设置方法跟以前类似 | 0% 0%       |
| [background-repeat](http://www.w3.org/TR/css3-background/#background-repeat) | repeat-x \| repeat-y \| [repeat \| space \| round \| no-repeat]{1,2} 平铺方式 | repeat      |
| [background-size](http://www.w3.org/TR/css3-background/#background-size) | [length \| % \| auto ]{1,2} \| cover \| contain 设置背景的大小。contain表示按比例缩放占据最大高度或者宽度的背景；cover表示铺满整个背景。 | auto        |

#### 3.13 网格布局 `grid`

 **CSS 网格布局**擅长于将一个页面划分为几个主要区域，以及定义这些区域的大小、位置、层次等关系（前提是HTML生成了这些区域）。 

>  网格是一组相交的水平线和垂直线，它定义了网格的列和行。我们可以将网格元素放置在与这些行和列相关的位置上。

**Grid布局特点：**

> -   固定的位置和弹性的轨道的大小 
>
>   你可以使用固定的轨道尺寸创建网格，比如使用像素单位。你也可以使用比如百分比或者专门为此目的创建的新单位 `fr`来创建有弹性尺寸的网格。 
>
> -  元素位置 
>
>    你可以使用行号、行名或者标定一个网格区域来精确定位元素。网格同时还使用一种算法来控制未给出明确网格位置的元素。 

**Grid布局与Flex布局**

>  Grid 布局与 [Flex 布局](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html)有一定的相似性，都可以指定容器内部多个项目的位置。但是，它们也存在重大区别。
>
> Flex 布局是轴线布局，只能指定"项目"针对轴线的位置，可以看作是**一维布局**。Grid 布局则是将容器划分成"行"和"列"，产生单元格，然后指定"项目所在"的单元格，可以看作是**二维布局**。 Grid 布局远比 Flex 布局强大。 

>  需要按行或者列控制布局？那就用弹性盒子 
>
>  需要同时按行和列控制布局？那就用网格 

- 容器和项目

> 采用网格布局的区域，称为"容器"（container）。容器内部采用网格定位的子元素，称为"项目"（item）。  项目只能是容器的顶层子元素，不包含项目的子元素

- 行和列

> 容器里面的水平区域称为"行"（row），垂直区域称为"列"（column）。 

- 单元格

> 行和列的交叉区域，称为"单元格"（cell）。

- 网格线

> 划分网格的线，称为"网格线"（grid line）。水平网格线划分出行，垂直网格线划分出列。
>
> 正常情况下，`n`行有`n + 1`根水平网格线，`m`列有`m + 1`根垂直网格线，比如三行就有四根水平网格线。

##### 3.13.1 **容器属性**

1. `display: grid / inline-grid`

>  注意，设为网格布局以后，容器子元素（项目）的`float`、`display: inline-block`、`display: table-cell`、`vertical-align`和`column-*`等设置都将失效。 

2. `grid-template-columns grid-template-rows`

 `grid-template-columns`属性定义每一列的列宽，`grid-template-rows`属性定义每一行的行高。 

> - 单位可以使用绝对单位，相对百分比，fr（表示比例关系），或者混合使用
>
> - 可以使用`repeat()`函数，简化重复的值。 `repeat()`接受两个参数，第一个参数是重复的次数，第二个参数是所要重复的值。 
> - auto-fill  如果希望每一行（或每一列）容纳尽可能多的单元格，这时可以使用`auto-fill`关键字表示自动填充。 `grid-template-columns: repeat(auto-fill, 100px);` 表示每列宽度`100px`，然后自动填充，直到容器不能放置更多的列。 
> -  `minmax()` 函数产生一个长度范围，表示长度就在这个范围之中。它接受两个参数，分别为最小值和最大值。 `grid-template-columns: 1fr 1fr minmax(100px, 1fr);` 表示列宽不小于`100px`，不大于`1fr`。 
> -  `auto`关键字表示由浏览器自己决定长度。 
> - 网格线的名称  `grid-template-columns`属性和`grid-template-rows`属性里面，还可以使用方括号，指定每一根网格线的名字，方便以后的引用。`grid-template-columns: [c1] 100px [c2] 100px [c3] auto [c4]; `  上面代码指定网格布局为3行 x 3列，因此有4根垂直网格线和4根水平网格线。方括号里面依次是这八根线的名字。网格布局允许同一根线有多个名字

两栏布局：

```css
.wrapper {
  display: grid;
  grid-template-columns: 70% 30%;
}
```

12列布局：

```css
grid-template-columns: repeat(12, 1fr);
```

3. `grid-gap` `grid-row-gap` `grid-column-grap`

>  `grid-row-gap`属性设置行与行的间隔（行间距），`grid-column-gap`属性设置列与列的间隔（列间距）。   如果`grid-gap`省略了第二个值，浏览器认为第二个值等于第一个值。 
>
> ```css
> grid-gap: <grid-row-gap> <grid-column-gap>;
> ```

>  根据最新标准，上面三个属性名的`grid-`前缀已经删除，`grid-column-gap`和`grid-row-gap`写成`column-gap`和`row-gap`，`grid-gap`写成`gap`。 

4. `grid-template-areas`

 网格布局允许指定"区域"（area），一个区域由单个或多个单元格组成。`grid-template-areas`属性用于定义区域。 

```css
display: grid;
grid-template-columns: 100px 100px 100px;
grid-template-rows: 100px 100px 100px;  
grid-template-areas: 'a b c'
                     'd e f'
                     'g h i';
/* grid-template-areas: "header header header"
                     "main main sidebar"
                     "footer footer footer"; * /
```

上面代码先划分出9个单元格，然后将其定名为`a`到`i`的九个区域，分别对应这九个单元格。  如果某些区域不需要利用，则使用"点"（`.`）表示。 

>  注意，区域的命名会影响到网格线。每个区域的起始网格线，会自动命名为`区域名-start`，终止网格线自动命名为`区域名-end`。 

5. `grid-auto-flow`

>  划分网格以后，容器的子元素会按照顺序，自动放置在每一个网格。默认的放置顺序是"先行后列"。

> 这个顺序由`grid-auto-flow`属性决定，默认值是`row`，即"先行后列"。也可以将它设成`column`，变成"先列后行"。
>
>  还可以设成`row dense`和`column dense`。这两个值主要用于，某些项目指定位置以后，剩下的项目怎么自动放置。（ 尽可能紧密填满 ）

6. **`align-items` `justify-items` `place-items`**

`justify-items`属性设置单元格内容的水平位置（左中右）

`align-items`属性设置单元格内容的垂直位置（上中下）。 

> - start：对齐单元格的起始边缘。
> - end：对齐单元格的结束边缘。
> - center：单元格内部居中。
> - stretch：拉伸，占满单元格的整个宽度（默认值）。

> ```css
> place-items: <align-items> <justify-items>;
> ```

7. **`justify-content` `align-content` `place-content`**

`justify-content`属性是整个内容区域在容器里面的水平位置（左中右）

`align-content`属性是整个内容区域的垂直位置（上中下）。 

> ```css
> start | end | center | stretch | space-around | space-between | space-evenly;
> ```

> ```css
> place-content: <align-content> <justify-content>
> ```

8. **`grid-auto-columns` `grid-auto-rows`**

`grid-auto-columns`属性和`grid-auto-rows`属性用来设置，浏览器自动创建的多余网格的列宽和行高。它们的写法与`grid-template-columns`和`grid-template-rows`完全相同。

9. **`grid-template`  `grid`**

>  `grid-template` 属性是 `grid-template-columns`、`grid-template-rows`和`grid-template-areas`这三个属性的合并简写形式。 

>  `grid`属性是`grid-template-rows`、`grid-template-columns`、`grid-template-areas`、 `grid-auto-rows`、`grid-auto-columns`、`grid-auto-flow`这六个属性的合并简写形式。 

##### 3.13.2 项目属性

1. `grid-column-start` `grid-column-end` `grid-row-start` `grid-row-end`  

项目的位置是可以指定的，具体方法就是指定项目的四个边框，分别定位在哪根网格线。 

> - `grid-column-start`属性：左边框所在的垂直网格线
> - `grid-column-end`属性：右边框所在的垂直网格线
> - `grid-row-start`属性：上边框所在的水平网格线
> - `grid-row-end`属性：下边框所在的水平网格线

```css
.item-1 {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 2;
  grid-row-end: 4;
}
.item-1 {
  grid-column-start: header-start;
  grid-column-end: header-end;
}
.item-1 {
  grid-column-start: span 2;
}
```

 属性的值还可以使用`span`关键字，表示"跨越"，即左右边框（上下边框）之间跨越多少个网格。  如果产生了项目的重叠，则使用`z-index`属性指定项目的重叠顺序。 

2. `grid-column` `grid-row`

 `grid-column`属性是`grid-column-start`和`grid-column-end`的合并简写形式

`grid-row`属性是`grid-row-start`属性和`grid-row-end`的合并简写形式。斜杠以及后面的部分可以省略，默认跨越一个网格。 

```css
.item {
  grid-column: <start-line> / <end-line>;
  grid-row: <start-line> / <end-line>;
}
```

3. `grid-area`

> `grid-area`属性指定项目放在哪一个区域。

>  `grid-area`属性还可用作`grid-row-start`、`grid-column-start`、`grid-row-end`、`grid-column-end`的合并简写形式，直接指定项目的位置。 

4. `justify-self` `align-self` `place-self`

> `justify-self`属性设置单元格内容的水平位置（左中右），跟`justify-items`属性的用法完全一致，但只作用于单个项目。
>
> `align-self`属性设置单元格内容的垂直位置（上中下），跟`align-items`属性的用法完全一致，也是只作用于单个项目。

```css
.item {
  justify-self: start | end | center | stretch;
  align-self: start | end | center | stretch;
}
```

> `place-self`属性是`align-self`属性和`justify-self`属性的合并简写形式。省略第二个值，`place-self`属性会认为这两个值相等。

#### 3.14 `will-change`与` transform-origin`

>  [CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) 属性 `will-change` 为web开发者提供了一种告知浏览器该元素会有哪些变化的方法，这样浏览器可以在元素属性真正发生变化之前提前做好对应的优化准备工作。 这种优化可以将一部分复杂的计算工作提前准备好，使页面的反应更为快速灵敏。 
>
> - **不要将 will-change 应用到太多元素上** 
> -  **有节制地使用** 
> -  **不要过早应用 will-change 优化** 
> -  **给它足够的工作时间** 

>  **`transform-origin`** CSS属性让你更改一个元素变形的原点。 `transform-origin`属性可以使用一个，两个或三个值来指定，其中每个值都表示一个偏移量。 没有明确定义的偏移将重置为其对应的[初始值](https://developer.mozilla.org/zh-CN/docs/Web/CSS/initial_value)。 

#### 3.15 块格式化上下文
块格式化上下文（Block Formatting Context，BFC） 是Web页面的可视CSS渲染的一部分，是块盒子的布局过程发生的区域，也是浮动元素与其他元素交互的区域。

> 块格式化上下文对浮动定位（参见 [`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float)）与清除浮动（参见 [`clear`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/clear)）都很重要。浮动定位和清除浮动时只会应用于同一个BFC内的元素。浮动不会影响其它BFC中元素的布局，而清除浮动只能清除同一BFC中在它前面的元素的浮动。外边距折叠（[Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing)）也只会发生在属于同一BFC的块级元素之间。

#### 3.16 Animation

[CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) **animation** 属性是 [`animation-name`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-name)，[`animation-duration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-duration), [`animation-timing-function`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-timing-function)，[`animation-delay`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-delay)，[`animation-iteration-count`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-iteration-count)，[`animation-direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-direction)，[`animation-fill-mode`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-fill-mode) 和 [`animation-play-state`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-play-state) 属性的一个简写属性形式。

创建动画序列，需要使用[`animation`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation)属性或其子属性，该属性允许配置动画时间、时长以及其他动画细节，但该属性不能配置动画的实际表现，动画的实际表现是由 [`@keyframes`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@keyframes)规则实现。`0%`表示动画的第一时刻，`100%`表示动画的最终时刻。因为这两个时间点十分重要，所以还有特殊的别名：`from`和`to`。

> **[`animation-delay`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-delay)**设置延时，即从元素加载完成之后到动画序列开始执行的这段时间。
>
> **[`animation-direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-direction)**设置动画在每次运行完后是反向运行还是重新回到开始位置重复运行。
>
> **[`animation-duration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-duration)**设置动画一个周期的时长。
>
> **[`animation-iteration-count`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-iteration-count)**设置动画重复次数， 可以指定infinite无限次重复动画
>
> **[`animation-name`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-name)**指定由[`@keyframes`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/@keyframes)描述的关键帧名称。
>
> **[`animation-play-state`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-play-state)**允许暂停和恢复动画。
>
> **[`animation-timing-function`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-timing-function)**设置动画速度， 即通过建立加速度曲线，设置动画在关键帧之间是如何变化。
>
> **[`animation-fill-mode`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/animation-fill-mode)**指定动画执行前后如何为目标元素应用样式。



### 4. Vue

#### 4.1 `ref`

`ref` 被用来给元素或者子组件注册引用信息。

引用信息将会注册在父组件的`$refs`对象上。

如果在普通DOM元素上使用，引用指向就是DOM元素，如果在子组件上使用，引用指向组件实例。

#### 4.2 Vue.js

- `slot` `v-slot` `slot-scope` 
- `keep-alive` ` v-once`

- **Vue 父子组件之间数据交换、通讯方式**
  - Vuex 
  - prop传递  v-bind:prop.sync
  - slot插槽 
  - $parent、$refs $root
  - 依赖注入 provide inject

- **进入、离开， 列表过渡**

> -  v-enter 
> - v-enter-active
> - v-enter-to
> - v-leave
> - v-leave-active
> - v-leave-to

- **混入 Vue.mixin Vue.extend**

- **自定义指令(directive)**

#### 4.2 Vue生命周期

Vue实例在被创建时与创建完成都要经历一系列的初始化过程， 需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。 在这期间运行的一系列的函数组成了Vue生命周期。

> **beforeCreated**
>
> Vue实例初始化 可以访问到this 无法访问其他属性（data computed method watch）
>
> **created**
>
> 实例创建完成 进行事件初始化 数据观测 可访问 data computed method watch 上的方法或数据 并会随之改变更新视图 未挂载到dom $el refs无法访问
>
> **beforeMouted**
>
> 挂载之前调用 首先判断是否提供$el 否则停止生命周期 有则根据是否提供template来编译成render函数 生成虚拟dom （访问不到$el因为还是虚拟dom尚未挂载），无template则使用outer html，如果实例中调用了render函数则 优先渲染render函数里的html
>
> **mouted**
>
> Vue实例挂载到dom上完成 可以操作dom $refs 但不能保证子节点挂载完成
>
> **beforeUpdate**
>
> 数据更新前 虚拟dom重新渲染前 调用，此时还可对改变的data做操作 可以监听到data的变化但view视图尚未更新
>
> **updated**
>
> 相应组件重新渲染完成 视图更新
>
> **beforeDestory**
>
> 实例销毁前最后的调用机会 实例完全可用 任可访问完整的实例和方法
>
> **destoryed**
>
> vue实例销毁 与之绑定的数据与方法 事件 监听器 全部解绑 不可访问到实例 所有子实例被销毁完成


#### 4.3 `Vue`源码学习
- `flow`
> Flow 是 facebook 出品的 JavaScript 静态类型检查工具。Vue.js 的源码利用了 Flow 做了静态类型检查。

- `AST`

>  在计算机科学中，抽象语法树（Abstract Syntax Tree，AST），或简称语法树（Syntax tree），是源代码语法结构的一种抽象表示。 它以树状的形式表现编程语言的语法结构，树上的每个节点都表示源代码中的一种结构。 

- 好的实现方法记录

1. 压平[[1,2], [3,4], [5,6]]这种结构的数组

```js
function normalizeArr(arr) { 
    for(let i = 0, len = arr.length; i < len; i++) {
		if (Array.isArray(arr[i])) {
            return Array.prototype.concat.apply([], arr)
        }
    }
    return arr
}
```
2. 没有赋值操作时，i++（后置赋值）与++i（前置赋值）是一样的结果。


### 5. Node.js
#### 5.1 **npm的依赖类型**

>  在安装一个要打包到生产环境的安装包时，你应该使用 `npm install --save`，如果你在安装一个用于开发环境的安装包（例如，linter, 测试库等），你应该使用 `npm install --save-dev` 

> `npm: --save  yarn: ` = dependencies
>
> `npm: --save-dev  yarn: --dev` / `-D` = devdependencies
>
>  `yarn: --peer` = peerDependencies 
>
> `npm: --save-optional  yarn: --optional` = optionalDependencies

#### 5.2 **node知识**

替代setInterval方法， 由于不知道函数执行时长，这样能保证每一次的myFunction调用间隔相同

```js
const myFunction = () => {
  // 做些事情

  setTimeout(myFunction, 1000)
}

setTimeout(myFunction, 1000)
```

### 6. HTML

- `p h1-h6 dt`元素属于文字类的块元素，不能包含其他块元素，只能嵌套内联元素。

>  1. 块元素可以包含内联元素或某些块元素，但内联元素却不能包含块元素，它只能包含其它的内联元素
>  2. 块级元素不能放在<p>里面
>  3. 有几个特殊的块级元素只能包含内嵌元素，不能再包含块级元素，这几个特殊的标签是
>> h1、h2、h3、h4、h5、h6、p、dt。

- 元素只在没有更适合的语义元素表示时使用。例如：

> - 使用 `em ` 表示强调或重读。
> - 使用 `strong ` 表示重要性。
> - 使用 `mark` 表示相关性。
> - 使用 `cite` 标记著作名，如一本书、剧本或是一首歌。
> - 使用 `dfn` 标记术语的定义实例。

- `form` `fieldset` `legend`

>  [`fieldset`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/fieldset)元素是一种方便的用于创建具有相同目的的小部件组的方式，出于样式和语义目的。 你可以在开口标签后加上一个`legend`元素来给[`fieldset`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/fieldset) 标上标签。 [`legend`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/legend)的文本内容正式地描述了[`fieldset`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/fieldset)里所含有部件的用途。

### 7. React

#### 7.1 react知识点

- **注意：** 组件名称必须以大写字母开头。

  React 会将以小写字母开头的组件视为原生 DOM 标签。

- 所有 React 组件都必须像**纯函数**一样保护它们的 props 不被更改。

- State

  > 不要直接修改 State
  >
  > State 的更新可能是异步的。因为 `this.props` 和 `this.state` 可能会异步更新，所以你不要依赖他们的值来更新下一个状态，可以让 `setState()` 接收一个函数而不是一个对象。这个函数用上一个 state 作为第一个参数，将此次更新被应用时的 props 做为第二个参数。
  
- 事件处理

  1. React 事件的命名采用小驼峰式（camelCase），而不是纯小写。

  2. 使用 JSX 语法时你需要传入一个**函数**作为事件处理函数，而不是一个字符串。

  3. 不能通过返回 `false` 的方式阻止默认行为。你必须显式的使用 `preventDefault` 

  4. 在循环中，通常我们会为事件处理函数传递额外的参数。例如，若 `id` 是你要删除那一行的 ID，以下两种方式都可以向事件处理函数传递参数：

     ```
     <button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
     <button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
     ```

     上述两种方式是等价的，分别通过[箭头函数](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)和 [`Function.prototype.bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) 来实现。

     在这两种情况下，React 的事件对象 `e` 会被作为第二个参数传递。如果通过箭头函数的方式，事件对象必须显式的进行传递，而通过 `bind` 的方式，事件对象以及更多的参数将会被隐式的进行传递。

- key 会传递信息给 React ，但不会传递给你的组件。

- 受控表单组件，非受控组件。

- 状态提升与组件组合

- React 通过一种比传统的双向绑定略微繁琐的方法来实现反向数据传递。`尽管如此，但这种需要显式声明的方法更有助于人们理解程序的运作方式。`

- `React.lazy` 接受一个函数，这个函数需要动态调用 `import()`。它必须返回一个 `Promise`，该 Promise 需要 resolve 一个 `default` export 的 React 组件。

  然后应在 `Suspense` 组件中渲染 lazy 组件，如此使得我们可以使用在等待加载 lazy 组件时做优雅降级（如 loading 指示器等）。

  ```js
  import React, { Suspense } from 'react';
  
  const OtherComponent = React.lazy(() => import('./OtherComponent'));
  
  function MyComponent() {
    return (
      <div>
        <Suspense fallback={<div>Loading...</div>}>
          <OtherComponent />
        </Suspense>
      </div>
    );
  }
  ```
  
  `fallback` 属性接受任何在组件加载过程中你想展示的 React 元素。你可以将 `Suspense` 组件置于懒加载组件之上的任何位置。你甚至可以用一个 `Suspense` 组件包裹多个懒加载组件。
  
- 如果模块加载失败（如网络问题），它会触发一个错误。你可以通过[异常捕获边界（Error boundaries）](https://zh-hans.reactjs.org/docs/error-boundaries.html)技术来处理这些情况，以显示良好的用户体验并管理恢复事宜。

- **context**

>  - `React.createContext` 创建一个 Context 对象。当 React 渲染一个订阅了这个 Context 对象的组件，这个组件会从组件树中离自身最近的那个匹配的 `Provider` 中读取到当前的 context 值。**只有**当组件所处的树中没有匹配到 Provider 时，其 `defaultValue` 参数才会生效
>
>  - `Context.Provider` 每个 Context 对象都会返回一个 Provider React 组件，它允许消费组件订阅 context 的变化。Provider 接收一个 `value` 属性，传递给消费组件。一个 Provider 可以和多个消费组件有对应关系。多个 Provider 也可以嵌套使用，里层的会覆盖外层的数据。当 Provider 的 `value` 值发生变化时，它内部的所有消费组件都会重新渲染。
>
>  ```js
>  <MyContext.Provider value={/* 某个值 */}>
>  ```
>  - `Class.contextType` 挂载在 class 上的 `contextType` 属性会被重赋值为一个由 [`React.createContext()`](https://zh-hans.reactjs.org/docs/context.html#reactcreatecontext) 创建的 Context 对象。这能让你使用 `this.context` 来消费最近 Context 上的那个值。你可以在任何生命周期中访问到它，包括 render 函数中。
>
>  - `Context.Consumer` 一个 React 组件可以订阅 context 的变更，这让你在[函数式组件](https://zh-hans.reactjs.org/docs/components-and-props.html#function-and-class-components)中可以订阅 context。这种方法需要一个[函数作为子元素（function as a child）](https://zh-hans.reactjs.org/docs/render-props.html#using-props-other-than-render)。这个函数接收当前的 context 值，并返回一个 React 节点。传递给函数的 `value` 值等价于组件树上方离这个 context 最近的 Provider 提供的 `value` 值。如果没有对应的 Provider，`value` 参数等同于传递给 `createContext()` 的 `defaultValue`。

- 错误边界

> 错误边界是一种 React 组件，这种组件**可以捕获并打印发生在其子组件树任何位置的 JavaScript 错误，并且，它会渲染出备用 UI**，而不是渲染那些崩溃了的子组件树。错误边界在渲染期间、生命周期方法和整个组件树的构造函数中捕获错误。
>
> 如果一个 class 组件中定义了 [`static getDerivedStateFromError()`](https://zh-hans.reactjs.org/docs/react-component.html#static-getderivedstatefromerror) 或 [`componentDidCatch()`](https://zh-hans.reactjs.org/docs/react-component.html#componentdidcatch) 这两个生命周期方法中的任意一个（或两个）时，那么它就变成一个错误边界。

#### 7.2 Hook

 Hook 是一些可以让你在函数组件里“钩入” React state 及生命周期等特性的函数。





### SQL



#### 1. 事务

- Read Uncommitted

> Read Uncommitted是隔离级别最低的一种事务级别。在这种隔离级别下，一个事务会读到另一个事务更新后但未提交的数据，如果另一个事务回滚，那么当前事务读到的数据就是脏数据，这就是脏读（Dirty Read）。

- Read Committed

> 在Read Committed隔离级别下，一个事务可能会遇到不可重复读（Non Repeatable Read）的问题。
>
> 不可重复读是指，在一个事务内，多次读同一数据，在这个事务还没有结束时，如果另一个事务恰好修改了这个数据，那么，在第一个事务中，两次读取的数据就可能不一致。

- Repeatable Read

> 在Repeatable Read隔离级别下，一个事务可能会遇到幻读（Phantom Read）的问题。
>
> 幻读是指，在一个事务中，第一次查询某条记录，发现没有，但是，当试图更新这条不存在的记录时，竟然能成功，并且，再次读取同一条记录，它就神奇地出现了。

-  Serializable

> Serializable是最严格的隔离级别。在Serializable隔离级别下，所有事务按照次序依次执行，因此，脏读、不可重复读、幻读都不会出现。
>
> 虽然Serializable隔离级别下的事务具有最高的安全性，但是，由于事务是串行执行，所以效率会大大下降，应用程序的性能会急剧降低。如果没有特别重要的情景，一般都不会使用Serializable隔离级别。

> 在MySQL中，如果使用InnoDB，默认的隔离级别是Repeatable Read。

# # 流程图设计模板
```flow
st=>start: Start
e=>end: End
op=>operation: Operation
cond=>condition: Yes or No?

st->op->cond
cond(yes)->e
cond(no)->op
```

## 98 New Tech
1. **WebAssembly**

   >  WebAssembly是一种新的编码方式，可以在现代的网络浏览器中运行 － 它是一种低级的类汇编语言，具有紧凑的二进制格式，可以接近原生的性能运行，并为诸如C / C ++等语言提供一个编译目标，以便它们可以在Web上运行。它也被设计为可以与JavaScript共存，允许两者一起工作。 
   >
   >  对于网络平台而言，WebAssembly具有巨大的意义——它提供了一条途径，以使得以各种语言编写的代码都可以以接近原生的速度在Web中运行。 

2. **Deno**

   > Node => No + de => Deno

3. RSS

   > RSS [简易信息聚合](https://baike.baidu.com/item/简易信息聚合)（也叫聚合内容）是一种基于[XML](https://baike.baidu.com/item/XML)标准，在互联网上被广泛采用的内容包装和投递协议。RSS(Really Simple Syndication)是一种描述和同步[网站](https://baike.baidu.com/item/网站)内容的格式，是使用最广泛的XML应用。 
   >
   > *简单来说，RSS是一种基于XML标准的文档格式，博客或者新闻网站发布RSS类型的文章，RSS阅读器就可以获取该文档*
   
4. Fetch api，Service Worker

   >  [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) 提供了一个 JavaScript 接口，用于访问和操纵 HTTP 管道的一些具体部分，例如请求和响应。它还提供了一个全局 [`fetch()`](https://developer.mozilla.org/zh-CN/docs/Web/API/GlobalFetch/fetch) 方法，该方法提供了一种简单，合理的方式来跨网络异步获取资源。 
   >
   > 请注意，`fetch` 规范与 `jQuery.ajax()` 主要有三种方式的不同：
   >
   > - 当接收到一个代表错误的 HTTP 状态码时，从 `fetch()` 返回的 Promise **不会被标记为 reject，** 即使响应的 HTTP 状态码是 404 或 500。相反，它会将 Promise 状态标记为 resolve （但是会将 resolve 的返回值的 `ok` 属性设置为 false ），仅当网络故障时或请求被阻止时，才会标记为 reject。
   > - 你可以使用 `fetch()` 建立起跨域会话。
   > - `fetch` **不会发送 cookies**。除非你使用了*credentials* 的[初始化选项](https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/fetch#Parameters)。

   >  Service workers 本质上充当 Web 应用程序、浏览器与网络（可用时）之间的代理服务器。这个 API 旨在创建有效的离线体验，它会拦截网络请求并根据网络是否可用采取来适当的动作、更新来自服务器的的资源。它还提供入口以推送通知和访问后台同步 API。 
   >
   >  Service worker是一个注册在指定源和路径下的事件驱动[worker](https://developer.mozilla.org/zh-CN/docs/Web/API/Worker)。它采用JavaScript控制关联的页面或者网站，拦截并修改访问和资源请求，细粒度地缓存资源。你可以完全控制应用在特定情形（最常见的情形是网络不可用）下的表现。 

## 99. 思考 ？ 建议

1. `Node`的 `serve` 与 `http-server` 区别在哪？

- v-model 双向绑定 input输入框时 不更新？@input事件 触发更新
- 部分组件数据改变时 并不能及时更新 强制改变：key可以生效

2. `Vue Cli3` 中怎样使用 `less.modifyVars`（）使用js操作css变量

> 当时解决方案为使用css变量功能 使用--vueColor：@lessvariable来定义颜色，再使用document.body.style.setProperty（‘--vueColor’: '#fff'） 使用js操作css样式

3. JS里的错误不catch或者catch会阻塞线程的运行吗 或者说程序是否正常往下运行
4. 两个数组里的元素为对象，怎样快速求两个数组的交集
```javascript
let arr_1 = [{id: 1, name: 'Jonh', desc: 'people'}, {id: 2, name: 'Huang', desc: 'dog'}]
let arr_2 = [{id: 3, name: 'Wee', desc: 'unknown'}, {id: 2, name: 'Huang', desc: 'dog'}]
```
5. 怎样快速判断两个数组里的元素都相同
```javascript
let arr_1 = [1, 2, 3, 4, 5]
let arr_2 = [5, 1, 4, 2, 3]
```
6. websocket 是否和 进程间通信 socket长连接 一个原理？
7. 


## 100. Watch Out Bug
- 不trim就判断字符串 === ''
- 数组的地址引用 深拷贝
- 考虑大就要考虑到小，边界问题
- e-chart图表容器使用绝对定位时，width会为0，图表不能随窗口resie
-  **pointer-events:none** 
-  W3C 标准中有如下[规定](https://www.w3.org/MarkUp/html-spec/html-spec_8.html#SEC8.2)：*When there is only one single-line text input field in a form, the user agent should accept Enter in that field as a request to submit the form.*即：当一个 form 元素中只有一个输入框时，在该输入框中按下回车应提交该表单。**注意一个表单组件时 按enter键的行为异常原因**
-  由于 箭头函数没有自己的this指针，通过 `call()` *或* `apply()` 方法调用一个函数时，只能传递参数（不能绑定this）
-  注意正则 全局匹配时的lastIndex

> 如果正则表达式设置了全局标志，`test() `的执行会改变正则表达式  [`lastIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex)属性。连续的执行`test()`方法，后续的执行将会从 lastIndex 处开始匹配字符串，([`exec()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec) 同样改变正则本身的 `lastIndex属性值`).

```js
var regex = /foo/g;

// regex.lastIndex is at 0
regex.test('foo'); // true

// regex.lastIndex is now at 3
regex.test('foo'); // false
```

- 注意，`Array.length `并不总是等于数组中元素的个数，如下所示：

```
var a = ["dog", "cat", "hen"];
a[100] = "fox";
a.length; // 101
```

> 记住：数组的长度是比数组最大索引值多一的数。



#### **TODO：**
1. 颜色主题 切换功能 √
2. 自适应页面样式 顶部 左侧导航栏自适应分辨率 √
3. 国际化（zh + en） √
4. TypeScript Learn
5. Vue.js source code learn
6. Webpack 打包不同结构的项目 配置

> **后端**
>
> 1.mongoose ORM
>
> 2.express restful api



#### **Bug**

1. 登录页面的button点击与hover效果
2. 登录页面的body元素上下有未意料的边距

#### **Done**

1. Vue项目 使用vue-cli3快速构建 使用vue-router vuex vue-loader开发
2. elementUI 按需
3. 代码检查与格式化工具eslint+prettier，自动查错 修复格式
4. css预编译语言less
5. 两个预制的不同主题切换 加单独的完整颜色定制
6. i18n 中文 English
7. 自适应手机 平板 PC
8. 项目组件化模块化明确 
9. yarn包管理



- js转换颜色格式 npm包

#### 

>  `/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/ `  check email regexp

**前端技术栈：**

> - JavaScript CSS HTML
> - Vue vue-router vuex vue-cli
> - iViewUI ElementUI
> - jQuery Bootstrap
> - Webpack Rollup Gulp
> - babel i18n eslint+prettier
> - Less/*Scss* HTML5
> - Flow *TypeScript* 
> - Git Svn Github.com npm yarn
> - js基于原型链的继承 js数据类型
> - JS模块化：AMD规范与CommonJS规范 ES6模块化 NodeJS模块化
> - Chrome调试 浏览器兼容 IE<9
> - 性能优化 浏览器内核 内存泄漏
> - 响应式 css布局--栅格--flex  移动端 小程序
> - 异步 AJAX Promise Callback async/await 单线程、任务队列、事件驱动
> - Node.js 服务端编程 Express Koa 数据库 路由 算法
> - API交互 前、后端渲染页面
> - CSS变量var(--variable)  精灵图
> - 工程编译（热重载 修复格式化）打包 部署配置
> - MVC MVVM模式
> - cookie session token localstorage history
> - Backbone.js LayUI D3.js echart.js lodash.js axios.js 
> - XSS 攻击

Chrome调试

> - HTML文件是 **blue (蓝色)** 的。
> - 脚本是 **yellow (黄色)** 的。
> - 样式表是 **purple (紫色)** 的。
> - 媒体文件是 **green (绿色)** 的。
> - 其他杂项资源是 **grey (灰色)** 的。



React受控表单组件的值与事件的处理方式，Vue的v-model更方便
