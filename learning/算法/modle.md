### 双指针

模板：

```c++
for(int i=0,j=0;i<n;i++){
	while(j<i && check(i,j)) j++;
    // 其他内容为当前题目的具体逻辑
}
```

