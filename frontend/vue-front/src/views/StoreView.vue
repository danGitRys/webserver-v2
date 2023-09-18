<!-- src/App.vue -->
<template>
    <div>
      <ComponentA />
      <ComponentB />
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import ComponentA from '@/components/ReceiveStore.vue';
  import ComponentB from '@/components/SendStore.vue';
  
  export default defineComponent({
    components: {
      ComponentA,
      ComponentB
    }
  });
  </script>
  