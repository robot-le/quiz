import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'
import Login from '../views/Login.vue';
// import authService from '../services/auth';


const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/login', name: 'Login', component: Login },
    // { path: '/test-auth', name: 'TestAuth', component: TestAuth },
]

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL,
    ),
    routes,
});


// router.beforeEach(async (to, from, next) => {
//     if (to.matched.some(record => record.meta.requiresAuth)) {
//         try {
//             await authService.checkSession();
//             next();
//         } catch (error) {
//             next({ name: 'Login' });
//         }
//     } else {
//         next();
//     }
// });

export default router;