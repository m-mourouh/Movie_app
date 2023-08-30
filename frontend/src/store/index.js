import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
  state: {
    moviesList: [],
    movie: {},
    grade: 0,
    pageCount: 0,
    currentPage: 1
  },
  mutations: {
    setMoviesList(state, payload) {
      state.moviesList = payload.movies
    },
    setMovie(state, payload) {
      state.movie = payload.movie
    },
    setPageCount(state, payload) {
      state.pageCount = payload.count
    },
    setMovieGrade(state, payload) {
      state.grade = payload.grade
    },
    editMovieDescription(state, { newDescription }) {
      state.movie = { ...state.movie, description: newDescription }
    },
    setMovieActors(state, { actors }) {
      state.movie.actors = actors
    }
  },
  actions: {
    async getMovies({ commit }) {
      await axios
        .get('/movies/')
        .then((res) => {
          let data = res.data
          let movies = data.results
          commit('setPageCount', { count: Math.ceil(data.count / 5) })
          commit('setMoviesList', { movies })
        })
        .catch((err) => {
          console.error(err)
        })
    },
    async getMovie({ commit }, { id }) {
      await axios
        .get(`/movies/${id}`)
        .then((res) => {
          let movie = res.data
          commit('setMovie', { movie })
        })
        .catch((err) => {
          console.error(err)
        })
    },
    async getPageMovies({ commit }, { currentPage: page }) {
      await axios
        .get(`/movies/?p=${page}`)
        .then((res) => {
          let data = res.data
          let movies = data.results
          console.log(data)
          commit('setMoviesList', { movies })
        })
        .catch((err) => {
          console.error(err)
        })
    },
    async getMovieReviews({ commit }, { id }) {
      await axios
        .get(`/movie-reviews/${id}`)
        .then((res) => {
          const reviews = res.data
          if (reviews.length > 0) {
            const grade = (
              reviews.reduce(
                (accumulator, currentElement) => accumulator + currentElement.grade,
                0
              ) / reviews.length
            ).toFixed(1)
            commit('setMovieGrade', { grade })
          } else {
            const grade = 0
            commit('setMovieGrade', { grade })
          }
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // update movie description
    async updateMovieDescription({ commit }, movie) {
      await axios
        .put(`/movies/${movie.id}/`, movie)
        .then((res) => {
          const newDescription = res.data.description
          commit('editMovieDescription', { newDescription })
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // add new movie actor
    // eslint-disable-next-line no-unused-vars
    async updateMovieActors({ commit }, { id, pk, actor, operation }) {
      // add new actor
      if (operation === 'add') {
        await axios
          .post(`/movie/${id}/actor`, actor)
          .then((res) => {
            commit('setMovieActors', { actors: res.data.actors })
          })
          .catch((err) => {
            console.error(err)
          })
      } else if (operation === 'delete') {
        await axios
          .delete(`/movie/${id}/actor/${pk}`, { data: { ...actor } })
          .then((res) => {
            commit('setMovieActors', { actors: res.data.actors })
          })
          .catch((err) => {
            console.error(err)
          })
      }
    }
  }
})

export default store
