<template>
    <div>
      <v-btn @click="fetchData">Fetch Data</v-btn>
      <button @click="clearData">Clear Data</button>
      <v-table fixed-header height="300px" density="compact" theme="light">
        <thead>
          <tr>
            <th class="text-left">
              Id
            </th>
            <th class="text-left">
              Name
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in liste" :key="item.id">
            <td class="with-border">{{ item.id }}</td>
            <td class="with-border">{{ item.name }}</td>
          </tr>
        </tbody>
      </v-table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        liste: []
      };
    },
    methods: {
      fetchData() {
        // Make an Axios GET request to your backend server
        axios.get('http://localhost:5000/test')
          .then(response => {
            // Update the 'liste' data property with the received data
            this.liste = response.data;
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
      },
      clearData(){
        this.liste = []
      }
    },
   
  };
  </script>
  

  <style scoped>
.with-border {
  border-left: 1px solid #ccc; /* Add a border to separate the cells */
  padding: 8px; /* Add some padding for better spacing */
}
</style>