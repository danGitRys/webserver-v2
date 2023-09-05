# Example

```js

<!-- homeView.vue -->
<template>
  <!-- Your view template -->
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      backendData: null
    };
  },
  mounted() {
    axios.get('/api/data') // Replace with your Flask API endpoint
      .then(response => {
        this.backendData = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }
};
</script>

<!-- homeView.vue -->
<template>
  <NavigationLayout :backendData="backendData">
    <!-- Your view content -->
  </NavigationLayout>
</template>

<script>
import NavigationLayout from './NavigationLayout.vue';

export default {
  components: {
    NavigationLayout
  },
  data() {
    return {
      backendData: null
    };
  },
  mounted() {
    // Fetch data as shown in the previous step
  }
};
</script>

```

```js

<!-- NavigationLayout.vue -->
<template>
  <!-- Your layout template -->
  <FirstComponent :dataToPass="backendData.part1"></FirstComponent>
  <SecondComponent :dataToPass="backendData.part2"></SecondComponent>
</template>

<script>
import FirstComponent from './FirstComponent.vue';
import SecondComponent from './SecondComponent.vue';

export default {
  components: {
    FirstComponent,
    SecondComponent
  },
  props: ['backendData']
};
</script>

```

```js
<!-- FirstComponent.vue -->
<template>
  <!-- Your component template -->
  <div>{{ dataToPass }}</div>
</template>

<script>
export default {
  props: ['dataToPass']
};
</script>

```

```js
<!-- SecondComponent.vue -->
<template>
  <!-- Your component template -->
  <div>{{ dataToPass }}</div>
</template>

<script>
export default {
  props: ['dataToPass']
};
</script>

```
https://vueschool.io/articles/vuejs-tutorials/techniques-for-sharing-data-between-vue-js-components/   
https://stackoverflow.com/questions/62571970/nuxt-how-to-pass-data-from-page-to-layout
 