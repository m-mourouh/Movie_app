<template>
  <v-main class="bg-white">
    <v-container class="h-screen d-flex align-center justify-center flex-column">
      <img src="@/assets/images/404.svg" alt="" style="max-width: 500px" />
      <p class="text-h5 mt-10 mb-15 text-grey-darken-2">We can't find what you are looking for.</p>
      <router-link to="/">
        <v-btn color="grey-3">
          <v-icon start icon="mdi-home"></v-icon>
          Home Page
        </v-btn>
      </router-link>
    </v-container>
  </v-main>
</template>
