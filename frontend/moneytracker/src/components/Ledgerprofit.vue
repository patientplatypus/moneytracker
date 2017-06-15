<template>
  <div class="ledgerprofit">

    <!-- <div class='dollarvalue'>{{dollars}}</div> -->
    <ul id="example-1">
      <li v-for="item in listArr">
        <p>Item name:  {{ item.itemname }}</p>
        <p ref='dollartag'>Item description: {{ item.itemdescription }}</p>
        <hr/>
      </li>
    </ul>

  </div>
</template>

<script>
import axios from 'axios';
import eventbus from '../bus/eventbus';

export default {
  name: 'ledgerprofit',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      listArr: [],
      offsetArr: [],
      profitLedgerArr: []
    }
  },
  // mounted: function(){
  //     console.log('inside mounted!!!');
  //     console.log('here is the output from this.$refs ', this.$refs);
  // },
  updated: function () {
    this.$nextTick(function() {
      // console.log('inside READY ***************************************');
      // console.log('here is the output from this.$refs ', this.$refs.dollartag);
      this.offsetArr = [];
      this.$refs.dollartag.forEach((val)=>{
        this.offsetArr.push(val.offsetTop);
      })
      // console.log('here is the offsetArr ', this.offsetArr);

      var profitLedgerArr = []

      var self = this;

      var promise = new Promise((resolve)=>{
        for(var x = 0; x<self.listArr.length; x++){
          profitLedgerArr.push([self.offsetArr[x], self.listArr[x]])
          if(x === self.listArr.length-1){
            resolve(true)
          }
        }
      });

      promise.then((resolve)=>{
        if (resolve){
          console.log('INSIDE PROFIT RESOLVE');
          eventbus.$emit('profitLedger', profitLedgerArr);
        }
      });
    })
  },
  props:['ledgerInputProfit', 'ledgername'],
  watch : {
      ledgerInputProfit : function (value) {

        // (ID, PROFITORLOSS, LISTNAME, ITEMNAME, ITEMDESCRIPTION)

        console.log('ledgerInputProfit changed to '+value);
        console.log('this.ledgername', this.ledgername);
        eventbus.$emit('resetLedgerInput', false);
        axios({
          method: 'post',
          url: 'http://localhost:5000/',
          headers: {
            'Content-type': 'application/json'
            },
          data:{
            'populateprofit': 'true',
            'listname': this.ledgername
              }
        })
        .then(response => {
          console.log('this is the response from the python server ', response);
          var tempArr = []
          response.data.forEach((val)=>{
            var tempObj = {};
            tempObj.id = val[0];
            tempObj.itemname = val[3];
            tempObj.itemdescription = val[4];
            tempArr.push(tempObj);
          })
          console.log('this is the value of the tempArr ', tempArr);
          this.listArr = tempArr;

        })
        .catch((error)=>{
          console.log('this is the error from the python server ', error);
        })
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

.dollarvalue{
    color: #F1F7ED;
}

ul {
  list-style-type: none;
  padding: 0;
  text-align: left;
  float: left;
}

li {
  display: inline-block;
  margin: 0 10px;
}

p {
  margin: 0;
  word-wrap: break-word;
  text-wrap: normal;
  white-space: normal;
}

a {
  color: #42b983;
}
</style>
