// src/store/sidebarStore.js
import { defineStore } from 'pinia';

export const useSidebarStore = defineStore('sidebar', {
  state: () => ({
    isSidebarOpen: false
  }),
  getters: {
    // Define your getter function here
    isSidebarOpenGetter(state) {
      return state.isSidebarOpen;
    }
  },
  actions: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    }
  }
});
