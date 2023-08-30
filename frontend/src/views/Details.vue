<template>
  <v-container>
    <router-link to="/">
      <v-btn class="ma-2" color="grey-3">
        <v-icon start icon="mdi-home"></v-icon>
        Home Page
      </v-btn>
    </router-link>
  </v-container>

  <v-main class="mt-15 pa-5">
    <v-container>
      <MovieDetails :movie="movie" :grade="grade" />
    </v-container>
  </v-main>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import MovieDetails from '../components/MovieDetails.vue'
import { useStore } from 'vuex'

// props
const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

// store
const store = useStore()

// computed properties
const movie = computed(() => store.state.movie)
const grade = computed(() => store.state.grade)

// life cycle hooks
onMounted(async () => {
  await store.dispatch('getMovie', { id: props.id })
  await store.dispatch('getMovieReviews', { id: props.id })
})
</script>
