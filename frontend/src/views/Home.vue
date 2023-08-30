<template>
  <v-main class="mt-15">
    <v-container>
      <h1 class="mb-5">Movies List</h1>
      <!-- Movie Cards -->
      <v-row no-gutters>
        <v-col v-for="movie in movies" :key="movie.id" cols="12" sm="4" md="4" lg="3" class="pa-1">
          <router-link :to="{ name: 'details', params: { id: movie.id } }" class="text-decoration-none">
            <MovieCard :movie="movie" />
          </router-link>
        </v-col>
      </v-row>
            <!-- pagination -->
      <Pagination :length="pageCount" />
    </v-container>
  </v-main>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue'
import Pagination from '@/components/Pagination.vue'
import { computed, onMounted, watch } from 'vue'
import { ref } from 'vue'

import { useStore } from 'vuex'

const pageCount = ref(0)
const movies = ref([])

const store = useStore()

//computed properties
const getMovies = computed(() => store.state.moviesList)
const getPageCount = computed(() => store.state.pageCount)

//life cycle
onMounted(async () => {
  await store.dispatch('getMovies')
  movies.value = getMovies.value
  pageCount.value = getPageCount.value
})

// watchers
watch(getMovies, () => {
  movies.value = getMovies.value
  console.log('getMovies = ', getMovies.value)
})
</script>
