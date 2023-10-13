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
```


```
import { defineStore } from 'pinia';
import jwt from 'jsonwebtoken';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
    user: null,
  }),

  actions: {
    // Action to log in and generate the token
    login(username, password) {
      // Perform authentication (e.g., API call to validate credentials)
      // Replace this with your actual authentication logic
      if (username === 'user1' && password === 'password1') {
        // Generate a JWT token with user information
        const userToken = jwt.sign({ username }, 'your-secret-key', {
          expiresIn: '1h', // Set token expiration time as needed
        });

        this.token = userToken;
        this.user = username;
      }
    },

    // Action to log out and clear the token
    logout() {
      this.token = null;
      this.user = null;
    },
  },
});

```


---------------------------------
<template>
  <div>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" placeholder="Password" type="password" />
    <button @click="login">Login</button>
  </div>
</template>

<script>
import { useAuthStore } from './authStore';

export default {
  setup() {
    const authStore = useAuthStore();
    let username = '';
    let password = '';

    const login = () => {
      // Perform authentication (e.g., API call to validate credentials)
      // Replace this with your actual authentication logic
      if (username === 'user1' && password === 'password1') {
        // Generate a JWT token with user information
        authStore.login(username, password);
      } else {
        // Show an error toast if login fails
        // Use this.$toast.error() to display the error message
        this.$toast.error('Login failed. Please check your credentials.');
      }
    };

    return {
      username,
      password,
      login,
    };
  },
};
</script>
------------------------------------------------------------------------------
<template>
  <div v-if="show" class="notification">
    {{ message }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      message: "",
    };
  },
  methods: {
    showNotification(message) {
      this.message = message;
      this.show = true;

      setTimeout(() => {
        this.hideNotification();
      }, 3000); // Hide the notification after 3 seconds (adjust as needed)
    },
    hideNotification() {
      this.show = false;
      this.message = "";
    },
  },
};
</script>

<style scoped>
.notification {
  position: fixed;
  bottom: 10px;
  right: 10px;
  background-color: #ff0000; /* Customize the background color */
  color: #ffffff; /* Customize the text color */
  padding: 10px;
  border-radius: 5px;
}
</style>
---------------------------------------------------------------------------------------------
<template>
  <div>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" placeholder="Password" type="password" />
    <button @click="login">Login</button>
    <notification ref="notification"></notification>
  </div>
</template>

<script>
import Notification from './Notification.vue'; // Import the Notification component

export default {
  components: {
    Notification, // Register the Notification component
  },
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      // Perform authentication (e.g., API call to validate credentials)
      // Replace this with your actual authentication logic
      if (this.username === 'user1' && this.password === 'password1') {
        // Successful login
        this.$refs.notification.showNotification('Login successful'); // Display a success message
      } else {
        // Failed login
        this.$refs.notification.showNotification('Login failed. Please check your credentials.'); // Display an error message
      }
    },
  },
};
</script>
-------------------------------------------------------------------
ALTER TRIGGER [dbo].[InsertIntoTable2]
ON [dbo].[Table_1]
AFTER UPDATE
AS
BEGIN
    -- Check if the "first" and "second" columns are updated
    IF UPDATE(first) OR UPDATE(second)
    BEGIN
		PRINT'Update';
        -- Insert the updated row into Table2
        INSERT INTO Table_2 (first, second)
        SELECT d.first, d.second
        FROM deleted d;
    END
END;


Test
Test-3
Test-4
Test-5