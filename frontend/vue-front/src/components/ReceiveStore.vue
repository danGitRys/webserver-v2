<template>
  <div>
    <h2>Component B</h2>
    <p>Received Message: {{ receivedMessage }}</p>
  </div>
</template>

<script>
import { defineComponent, computed } from 'vue';
import { testStore } from '@/store/testStore'; // Import the correct store

export default defineComponent({
  setup() {
    const dataStore = testStore(); // Use the correct store
    const receivedMessage = computed(() => dataStore.test); // Access the correct state property

    return {
      receivedMessage
    };
  }
});
</script>
