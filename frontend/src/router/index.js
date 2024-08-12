import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue'
import store from '@/store'


const routes = [
    { path: '/', name: 'Home', component: Home, meta: { requiresGuest: true } },
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
    if (to.matched.some(record => record.meta.requiresAuth)) {
        await store.dispatch('checkAuth')
        if (!store.state.isAuthenticated) {
            next('/login')
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router