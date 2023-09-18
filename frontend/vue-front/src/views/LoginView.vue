<!-- src/App.vue -->
<template>
    <div>
      <ComponentA />
      <ComponentB />
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import ComponentA from '@/components/LogComponent.vue';
  import ComponentB from '@/components/LoginResult.vue';
  
  export default defineComponent({
    components: {
      ComponentA,
      ComponentB,
    }
  });
  </script>
  