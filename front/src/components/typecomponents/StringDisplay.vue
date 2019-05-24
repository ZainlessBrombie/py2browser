<template>
  <div style="display: flex; flex-direction: row" :class="expanded ? 'text-container-freed' : 'text-container'">
    <div><b v-if="isOverflowing" v-on:click="toggle" class="hoverclick">+</b></div>
    <div class="str" style="margin-left: .2em;">{{(expanded && isOverflowing) ? value : value.slice(0, 1000)}}</div>
  </div>
</template>

<script>
  export default {
    name: "StringDisplay",
    props: {
      value: {
        type: String,
        default: '',
      },
    },
    data: () => ({
      isOverflowing: false,
      expanded: false,
    }),
    methods: {
      toggle() {
        this.expanded = !this.expanded;
      },
      textWidth(text, fontProp) {
        const tag = document.createElement("div");
        tag.style.position = "absolute";
        tag.style.left = "-99in";
        tag.style.whiteSpace = "nowrap";
        tag.style.font = fontProp;
        tag.innerHTML = text;

        document.body.appendChild(tag);

        const result = tag.clientWidth;

        document.body.removeChild(tag);

        return result;
      }
    },
    mounted() {
      console.log(this.$el.style.font);
      console.log(this.$el.clientWidth < this.textWidth(this.value, this.$el.style.font));
      this.isOverflowing = this.$el.clientWidth < this.textWidth(this.value, this.$el.style.font);
    }
  }
</script>

<style scoped>
  .text-container {
    height: 1.2em;
    overflow: hidden;
    padding: 7px;
    width: 90%;
    white-space: nowrap;
    border-radius: 5px;
    border: solid dimgrey;
  }

  .text-container-freed {
    height: unset;
    padding: 7px;
    border-radius: 5px;
    border: solid dimgrey;
  }

  .hoverclick {
    cursor: pointer;
  }

  .str {
    font-family: "Lucida Console", Monaco, monospace;
    color: green;
  }
</style>
