// pages/index/test01.js
Page({
  /**
   * 页面的初始数据
   */
  //  var match_list:function{
    
  //  },
  data: {
    name1:'',
    name2:'',
    result:0
  },
  inputchange1:function(e){
    console.log(e);
    this.data.name1=e.detail.value;
  },
  inputchange2:function(e){
    console.log(e);
    this.data.name2=e.detail.value;
  },
  match:function(e){
    // for(var index in match_list){
    //   if(this.data.name1 == this.match_list[index]['a'] ||this.data.name1 == this.match_list[index]['b'])
    //   if(this.data.name2 == this.match_list[index]['a'] ||this.data.name2 == this.match_list[index]['b'])
    //   this.data(match_list[index].score);
    //   return;
    // }
    console.log(e);
    var charcode1 = this.charcode(this.data.name1);
    var charcode2 = this.charcode(this.data.name2);
    var result = 100 - Math.abs(charcode1 - charcode2);
    console.log(result);
    // this.data.result = result;
    //告诉前端更新
    this.setData({result:result})
  },
  charcode:function(name){
    var totalcod = 0;
    for(var idx in name){
      totalcod += name.charCodeAt(idx);
    }
    return totalcod % 100;
  }
})