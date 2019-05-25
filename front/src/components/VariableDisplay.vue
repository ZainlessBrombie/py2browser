<template>
  <div class="container">
    <div class="container">
      <component :is="TypeRegistry.obtain(showing, path).component"
                 v-bind="TypeRegistry.obtain(showing, path).props(showing)" v-on:select="evt => $emit('select', evt)"></component>
    </div>
  </div>
</template>

<script>
  import Empty from "./typecomponents/Empty";
  import TypeRegistry from "./typecomponents/TypeRegistry";

  export default {
    name: "VariableDisplay",
    components: {
      Empty,
    },
    props: {
      showing: {
        type: Object,
        default: undefined,
      },
      path: {
        type: Array,
      }
    },
    data: () => ({
      TypeRegistry,
      Empty,
    })
  }
</script>

<style scoped>
  .container {
    padding: 2em;
    box-sizing: border-box;
  }

  .content {
    width: calc(85vw - 4em)
  }
</style>
