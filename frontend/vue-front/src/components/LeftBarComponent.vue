<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        v-model="isSidebarOpen"
        temporary
      >
        <!-- Sidebar content goes here -->
        <v-list-item
          prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
          title="John Leider"
        ></v-list-item>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-view-dashboard" title="Home" value="home"></v-list-item>
          <v-list-item prepend-icon="mdi-forum" title="About" value="about"></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main style="height: 250px">
        <!-- Main content goes here -->
      </v-main>
    </v-layout>
  </v-card>
</template>

<script>
import { defineComponent, computed, watch } from 'vue';
import { useSidebarStore } from '@/store/sidebarStore'; // Import the sidebar store

export default {
  setup() {
    const sidebarStore = useSidebarStore(); // Use the sidebar store
    const isSidebarOpen = computed(() => sidebarStore.isSidebarOpenGetter); // Wrap it in a computed property

    // Optionally, you can watch isSidebarOpen, but it's not necessary when using v-model
    // watch(isSidebarOpen, (newValue, oldValue) => {
    //   console.log('isSidebarOpen changed:', newValue);
    // });

    return {
      isSidebarOpen
    };
  }
};
</script>
