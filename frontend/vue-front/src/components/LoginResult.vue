<template>
    <h2>Welcome, {{ userStore.user }}</h2>
  </template>
  
  <script>
  import { useUserStore } from '@/store/userStore';
  export default {
    setup() {
      const userStore = useUserStore;
      return { userStore };
    },
  };
  </script>