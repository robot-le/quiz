import { createStore } from 'vuex'
import auth from '@/services/auth'

export default createStore({
    state: {
        user: null,
        isAuthenticated: false,
        lastChecked: null,
    },
    mutations: {
        setUser(state, user) {
            state.user = user
            state.isAuthenticated = !!user
            state.lastChecked = Date.now()
        }
    },
    actions: {
        async login({ commit }, { username, password }) {
            const resp = await auth.login(username, password)
            commit('setUser', resp)
        },
        async logout({ commit }) {
            await auth.logout()
            commit('setUser', null)
        },
        async register({ commit }, { username, password }) {
            const user = await auth.register(username, password)
            commit('setUser', user)
        },
        async checkAuth({ commit, state }) {
            if (!state.isAuthenticated || (Date.now() - state.lastChecked > 600_000)) { // 600_000 ms = 10 min
                try {
                    const user = await auth.getCurrentUser()
                    commit('setUser', user)
                } catch (error) {
                    commit('setUser', null)
                }
            }
        }
    }
})