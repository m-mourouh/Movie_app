<template>
  <h3 class="mt-16 mb-5">How do you rate this movie ?</h3>
  <form @submit.prevent="addRating" class="mt-5">
    <div class="">
      <v-rating v-model="rating" item-aria-label="custom icon label text {0} of {1}"></v-rating>
      <v-text-field
        type="number"
        min="1"
        max="5"
        disabled
        v-model.number="rating"
        variant="outlined"
        style="max-width: 225px"
      ></v-text-field>
    </div>
    <v-btn :loading="loading" type="submit" variant="tonal" class="text-capitalize mt-5 d-block">
      Add Review</v-btn
    >
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})

// state
const rating = ref(4)
const loading = ref(false)
// store
const store = useStore()

// methods
const addRating = async () => {
  if (rating.value && rating.value >= 1 && rating.value <= 5) {
    loading.value = true
    const review = {
      grade: +rating.value,
      movie: +props.movie.id
    }
    await store.dispatch('addMovieReview', review)
    await store.dispatch('getMovieReviews', { id: props.movie.id })
    
    loading.value = false
    alert('Review added successfully')
    
  } else {
    alert('Something went wrong, please try again')
  }
}
</script>
