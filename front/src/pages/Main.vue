<template>
  <div style="display: flex; flex-direction: row">
    <SidebarLeft class="sidebar" v-on:varSelected="varName => selectGlobal([varName])"
                 :vars="variables"></SidebarLeft>
    <VariableDisplay class="var-display" :showing="selectionMethod(path, variables)" :path="[]" v-on:select="selectSubjectively"></VariableDisplay>
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
      updating: false,
      updateSuppressed: false,
      path: [],
      subjectivePath: [],
      currentHash: 'none',
    }),
    methods: {
      update() {
        if (this.updating) return;
        this.updating = true;
        axios.get(`${false ? window.location.origin : 'http://localhost:8081'}/api/v1/variables`, {timeout: 20000})
          .then(({data}) => {
            this.error = '';
            // save performance
            if (data.hash !== this.currentHash) {
              this.variables = data.vars;
              this.currentHash = data.hash;
            }
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
            return typeof p === 'number' && cur.data.value[p] || undefined;
          }
          if (cur.type === 'map') {
            return typeof p[0] === "number" && cur.data.value[p[0]][p[1]] || undefined;
          }
          // TODO dynamic/adjustable content field
          // TODO search recursively
          // TODO option to hide components
          // TODO pickle
          // TODO pandas support
          // TODO name in options support
          return undefined;
        }, variables[path[0]]);
      },
      selectGlobal(path) {
        this.path = path;
        this.subjectivePath = path;
      },
      selectSubjectively(path) {
        this.path = [...this.path, ...path];
      }
    },
    watch: {
      error() {
        if (this.error !== '') {
          this.$notify({
            group: 'alertPopups',
            title: 'Error',
            text: this.error,
            type: 'error',
            duration: 600000,
            max: 2,
          });
        } else {
          this.$notify({
            group: 'alertPopups',
            clean: true,
          });
          this.$notify({
            group: 'alertPopups',
            title: 'Reconnected',
            text: 'Connection reestablished',
            type: 'success',
            duration: 10000,
            max: 2,
          });
        }
      },
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
    background: #fdfdff;
    overflow-y: auto;
  }

  .sidebar {
    width: 15vw;
    height: 100vh;
  }
</style>
