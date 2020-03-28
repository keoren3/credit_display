<template>
  <div id="mainbar">
    <h1>Welcome to Credit Display</h1>
    <v-row align="center">
      <v-col
        align-self="center"
        cols="12"
      >
        <v-btn to="/upload">
          Click here to upload an Excel sheet
        </v-btn>
      </v-col>
    </v-row>
    <pie-chart
      :data="chartData"
      :options="chartOptions"
    />
  </div>
</template>

<script>
import PieChart from "./PieChart";

export default {
  name: "MainPage",
  components: {
    PieChart,
  },
  data() {
    return {
      chartOptions: {
        hoverBorderWidth: 20,
      },
      chartData: {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        labels: ["Green", "Red", "Blue"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
            data: [1, 10, 5],
          },
        ],
      },
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
