<template>
  <div class="grey">
    <div class="variable-list">
      <div v-for="varname in Object.keys(vars)" v-on:click="() => clicked(varname)">
        <Button :text="varname + '(' + vars[varname].type + (vars[varname].data.subtype ? ':' + vars[varname].data.subtype : '') + ')'"></Button>
      </div>
    </div>
  </div>
</template>

<script>
  import Button from "./Button";
  export default {
    name: "SidebarLeft.vue",
    components: {Button},
    props: {
      vars: {
        type: Object,
        default: () => ({}),
      }
    },
    methods: {
      clicked(varname) {
        this.$emit('varSelected', varname);
      }
    }
  }
</script>

<style scoped>
  .grey {
    background: grey;
  }

  .variable-list {
    overflow-y: scroll;
    height: 100vh;
  }
</style>
