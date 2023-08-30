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

    setPageCount(state, payload) {
      state.pageCount = payload.count
    },

  },
  actions: {
    async getMovies({ commit }) {
      await axios
        .get('/movies/')
        .then((res) => {
          let data = res.data
          let movies = data.results
          console.log(data)
          commit('setPageCount', { count: Math.ceil(data.count / 5) })
          commit('setMoviesList', { movies })
        })
        .catch((err) => {
          console.error(err)
        })
    }
  }
})

export default store
