import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue'
import store from '@/store'


const routes = [
    { path: '/', name: 'Home', component: Home },
    {
        path: '/login',
        component: () => import('@/components/Login.vue'),
        meta: { requiresGuest: true }
    },
    {
        path: '/register',
        component: () => import('@/components/Register.vue'),
        meta: { requiresGuest: true }
    },
    {
        path: '/dashboard',
        component: () => import('@/components/Dashboard.vue'),
        meta: { requiresAuth: true }
    },
]

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL,
    ),
    routes,
});

router.beforeEach(async (to, from, next) => {
    await store.dispatch('fetchCurrentUser')

    if (to.meta.requiresAuth && !store.state.isAuthenticated) {
        next('/login')
    } else if (to.meta.requiresGuest && store.state.isAuthenticated) {
        next('/dashboard')
    } else {
        next()
    }
})

export default router