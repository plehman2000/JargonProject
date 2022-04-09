<template>
  <form enctype = "multipart/form-data">
        <input type="file"
        accept=".pdf"
        class="fileinput"
        name="file"
        @change="onChange"
        >
      </form>   
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
  name: 'HomePage',
  methods:{
    async onChange(e) {
      let text = "";

      let path = 'http://127.0.0.1:5000/gettext';
      let file = e.target.files[0];
      let formData = new FormData();
      formData.append('file', file);
      
      await axios.post(path,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      ).then(response => {
        text = response.data;
      }).catch(err => {
        console.log(err);
      });
      console.log(text)
      router.push({
        name: 'TextDisplay',
        params: {
          pdftext: text
        }
      });
	},
  }
}
</script>


