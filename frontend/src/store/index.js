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
    }
  }
})

export default store
