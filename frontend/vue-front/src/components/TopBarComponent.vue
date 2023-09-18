<!-- AppBar.vue -->
<template>
    <v-app>
    <v-app-bar color="primary" density="compact">
      <v-app-bar-nav-icon @click="toggleSidebar"></v-app-bar-nav-icon>
    </v-app-bar>
    </v-app>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { useSidebarStore } from '@/store/sidebarStore'; // Import the sidebar store
  
  export default defineComponent({
    methods: {
      toggleSidebar() {
        const sidebarStore = useSidebarStore(); // Use the sidebar store
        sidebarStore.toggleSidebar();
      }
    }
  });
  </script>
  