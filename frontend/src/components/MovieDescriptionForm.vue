<template>
  <div v-if="notification.show" class="mb-5">
    <v-alert
      v-model="notification.show"
      closable
      :text="notification.message"
      :type="notification.status"
      variant="tonal"
    ></v-alert>
  </div>

  <form @submit.prevent="updateDescription">
    <v-textarea
      clearable
      label="Description"
      variant="outlined"
      color="grey-3"
      auto-grow
      :rules="rules"
      v-model="description"
      class="text-grey-3"
    ></v-textarea>
    <v-btn type="submit" variant="tonal" class="text-capitalize mt-5">Edit Description</v-btn>
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
//
const rules = [
  (value) => {
    if (value) return true

    return 'Description is required.'
  }
]
// state
const description = ref()
const notification = ref({
  status: '',
  show: false,
  message: ''
})
// store
const store = useStore()

// methods
const updateDescription = async () => {
  if (description.value) {
    const newDescription = description.value
    await store.dispatch('updateMovieDescription', {
      ...props.movie,
      description: newDescription
    })
    notification.value = {
      status: 'success',
      show: true,
      message: 'Movie description updated successfully'
    }
  } else {
    notification.value = {
      status: 'error',
      show: true,
      message: 'Invalid description'
    }
  }
}
</script>
