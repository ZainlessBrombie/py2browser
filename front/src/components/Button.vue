<template>
  <div class="button">
    {{text}}
  </div>
</template>

<script>
  export default {
    name: "Button",
    props: {
      text: {
        type: String,
        default: '',
      }
    }
  }
</script>

<style scoped>
.button{
  padding-top: 1.2em;
  text-align: center;
  margin-top: 15px;
  margin-left: 20px;
  margin-right: 20px;
  height: 2.5em;
  background: aquamarine;
}
</style>
