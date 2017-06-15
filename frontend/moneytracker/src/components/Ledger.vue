<template>
  <div class="ledger">

    <div class="container">
      <div class='row'>
            <button v-on:click="getLedgers()">get ledgers</button>
            <button v-on:click="openLedgerMaker()">make a new ledger</button>
            <div v-if='this.newledger=="maker"'>
              <input v-model="ledgername" placeholder="ledger name">
              <button v-on:click="setLedgername()">create!</button>
            </div>
            <div v-if='this.newledger=="name"' >
              <div class="ledgernameclass">
                <p>Ledger Name is: {{ledgername}}</p>
                <button v-on:click="consoleLedger()">console current ledger</button>
              </div>
            </div>
      </div>


  <div v-if='this.newledger=="name"' >

      <div class='row'>


        <div class="col-4 ">
          <input v-model="itemname" placeholder="item name">
          <input v-model="itemdescription" placeholder="how much green we talkin">
          <button v-on:click="updateProfit()">profit</button>
          <button v-on:click="updateLoss()">loss</button>
        </div>
      </div>


      <div class="row">
        <div class="col-4 profitcontainer">
          <!-- <div v-if='this.whichuse=="profit"'> -->
            <Ledgerprofit v-bind:ledgerInputProfit="ledgerInputProfit"
            v-bind:ledgername="ledgername"></Ledgerprofit>
          <!-- </div> -->
        </div>
        <div class="col-4  losscontainer">
          <!-- <div v-if='this.whichuse=="loss"'> -->
            <Ledgerloss v-bind:ledgerInputLoss="ledgerInputLoss"
            v-bind:ledgername="ledgername"></Ledgerloss>
          <!-- </div> -->
        </div>
        <div class="col-4 totalcontainer">
            <Ledgersubtotal v-bind:lossLedgerArrprop='lossLedgerArr' v-bind:profitLedgerArrprop='profitLedgerArr'></Ledgersubtotal>
        </div>
      </div>

  </div>

    </div>

  </div>
</template>

<script>
import axios from 'axios';
import eventbus from '../bus/eventbus';
import Ledgerloss from './Ledgerloss';
import Ledgerprofit from './Ledgerprofit';
import Ledgersubtotal from './Ledgersubtotal';

export default {
  name: 'ledger',
  components: { Ledgerprofit, Ledgerloss, Ledgersubtotal },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      dollarvariable: null,
      profitvariable: null,
      lossvariable: null,
      ledgername: '',
      itemname: '',
      itemdescription: '',
      whichuse: null,
      newledger: false,
      ledgerInputProfit: false,
      ledgerInputLoss: false,
      lossLedgerArr:[],
      profitLedgerArr: []
    }
  },
  mounted(){
    eventbus.$on('resetLedgerInput', (newvalue)=>{
      // console.log('inside eventbus on');
      this.ledgerInputProfit = newvalue;
      this.ledgerInputLoss = newvalue;
    });
    eventbus.$on('profitLedger', (newvalue)=>{
      // console.log('inside profitledger on');
      this.profitLedgerArr = newvalue;
      this.updatedLedger++;
    });
    eventbus.$on('lossLedger', (newvalue)=>{
      // console.log('inside lossLedger on');
      this.lossLedgerArr = newvalue;
      this.updatedLedger++;
    });
  },
  methods:{
      updateProfit(){
        axios({
          method: 'post',
          url: 'http://localhost:5000/',
          headers: {
            'Content-type': 'application/json'
            },
          data:{
            'id': Date.now(),
            'profitorloss': 'profit',
            'listname': this.ledgername,
            'itemname': this.itemname,
            'itemdescription': this.itemdescription,
            'generalpost': true
              }
        })
        .then(response => {
          // console.log('this is the response from the python server ', response);
        })
        .catch((error)=>{
          // console.log('this is the error from the python server ', error);
        })

        this.ledgerInputProfit = true;
      },
      updateLoss(){
        axios({
          method: 'post',
          url: 'http://localhost:5000/',
          headers: {
            'Content-type': 'application/json'
            },
          data:{
            'id': Date.now(),
            'profitorloss': 'loss',
            'listname': this.ledgername,
            'itemname': this.itemname,
            'itemdescription': this.itemdescription,
            'generalpost': true
              }
        })
        .then(response => {
          // console.log('this is the response from the python server ', response);
        })
        .catch((error)=>{
          // console.log('this is the error from the python server ', error);
        })

        this.ledgerInputLoss = true;
      },
      getLedgers(){
        axios({
          method: 'get',
          url: 'http://localhost:5000/'
        })
        .then((response)=>{
          // console.log('this is the response from the python server on a get request ', response);
        })
        .catch(error=>{
          // console.log('here is the error on a get request from the python server ', error);
        })
      },
      openLedgerMaker(){
        this.newledger = "maker";
      },
      setLedgername(){
        this.newledger = "name";
      },
      consoleLedger(){
        // console.log('inside consoleLedger method and the value of this.ledgername is ', this.ledgername);
        axios({
          method: 'post',
          url: 'http://localhost:5000/',
          headers: {
            'Content-type': 'application/json'
            },
          data:{
            'listname': this.ledgername,
            'consoleLedger': true
              }
        })
        .then((response)=>{
          // console.log('this is the response from the python server on a get request of listname ', response);
        })
        .catch(error=>{
          // console.log('here is the error on a get request from the python server of listname ', error);
        })


      }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<!-- brown #54494B
white #F1F7ED
green #91C7B1
red #B33951
gold #F3D081 -->

<style scoped>

.profitcontainer{
  background: #91C7B1;
  color: #F1F7ED;
  height: 100vh;
}
.losscontainer{
  background: #B33951;
  color: #F1F7ED;
  height: 100vh;
}
.totalcontainer{
  background: #F3D081;
  color: #F1F7ED;
  height: 100vh;
}
.ledgernameclass{
  background:#F1F7ED;
  /*color: white;*/

}


h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
