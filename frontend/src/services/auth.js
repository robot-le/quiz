import { loadConfigFromFile } from "vite";
import apiClient from "./axios";

export default {
    login(credentials) {
        return apiClient.post('/login', credentials);
    },
    logout() {
        return apiClient.post('/logout');
    },
    checkSession() {
        return apiClient.get('/check-session');
    }
};