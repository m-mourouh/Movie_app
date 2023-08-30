<template>
  <h1 class="mb-5">Movie Details</h1>
  <v-row no-gutters class="d-flex justify-center">
    <!-- left column -->
    <v-col cols="12" sm="3" lg="2" class="pa-1 rounded">
      <v-card
        class="bg-grey-4 h-100 py-5 px-2 pb-2 d-flex justify-center align-center"
        style="position: relative"
        :elevation="isHovering ? 16 : 2"
        :class="{ 'on-hover': isHovering }"
      >
        <!-- Card Top -->
        <small class="position-absolute text-caption" style="top: 10px; right: 15px">Movie</small>
        <!-- Card Image -->
        <div class="text-center">
          <img src="@/assets/images/movie.svg" alt="" width="80" />
        </div>
      </v-card>
    </v-col>
    <!-- right column -->
    <v-col cols="12" sm="9" lg="10" class="pa-1">
      <v-card
        class="bg-grey-4 h-100 rounded py-5 px-2 pb-2"
        style="position: relative"
        :elevation="isHovering ? 16 : 2"
        :class="{ 'on-hover': isHovering }"
      >
        <!-- Movie Grade score-->
        <!-- if there some reviews -->
        <span
          class="position-absolute text-caption d-flex align-center"
          style="top: 10px; right: 15px"
          v-if="grade != 0"
          ><span class="mr-1 font-weight-bold">{{ grade }}</span>
          <v-icon size="medium" color="grey" icon="mdi-star"></v-icon>
        </span>
        <!-- if there are no reviews -->
        <span
          class="position-absolute text-caption d-flex align-center"
          style="top: 10px; right: 15px"
          v-else
          ><span class="mr-1 font-weight-bold">0 reviews</span>
        </span>
        <!-- Card Body -->
        <div class="px-5">
          <!-- Title -->
          <div>
            <h6 class="text-h6">Title</h6>
            <p class="text-grey-3">{{ movie?.title }}</p>
          </div>
          <!-- Description -->
          <div class="mt-5">
            <h6 class="text-h6">Description</h6>
            <p class="text-grey-3" style="max-width: 800px">{{ movie?.description }}</p>
          </div>
          <!-- Description -->
          <div class="mt-5">
            <h6 class="text-h6">Actors</h6>
            <div class="d-flex mt-5 flex-wrap">
              <span
                class="bg-grey-3 rounded-pill px-5 py-1 ma-2"
                v-for="actor in movie?.actors"
                :key="actor.id"
                >{{ actor.first_name }} {{ actor.last_name }}</span
              >
            </div>
          </div>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup>
defineProps({
  movie: {
    type: Object,
    required: true
  },
  grade: {
    type: Number,
    required: true
  }
})
</script>
