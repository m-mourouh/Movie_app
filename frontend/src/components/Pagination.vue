<template>
  <div class="mt-16 pt-16">
    <v-pagination :length="length" v-model="page"></v-pagination>
  </div>
</template>

<script setup>
import { onUpdated } from 'vue'
import { ref } from 'vue'
import { useStore } from 'vuex'

// Props
defineProps({
  length: String
})
// Store 
const store = useStore()
// State
const page = ref(1)

// life cycle hooks
onUpdated(() => {
  console.log("Current Page",page.value)
  const currentPage = page.value
  store.dispatch('getPageMovies', { currentPage })
})
</script>
