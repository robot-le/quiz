import apiClient from "./axios";

export default {
    async login(username, password) {
        const response = await apiClient.post('/login', { username, password })
        return response.data
    },

    async logout() {
        const response = await apiClient.post('/logout')
        return response.data
    },

    async register(username, password) {
        const response = await apiClient.post('/register', { username, password })
        return response.data
    },

    async getCurrentUser() {
        const response = await apiClient.get('/current-user')
        return response.data
    },
}