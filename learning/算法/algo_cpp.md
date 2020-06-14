## 第零章 C/C++ 函数的应用

### `C++`中的函数库

#### `容器`

* **`map`**容器
  * 如：`map<char, int>mc;`

​						在`map`中，需要一个键和值，前者为键，后者为值

​		&bull; 相关函数：

​			`map.find(value)`: 在`map`容器中寻找`value`这个值，如果存在就返回`value`的位置，否则返回`end`(最后一个迭代器)

​			`map.count(value)`： 查找`map`中`value`是否存在，返回值`1`表示存在，`0`表示不存在

* **`vector`**容器
  * 如：`vector<int>vi;`

​							在`vector`容器中，支持初始化.

​			&bull; 相关函数：

​				`vi.size()`：查看容器中的元素大小.

​				`vi.resize(const size_t New_size,const int &val)`：可以接受两个参数.(可用于拷贝)



​		成员：

​		`vi.capacity`：查看当前容器的大小.

* **`bitset`**库

  * `bitset`常用于把整形转化为二进制类型，也可以接受一个字符串.

  * ```
    bitset<t>n(str);
    //在这里面，t 表示保留多少位的二进制
    ```

  * 成员函数：

    * `all`：查找是否全部为`1`，如果存在返回`true`.
    * `any`：查看是否有`1`，如果有返回`true`.
    * `count`：计算有多少个`1`.

    

#### `算法函数`

* **`accumulate()`**求和算法，返回求的总和
  * 如：`int sum = accumulate(nums.begin(), nums.end(), 0)`

​					先初始化为0，然后再计算从第一个下标开始到最后一个下标结束的所有元素的和

* **`copy()`**可以复制一个数组到另外一个数组中
  * 如：`copy(nums1.begin(), nums1.end(), nums2.begin()+k)`

​					意思是把`nums1`中的所有元素复制到`nums2`中`k`开始的到最后的位置

​			*<font size=2>注意：copy函数不能增大容器的大小，如果要进行复制到原容器后面，需要先变大容器大小.</font>*



* **`count()`**计数函数
  * 如：`count(nums.begin(), nums.end(), value)`

​					在`nums`这个容器中寻找`value`这个值，返回查找到的*个数*



* **`next_permutation()`**和**`prev_permutation()`**函数

  * 此函数为全排列函数
  * 用法如下：

* ```c++
  int ar[3]={1,2,3};
  do{cout<<ar[0]<<" "<<ar[1]<<" "<<ar[2]<<endl;}
  while(next_permutation(ar,ar+3));
  //每一次循环会对此进行一次排列
  //同时，支持容器操作.
  ```

  * `next_permutation()`和`prev_permutation()`的区别：
  * 前者为输出比初始序列大的序列.
  * 后者为输出比初始序列小的序列.



* **`exp()`**函数
  *  如：`exp(1)`，此函数接受一个参数，代表着 `lnx`，其中`x`代表未知数

   				`exp(1)`=`2.71828`，以 e 为底的**对数函数**

* **`find()`**从一个容器中寻找某一个元素
  
  * 如：`find(vi.begin(), vi.end(),num)`

​					在`vi`这个容器中寻找`num`这个元素，如果存在就返回1，不存在就返回尾后迭代器

* **`earse()` **删除容器中的元素(一般为容器的成员函数)
  * 如：`nums.earse(nums.begin()+k, nums.end())`

​					删除从`k`开始的元素到最后的位置

* **`insert()`**插入一段元素(一般为容器的成员函数)
  * 如：`st.insert(nums.begin(), i)`

​					把一个元素`i`插入到容器的第一个位置(`i`的元素要和容器的类型相同)

* **`*max_element()`**寻找最大值,并返回最大值
  * 如：`*max_element(nums.begin(), nums.end());`

​					在这里，需要两个迭代器来计算哪一段的最大值

​					`*max_element(array, array+k);`

​					而在这里，传送的实参是一个数组，k 为下标，同样可以计算出一个数组中的最大值

* **`max()`**比较大小函数
  *  如：`max(a,b)`对`a`和`b`进行比较，返回大的值

​			*C++11新特性：*

​			`max({a,b,c})`对`{ }`里面的值进行比较，返回大的值

* **`min()`**比较大小函数

​			和上面`max`函数相反，`min`函数是返回小的值，同时也满足*C++11的新特性*

* **`*min_element()`**寻找最小值

​					用法和`*max_element()`相同，唯一不同的是返回值

* **`memset()`**把指定的一块内层初始化为一个相同的值
  *  原型：`extern void *memset(void *buffer, int c, int count)`

  *  例：

  * ```c++
    int arr[2][4];
    memset(arr,0,sizeof(array));
    ```

    



* **`reverse()`**倒转函数
  *  如：`reverse(st.begin(), st.end())`

​							可以把字符串、数组中的元素倒转

* **`sort()`**排序算法，无返回值
  *  如：`sort(nums.begin(), nums.end())`

​					排序从第一个下标开始到最后以一个元素

* **`__gcd()`**求最大公约数
  *  如：`__gcd(a,b)`；

​						在此函数中，a 和 b 的类型要一样，可以用的类型`int`和`long long`

​						在头文件`<algorithm> `中

#### `关于串的函数`

​		在Ｃ＋＋中，可以使用关于串的一些函数

* **`substr()`**得到字符串中某一段子串
  * 如：`str.substr(0, 5)`

​				得到字符串`str`中从0开始到5的子串

* **`to_string()`** 可以把其他类型转化成字符串类型

* **`itoi()&atoi()`**整形字符串(某进制)的相互转化
  * 如：`itoi(num, str, 2)`

​					在上述中，`num`为整形`(int)`，`str`为缓存区，用于保存转化后的字符串`(char* Buffer)`，`2`为要转化的进制数`(int)`

​		&bull; 如：`atoi(str.c_str())`

​					`str`为`string`类型

```
c_str()函数返回一个指向正规C字符串的指针常量, 内容与本string串相同. 
这是为了与c语言兼容，在c语言中没有string类型，故必须通过string类对象的成员函数c_str()把string 对象转换成c中的字符串样式。
注意：一定要使用strcpy()函数 等来操作方法c_str()返回的指针 
```

### `C`中的函数库

**`qsort()`**函数

* ```c
  #include<stdio.h>
  #include<stdlib.h>//qsort()函数在这个库里面
  
  //需要自定义排序方式（顺序和逆序）
  int compare(const void *a,const void *b) {
  	return (*(int*)a - *(int*)b);
  }
  
  int main() {
  	int a[] = { 3, 513, 2, 5, 13 };
      //第一个参数为数组地址，第二个参数为数组大小.
      //第三个参数为数组中每元素的大小.
      //第四个参数为一个函数，定义排序顺序.
  	qsort(a, 5,sizeof(int),compare);
  	for (int i = 0; i < 5; i++) {
  		printf("%d ", a[i]);
  	}
  	return 0;
  }
  ```

**`sscanf()`**函数

* 最多的用法就是把字符串转化为其他类型.
  * `sscanf(str.c_str(), "%d-%d-%d", &year, &month, &day )`，在这里面把字符串中的相关数字的字符转化为数字.



### `不常用数据类型`

* `typedef unsigned int`   `unit32_t`
  * 	指<font color=blue>无符号</font><font color=skeyblue>整形</font>



## 第一章 辅助算法

### 1.1. 快读和快输

* 快读算法的速度是普通输入算法的速度的20倍

  ```c++
  /*
  # input()
  */
  int input(){
      char ch;
      int x=0,f=1;
      getchar(ch);
      while(x>'9'&&x<'0'){if(ch=='-')f=-1;ch=getchar();}
      while(x>='0'&&x<='9'){x=x*10+ch-'0';ch=gethcar();}
      return x*f;
  }
  ```

* 快速输出

```c++
char f[100]; // the digits of the output number

void output(const int& x) {
  	int tmp = x;
  	//把负数情况列出来
  	if (tmp < 0) {tmp = -tmp;putchar('-');}
  	int s = 0;
  	//把数字转化为字符，保存到字符串中.
  	while (tmp > 0) {f[s++] = tmp%10 + '0';tmp /= 10;}
    //逐个输出字符
  	while (s > 0) putchar(f[--s]);
}

```



### 1.2. 大数的基本运算

* 大数相加

  (1). 字符串形式

  ```C++
  class Solution {
  public:
      string addStrings(string num1, string num2) {
  		string sum;
          int cur=0,i=num1.size()-1,j=num2.size()-1;
          /*
          *cur之所以不能等于0，是因为要实现进制，比如1和9相加
          */
          while(i>=0||j>=0||cur!=0){
              if(i>=0)cur+=num1[i--]-'0';
              if(j>=0)cur+=num2[j--]-'0';
              sum.insert(sum.begin(),cur%10+'0');
              cur/=10;
          }
          return sum;
      }
  };
  ```

  

* 大数相乘

* 阶乘

  函数`pow()`的实现

  * 用一般方法实现`pow()`函数效率不是太高，使用*快速幂* 的方法，可以提高很多
  * 快速幂的实现和二进制转为十进制差不多，如：1010的十进制为10
  * 10=1&times;2<sup>3</sup>+0&times;2<sup>2</sup>+0&times;2<sup>1</sup>+0&times;2<sup>0</sup>

  ```C++
  class Solution {
  public:
      double myPow(double x, int n) {
          long long N=n;
          if(N<0){x=1/x;N=-N;}
          double xi=1;
          double xj=x;
          //核心代码如下：
          for(long long k=N;k;k/=2){
              if(k%2==1)xi*=xj;
              xj=xj*xj;
          }
          return xi;
      }
  };
  ```

  




## 第二章 时间计算

* 计算时间间隔
* 给出年月日，计算是周几

## 第三章 位运算

* 异或运算`^`

  * 异或（[xor](https://baike.baidu.com/item/xor/64178)）是一个数学运算符。它应用于逻辑运算。异或的数学符号为“⊕”，计算机符号为“`xor`”，常用"`^`"表示。其运算法则为：

    `a⊕b = (¬a ∧ b) ∨ (a ∧¬b)`.

  * 异或也叫**<font color=red>半加运算</font>**，其运算法则相当于不带进位的二进制加法：二进制下用`1`表示真，`0`表示假，则异或的运算法则为：`0⊕0=0`，`1⊕0=1`，`0⊕1=1`，`1⊕1=0`（同为0，异为1），这些法则与加法是相同的，只是不带进位，所以异或常被认作不进位加法.

    <table border="1" style="text-align:center"><tr><td>^(异或运算)</td><td>00(0)</td><td>01(1)</td><td>10(2)</td><td>11(3)</td><td>100(4)</td></tr><tr><td>00(0)</td><td>00^00=00(0)</td><td>00^01=01(1)</td><td>00^10=10(2)</td><td>00^11=11(3)</td><td>000^100=100(4)</td></tr></table>

  

  <a herf="https://leetcode-cn.com/problems/single-number/" style="color:purple">**136. 只出现一次的数字**</a>

  给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

  **说明：**

  *<font size=2>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</font>*

  

  **示例 1:**

  ```
  输入: [2,2,1]
  输出: 1
  ```

  **示例 2:**

  ```
  输入: [4,1,2,1,2]
  输出: 4
  ```

  

  ```c++
  class Solution {
  public:
      int singleNumber(vector<int>& nums) {
  		int a=0;
          for(int num:nums){
              a^=num;
          }
          return a;
      }
  };
  ```

   

  <a herf="https://leetcode-cn.com/problems/power-of-two/" style="color:purple">231. 2的幂</a>

  给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

  

  **示例 1:**

  ```
  输入: 1
  输出: true
  解释: 20 = 1
  ```

  **示例 2:**

  ```
  输入: 16
  输出: true
  解释: 24 = 16
  ```

  **示例 3:**

  ```
  输入: 218
  输出: false
  ```

  

  ```c++
  class Solution {
  public:
      bool isPowerOfTwo(int n) {
  		return n>0&&(n&(n-1)==0);
      }
  };
  ```

  <table border="1" style="text-align:center"><tr><td>&bull;</td><td>2<sup>0</sup></td><td>2<sup>1</sup></td><td>2<sup>2</sup></td><td>2<sup>3</sup></td><td>2<sup>4</sup></td></tr><tr><td>二进制</td><td>1</td><td>‭0010‬</td><td>‭0100‬</td><td>‭1000‬</td><td>‭00010000‬</td></tr></table>

  

* 移位运算(`<<`和`>>`)

  * 右移运算符`>>`

    <img src="右移位.png"></img>

  

  

  

  * 左移运算符

  

  <a herf="https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/" style="color:purple">1290. 二进制链表转整数</a>

  给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

  请你返回该链表所表示数字的 十进制值 。

   

  **示例 1：**

  ```
  输入：head = [1,0,1]
  输出：5
  解释：二进制数 (101) 转化为十进制数 (5)
  ```

  **示例 2：**

  ```
  输入：head = [0]
  输出：0
  ```

  **示例 3：**

  ```
  输入：head = [1]
  输出：1
  ```

  **示例 4：**

  ```
  输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
  输出：18880
  ```

  **示例 5：**

  ```
  输入：head = [0,0]
  输出：0
  ```

  *<font size=2>提示：</font>*

  *<font size=2>链表不为空。</font>*
  *<font size=2>链表的结点总数不超过 30。</font>*
  *<font size=2>每个结点的值不是 0 就是 1。</font>*

  ```C++
  /**
   * Definition for singly-linked list.
   * struct ListNode {
   *     int val;
   *     ListNode *next;
   *     ListNode(int x) : val(x), next(NULL) {}
   * };
   */
  class Solution {
  public:
      int getDecimalValue(ListNode* head) {
  		int ans=0;
          while(head){
              ans=(ans<<1)+head->val;
          }
          return ans;
      }
  };
  ```





* 原地算法

  <a herf="https://leetcode-cn.com/problems/game-of-life/" style="color:purple">289 生命游戏</a>

  根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

  给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

  如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
  如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
  如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
  如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
  根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

   

  示例：

  ```
  输入：
  [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
  ]
  输出：
  [
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [0,1,0]
  ]
  ```





## 第四章 贪心算法



​		**思想：**贪心算法的基本思路是从问题的某一个初始解出发一步一步地进行，根据某个优化测度，每一步都要确保能获得局部最优解。

​		每一步只考虑一个数据，他的选取应该满足局部优化的条件。

​		若下一个数据和部分最优解连在一起不再是可行解时，就不把该数据添加到部分解中，直到把所有数据枚举完，或者不能再添加算法停止 。

*<font size=2>即从初始解出发，每一步都要考虑最优解</font>*



**55. 跳跃游戏**

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

```
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
```


示例 2:

```
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
```

```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int result=0;
        for(int i=0;i<nums.size();i++){
            if(i>result)return false;
            result=max(result,nums[i]+i);
        }
        return true;
    }
};
```



<a herf="https://leetcode-cn.com/problems/coin-lcci/">面试题 08.11. 硬币</a>

给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

```
 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
```

示例2:

```
 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
```

````c++
class Solution {
public:
    int waysToChange(int n) {
        int max_len=1000000007;
        vector<int>dp(n+1);
        vector<int>coins={1,5,10,25};
        dp[0]=1;
        for(int coin:coins){
            for(int i=coin;i<=n;i++){
                dp[i]=(dp[i]+dp[i-coin])%max_len;
            }
        }
        return dp.back();
    }
};
````



<a herf="https://leetcode-cn.com/problems/two-city-scheduling/">1029. 两地调度</a>



公司计划面试 `2N` 人。第 i 人飞往 A 市的费用为 `costs[i][0]`，飞往 B 市的费用为` costs[i][1]`。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 `N` 人抵达。 

**示例：**

```
输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
```

*提示：*

1 <= `costs.length `<= 100
`costs.length` 为偶数
1 <= `costs[i][0], costs[i`][1] <= 1000

```c++
//思路：先全到 A 地，然后减去到 B 地的额外消费
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
		vector<int>dox;//每一次到A地或B地的差
        int sum=0;
        for(auto val:costs){
            dox.push_back(val[1]-val[0]);
            sum+=val[0];//每次都到达A地时需要的总费用
        }
        sort(dox.begin(),dox.end());
        for(int i=0;i<dox.size()/2;i++){
            sum+=dox[i];
        }
        return sum;
    }
};
```



## 第五章 回溯算法

[百度回溯算法]([https://baike.baidu.com/item/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95/9258495](https://baike.baidu.com/item/回溯算法/9258495))

基本思想：从一条路往前走，能进则进，不能进则退回来，换一条路再试。

**46. 全排列**

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

```c++
class Solution {
public:
    void depth(vector<vector<int>>&pre,vector<int>nums,int first,int len){
		if(first==len){
            pre.push_back(nums);
            return;
        }
        for(int i=first;i<len;i++){
            swap(nums[first],nums[i]);
            depth(pre,nums,first+1,len);
            swap(nums[first],nums[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
       	vector<vector<int>>pre;
        depth(pre,nums,0,nums.size());
        return pre;
    }
};
```



**784. 字母大小写全排列**

给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

**示例:**

```
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
```


*<font size=2>注意：</font>*

*<font size=2>S 的长度不超过12。</font>*
*<font size=2>S 仅由数字和字母组成。</font>*

**新知识点**：大小写转化：S[index]=S[index]^32.

```c++
class Solution {
public:
    void dfs(string &S,vector<string>&pre,int index){
        if(index==S.size()){
            pre.push_back(S);
            return;
        }
        dfs(S,pre,index+1);
        if(isalpha(S[index])){
            S[index]^=32;
            dfs(S,pre,index+1);
        }
    }
    vector<string> letterCasePermutation(string S) {
		vector<string>pre;
        dfs(S,pre,0);
        return pre;
    }
};
```



