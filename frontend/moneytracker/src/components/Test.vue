<template>
  <div class="Test">
    <h1>Hey you got to the test page good for you</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Test',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created () {
    // axios({
    //   method: 'post',
    //   url: 'http://localhost:5000/api/book',
    //   headers: {
    //            'Content-type': 'application/json'
    //     },
    //   data:{
    //     'title': "The Eye of the World",
    //     'author': {
    //         'first_name': "Robert",
    //         'last_name': "Jordan"
    //         }
    //       }
    // })
    // .then(response => {
    //   console.log('this is the response from the python server ', response);
    // })
    // .catch((error)=>{
    //   console.log('this is the error from the python server ', error);
    // })
    // axios({
    //   method: 'post',
    //   url: 'http://localhost:5000/profit',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   data:{
    //     'id': '1',
    //     'name': 'testname',
    //     'description': 'testdescription'
    //   }
    // })
    // .then(response => {
    //   console.log('this is the response from the python server ', response);
    // })
    // .catch((error)=>{
    //   console.log('this is the error from the python server ', error);
    // })

    axios({
      method: 'get',
      url: 'http://localhost:5000/profit'
    })
    .then((response)=>{
      console.log('this is the response from the python server on a get request ', response);
    })
    .catch(error=>{
      console.log('here is the error on a get request from the python server ', error);
    })




  }

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
