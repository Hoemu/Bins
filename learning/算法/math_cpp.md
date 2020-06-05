## 数学

### 第一章 动态规划

* 贪心算法是动态规划中特殊的一种
* 贪心算法必须无后效性，就是以前的过程对后来的状态不产生影响



#### 1.1. 常见`dp`



**6.1.1 插入数字**

​	给定一个数组和一个数 n，在数组中只存在0和1，现在要插入n 个数字1到数组中，插入规则如下：

​	不能把数字1插入到原数组中数字1旁边

​	求是否还能插入数字1，如果能插入返回true，否则返回false

```
输入：[1,0,0,0,1] 1
输出：true
```


```C++
bool canPlaceFlowers(vector<int>& flowerbed, int n){
    int count=0;
    flowerbed.insert(flowerbed.begin(),0);
    flowerbed.insert(flowerbed,end(),0);
   	//也可以用 flowerbed.push_back(0);
    for(int i=1;i<flowerbed.size()-1;i++){
        if(flowerbed[i]==0&&flowerbed[i-1]==0&&flowerbed[i+1]==0){
            flowerbed[i]=1;//插入1
            count++;
        }
    }
    return n<=count;
    //return n<=count?1:0;
}
```



**300 最长上升子序**

给定一个无序的整数数组，找到其中最长上升子序列的长度。

```
输入: [1,3,5,6], 5
输出: 2
```

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int len=nums.size();
        if(len==0)
            return 0;
      	vector<int>dp(len,0);
        for(int i=0;i<len;i++){
            dp[i]=1;
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j])
                    dp[i]=max(dp[i],dp[j]+1);
                	/*
                    *寻找dp[i]以前的所有值比当前值小时，+1后做对比，然后更新dp[i]
                    *如果没有出现，dp[i]就为1
                	*/
            }
        }
        return *max_element(dp.begin(),dp.end());
    }
}
```



**118. 杨辉三角**

给定一个非负整数 *`numRows`，*生成杨辉三角的前 *`numRows`* 行。

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)



<h5>在杨辉三角中，每个数是它左上方和右上方的数的和。</h5>

**示例:**

```
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

```c++
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>vi(numRows);
        if(numRows==0)
            return vi;
        //主要代码，在这里采取了动态规划的思想
        for(int i=0;i<numRows;i++){
            for(int j=0;j<=i;j++){
                if(j==0||i==j)
                    vi[i].push_back(1);
                else
                    vi[i].push_back(vi[i-1][j]+vi[i-1][j-1]);
            }
        }
        return vi;
    }
};
```



**746. 使用最小花费爬楼梯**

* 记录型问题
  * 相识题目{213. 打家劫舍 **|**面试题 17.16. 按摩师}

数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

```
示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
```

**注意：**

*cost 的长度将会在 [2, 1000]。*
*每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。*

```c++
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int len=cost.size();
        for(int i=2;i<len;i++){
            cost[i]+=min(cost[i-1],cost[i-2]);
        }
        return min(cost[len-1],cost[len-2]);
    }
};
```

<a herf="https://leetcode-cn.com/problems/house-robber/" style="color:purple">198. 打家劫舍</a>

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

**示例 1:**

```
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2:**

```
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

<img src="E:\Users\hasee\Pictures\其他\4HR387CY2[6B0Y~XVNIY0[3.png">

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
		int first=0,second=0,temp=0;
        for(int num:nums){
            temp=first;
            firts=max(second+num,first);
            second=temp;
        }
        return first;
    }
};
```



<a herf="https://leetcode-cn.com/problems/minimum-cost-for-tickets/" style="color:purple">**983. 最低票价**</a>



在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

 

**示例 1：**

```
输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释： 
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。
```

**示例 2：**

```
输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
你总共花了 $17，并完成了你计划的每一天旅行。
```

*提示：*

1 <=` days.length` <= 365
1 <= `days[i] `<= 365
`days` 按顺序严格递增
`costs.length` == 3
1 <=` costs[i] `<= 1000

<img src="E:\Users\hasee\Pictures\其他\dp983.png" />

```c++
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        //用一个数组来存储最小的花费
        vector<int>dp(days.back()+1);
        for(int i=0;i<dp.size();i++)
            dp[i]=i;
        int days_idx=0;
        for(int i=1;i<dp.size();i++){
            if(i!=days[days_idx])
                dp[i]=dp[i-1];
            else{
                dp[i]=min({dp[max(0,i-1)]+costs[0],
                          dp[max(0,i-7)]+costs[1],
                          dp[max(0,i-30)]+costs[2]});
                days_idx++;
            }
        }
        return dp.back();
    }
};
```



<a herf="https://leetcode-cn.com/problems/longest-palindromic-substring/" style="color:purple">**5. 最长回文子串**</a>

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。



**示例 1：**

```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```

**示例 2：**

```
输入: "cbbd"
输出: "bb"
```

```c++

```





#### 1.2. 状态压缩

<a herf="https://www.cnblogs.com/ibilllee/p/7651971.html" style="color=blue">入门题型</a>

<a herf="https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/" style="color:purple">1371. 每个元音包含偶数次的最长子字符串</a>

给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

**示例 1：**

```
输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
```



**示例 2：**

```
输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
```

```c++
class Solution {
public:
    string sub(string &s,int x,int y){
        string ss;
        for(int i=x;i<y;i++){
            ss.push_back(s[i]);
        }
        return ss;
    }
    string longestPalindrome(string s) {
        string origin=s;
        reverse(s.begin(),s.end());
        int len=s.size(),MaxLen=0,MaxEnd=0;
        vector<vector<int>>dp(len,vector<int>(len));
        for(int i=0;i<len;i++){
            for(int j=0;j<len;j++){
                if(s[i]==origin[j]){
                    if(i==0||j==0)
                        dp[i][j]=1;
                    else
                        dp[i][j]=dp[i-1][j-1]+1;
                }
                if(dp[i][j]>MaxLen){
                    int before_index=len-1-j;
                    if(before_index+dp[i][j]-1==i){
                        MaxLen=dp[i][j];
                        MaxEnd=i;
                    }
                }
            }
        }
        return sub(s,MaxEnd-MaxLen+1,MaxLen+1);
    }
};
```



**示例 3：**

```
输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
```

**提示：**

- `1 <= s.length <= 5 x 10^5`
- `s` 只包含小写英文字母。

```c++
class Solution {
public:
    int findTheLongestSubstring(string s) {
        vector<int>pos(1<<5,-1);
        pos[0]=0;
        int ans=0,status=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='a')
                status^=1<<0;
           	else if(s[i]=='e')
                status^=1<<1;
            else if(s[i]=='i')
                status^=1<<2;
            else if(s[i]=='o')
                status^=1<<3;
            else if(s[i]=='u')
                status^=1<<4;
            if(~pos[status])
                ans=max(ans,i+1-pos[status]);
            else
                pos[status]=i+1;
        }
        return ans;
    }
};
```



### 第二章 数论

#### 2.1. 欧几里得算法

​	最大公约数缩写 `gcd`

​	欧几里得算法又叫做**辗转相除法**

​	欧几里得算法是求两个数的最大公约数的算法

​	在算法中具体原来连接如右[[点击链接](https://blog.csdn.net/Ljnoit/article/details/99319849)]

**例6.1.1**

```
	给我们两个数1998和615
	~1998/615=3(余 152)
	~615/152=4(余 7)
	最后计算到没有余数时，那个数就是我们要求的最大公约数
```

算法实现：

```C++
方法1：
    int gcd(int a,int b){
    	//如果b==0时，刚好是最后一次，就可以得到结果a
    	return b>0?gcd(b,a%b):a;
	}
方法2：
    int gcd(int a,int b){
    	while(b){
            b=a%b;
            a=b;
        }
    	return a;
	}
方法3：
    int gcd(int a,int b){
    	if(b)
            while((a%b)&&(b%a));
    	return a+b;
	}
方法4：
    int gcd(int a,int b){
    	while(b^=a^=b^=a%=b);
    	return a;
	}
```

**1071 求两个字符串的最大公约数**

​	如：对于字符串 `S` 和 `T`，只有在 `S = T + ... + T`（`T` 与自身连接 1 次或多次）时，我们才认定 “`T` 能除尽 		"`S`”。返回最长字符串 `X`，要求满足 `X` 能除尽 `str1` 且 `X` 能除尽 `str2`。

```
输入：
	str1 = "ABCABC", str2 = "ABC"
输出：
	"ABC"
```

```C++
class Solution {
public:
    inline int gcd(int &a,int &b) {
		while(b){
            b=a%b;
            b=a;
        }
        return a;
    }
    string gcdOfStrings(string str1, string str2) {
		if(str1+str2!=str2+str1)
            return "";
       	return str1.substr(0,gcd(str1.size(),str2.size()));
    }
};
```

#### 2.2. 贝祖定理

* 裴蜀定理（或[`贝祖定理`](https://baike.baidu.com/item/贝祖定理)）
* 若a,b是整数,且`gcd(a,b)=d`，那么对于任意的整数`x`,`y`,`ax+by`都一定是`d`的倍数，特别地，一定存在整数x,y，使`ax+by=d`成立。

**365. 水壶问题**

有两个容量分别为 *x*升 和 *y*升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 *z*升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 *z*升水。

你允许：

- 装满任意一个水壶
- 清空任意一个水壶
- 从一个水壶向另外一个水壶倒水，直到装满或者倒空

**示例 1:** 

```
输入: x = 3, y = 5, z = 4
输出: True
```

**示例 2:**

```
输入: x = 2, y = 6, z = 5
输出: False
```

```c++
class Solution {
public:
    int gcd(int x,int y){return y>0?gcd(y,x%y):x;}
    bool canMeasureWater(int x, int y, int z) {
		if(x==0||y==0)
            return x+y==0||z==0;
        if(x+y<z)
            return false;
        return z%gcd(x,y)==0;
    }
};
```





#### 2.3. 回文

 **409. 最长回文串**

在构造过程中，请注意区分大小写。比如 `"Aa"` 不能当做一个回文字符串。

**注意:**
假设字符串的长度不会超过 1010。

**示例 1:**

```
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```

```C++
class Solution {
public:
    int longestPalindrome(string s) {
		unordered_map<char,int>umc;
        int v=0,ans=0;
        //当作计数器，把每一个字符出现的次数记录下来
        for(char c:s)
            ++umc[c];
        for(auto d:umc){
            v=d.second;
            //每次能计数的只能是偶数
            ans+=v/2*2;
            //有且只能存在一个奇数
            if(ans%2==0&&v%2==1)
                ans++;
        }
        return ans;
    }
};
```



<a herf="https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/" style="color:purple">1457.  二叉树中的伪回文路径</a>

给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中**伪回文**路径的数目。

 

**示例 1：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_1.png">

```
输入：root = [2,3,1,3,1,null,1]
输出：2 
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
```



**示例 2：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_2.png"/>

```
输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1 
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
```



**示例 3：**

```
输入：root = [9]
输出：1
```

**<font size=2>提示：</font>**

*<font size=2>给定二叉树的节点数目在 1 到 10^5 之间。</font>*
*<font size=2>节点值在 1 到 9 之间。</font>*

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res=0;
    void dfs(TreeNode* root,int count){
        if(root->NULL)return;
        count^=(1<<res);
        if(root->left==null&&root->right==null){
            if()
        }
        dfs(root->left);
        dfs(root->right);
    }
    int pseudoPalindromicPaths (TreeNode* root) {
        dfs(root,0);
        return res;
    }
};
```



#### 2.4. 同余定理

<a herf="[https://baike.baidu.com/item/%E5%90%8C%E4%BD%99%E5%AE%9A%E7%90%86/1212360?fr=aladdin](https://baike.baidu.com/item/同余定理/1212360?fr=aladdin)">【同余定理】</a>

​		给定一个正整数`m(m>0)`，如果两个整数`a`和`b`满足`a-b`能够被`m`整除，即`(a-b)/m`得到一个整数，那么就称整数`a`与`b`对模`m`同余，记作*<font color=red>`a≡b(mod m)`</font>*。对模m同余是整数的一个等价关系。 

​		例：`m=5，a=22，b=2，`那么有 `(a-b)/5=4`，22 &equiv; 2 (mod 5). 

​		<font size=2>*1. 当`(a+b)`/`m`时，余数为 `b`.*</font>

​	    <font size=2>*2.  当`a/m`时，必为整除.*</font>

性质：

（1）若a≡0(mod m)，则m|a；(整除)

（2）a≡b(mod m)等价于`a`与`b`分别用`m`去除，余数相同.



<a herf="https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/" style="color:purple">974. 和可被 K 整除的子数组</a>

给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

**示例：**

```
输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

*提示：*

*1 <= `A.length `<= 30000*
*-10000 <= `A[i]` <= 10000*
*2 <=` K` <= 10000*

```c++
class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
		int sum=0,ans=0;
        unordered_map<int,int>umap={{0,1}};
        for(int a:A){
            sum+=a;
            //同余
            int mod=(sum%K+K)%K;
            if(umap.count(mod))
                ans+=umap[mod];
            ++umap[mod];
        }
        return ans;
    }
};
```





### 第三章 距离

#### 3.1 切比雪夫距离

* 切比雪夫距离一般是在一个二维坐标中，两个坐标差的绝对值的最大值
  * ans=max(abs(`x2-x1`)，abs(`y2-y1`));

**题号1266 最小时间**

​		平面上有n个点，用坐标(x,y)表示，求访问这些点的最小时间

```中文
* 按顺序访问
* 每秒按水平、竖直或跨对角线移动
```

​	<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/1626_example_1.png" alt="img" style="zoom: 50%;" />

```C++
int minTimeToVisitAllPoints(vector<vector<int>>& points) {
    int x1=points[0][0],y1=points[0][1];
    int x2,y2;
    int second=0;
    for(int i=1;i<points.size();i++){
        x2=points[i][0],y2=points[i][1];
        second+=max(abs(x2-x1),abs(y2-y1));
        x1=x2;
        y1=y2;
    }
    return second;
}
```

#### 3.2 曼哈顿距离

#### 3.3 汉明距离

**汉明距离的特性：**

对于固定的长度 n，汉明距离是该长度字符向量空间上的度量，很显然它满足非负、唯一及对称性，并且可以很容易地通过完全归纳法证明它满足三角不等式。

如果把a和b两个单词看作是向量空间中的元素，则它们之间的汉明距离等于它们汉明重量的差a-b。如果是二进制字符串a和b，汉明距离等于它们汉明重量的和a+b或者a和b汉明重量的异或a XOR b。汉明距离也等于一个n维的超立方体上两个顶点间的曼哈顿距离，n指的是单词的长度。

给予两个任何的字码，10001001和10110001，即可决定有多少个相对位是不一样的。在此例中，有三个位不同。要决定有多少个位不同，只需将exclusive OR运算加诸于两个字码就可以，并在结果中计算有多个为1的位。例如：

10001001

`Xor` 10110001

00111000

两个字码中不同位值的数目称为汉明距离(`Hamming distance`) 。它的重要性在于如果有两个字码的汉明距离为d的话，就需要d的单一位错误已将其中一个字码转换为另一个。

**461. 汉明距离**

在`d(x, y)`中，寻找`x`到`y`的二进制位的距离：

**示例:**

```中文
输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
```

普通解法：

```c++
class Solution {
public:
    int hammingDistance(int x, int y) {
		int z=x^y;
        int cot=0;
        while(z){
            //也可以用cot+=z&1来实现，这样就不需要if判断了
            if(z%2==1)
                cot++;
            z>>=1;
        }
        return cot;
    }
};
```



布赖恩·克尼根算法：

```c++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int z=x^y;
        int cot=0;
        while(z){
            //最主要的是下面这一个语句
            z=z&(z-1);
            cot++;
        }
        return cont;
    }
}
```



### 第四章 求解



#### 4.1 等差数列

* 等差数列通项公式、求和公式：

  ​	a<sub>n</sub>=a<sub>1</sub>+(n-1) &times;d

  ​	S<sub>n</sub>=na<sub>1</sub>+[n(n-1)/2]d  (n&isin;N<sup>*</sup>)

  ​	S<sub>n</sub>=n(a<sub>1</sub>+a<sub>n</sub>)&times;d/2

* 等差中项的关系：		

  ​	a<sub>n</sub>=a<sub>m</sub>+(n-m)d

**268 缺失的数字** 

在一组数组中，找出缺失的数字：

```
输入: [3,0,1]
输出: 2

缺失的数字为2
```

```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        return nums.size()*(nums.size()+1)/2
            -accumulate(nums.begin(),nums.end(),0);
    }
}
```

#### 4.2 弦图

* 常用算法：最大优势算法

#### 4.3 牛顿求解法

* 参考公式：

  X<sub>n+1</sub>=X<sub>n</sub> - F(X<sub>n</sub>)/F'(X<sub>n</sub>)

  ![](https://bkimg.cdn.bcebos.com/pic/f703738da97739126a4f98f3ff198618367ae233?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg)

<a herf="https://leetcode-cn.com/problems/sqrtx/" style="color:purple">**69. x 的平方根**</a>

实现 `int sqrt(int x)` 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

**示例 1:**

```
输入: 4
输出: 2
```

**示例 2:**

```
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```

<img src="https://pic.leetcode-cn.com/36b76d291e8c934a5f1826f52f9f4f8b20c47e301e7c408123a43486a8c4e3dc-image.png" width="600">

> ( 4 + 2/ 4 ) / 2 = 2.25
>
> ( 2.25 + 2/ 2.25 ) / 2 = 1.56944..
>
> ( 1.56944..+ 2/1.56944..) / 2 = 1.42189..
>
> ( 1.42189..+ 2/1.42189..) / 2 = 1.41423..
>
> ….

<img src="https://pic.leetcode-cn.com/c142efde7a7261c6c799d3269cee2f921dc5f5144a410b32afce4dbf036d0ed7-image.png" width="300">

&diams; 设一个数为 x ，我们可以有 x<sub>1</sub>=(x+a/x)，一直循环计算下去，最后 x<sub>1</sub>无限接近于 x，就是我们要找的结果了.

```c++
class Solution {
public:
    int mySqrt(int a) {
        //注意在此处需要用 long 类型
        long x=a;
        while(x*x>a){
            x=(x+a/x)/2;
        }
        return int(x);
    }
};
```



### 第五章 集合

<a herf="https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/" style="color:purple">5426. 重新规划路线</a>

`n` 座城市，从 0 到 `n-1` 编号，其间共有 `n-1` 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

路线用 `connections` 表示，其中 `connections[i]` = `[a, b]` 表示从城市 a 到 b 的一条有向路线。

今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

 

**示例 1：**

```
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```

**示例 2：**

```
输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```

**示例 3：**

```
输入：n = 3, connections = [[1,0],[2,0]]
输出：0
```



<font size=2>*提示：*</font>

<font size=2>2 <= n <= 5 * 10^4</font>
<font size=2>`connections.length` == n-1</font>
<font size=2>`connections[i].length` == 2</font>
<font size=2>0 <= `connections[i][0]`, `connections[i][1]` <= n-1</font>
<font size=2>`connections[i][0] `!= `connections[i][1]`</font>



```c++
/*
* 从每一输入中，我们可以找出规律：
* [[0,1],[1,3],[2,3],[4,0],[4,5]]	结果为：3
* [[1,0],[1,2],[3,2],[3,4]]			结果为：2
* [[1,0],[2,0]]						结果为：0
*/
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
		set<int>seti;
        seti.insert(0);
        int res=0;
        for(auto e:connections){
            if(seti.find(e[1])==seti.end()){
                res++;
                seti.insert(e[1]);
            }
            else
                seti.insert(e[0]);
        }
        return res;
    }
};
```



### 第六章 概率论

<a herf="https://leetcode-cn.com/problems/new-21-game/" style="color:purple">837. 新21点</a>

爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

爱丽丝以 `0` 分开始，并在她的得分少于 `K` 分时抽取数字。 抽取时，她从 `[1, W]` 的范围中随机获得一个整数作为分数进行累计，其中 `W` 是整数。 每次抽取都是独立的，其结果具有相同的概率。

当爱丽丝获得不少于 `K`分时，她就停止抽取数字。 爱丽丝的分数不超过 `N` 的概率是多少？



**示例 1：**

```
输入：N = 10, K = 1, W = 10
输出：1.00000
说明：爱丽丝得到一张卡，然后停止。
```



**示例 2：**

```
输入：N = 6, K = 1, W = 10
输出：0.60000
说明：爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
```



**示例 3：**

```
输入：N = 21, K = 17, W = 10
输出：0.73278
```


*<font size=2>提示：</font>*

*<font size=2>0 <= K <= N <= 10000</font>*
*<font size=2>1 <= W <= 10000</font>*
*<font size=2>如果答案与正确答案的误差不超过 10^-5，则该答案将被视为正确答案通过。</font>*
*<font size=2>此问题的判断限制时间已经减少。</font>*

```c++
class Solution {
public:
    double new21Game(int N, int K, int W) {
		if(K==1)return 1.0;
        vector<int>dp(K+W);
        for()
    }
};
```













