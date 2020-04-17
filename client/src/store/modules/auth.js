/* eslint-disable no-shadow */
/* eslint-disable no-param-reassign */

import Axios from "axios";
import {
  AUTH_REQUEST,
  AUTH_ERROR,
  AUTH_SUCCESS,
  AUTH_LOGOUT,
} from "../actions/auth";

const state = {
  token: localStorage.getItem("user-token") || "",
  status: "",
};

const getters = {
  isAuthenticated: (state) => !!state.token,
  authStatus: (state) => state.status,
};

const actions = {
  [AUTH_REQUEST]: ({ commit }, user) => new Promise((res, rej) => {
    commit(AUTH_REQUEST);
    console.log(user);
    Axios.post("http://127.0.0.1:5000/login", user)
      .then((response) => {
        console.log(response.data);
        const { token } = response.data;
        localStorage.setItem("user-token", token);
        console.log(localStorage);
        Axios.defaults.headers.common.Authorization = token;
        commit(AUTH_SUCCESS, token);
        console.log("Got here");
        res(response);
      }).catch((err) => {
        commit(AUTH_ERROR, err);
        localStorage.removeItem("user-token"); // if the request fails, remove any possible user token if possible
        rej(err);
      });
  }),
  [AUTH_LOGOUT]: ({ commit }) => new Promise((resolve) => {
    commit(AUTH_LOGOUT);
    localStorage.removeItem("user-token");
    delete Axios.defaults.headers.common.Authorization;
    resolve();
  }),
};

const mutations = {
  [AUTH_REQUEST]: (state) => {
    state.status = "loading";
  },
  [AUTH_SUCCESS]: (state, token) => {
    state.status = "success";
    state.token = token;
  },
  [AUTH_ERROR]: (state) => {
    state.status = "error";
  },
  [AUTH_LOGOUT]: (state) => {
    state.token = "";
  },
};


export default {
  state,
  getters,
  actions,
  mutations,
};
