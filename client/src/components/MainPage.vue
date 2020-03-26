<template>
  <div>
    <h1>Wellcome to credit Display</h1>
    <router-link
      to="upload"
      tag="button"
    >
      Click to upload your exel shit
    </router-link>
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
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  display: flex;
  align-items: center;
  color: #42b983;
}
</style>
