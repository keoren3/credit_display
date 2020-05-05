/* eslint-disable no-shadow */
/* eslint-disable no-param-reassign */

import axios from "axios";
import Cookies from "js-cookie";
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
    axios.post("http://127.0.0.1:5000/login", user)
      .then((response) => {
        const { token } = response.data;
        localStorage.setItem("user-token", token);
        axios.defaults.headers.common.Authorization = `Bearer ${token}`;
        Cookies.set("token", `Bearer ${token}`);
        commit(AUTH_SUCCESS, token);
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
    delete axios.defaults.headers.common.Authorization;
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
