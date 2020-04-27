<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input
          id="file"
          ref="file"
          type="file"
          @change="handleFileUpload()"
        >
      </label>
      <button
        class="btn btn-primary"
        @click="submitFile()"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Upload",
  /*
      Defines the data used by the component
    */
  data() {
    return {
      file: "",
    };
  },

  methods: {
    /*
        Submits the file to the server
      */
    submitFile() {
      /*
                Initialize the form data
            */
      const formData = new FormData();

      /*
                Add the form data we need to submit
            */
      formData.append("file", this.file);

      /*
          Make the request to the POST /single-file URL
        */
      axios.post("http://127.0.0.1:5000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }).then((res) => {
        console.log(res.data);
      })
        .catch(() => {
          console.log("FAILURE!!");
        });
    },

    /*
        Handles a change on the file upload
      */
    handleFileUpload() {
      [this.file] = this.$refs.file.files;
    },
  },
};
</script>
