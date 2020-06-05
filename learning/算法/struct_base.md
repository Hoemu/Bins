<h1 style="text-align:center">数据结构</h1>





### 第一章 数组/链表(双指针)

#### 1.1. 投票算法

- 投票算法模拟投票，例如：当有人选择候选者1号时，得到的票就会增加，而当有人选择后选择2号时，用1号得票表示就是1号的票减少，当1号得票为0时，1号失竞选资格，此时也可以代表2号的票超过1号的票.
- 投票算法还用于**括号深度**的计算

**题号169**

​	在一组数组中计算出出现次数大于数组大小1/2的数
​	

```中文
	输入：[1 2 3 2 2 2]
	输出：2
在上述中，数组长度为6，即大于3的元素为2，所以输出2
```

```c++
代码：

	int majorityElement2(vector<int>& nums){
		int count_1=0;
    	int num=nums[0];
    	for(int i=1;i<nums.size();i++){
            if(count_1==0){
                count_1=1;
                num=nums[i];
            }
            if(num==nums[0])
                count_1++;
           	else
                count_1--;
        }
    	return num;
	}
```

#### 1.2. 双指针

* 通常双指针需要定义两个变量来模仿指针.

* 常遇到的题型：

  1. 在同一个数组中，进行元素的变化.

     ​	如：在一个数组中寻找这个值，并在这个数组中删除这个值，最后返回数组的长度.
     
     

<a herf="https://leetcode-cn.com/problems/product-of-array-except-self/">**238. 除自身以外数组的乘积**</a>

给你一个长度为 n 的整数数组 `nums`，其中` n `> 1，返回输出数组 `output `，其中 `output[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积。

**示例:**

```
输入: [1,2,3,4]
输出: [24,12,8,6]
```

<font size=2> *提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。*</font>
<font size=2> *说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。*</fong>

**进阶：**
<font size=2> *你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）*</font>

**思想与<a herf="https://leetcode-cn.com/problems/trapping-rain-water/" style="color:red">接雨水</a>题目相似**

```c++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len=nums.size();
        vector<int>L(len,0),R(len,0);
        vector<int>result(len);
        L[0]=1,R[len-1]=1;
        for(int i=1;i<len;i++)L[i]=L[i-1]*nums[i-1];
        for(int i=len-2;i>=0;i--)R[i]=R[i+1]*nums[i+1];
        for(int i=0;i<len;i++)result[i]=R[i]*L[i];
        return result;
    }
};
```



**例 2.2 **

​	在一组数组中，将所有为0的元素排到数组末尾，非0元素的顺序不变(尽量使用少的空间)

	如：
		输入：[0 3 1 0 8 0]
		输出：[3 1 8 0 0 0]

~~~c++
	void moveZeroes(vector<int>& nums){
    	int i=0,j=0;
    	while(i<nums.size()&&j<nums.size()){
            if(nums[i]==0)
                i++;
            else{
                nums[j]=nums[i];
                j++;
                i++;
            }
        }
    	for(int k=j;k<nums.size();k++){
            nums[k]=0;
        }
	}
~~~

#### 1.3. 滑动窗口

* 在滑动窗口中，需要给窗口定一个界限
* 当滑动窗口中的元素大于窗口中的元素时需要删除某些元素



**1248. 统计 [优美子数组」**

给你一个整数数组 `nums `和一个整数` k`。

如果某个 连续 子数组中恰好有 `k` 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。



示例 1：

```
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
```

示例 2：

```
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
```

示例 3：

```
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
```

*提示：*

* 1 <= `nums.length `<= 50000
* 1 <= `nums[i]` <= 10^5
* 1 <= k <= `nums.length`

```c++
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int ans=0,count=0;
        vector<int>vei;
        for(auto num:nums){
            ans++;
            if(num%2==1){
                vei.push_back(ans);
                ans=0;
            }
            if(vei.size()>=k)
                count+=vei[size(vei)-k];
        }
        return count;
    }
};
```



### 第二章 串

####  2.1.  串的匹配算法

* **`BF`** 算法
* **`KMP`**算法

#### **2.2. 串的算法**

<a herf="https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/" style="color:purple">**1160. 拼写单词**</a>

给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） `chars`。

假如你可以用 `chars` 中的『字母』（字符）拼写出 `words` 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，`chars` 中的每个字母都只能用一次。

返回词汇表 `words` 中你掌握的所有单词的 长度之和。

**示例 1：**

```
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
```

**示例 2：**

```
输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
```


提示：

1 <= `words.length` <= 1000
1 <= `words[i].length, chars.length` <= 100
所有字符串中都仅包含小写英文字母

```c++
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        //字典中的字符出现的次数记录到map中
		unordered_map<char,int>char_cont;
        for(char e:chars)
            char_cont[e]++;
        bool br=true;
        int ans=0;
        for(string stc:words){
            //将每个单词中每个字母的出现次数记录到map中
            unordered_map<char,int>word_cont;
            for(char c:stc)
                word_cont[c]++;
            br=true;
            for(char c:stc){
                //比较在这个单词中是否有字母出现次数大于字典中的字母数
                if(char_cont[c]<word_cont[c]){
                    br=false;
                    break;
                }
            }
            if(br)
                ans+=stc.size();
        }
        return ans;
    }
};
```



### 第三章 栈和队列

#### 3.1 **普通栈**和普通队列

* 指先进后出的一种线性结构.

* 一般我们把插入和删除元素的一头叫做栈顶，第一个插入的元素叫做栈底.

  

  <a herf="https://leetcode-cn.com/problems/decode-string/" style="color:purple">394. 字符串解</a>

  给定一个经过编码的字符串，返回它解码后的字符串。

  编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 k 次。注意 k 保证为正整数。

  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

  

  **示例:**

  ```
  s = "3[a]2[bc]", 返回 "aaabcbc".
  s = "3[a2[c]]", 返回 "accaccacc".
  s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
  ```

  ```c++
  class Solution {
  public:
      string decodeString(string s) {
  		stack<pair<int,string>>soo;
          int count=0;
          string res;
          for(char c:s){
              if(isdigit(c))
                  count=count*10+(c-'0');
             	else if(c=='['){
                  soo.push({count,res});
                  count=0;
                  res="";
              }
              else if(c==']'){
                  auto pai=soo.top();
                  soo.pop();
                  string tmp=res;
                  for(int i=1;i<pai.first;i++)
                      res+=temp;
                 	res=p.second+res;
              }
              else
                  res+=c;
          }
          return res;
      }
  };
  ```



#### 3.2. **单调栈和单调队列**

* 单调队列，即单调递减或单调递增的[队列](https://baike.baidu.com/item/队列/718364).



* 单调递增或单调减的栈.

  单调栈模板：

  ```c++
  stack<int> st;
  for(int i = 0; i < nums.size(); i++)
  {
  	while(!st.empty() && st.top() > nums[i])
  	{
  		st.pop();
  	}
  	st.push(nums[i]);
  }
  ```

  

  <a herf="https://leetcode-cn.com/problems/largest-rectangle-in-histogram/" style="color:purple">84. 柱状图中最大的矩形</a>

  

  给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 .

  求在该柱状图中，能够勾勒出来的矩形的最大面积.

  <img style="text-align:left" src="pic/柱状矩形.png" >

  以上是柱状图的示例，其中每个柱子的宽度为 `1`，给定的高度为 `[2,1,5,6,2,3]`.

  <img style="text-align:left" src="pic/柱状矩形_面积.png">

  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

   

  **示例:**

  ```
  输入: [2,1,5,6,2,3]
  输出: 10
  ```

  

  ```C++
  class Solution {
  public:
      int largestRectangleArea(vector<int>& heights) {
          stack<int>st;
          int ans=0;
          heights.insert(heights.begin(),0);
          heights.push_back(0);
          for(int i=0;i<heights.size();i++){
              while(!st.empty()&&heights[st.top()]>heights[i]){
                  int cur=st.top();
                  st.pop();
                  int left=st.top()+1;
                  int right=i-1;
                  ans=max(ans,(right-left+1)*heights[cur]);
              }
              st.push(i);
          }
          return ans;
      }
  };
  ```

  

  



### 第四章 树

#### 4.1.  二叉树

*二叉树结构体模板如下：*

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
```



##### 4.1.1 **二叉树树的直径**

**543 树的直径**

​	给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

```
      1
     / \
    2   3
   / \     
  4   5    
```

返回 **3**, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

**注意：**两结点之间的路径长度是以它们之间边的数目表示。



a). 自上而下

```c++
class Solution {
public:
    int ans;
    int deepth(TreeNode *root){
		if(root==NULL)
            return 0;
       	int L=deepth(root->left);
        int R=deepth(root->right);
        ans=max(ans,R+L+1);
       	return max(L,R)+1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int ans=1;
        deepth(root);
        return ans-1;
    }
};
```

b). 自下而上

##### 4.1.2 二叉树的遍历

* 中序遍历

给定一个二叉树，判断其是否是一个有效的二叉搜索树。



假设一个二叉搜索树具有如下特征：

* 节点的左子树只包含小于当前节点的数。

* 节点的右子树只包含大于当前节点的数。

* 所有左子树和右子树自身必须也是二叉搜索树。



**示例 1:**

```
输入:
    2
   / \
  1   3
输出: true
```



**示例 2:**

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

```c++
class Solution {
public:
    long pre=LONG_MIN;
    bool isValidBST(TreeNode* root) {
        if(root==null)
            return true;
        //访问左子树
        if(!(isValidBST(root->left)))
            return false;
        //与上一个节点进行比较，如果大于上衣个节点就满足 root>root->left->val
        if(root->val<=pre)
            return false;
        pre=root->val;
        return isValidBST(root->right);
    }
};
```



##### 4.1.3 二叉树的判断

* 判断二叉树是否为对称二叉树

* <a herf="https://leetcode-cn.com/problems/symmetric-tree/" style="color:purple">101. 对称二叉树</a>

  给定一个二叉树，检查它是否是镜像对称的。

  例如，二叉树 `[1,2,2,3,4,4,3]` 是对称的。

  ```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
  ```

   

  但是下面这个 `[1,2,2,null,3,null,3]` 则不是镜像对称的:

  ```
      1
     / \
    2   2
     \   \
     3    3
  ```

   

  **<font size=2>进阶：</font>**

  <font size=2>你可以运用递归和迭代两种方法解决这个问题吗？</font>

  ```c++
  /*
  * 迭代法：
  */
  class Solution {
  public:
      bool check(TreeNode* node1,TreeNode* node2){
          queue<TreeNode*>qu;
          qu.push(node1),qu.push(node2);
          while(!qu.empty()){
              node1=qu.front(),qu.pop();
              node2=qu.front(),qu.pop();
              if(!node1&&!node2)continue;
              if(!node1||!node2||(node1->val!=node2->val))
                  return false;
              
              qu.push(node1->left),qu.push(node2->right);
              qu.push(node1->right),qu.push(node2->left);
          }
          return true;
      }
      bool isSymmetric(TreeNode* root) {
          return check(root,root);
      }
  };
  
  /*
  * 递归
  */
  class Solution {
  public:
      bool check(TreeNode* node1,TreeNode* node2){
          if(node1==NULL&&node2==NULL)return true;
          if(node1==NULl||node2==NUll||node1->val!=node2->val)
              return false;
         	return check(node1->left,node2->right)&&check(node1->right,node2->left);
      }
      bool isSymmetric(TreeNode* root) {
          if(root==NULL)return true;
          return check(root,root);
      }
  };
  
  ```



* 判断是否为平衡二叉树

  * ​	左右子树高度差的绝对值小于1的二叉树叫做平衡二叉树

  

  <a herf="https://leetcode-cn.com/problems/balanced-binary-tree/" style="color:purple">110. 平衡二叉树</a>

  

  给定一个二叉树，判断它是否是高度平衡的二叉树。

  本题中，一棵高度平衡二叉树定义为：

  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

  

  **示例 1:**

  ```
  给定二叉树 [3,9,20,null,null,15,7]
      3
     / \
    9  20
      /  \
     15   7
  返回 true 。
  ```

  

  **示例 2:**

  ```
  给定二叉树 [1,2,2,3,3,null,null,4,4]
         1
        / \
       2   2
      / \
     3   3
    / \
   4   4
   返回 false 。
  ```



#### 2.3.2 哈希树

##### 4.2.1 **前缀树(字典树)**



**208. 实现 `Trie` (前缀树)**

实现一个 `Trie `(前缀树)，包含` insert`,` search`, 和` startsWith` 这三个操作。

示例:

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
```

**说明:**

你可以假设所有的输入都是由小写字母 a-z 构成的。

保证所有输入均为非空字符串。



关于保存字符如 *图a* 示

<img src="https://pic.leetcode-cn.com/3a0be6938b0a5945695fcddd29c74aacc7ac30f040f5078feefab65339176058-file_1575215106942" width="600" high="600">

<p style="text-align:center">图a</p>

```C++
class Trie {
private:
    bool isempty;
    Trie *next[26];
public:
    /** Initialize your data structure here. */
    Trie():isempty(false),next{nullptr} {}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
		Trie *root=this;
        for(const char w:word){
            if(root->next[w-'a']==nullptr)
                root->next[w-'a']=new Trie();
            root=root->next[w-'a'];
        }
        root->isempty=true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
		Trie *root=this;
        for(const char w:word){
            root=root->next[w-'a'];
            if(root==nullptr)
                return false;
        }
        return root->isempty;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
		Trie *root=this;
        for(const char w:prefix){
            root=root->next[w-'a'];
            if(root==nullptr)
                return false;
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

### **第五章 图**



### 第六章 搜索

#### 2.5.1 深度优先搜索(`dfs`)

**695. 岛屿的最大面积**

给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

**示例 1:**

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
 
 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
```

**示例 2:**

```
[[0,0,0,0,0,0,0,0]]
```

对于上面这个给定的矩阵, 返回 `0`。

**注意:** 给定的矩阵`grid` 的长度和宽度都不超过 50。

```C++
class Solution {
public:
    int dfs(vector<vector<int>>&grid,int i,int j){
        if(i<0||j<0||i==grid.size()||
           j==grid[0].size())
            return 0;
        if(grid[i][j]==1){
            grid[i][j]=0;
            //这段代码与树的深度搜索有相似之处
            return dfs(grid,i-1,j)+dfs(grid,i,j-1)
            +dfs(grid,i+1,j)+dfs(grid,i,j+1)+1;
        }
        return 0;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxarea=0;
    	for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                if(grid[i][j]==1)
                    maxarea=max(maxarea,dfs(grid,i,j));
            }
        }
        return maxarea;
    }
};
```



#### 5.5.2 二分查找



### 第七章 排序

#### 2.6.1. 交换排序

* 冒泡排序

![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015223238449-2146169197.gif)

```c++
    vector<int> sortArray(vector<int>& nums) {
        int len=nums.size()-1;
        for(int i=0;i<len;i++){
            for(int j=0;j<len-i;j++)
                if(nums[j]>nums[j+1])
                    swap(nums[j],nums[j+1]);
        }
        return nums;
    }
```

#### 3.6.2. 选择排序

* 简单选择排序

![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015224719590-1433219824.gif)

```c++
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int len=nums.size()-1;
        //temp用来记住下标
        int temp=0;
        for(int i=0;i<len;i++){
            temp=i;
            for(int j=i+1;j<=len;j++){
                if(nums[j]<nums[temp])
                    temp=j;
            }
            swap(nums[i],nums[temp]);
        }
        return nums;
    }
};
```

#### 2.6.3. 插入排序

1. **简单插入排序**

![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015225645277-1151100000.gif)

```c++
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int In=0,Out=0;
        for(int i=1;i<nums.size();i++){
            In=i-1;
            Out=nums[i];
            while(In>=0&&nums[In]>Out){
                nums[In+1]=nums[In];
                --In;
            }
            nums[In+1]=Out;
        }
        return nums;
    }
};
```

2. **希尔排序**

![](https://images2018.cnblogs.com/blog/849589/201803/849589-20180331170017421-364506073.gif)

*原始的希尔排序如下：*

```c++
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        for(int len=nums.size();len>0;len/=2){
            for(int i=len;i<nums.size();i++){
                int In=i-len;
                int Out=nums[i];
                while(In>=0&&nums[In]>Out){
                    nums[In+len]=nums[In];
                    In-=len;
                }
                nums[In+len]=Out;
            }
        }
        return nums;
    }
};
```



#### 2.6.4. 归并排序

* 归并排序采用**分治**和**递归**的思想
* `LeetCode`上归并相关题型（21. 合并两个有序链表，912. 排序数组）

![](https://images2017.cnblogs.com/blog/849589/201710/849589-20171015230557043-37375010.gif)



#### 2.6.5. 基数排序



