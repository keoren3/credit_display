<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a
      class="navbar-brand"
      href="localhost:8080"
    >Credit Display Web</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    />
    <div
      id="navbarNav"
      class="collapse navbar-collapse"
    >
      <div class="navbar-nav">
        <v-btn to="/register">
          Register
        </v-btn>
        <v-btn to="/login">
          Login
        </v-btn>
        <v-btn to="/upload">
          Upload
        </v-btn>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  Main: "NavBar",
};
</script>
