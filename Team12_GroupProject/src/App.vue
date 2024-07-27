<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header
  },
  data() {
    return {
      heading: ''
    }
  },
  watch: {
    $route(to) {
      this.heading = to.meta.heading
    }
  },
  created() {
    this.heading = this.$route.meta.heading
  }
}
</script>

<template>
  <header>
    <Header :heading="heading" />
  </header>
  <RouterView />
</template>

<style>
header {
  background-color: #8d493a;
  color: #f8ede3;
  width: 100%;
  height: fit-content;
  font-family: 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  font-weight: bolder;
  font-size: 45px;
  text-align: center;
  top: 0;
  left: 0;
  position: fixed;
}

a {
  text-decoration: none;
  color: black;
}
</style>
