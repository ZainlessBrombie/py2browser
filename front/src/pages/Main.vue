<template>
  <div style="display: flex; flex-direction: row">
    <SidebarLeft class="sidebar" v-on:varSelected="varName => select(varName)"
                 :vars="variables"></SidebarLeft>
    <VariableDisplay class="var-display" :showing="selected"></VariableDisplay>
  </div>
</template>

<script>
  import SidebarLeft from '../components/SidebarLeft';
  import VariableDisplay from "../components/VariableDisplay";
  import axios from "axios";


  export default {
    components: {VariableDisplay, SidebarLeft},
    data: () => ({
      error: '',
      variables: {},
      selected: undefined,
      updating: false,
      updateSuppressed: false,
      selectedName: undefined,
    }),
    methods: {
      update() {
        if (this.updating) return;
        this.updating = true;
        axios.get(`${false ? window.location.origin : 'http://localhost:8081'}/api/v1/variables`, {timeout: 20000})
          .then(({data}) => {
            this.error = '';
            this.variables = data.vars;
            this.selected = this.variables[this.selectedName];
          })
          .catch(err => {
            this.error = `Could not load, data stale: ${err}`
          })
          .finally(() => {
            this.updating = false;
          })
      },
      select(varName) {
        this.selectedName = varName;
        this.selected = this.variables[varName];
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
  }

  .sidebar {
    width: 15vw;
    height: 100vh;
  }
</style>
