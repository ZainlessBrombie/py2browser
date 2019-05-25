<template>
  <div class="grey">
    <div class="variable-list">
      <CustomDivider text="Standard Types" background-color="lightgrey"></CustomDivider>
      <div v-for="varname in Object.keys(vars).filter(n => isStandardType(vars[n].type))" v-on:click="() => clicked(varname)">
        <VarButton :name="varname" :type="vars[varname].type" :subtype="vars[varname].data.subtype" :marker-color="colorMap[vars[varname].type]"></VarButton>
      </div>
      <CustomDivider text="Unknown" v-if="Object.keys(vars).filter(n => vars[n].type === 'unknown').length" background-color="grey"></CustomDivider>
      <div v-for="varname in Object.keys(vars).filter(n => vars[n].type === 'unknown')" v-on:click="() => clicked(varname)">
        <VarButton :name="varname" :type="vars[varname].type" :subtype="vars[varname].data.subtype" :marker-color="colorMap[vars[varname].type]"></VarButton>
      </div>
      <CustomDivider text="Modules, Functions etc." background-color="lightgrey"></CustomDivider>
      <div v-for="varname in Object.keys(vars).filter(n => !isStandardType(vars[n].type))" v-on:click="() => clicked(varname)">
        <VarButton :name="varname" :type="vars[varname].type" :subtype="vars[varname].data.subtype" :marker-color="colorMap[vars[varname].type]"></VarButton>
      </div>
    </div>
  </div>
</template>

<script>
  import Button from "./Button";
  import CustomDivider from "./CustomDivider";
  import VarButton from "./VarButton";
  export default {
    name: "SidebarLeft.vue",
    components: {CustomDivider, Button, VarButton},
    props: {
      vars: {
        type: Object,
        default: () => ({}),
      }
    },
    data: () => ({
      colorMap: {
        string: 'green', // TODO central color management
        number: 'red',
        boolean: 'orange',
        datetime: 'blue',
        collection: 'grey',
        map: 'brown',
        stream: 'lightblue',
        bytes: 'pink'
      }
    }),
    methods: {
      clicked(varname) {
        this.$emit('varSelected', varname);
      },
      isStandardType: t => ['string', 'number', 'collection', 'map', 'datetime', 'boolean', 'stream', 'bytes'].includes(t)
    }
  }
</script>

<style scoped>
  .grey {
    background: lightgrey;
  }

  .variable-list {
    overflow-y: scroll;
    height: 100vh;
    padding-top: 7px;
  }
</style>
