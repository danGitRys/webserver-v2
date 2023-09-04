<template>
    <v-app-bar color="primary" density="compact">
        <v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon>
    </v-app-bar>
</template>

<script>
export default {
    methods: {
        handleButtonClick() {
            // Handle button click event here
            alert('Button clicked!');
        },

        toggleDrawer() {
            // You can implement logic to toggle a side drawer here
            // For example, if you have a navigation drawer
            // You can use a Vuex store to manage the drawer state
            this.$emit('toggle-sidebar');
        },
    },
};
</script>