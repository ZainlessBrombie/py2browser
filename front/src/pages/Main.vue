<template>
  <div style="display: flex; flex-direction: row">
    <SidebarLeft class="sidebar" v-on:varSelected="varName => select([varName])"
                 :vars="variables"></SidebarLeft>
    <VariableDisplay class="var-display" :showing="selectionMethod(path, variables)" :path="path" v-on:select="select"></VariableDisplay>
  </div>
</template>

<script>
  import SidebarLeft from '../components/SidebarLeft';
  import VariableDisplay from "../components/VariableDisplay";
  import axios from "axios";
  import util from "../utils/util";


  export default {
    components: {VariableDisplay, SidebarLeft},
    data: () => ({
      error: '',
      variables: {},
      updating: false,
      updateSuppressed: false,
      path: [],
    }),
    methods: {
      update() {
        if (this.updating) return;
        this.updating = true;
        axios.get(`${false ? window.location.origin : 'http://localhost:8081'}/api/v1/variables`, {timeout: 20000})
          .then(({data}) => {
            this.error = '';
            this.variables = data.vars;
          })
          .catch(err => {
            this.error = `Could not load, data stale: ${err}`
          })
          .finally(() => {
            this.updating = false;
          })
      },
      selectionMethod(path, variables) {
        if (!path || !path.length || !variables) return undefined;

        return path.slice(1).reduce((cur, p) => {
          if (!cur) return undefined;
          if (cur.type === 'collection') {
            return typeof p === 'number' && cur.data.value[p];
          }
          if (cur.type === 'map') {
            return (cur.data.value.filter(({key}) => util.deepEquals(key, p))[0] || {}).value
          }
          return undefined;
        }, variables[path[0]])
      },
      select(path) {
        this.path = path;
      }
    },
    mounted() {
      this.update();
      this.intervalId = setInterval(() => {
        if (!this.updateSuppressed) this.update();
      }, 5000);
    },
    beforeDestroy() {
      clearInterval(this.intervalId);
    }
  }
</script>

<style>
  .var-display {
    width: 85vw;
    height: 100vh;
    background: #42b983;
    overflow-y: auto;
  }

  .sidebar {
    width: 15vw;
    height: 100vh;
  }
</style>
