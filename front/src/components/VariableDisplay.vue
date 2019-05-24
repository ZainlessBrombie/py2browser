<template>
  <div class="container">
    <div v-if="showing" class="container">
      <component :is="typeMap[showing.type] && typeMap[showing.type].component || Empty"
                 v-bind="typeMap[showing.type] ? typeMap[showing.type].props(showing) : {}"></component>
    </div>
  </div>
</template>

<script>
  import StringDisplay from "./typecomponents/StringDisplay";
  import Empty from "./typecomponents/Empty";

  export default {
    name: "VariableDisplay",
    components: {
      Empty,
    },
    props: {
      showing: {
        type: Object,
        default: undefined,
      }
    },
    data: () => ({
      typeMap: {
        string: {
          component: StringDisplay,
          props: (stringVar) => stringVar ? ({value: stringVar.data.value}) : {value: '' /* wont be rendered */}
        },
      },
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
