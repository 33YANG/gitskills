

[【Chrome 快捷键 】]( https://support.google.com/chrome/answer/157179?hl=zh-Hans )

[【VSCode 快捷键】]( https://blog.csdn.net/crper/article/details/54099319 )

​	

|  序号   |                             单词                             |                    释义                    | 备注 |
| :-----: | :----------------------------------------------------------: | :----------------------------------------: | :--: |
| VS Code |                                                              |                                            |      |
|    1    |                      crtl + k crtl + w                       |                关闭所有窗口                |      |
|    2    |                           crtl + u                           |            撤销最后一次光标操作            |      |
|    3    |                      crtl + k crtl + 0                       |              折叠所有区域代码              |      |
|    4    |                      crtl + k crtl + j                       |                打开所有折叠                |      |
|    5    |               crtl + shift + l  / f2(js文件中)               |             修改文件中所有同名             |      |
|    6    |        crtl + left/right // crtl +shift + left/right         |         按单词移动光标//按单词选中         |      |
|    7    |              crtl +enter / crtl + shift + enter              | 从当前行任意位置换行到下一新行//到上一新行 |      |
|    8    |            crtl + shift + k / crtl + x也有此效果             |       从任意位置删除当前行，不留空行       |      |
|    9    |                   crtl + alt + bottom/top                    |            向下/上 增加一个光标            |      |
|   10    |                           crtl + d                           |           选中当前光标周围的单词           |      |
|   11    |                       alt + shift + i                        |        在当前选中的多个行末创建光标        |      |
|   12    |                       crtl + shift + \                       |       光标在代码块的括号之间移动(){}       |      |
|   13    |                  命令行中 expand selection                   |             选中光标所在代码块             |      |
|   14    |                       crtl + backspace                       |               删除前一个单词               |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
| Chrome  |                                                              |                                            |      |
|    1    |                           crtl + P                           |                按文件名搜索                |      |
|    2    |                       crtl + shift + O                       |            搜索文件里的成员函数            |      |
|    3    |                           crtl + G                           |                 跳至某一行                 |      |
|    4    |                     crtl + shift + I / J                     |            开发者工具source页面            |      |
|    5    |                         shift + ESC                          |            打开chrome任务管理器            |      |
|    6    |                           alt + F                            |               打开chrome菜单               |      |
|    7    |                         crtl + ] / [                         |           切换上、下开发工具面板           |      |
|    8    |                          crtl + 1-9                          |              切换开发工具面板              |      |
|    9    |                        crtl + R / F5                         |                  刷新页面                  |      |
|   10    |                    crtl + shift + R / F5                     |   刷新忽略缓存内容的页面（硬性重新加载）   |      |
|   11    |                       crtl + shift + F                       |             在所有源中搜索文本             |      |
|   12    |                     开发者页面 crtl + L                      |                 清空控制台                 |      |
|   13    |              chrome网页 crtl + L / alt + D / F6              |                聚焦于地址栏                |      |
|   13    |                       crtl + shift + c                       |                检查元素工具                |      |
|   14    |                         shift + esc                          |              chrome任务管理器              |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|   Git   |                                                              |                                            |      |
|         | git log --format='%aN' \| sort -u \| while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat \| awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'-; done |               统计每人增删数               |      |
|         | git log --author="username" --pretty=tformat: --numstat \| awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' - |               查看个人代码量               |      |
|         |                  git log --oneline \| wc -l                  |                 提交数统计                 |      |
|         | git log --pretty='%aN' \| sort \| uniq -c \| sort -k1 -n -r \| head -n 5 |                查看提交前五                |      |
|         |          git log --pretty='%aN' \| sort -u \| wc -l          |                 贡献值排名                 |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |
|         |                                                              |                                            |      |



## Linux

```bash
ls -a/-l         #显示隐藏文件/使用长格式显示文件内容
mkdir [dir]      #如果目录存在会报错
rmdir [dir]      #只能删除空的文件夹
rm -rf [dir]     #删除非空的文件夹  -r 递归地删除 -f 忽略不存在的文件，从不给出提示，强制删除。
mv [dir/file]    #移动目录或文件,给目录或文件重命名，递归移动 -b覆盖前备份 -f强制覆盖 -i覆盖前询问 -u比较更新覆盖 -t多移一
du               #目录所占的磁盘空间
df               #磁盘剩余的磁盘空间
cat [filename]   #显示整个文件
cat > [filename] #从键盘创建一个文件 crtl+d 保存
cat file1 file2 > file #将几个文件合并为一个文件
less [file]      #显示一般文本文件的指令,可以用方向键往上或往下的滚动文件
clear 			 #清除屏幕
grep [str]		 #查找文件中符合字符串的哪行 -a将 binary 文件以 text 文件的方式搜寻数据 -c计算找到 '搜寻字符串' 的次数 -i忽略大小写 -n输出行号 -v反向选择
```



## mysql

```bash
net start [mysql_name]
net stop [mysql_name]

mysql -v root -p
show database;
use [database];
show tables;
```




