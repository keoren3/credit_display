<template>
  <div id="mainbar">
    <h1>Wellcome to Credit Display</h1>
    <v-row align="center">
      <v-col
        align-self="center"
        cols="12"
      >
        <v-btn to="/upload">
          Click here to upload exel shit
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "MainPage",
  data() {
    return {
      msg: "",
    };
  },
};
</script>


<style scoped>

h1 {
  text-align: center;
}

a {
  display: flex;
  color: #42b983;
}
.router-link-exact-active{
    align-items: center;
}
</style>
