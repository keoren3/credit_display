<template>
  <v-container
    class="fill-height"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        sm="8"
        md="4"
      >
        <v-card class="elevation-12">
          <v-toolbar
            color="primary"
            dark
            flat
          >
            <v-toolbar-title>Register form</v-toolbar-title>
            <v-spacer />
            <v-tooltip bottom />
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                v-model.lazy="userName"
                label="Login"
                name="login"
                prepend-icon="person"
                type="text"
              />

              <v-text-field
                id="password"
                v-model.lazy="password"
                label="Password"
                name="password"
                prepend-icon="lock"
                type="password"
              />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn
              color="primary"
              @click="register"
            >
              Register
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Axios from "axios";

export default {
  data () {
    return {
      userName: "",
      password: "",
      passwordConfirm: "",
    };
  },
  methods: {
    register () {
      const { userName, password } = this;
      Axios.post("http://localhost:5000/register",
        { user_name: userName, password })
        .then(() => {
          this.$router.push({ name: "Login" });
        }).catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
