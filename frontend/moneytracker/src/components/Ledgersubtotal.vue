<template>
  <div class="ledgersubtotal">

        <div id="example-1">
          <div v-bind:style="{}" v-for="item in cleanedarrsorted">
            <div  v-bind:style="{top: item[0] + 'px', margin: '0px', padding: '0px',
            position: 'absolute', float: 'left', display: 'inlineBlock', width:'29%'}" >
              <p>
                Ledgeramount: {{ item[1] }}</p>
              <hr/>
            </div>
          </div>
          <p>Total Amount: {{totalcleaned}}</p>
        </div>


  </div>
</template>

<script>
import axios from 'axios';
import eventbus from '../bus/eventbus';

export default {
  name: 'ledgersubtotal',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      listArr: [],
      offsetArr: [],
      updatedLedger: 0,
      subtotalArr: [],
      profitLedgerArr: [],
      lossLedgerArr: [],
      cleanedarrsorted: [],
      totalcleaned: 0
    }
  },
  mounted: function(){

    console.log('inside mounted ledgersubtotal');


  },
  props:['profitLedgerArrprop', 'lossLedgerArrprop'],
  watch : {
      lossLedgerArrprop: function(value){
        this.lossLedgerArr = value;
        this.updatedLedger++;
      },
      profitLedgerArrprop: function(value){
        this.profitLedgerArr = value;
        this.updatedLedger++;
      },
      updatedLedger : function (value) {
        var self = this;
        var lossLedgerArrclean = [];

        self.lossLedgerArr.forEach(val=>{
          var tempArr = [val[0], -1*val[1].itemdescription];
          lossLedgerArrclean.push(tempArr);
        })

        var profitLedgerArrclean = [];

        self.profitLedgerArr.forEach(val=>{
          var tempArr = [val[0], val[1].itemdescription];
          profitLedgerArrclean.push(tempArr);
        })

        const sums = {};
        const arrays = [lossLedgerArrclean, profitLedgerArrclean];
        arrays.map(a => a.map( ai => sums[ai[0]] = (sums[parseInt(ai[0])] || 0) + parseInt(ai[1])));
        var cleanedarr = Object.keys(sums).map(k => [k, sums[k]]);

        var cleanedarrsorted = cleanedarr.sort((a,b)=>a[0]-b[0]);

        self.cleanedarrsorted = cleanedarrsorted;


        console.log('cleanedarrsorted is ', cleanedarrsorted);
        this.totalcleaned = 0;
        self.cleanedarrsorted.forEach(val=>{
          self.totalcleaned = val[1] + self.totalcleaned
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
  height: 0;
  width: 0;
  border-width: 0;
  border: none;
  outline: 0;
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
