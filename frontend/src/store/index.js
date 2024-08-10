import { createStore } from 'vuex'
import auth from '@/services/auth'

export default createStore({
    state: {
        user: null,
        isAuthenticated: false
    },
    mutations: {
        setUser(state, user) {
            state.user = user
            state.isAuthenticated = !!user
        }
    },
    actions: {
        async login({ commit }, { username, password }) {
            const user = await auth.login(username, password)
            commit('setUser', user)
        },
        async logout({ commit }) {
            await auth.logout()
            commit('setUser', null)
        },
        async register({ commit }, { username, password }) {
            const user = await auth.register(username, password)
            commit('setUser', user)
        },
        async fetchCurrentUser({ commit }) {
            try {
                const user = await auth.getCurrentUser()
                commit('setUser', user)
            } catch (error) {
                commit('setUser', null)
            }
        }
    }
})