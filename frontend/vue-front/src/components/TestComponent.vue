<template>
    <h1>Test</h1>
    <div v-on:mousemove="mousePos">
        <span>xPos: {{ xPos }}</span><br><span>yPos: {{ yPos }}</span>
    </div>
</template>

<script>
export default{
    data() {
      return {
        xPos: 0,
        yPos: 0
      }
    },
    methods: {
      mousePos(event) {
        this.xPos = event.offsetX
        this.yPos = event.offsetY
      }
    }
}
</script>

<style>
    #app > div {
      width: 160px;
      height: 80px;
      background-color: lightcoral;
      padding: 20px;
    }
</style>