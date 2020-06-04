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

```C++
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