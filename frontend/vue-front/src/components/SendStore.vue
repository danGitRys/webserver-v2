<!-- src/components/ComponentA.vue -->
<template>
  <div>
    <h2>Component A</h2>
    <input v-model="message" placeholder="Enter a message" />
    <button @click="sendMessage">Send Message</button>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'; // Import defineComponent and ref

import { testStore } from '@/store/testStore';

export default defineComponent({
  setup() {
    // Use ref to create a reactive variable
    const message = ref('');
    
    // Import the testStore
    const dataStore = testStore();

    // Define the sendMessage method
    const sendMessage = () => {
      dataStore.set(message.value);
    };

    return {
      message,
      sendMessage
    };
  }
});
</script>
