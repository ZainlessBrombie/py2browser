<template>
  <div :class="expanded ? 'text-container-freed' : 'text-container'">
    <b v-if="isOverflowing" v-on:click="toggle">+</b>{{(expanded && isOverflowing) ? value : value.slice(0, 1000)}}
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
  }

  .text-container-freed {
    height: unset;
    padding: 7px;
  }
</style>
