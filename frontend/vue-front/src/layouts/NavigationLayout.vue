<!-- AppLayout.vue -->

<template>
    <v-app>
      <app-bar @toggle-sidebar="toggleSidebar"></app-bar>
      <v-navigation-drawer  v-model="sidebarOpen"  :app="true" :clipped="true">
        <v-list>
            <v-list-item>
                <h1>Hello</h1>
            </v-list-item>
        </v-list>
        <sidebar></sidebar>
      </v-navigation-drawer>
      <v-main>
        <!-- Main content goes here -->
        <slot></slot>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import AppBar from  '@/components/TopBarComponent.vue';
  import Sidebar from  '@/components/LeftBarComponent.vue';
  
  export default {
    components: {
      AppBar,
      Sidebar,
    },
    data() {
      return {
        sidebarOpen: false,
      };
    },
    methods: {
      toggleSidebar() {
        this.sidebarOpen = !this.sidebarOpen;
      },
    },
  };
  </script>
  