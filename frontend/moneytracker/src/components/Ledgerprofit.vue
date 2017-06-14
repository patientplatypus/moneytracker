<template>
  <div class="ledgerprofit">

    <!-- <div class='dollarvalue'>{{dollars}}</div> -->
    <ul id="example-1">
      <li v-for="item in listArr" ref='cvglisbox'>
        <p>Item name:  {{ item.itemname }}</p>
        <p>Item description: {{ item.itemdescription }}</p>
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
      listArr: []
    }
  },
  props:['ledgerInputProfit', 'ledgername'],
  watch : {
      ledgerInputProfit : function (value) {

        // (ID, PROFITORLOSS, LISTNAME, ITEMNAME, ITEMDESCRIPTION)

        console.log('ledgerInputProfit changed to '+value);
        console.log('this.ledgername', this.ledgername);
        console.log('here is the output from this.$refs ', this.$refs);
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
