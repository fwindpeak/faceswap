<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
      <form enctype="multipart/form-data" >
        <span>head:</span><input name="head" @change="handleHeadChange" type="file"/>
        <span>face:</span><input name="face" @change="handleFaceChange" type="file"/>
        <input value="提交" type="button" @click="handleSubmit"/>
      </form>
      <img v-if="img_output" :src="img_output" />
    </div>
  </div>
</template>

<script>

  import {uploadPic} from '../api/faceswap'

  export default {
    name: 'hello',
    data () {
      return {
        msg: 'faceswap',
        file_head:'',
        file_face:'',
        img_output:''
      }
    },
    methods:{
      handleSubmit(){
        console.log(this.file_head,this.file_face);
        let param = new FormData();
        param.append('head',this.file_head);
        param.append('face',this.file_face);

        uploadPic(param).then(res =>{
          console.log(res);
          this.img_output = `/api/${res}`;
        })
      },
      handleHeadChange(v){
        this.file_head = v.target.files[0];
      },
      handleFaceChange(v){
        this.file_face = v.target.files[0];
      }
    },
    mounted(){

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
  color: #42b983;
}
</style>
