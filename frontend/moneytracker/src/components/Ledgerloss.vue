<template>
  <div class="ledgerloss">

    <div class='dollarvalue'>{{dollars}}</div>

  </div>
</template>

<script>
import axios from 'axios';
import eventbus from '../bus/eventbus';

export default {
  name: 'ledgerloss',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',

    }
  },
  props:['dollars']
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
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
