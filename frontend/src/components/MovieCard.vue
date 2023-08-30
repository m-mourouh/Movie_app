<template>
  <v-hover v-slot="{ isHovering, props }" open-delay="200">
    <v-card
      class="bg-grey-4 rounded py-5 px-2 pb-2 v-card--hover "
      style="position: relative"
      :elevation="isHovering ? 16 : 2"
      :class="{ 'on-hover': isHovering }"
      v-bind="props"
    >
      <!-- Card Top -->
      <small class="position-absolute text-caption" style="top: 10px; right: 15px">Movie</small>
      <!-- Card Image -->
      <div class="text-center mt-10">
        <img src="@/assets/images/movie.svg" alt="" />
      </div>
      <!-- Card Title -->
      <p class="mt-16 text-center font-weight-bold ">{{movie.title}}</p>
    </v-card>
  </v-hover>
</template>

<script setup>
defineProps({
  movie: {
    type: Object,
    required: true,
  }
})
</script>

<style scoped>
.v-card {
  transition: opacity 0.1s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.6;
}

.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}
</style>
