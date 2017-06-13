<template>
  <div class="Childtest">
    <div>{{message}}</div>
    <button v-on:click="onClick()">subtract 1</button>
  </div>
</template>

<script>
import axios from 'axios';
import eventbus from '../bus/eventbus';

export default {
  name: 'Childtest',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      counter: this.message
    }
  },
  methods:{
    onClick(){
      console.log('inside onclick method');
      var counter = this.message - 1;
      console.log('value of counter is ', counter);
      console.log('value of this.counter is ', this.counter);
      eventbus.$emit('ChildCounter', counter);
    }
  },
  props:['message']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
