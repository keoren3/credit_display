<template>
  <div id="app">
    <v-app id="inspire">
      <v-data-table
        :headers="headers"
        :items="items"
        :items-per-page="5"
        class="elevation-1"
      />
    </v-app>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data () {
    return {
      headers: [
        { text: "Business Name", value: "business_name" },
        { text: "Charge", value: "charge_value" },
        { text: "Data", value: "deal_date" },
        { text: "Deal Value", value: "deal_value" },
        { text: "More Deatils", value: "more_details" },
      ],
      items: []
    };
  },
  mounted () {
    console.log("mount");
    axios.get("http://127.0.0.1:5000/transactions", {
      headers: { "Content-Type": "application/json" }
    }).then((res) => {
      console.log(res.data);
      this.items = res.data.trans;
      console.log(this.items);
    });
  }
};
</script>

<style></style>
