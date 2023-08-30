<template>
  <h1 class="mt-16 mb-5">Edit Movie Details</h1>
  <v-row no-gutters>
    <!-- left column -->
    <v-col xs="12" sm="6">
      <MovieDescriptionForm :movie="movie" />
      <MovieActorsForm :movie="movie"/>
      <MovieRatingForm :movie="movie" />
    </v-col>
  </v-row>
</template>

<script setup>
import MovieDescriptionForm from './MovieDescriptionForm.vue'
import MovieActorsForm from './MovieActorsForm.vue'
import MovieRatingForm from '../components/MovieRatingForm.vue'

defineProps({
  movie: {
    type: Object,
    required: true
  }
})
</script>
