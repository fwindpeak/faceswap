<template>
  <div id="app">
    <img src="./assets/logo.png">
    <Faceswap></Faceswap>
  </div>
</template>

<script>
import Faceswap from './components/Faceswap'

export default {
  name: 'app',
  components: {
    Faceswap
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
