<template>
  <div v-if="notification.show" class="mt-10">
    <v-alert
      v-model="notification.show"
      closable
      :text="notification.message"
      :type="notification.status"
      variant="tonal"
    ></v-alert>
  </div>
  <form @submit.prevent="updateMovieActors" :class="notification.show ? 'mt-5' : 'mt-10' ">
    <v-text-field
      v-model="actorRef.firstname"
      :rules="rules"
      label="Actor's first name"
      variant="outlined"
      color="grey-3"
      class="text-grey-3 mb-5"
    ></v-text-field>

    <v-text-field
      v-model="actorRef.lastname"
      :rules="rules"
      label="Actor's last name"
      variant="outlined"
      color="grey-3"
      class="text-grey-3"
    ></v-text-field>

    <v-switch
      v-model="operation"
      :label="`${operation}`"
      true-value="add"
      false-value="delete"
      hide-details
      :color="operation === 'add' ? 'green' : 'red'"
    ></v-switch>
    <v-btn type="submit" variant="tonal" class="text-capitalize mt-3">{{ operation }} Actor </v-btn>
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

const rules = [
  (value) => {
    if (value) return true

    return 'This field is required.'
  }
]

// state
const actorRef = ref({
  firstname: '',
  lastname: ''
})
const notification = ref({
  status: '',
  show: false,
  message: ''
})
const operation = ref('add')
// store
const store = useStore()

// methods
const updateMovieActors = async () => {
  //check if the actor is already added
  if (actorRef.value.firstname && actorRef.value.lastname) {
    const actor = {
      first_name: actorRef.value.firstname,
      last_name: actorRef.value.lastname
    }
    const isExist = props.movie.actors.find(
      (a) =>
        a.first_name.toLowerCase() === actorRef.value.firstname.toLowerCase() &&
        a.last_name.toLowerCase() === actorRef.value.lastname.toLowerCase()
    )

    // check if the actor  already exists
    if (isExist) {
      notification.value = {
        status: 'warning',
        show: true,
        message: 'This actor already exists '
      }
    } else if (!isExist && operation.value === 'delete') {
      notification.value = {
        status: 'info',
        show: true,
        message: "This actor don't exist "
      }
    }
    if (!isExist && operation.value === 'add') {
      // Add new actor -> movie
      await store.dispatch('updateMovieActors', {
        id: props.movie.id,
        actor,
        operation: operation.value
      })

      notification.value = {
        status: 'success',
        show: true,
        message: 'Actor has been successfully added'
      }
    } else if (isExist && operation.value === 'delete') {
      // delete actor <- movie
      await store.dispatch('updateMovieActors', {
        id: props.movie.id,
        pk: isExist.id,
        actor,
        operation: operation.value
      })
      notification.value = {
        status: 'error',
        show: true,
        message: 'Actor was deleted'
      }
    }
  } else {
    notification.value = {
      status: "warning",
      show: true,
      message: 'Please enter the first name and  the last name'
    }
  }
}
</script>
